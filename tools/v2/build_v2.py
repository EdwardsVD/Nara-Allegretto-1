"""Pembuat utama dataset Nara-Allegretto-2 (v2).

Alur kerja sesuai aturan:
1. Pisah file per kategori di direktori split:
   - chat.jsonl
   - kode.jsonl
   - pengetahuan.jsonl
   - bahasa.jsonl
   - math.jsonl
2. Semua baris ditulis menggunakan json.dumps(obj, ensure_ascii=False) di Python.
3. Validasi masing-masing file kategori, lalu gabung dan acak secara deterministik
   menjadi Nara-Allegretto-2.jsonl.
4. Mendukung mode `--pilot` (500 contoh per kategori) untuk uji awal cepat.
"""
from __future__ import annotations

import argparse
import json
import os
import random
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
TOOLS_DIR = os.path.dirname(HERE)
if TOOLS_DIR not in sys.path:
    sys.path.insert(0, TOOLS_DIR)

from v2.core_v2 import CategoryCollector, DEFAULT_OUTPUT, DEFAULT_SPLIT_DIR  # noqa: E402
from v2.gen_bahasa import build_bahasa_v2  # noqa: E402
from v2.gen_chat import build_chat_v2  # noqa: E402
from v2.gen_kode import build_kode  # noqa: E402
from v2.gen_math import build_math_v2  # noqa: E402
from v2.gen_pengetahuan import build_pengetahuan_v2  # noqa: E402
from v2.validate_v2 import validate_file  # noqa: E402


def build_all(
    *,
    split_dir: str = DEFAULT_SPLIT_DIR,
    merged_out: str = DEFAULT_OUTPUT,
    limit_per_cat: int | None = None,
    math_target: int = 36500,
    seed: int = 20261023,
) -> dict:
    started = time.time()
    os.makedirs(split_dir, exist_ok=True)

    # Registri global agar lintas kategori pun dijamin 0 duplikat pertanyaan & jawaban!
    seen_q_norm: set[str] = set()
    seen_q_trim: set[str] = set()
    seen_a_norm: set[str] = set()
    seen_a_trim: set[str] = set()

    c_chat = CategoryCollector("chat", seen_q_norm, seen_q_trim, seen_a_norm, seen_a_trim, max_answer=660, max_prefix_repeat=1500)
    c_kode = CategoryCollector("kode", seen_q_norm, seen_q_trim, seen_a_norm, seen_a_trim, max_answer=700, max_prefix_repeat=2000)
    c_peng = CategoryCollector("pengetahuan", seen_q_norm, seen_q_trim, seen_a_norm, seen_a_trim, max_answer=640, max_prefix_repeat=1500)
    c_bhs = CategoryCollector("bahasa", seen_q_norm, seen_q_trim, seen_a_norm, seen_a_trim, max_answer=640, max_prefix_repeat=3000)
    c_math = CategoryCollector("math", seen_q_norm, seen_q_trim, seen_a_norm, seen_a_trim, max_answer=640, max_prefix_repeat=4000)

    build_chat_v2(c_chat, limit=limit_per_cat)
    kode_ver_stats = build_kode(c_kode, seed=seed, limit=limit_per_cat)
    build_pengetahuan_v2(c_peng, seed=seed, limit=limit_per_cat)
    build_bahasa_v2(c_bhs, seed=seed, limit=limit_per_cat)
    build_math_v2(c_math, seed=seed, target_rows=math_target, limit=limit_per_cat)

    collectors = [c_chat, c_kode, c_peng, c_bhs, c_math]
    split_reports: dict[str, dict] = {}
    all_rows: list[dict] = []

    for idx, col in enumerate(collectors):
        split_path = os.path.join(split_dir, f"{col.category}.jsonl")
        w_rep = col.write_jsonl(split_path, shuffle_seed=seed + idx)
        v_rep = validate_file(split_path, check_code=(col.category == "kode"))
        if v_rep["issues_count"] > 0:
            raise RuntimeError(
                f"Validasi gagal pada split {col.category}: {v_rep['sample_issues']}"
            )
        w_rep["validation"] = v_rep
        split_reports[col.category] = w_rep
        all_rows.extend(col.rows)

    # Gabung dan acak secara deterministik ke file final
    rng = random.Random(seed + 999)
    rng.shuffle(all_rows)
    os.makedirs(os.path.dirname(os.path.abspath(merged_out)), exist_ok=True)
    with open(merged_out, "w", encoding="utf-8", newline="\n") as handle:
        for record in all_rows:
            handle.write(
                json.dumps(record, ensure_ascii=False, separators=(", ", ": ")) + "\n"
            )

    merged_val = validate_file(merged_out, check_code=True)
    if merged_val["issues_count"] > 0:
        raise RuntimeError(f"Validasi file gabungan gagal: {merged_val['sample_issues']}")

    elapsed = round(time.time() - started, 2)
    return {
        "merged": merged_val,
        "splits": {
            k: {
                "rows": v["rows"],
                "size_bytes": v["size_bytes"],
                "size_mib": v["size_mib"],
                "issues": v["validation"]["issues_count"],
                "rejects": v["rejects"],
            }
            for k, v in split_reports.items()
        },
        "code_verifier": kode_ver_stats,
        "seconds": elapsed,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pilot", action="store_true", help="Bangun 500 contoh per kategori dulu")
    parser.add_argument("--limit-per-cat", type=int, default=0)
    parser.add_argument("--math-target", type=int, default=36500)
    parser.add_argument("--split-dir", default=DEFAULT_SPLIT_DIR)
    parser.add_argument("--out", default=DEFAULT_OUTPUT)
    parser.add_argument("--report", default="")
    args = parser.parse_args()

    lim = 500 if args.pilot else (args.limit_per_cat if args.limit_per_cat > 0 else None)
    if args.pilot and args.split_dir == DEFAULT_SPLIT_DIR:
        args.split_dir = os.path.join(os.path.dirname(DEFAULT_SPLIT_DIR), "v2_pilot")
    if args.pilot and args.out == DEFAULT_OUTPUT:
        args.out = os.path.join(args.split_dir, "pilot_merged.jsonl")

    summary = build_all(
        split_dir=args.split_dir,
        merged_out=args.out,
        limit_per_cat=lim,
        math_target=args.math_target,
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    if args.report:
        with open(args.report, "w", encoding="utf-8") as f:
            json.dump(summary, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
