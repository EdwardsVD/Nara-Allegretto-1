"""Utilitas inti untuk membangun dataset Nara-Allegretto-1.

Semua contoh ditulis dengan gaya santai (aku/kamu), konsisten, dan divalidasi
secara ketat supaya file .jsonl selalu satu baris per contoh.
"""
from __future__ import annotations

import json
import os
import random
import re
import unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT = os.path.join(ROOT, "data_Nara_Allegretto_1.jsonl")

# Gaya bahasa: hindari "saya/Anda" agar tidak campur formal-santai.
_BAD_STYLE = re.compile(r"\b(saya|anda)\b", re.IGNORECASE)
_BAD_NAME = re.compile(r"nara\s+(ai|n1)\b", re.IGNORECASE)
_ENGLISH_MARKERS = re.compile(
    r"\b(the|is|are|was|were|you|your|this|that|with|have|has|does|will|would|"
    r"can|could|there|they|from|what|which|because|about|into)\b",
    re.IGNORECASE,
)
_WS = re.compile(r"[ \t]+")


def clean(text: str) -> str:
    """Rapikan spasi tanpa mengubah isi kalimat."""
    text = unicodedata.normalize("NFC", text)
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    lines = [_WS.sub(" ", line).strip() for line in text.split("\n")]
    text = "\n".join(lines).strip()
    text = re.sub(r" *\n *", "\n", text)
    return text


def norm(text: str) -> str:
    """Kunci pembanding untuk mendeteksi duplikat."""
    text = unicodedata.normalize("NFKD", text.lower())
    text = "".join(ch for ch in text if not unicodedata.combining(ch))
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def fmt_id(number: int) -> str:
    """1234567 -> '1.234.567' (format angka Indonesia)."""
    return f"{number:,}".replace(",", ".")


def fmt_rp(number: int) -> str:
    return "Rp" + fmt_id(number)


def is_english(text: str) -> bool:
    words = re.findall(r"[A-Za-z']+", text)
    if len(words) < 6:
        return False
    hits = len(_ENGLISH_MARKERS.findall(text))
    return hits / max(len(words), 1) > 0.12 and hits >= 2


def count_vowels(word: str) -> list[str]:
    return [ch for ch in word.lower() if ch in "aeiou"]


def count_consonants(word: str) -> list[str]:
    return [ch for ch in word.lower() if ch.isalpha() and ch not in "aeiou"]


class Builder:
    """Penampung contoh dengan penjagaan duplikat dan gaya bahasa."""

    MIN_ANSWER = 45

    def __init__(self, seed: int = 20261022) -> None:
        self.rows: list[dict] = []
        self.prompts: dict[str, int] = {}
        self.answers: dict[str, int] = {}
        self.facts: dict[str, int] = {}
        self.rng = random.Random(seed)
        self.stats: dict[str, dict] = {}
        self.rejects: dict[str, int] = {}

    # ------------------------------------------------------------------ #
    def _reject(self, reason: str) -> None:
        self.rejects[reason] = self.rejects.get(reason, 0) + 1

    def add(
        self,
        question: str,
        answer: str,
        category: str,
        *,
        fact: str | None = None,
        max_fact: int = 1,
        min_answer: int | None = None,
        allow_english: bool = False,
    ) -> bool:
        question = clean(question)
        answer = clean(answer)
        limit = self.MIN_ANSWER if min_answer is None else min_answer

        if not question or not answer:
            self._reject("kosong")
            return False
        if "\n" in question:
            self._reject("baris_baru_di_pertanyaan")
            return False
        if len(answer) < limit:
            self._reject("jawaban_terlalu_pendek")
            return False
        if _BAD_STYLE.search(question) or _BAD_STYLE.search(answer):
            self._reject("gaya_formal")
            return False
        if _BAD_NAME.search(question) or _BAD_NAME.search(answer):
            self._reject("nama_lama")
            return False
        if not allow_english and (is_english(question) or is_english(answer)):
            self._reject("bahasa_inggris")
            return False
        if question.count('"') != question.count('"'):
            self._reject("kutip_tidak_seimbang")
            return False

        qkey, akey = norm(question), norm(answer)
        if qkey in self.prompts:
            self._reject("pertanyaan_duplikat")
            return False
        if akey in self.answers:
            self._reject("jawaban_duplikat")
            return False
        if fact is not None:
            fkey = norm(fact)
            if self.facts.get(fkey, 0) >= max_fact:
                self._reject("fakta_penuh")
                return False

        self.prompts[qkey] = len(self.rows)
        self.answers[akey] = len(self.rows)
        if fact is not None:
            fkey = norm(fact)
            self.facts[fkey] = self.facts.get(fkey, 0) + 1
        self.rows.append(
            {
                "messages": [
                    {"role": "user", "content": question},
                    {"role": "assistant", "content": answer},
                ],
                "_cat": category,
            }
        )
        bucket = self.stats.setdefault(category, {"rows": 0, "chars": 0})
        bucket["rows"] += 1
        bucket["chars"] += len(question) + len(answer)
        return True

    # ------------------------------------------------------------------ #
    def pick(self, options: list[str], key: str) -> str:
        """Pilih varian secara deterministik berdasarkan kategori + kunci."""
        h = 0
        for ch in key:
            h = (h * 131 + ord(ch)) % 1000003
        return options[h % len(options)]

    def write(self, path: str = OUTPUT, shuffle: bool = True) -> dict:
        rows = list(self.rows)
        if shuffle:
            random.Random(777).shuffle(rows)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8", newline="\n") as handle:
            for row in rows:
                record = {"messages": row["messages"]}
                handle.write(
                    json.dumps(record, ensure_ascii=False, separators=(", ", ": "))
                    + "\n"
                )
        size = os.path.getsize(path)
        return {
            "path": path,
            "rows": len(rows),
            "size_bytes": size,
            "size_mb": round(size / (1024 * 1024), 2),
            "chars": sum(len(r["messages"][0]["content"]) + len(r["messages"][1]["content"]) for r in rows),
            "stats": dict(sorted(self.stats.items(), key=lambda kv: -kv[1]["rows"])),
            "rejects": dict(sorted(self.rejects.items(), key=lambda kv: -kv[1])),
        }
