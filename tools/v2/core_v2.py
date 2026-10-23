"""Utilitas inti untuk membangun dataset Nara-Allegretto-2 (v2).

Prinsip utama:
1. Semua JSON ditulis lewat json.dumps(..., ensure_ascii=False) di Python.
2. Gaya bahasa konsisten: nama Nara (Nara-Allegretto-2), santai (aku/kamu).
3. Bebas duplikat pertanyaan & jawaban (baik lower+trim maupun normalisasi).
4. Bebas karakter rusak (mojibake seperti Ã©, â€™, replacement char).
5. Pembatasan panjang pertanyaan/jawaban dan variasi pembuka kalimat agar
   model kecil belajar respons yang alami dan tidak seragam.
"""
from __future__ import annotations

import hashlib
import json
import os
import random
import re
import unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DEFAULT_SPLIT_DIR = os.path.join(ROOT, "build", "v2")
DEFAULT_OUTPUT = os.path.join(ROOT, "Nara-Allegretto-2.jsonl")

BAD_STYLE_RE = re.compile(r"\b(saya|anda)\b", re.IGNORECASE)
OLD_NAME_RE = re.compile(r"nara\s+(ai|n1)\b", re.IGNORECASE)
OLD_V1_SELF_RE = re.compile(r"(namaku|aku|aku ini)\s+nara-allegretto-1\b", re.IGNORECASE)
MOJIBAKE_RE = re.compile(
    r"(Ã[\x80-\xbf©¨¡¢£¤¥§ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿]|â€[™˜œ\x9d–—¦¢]|Â |\ufffd)"
)
CONTROL_RE = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]")
CODE_BLOCK_RE = re.compile(r"```[a-zA-Z0-9_+-]*\n.*?\n```", re.DOTALL)
ENGLISH_MARKERS_RE = re.compile(
    r"\b(the|is|are|was|were|your|this|that|with|have|has|does|will|would|"
    r"could|there|they|from|which|because|about|into|should|their)\b",
    re.IGNORECASE,
)
ID_MARKERS_RE = re.compile(
    r"\b(aku|kamu|yang|dan|di|ke|dari|untuk|dengan|kalau|bisa|ini|itu|jadi|"
    r"nggak|aja|ya|karena|atau|ada|lebih|buat|coba|hasilnya)\b",
    re.IGNORECASE,
)
WS_LINE_RE = re.compile(r"[ \t]+")


def clean_text(text: str, preserve_code_indent: bool = True) -> str:
    """Rapikan spasi dan newline tanpa merusak indentasi blok kode."""
    text = unicodedata.normalize("NFC", text)
    text = text.replace("\r\n", "\n").replace("\r", "\n").replace("\t", "  ")
    if preserve_code_indent and "```" in text:
        parts = text.split("```")
        out_parts: list[str] = []
        for idx, part in enumerate(parts):
            if idx % 2 == 0:
                lines = [WS_LINE_RE.sub(" ", ln).strip() for ln in part.split("\n")]
                cleaned = "\n".join(lines)
                cleaned = re.sub(r"\n{3,}", "\n\n", cleaned)
                out_parts.append(cleaned)
            else:
                code_lines = [ln.rstrip() for ln in part.split("\n")]
                out_parts.append("\n".join(code_lines))
        return "```".join(out_parts).strip()

    lines = [WS_LINE_RE.sub(" ", ln).strip() for ln in text.split("\n")]
    text = "\n".join(lines).strip()
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text


def norm_key(text: str) -> str:
    """Kunci alfanumerik ketat untuk deteksi duplikat lintas tanda baca."""
    text = unicodedata.normalize("NFKD", text.lower())
    text = "".join(ch for ch in text if not unicodedata.combining(ch))
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def trim_lower_key(text: str) -> str:
    """Kunci sesuai aturan validator: lowercase + trim + rapikan spasi."""
    return re.sub(r"\s+", " ", text.lower().strip())


def has_mojibake(text: str) -> bool:
    return bool(MOJIBAKE_RE.search(text) or CONTROL_RE.search(text))


def strip_code_blocks(text: str) -> str:
    return CODE_BLOCK_RE.sub(" ", text)


def is_mostly_english_prose(text: str) -> bool:
    prose = strip_code_blocks(text)
    words = re.findall(r"[A-Za-z']+", prose)
    if len(words) < 8:
        return False
    en_hits = len(ENGLISH_MARKERS_RE.findall(prose))
    id_hits = len(ID_MARKERS_RE.findall(prose))
    return en_hits >= 3 and en_hits > id_hits


def fmt_id(number: int) -> str:
    return f"{number:,}".replace(",", ".")


def fmt_rp(number: int) -> str:
    return "Rp" + fmt_id(number)


def stable_hash(key: str) -> int:
    digest = hashlib.blake2b(key.encode("utf-8"), digest_size=8).digest()
    return int.from_bytes(digest, "big")


def pick_det(options: list, key: str):
    return options[stable_hash(key) % len(options)]


class CategoryCollector:
    """Penampung contoh per kategori yang berbagi registri duplikat global."""

    def __init__(
        self,
        category: str,
        seen_q_norm: set[str],
        seen_q_trim: set[str],
        seen_a_norm: set[str],
        seen_a_trim: set[str],
        *,
        min_answer: int = 40,
        max_answer: int = 620,
        max_question: int = 280,
        max_prefix_repeat: int = 450,
    ) -> None:
        self.category = category
        self.seen_q_norm = seen_q_norm
        self.seen_q_trim = seen_q_trim
        self.seen_a_norm = seen_a_norm
        self.seen_a_trim = seen_a_trim
        self.min_answer = min_answer
        self.max_answer = max_answer
        self.max_question = max_question
        self.max_prefix_repeat = max_prefix_repeat
        self.rows: list[dict] = []
        self.rejects: dict[str, int] = {}
        self.prefix_counts: dict[str, int] = {}
        self.total_bytes_est = 0

    def _reject(self, reason: str) -> bool:
        self.rejects[reason] = self.rejects.get(reason, 0) + 1
        return False

    def add(
        self,
        question: str,
        answer: str,
        *,
        min_answer: int | None = None,
        max_answer: int | None = None,
        allow_english: bool = False,
        allow_multiline_q: bool = False,
    ) -> bool:
        q = clean_text(question, preserve_code_indent=allow_multiline_q)
        a = clean_text(answer, preserve_code_indent=True)

        min_a = self.min_answer if min_answer is None else min_answer
        max_a = self.max_answer if max_answer is None else max_answer

        if not q or not a:
            return self._reject("kosong")
        if not allow_multiline_q and "\n" in q:
            return self._reject("newline_di_pertanyaan")
        if len(q) > self.max_question:
            return self._reject("pertanyaan_terlalu_panjang")
        if len(a) < min_a:
            return self._reject("jawaban_terlalu_pendek")
        if len(a) > max_a:
            return self._reject("jawaban_terlalu_panjang")
        if has_mojibake(q) or has_mojibake(a):
            return self._reject("karakter_rusak")
        if BAD_STYLE_RE.search(q) or BAD_STYLE_RE.search(a):
            return self._reject("gaya_formal_saya_anda")
        if OLD_NAME_RE.search(q) or OLD_NAME_RE.search(a):
            return self._reject("nama_lama")
        if OLD_V1_SELF_RE.search(a):
            return self._reject("identitas_v1")
        if "nara-allegretto-1" in a.lower() and "nara-allegretto-1" not in q.lower():
            return self._reject("sebut_v1_tanpa_ditanya")
        if not allow_english and is_mostly_english_prose(a):
            return self._reject("prosa_terlalu_inggris")

        qk_norm = norm_key(q)
        qk_trim = trim_lower_key(q)
        ak_norm = norm_key(a)
        ak_trim = trim_lower_key(a)

        if not qk_norm or not ak_norm:
            return self._reject("kunci_kosong")
        if qk_trim in self.seen_q_trim or qk_norm in self.seen_q_norm:
            return self._reject("pertanyaan_duplikat")
        if ak_trim in self.seen_a_trim or ak_norm in self.seen_a_norm:
            return self._reject("jawaban_duplikat")

        # Jaga keberagaman pembuka jawaban (5 kata pertama).
        prose_words = norm_key(strip_code_blocks(a)).split()
        if len(prose_words) >= 5:
            prefix5 = " ".join(prose_words[:5])
            if self.prefix_counts.get(prefix5, 0) >= self.max_prefix_repeat:
                return self._reject("pembuka_terlalu_sering")
            self.prefix_counts[prefix5] = self.prefix_counts.get(prefix5, 0) + 1

        self.seen_q_trim.add(qk_trim)
        self.seen_q_norm.add(qk_norm)
        self.seen_a_trim.add(ak_trim)
        self.seen_a_norm.add(ak_norm)

        record = {
            "messages": [
                {"role": "user", "content": q},
                {"role": "assistant", "content": a},
            ]
        }
        line_str = json.dumps(record, ensure_ascii=False, separators=(", ", ": ")) + "\n"
        self.rows.append(record)
        self.total_bytes_est += len(line_str.encode("utf-8"))
        return True

    def write_jsonl(self, path: str, shuffle_seed: int | None = None) -> dict:
        rows = list(self.rows)
        if shuffle_seed is not None:
            random.Random(shuffle_seed).shuffle(rows)
        os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
        with open(path, "w", encoding="utf-8", newline="\n") as handle:
            for record in rows:
                handle.write(
                    json.dumps(record, ensure_ascii=False, separators=(", ", ": ")) + "\n"
                )
        size = os.path.getsize(path)
        return {
            "category": self.category,
            "path": path,
            "rows": len(rows),
            "size_bytes": size,
            "size_mib": round(size / (1024 * 1024), 2),
            "rejects": dict(sorted(self.rejects.items(), key=lambda kv: -kv[1])),
        }
