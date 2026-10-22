"""Validasi ketat data_Nara_Allegretto_1.jsonl.

Pemeriksaan:
- setiap baris JSON valid dan formatnya tepat (messages + user/assistant)
- tidak ada pertanyaan/jawaban duplikat
- tidak ada gaya formal "saya/anda", nama lama, atau baris kosong
- semua persamaan aritmetika di jawaban benar
- statistik panjang dan komposisi kategori
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter

sys.path.insert(0, ".")
from nara_core import is_english, norm  # noqa: E402

BAD_STYLE = re.compile(r"\b(saya|anda)\b", re.IGNORECASE)
OLD_NAME = re.compile(r"nara\s+(ai|n1)\b", re.IGNORECASE)
EQ = re.compile(r"([0-9][0-9. /]*(?:[x:+\-]\s*[0-9][0-9. /]*)+)=\s*([0-9][0-9.]*)")
PCT = re.compile(r"(\d+)\s*%\s*dari\s*([\d.]+)\s*(?:adalah|=)\s*([\d.]+)", re.IGNORECASE)


def to_int(text: str) -> int:
    return int(text.replace(".", ""))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("path")
    parser.add_argument("--show", type=int, default=8)
    args = parser.parse_args()

    total = 0
    errors: list[str] = []
    prompts: dict[str, int] = {}
    answers: dict[str, int] = {}
    categories: Counter = Counter()
    lengths: list[int] = []
    line_bytes: list[int] = []
    eq_checked = 0
    eq_bad = 0

    with open(args.path, "rb") as raw:
        for lineno, raw_line in enumerate(raw, 1):
            total += 1
            line_bytes.append(len(raw_line))
            if not raw_line.endswith(b"\n"):
                errors.append(f"baris {lineno}: tidak diakhiri newline")
            try:
                line = raw_line.decode("utf-8")
            except UnicodeDecodeError as exc:
                errors.append(f"baris {lineno}: bukan UTF-8 ({exc})")
                continue
            if not line.strip():
                errors.append(f"baris {lineno}: kosong")
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError as exc:
                errors.append(f"baris {lineno}: JSON invalid ({exc})")
                continue
            if set(obj.keys()) != {"messages"}:
                errors.append(f"baris {lineno}: key tidak tepat {list(obj.keys())}")
                continue
            msgs = obj["messages"]
            if not isinstance(msgs, list) or len(msgs) != 2:
                errors.append(f"baris {lineno}: messages bukan 2 item")
                continue
            if [m.get("role") for m in msgs] != ["user", "assistant"]:
                errors.append(f"baris {lineno}: role salah")
                continue
            q, a = msgs[0].get("content"), msgs[1].get("content")
            if not isinstance(q, str) or not isinstance(a, str):
                errors.append(f"baris {lineno}: content bukan string")
                continue
            if not q.strip() or not a.strip():
                errors.append(f"baris {lineno}: content kosong")
                continue
            if q != q.strip() or a != a.strip():
                errors.append(f"baris {lineno}: spasi di awal/akhir")
            if any(ch in q + a for ch in "\r\t"):
                errors.append(f"baris {lineno}: ada CR/tab")
            if BAD_STYLE.search(q) or BAD_STYLE.search(a):
                errors.append(f"baris {lineno}: gaya formal saya/anda")
            if OLD_NAME.search(q) or OLD_NAME.search(a):
                errors.append(f"baris {lineno}: nama lama Nara Ai/Nara N1")
            if is_english(a) and len(re.findall(r"\b(yang|dan|aku|kamu|adalah|dengan)\b", a)) < 2:
                errors.append(f"baris {lineno}: jawaban terlalu Inggris")

            qk, ak = norm(q), norm(a)
            if qk in prompts:
                errors.append(f"baris {lineno}: pertanyaan duplikat dengan baris {prompts[qk] + 1}")
            else:
                prompts[qk] = lineno - 1
            if ak in answers:
                errors.append(f"baris {lineno}: jawaban duplikat dengan baris {answers[ak] + 1}")
            else:
                answers[ak] = lineno - 1

            if len(a) < 30:
                errors.append(f"baris {lineno}: jawaban terlalu pendek ({len(a)})")
            lengths.append(len(a))
            categories[_category(q)] += 1

            for ma in EQ.finditer(a):
                expr = ma.group(1).strip()
                if not any(op in expr for op in ("+", "-", "x", ":")):
                    continue
                if ":" in expr and not re.search(r"\s:\s", expr):
                    continue
                try:
                    py = expr.replace("x", "*").replace(":", "/")
                    py = re.sub(r"(\d)\.(\d{3})", r"\1\2", py)
                    py = re.sub(r"(\d)\.(\d{3})", r"\1\2", py)
                    if not re.fullmatch(r"[0-9./+*\-() ]+", py):
                        continue
                    expected = eval(py, {"__builtins__": {}}, {})
                except Exception:
                    continue
                if isinstance(expected, float) and abs(expected - round(expected)) > 1e-6:
                    continue
                eq_checked += 1
                try:
                    actual = to_int(ma.group(2))
                except ValueError:
                    continue
                if abs(float(expected) - actual) > 1e-6:
                    eq_bad += 1
                    errors.append(f"baris {lineno}: persamaan salah: {ma.group(0)} (harusnya {expected})")

            for mp in PCT.finditer(a):
                p, n, r = int(mp.group(1)), to_int(mp.group(2)), to_int(mp.group(3))
                if n * p % 100 == 0 and n * p // 100 != r:
                    errors.append(f"baris {lineno}: persen salah: {mp.group(0)}")

    line_bytes.sort()
    lengths.sort()
    print(f"file           : {args.path}")
    print(f"baris          : {total:,}")
    print(f"ukuran         : {sum(line_bytes) / (1024 * 1024):.2f} MiB")
    print(f"baris terpanjang: {line_bytes[-1]:,} byte")
    print(f"panjang jawaban: min {lengths[0]}, median {lengths[len(lengths) // 2]}, "
          f"rata-rata {sum(lengths) / len(lengths):.1f}, max {lengths[-1]}")
    print(f"persamaan dicek: {eq_checked:,} (salah: {eq_bad})")
    print(f"kategori       : {dict(categories.most_common())}")
    print(f"masalah        : {len(errors):,}")
    for err in errors[: args.show]:
        print("  -", err)
    if errors:
        raise SystemExit(1)


def _category(question: str) -> str:
    q = question.lower()
    if any(k in q for k in (" + ", " - ", " x ", " : ", "persen", "bulatkan", "prima",
                             "faktor", "kpk", "fpb", "kuadrat", "akar", "pangkat",
                             "rata-rata", "deret", "diskon", "kembalian", "luas",
                             "keliling", "perbandingan", "rasio", "bagian dari",
                             "tambah", "kurang", "dikali", "dibagi", "jumlah")):
        return "matematika"
    if any(k in q for k in ("eja", "huruf", "kata", "vokal", "konsonan", "kapital",
                             "sinonim", "antonim", "arti", "bahasa inggris", "bahasa indonesia",
                             "baku", "peribahasa", "penulisan", "diurutkan")):
        return "bahasa"
    if any(k in q for k in ("kamu", "aku", "halo", "hai", "selamat", "makasih", "maaf",
                             "kode", "python", "javascript", "html", "css")):
        return "percakapan"
    return "pengetahuan"


if __name__ == "__main__":
    main()
