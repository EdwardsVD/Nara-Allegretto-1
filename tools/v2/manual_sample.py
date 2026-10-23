"""Sampling acak 30-50 baris per kategori untuk pengecekan manual (Point 8)."""
from __future__ import annotations

import argparse
import json
import os
import random


def sample_category(path: str, count: int = 35, seed: int = 2026) -> list[tuple[int, str, str]]:
    with open(path, encoding="utf-8") as f:
        lines = [ (idx, json.loads(line)) for idx, line in enumerate(f, start=1) ]
    rng = random.Random(seed)
    picked = rng.sample(lines, min(count, len(lines)))
    picked.sort(key=lambda x: x[0])
    return [
        (lineno, obj["messages"][0]["content"], obj["messages"][1]["content"])
        for lineno, obj in picked
    ]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("split_dir")
    parser.add_argument("--count", type=int, default=35)
    parser.add_argument("--out", default="")
    args = parser.parse_args()

    categories = ["chat", "kode", "pengetahuan", "bahasa", "math"]
    out_lines: list[str] = []
    for idx, cat in enumerate(categories):
        p = os.path.join(args.split_dir, f"{cat}.jsonl")
        if not os.path.exists(p):
            continue
        samples = sample_category(p, count=args.count, seed=2026 + idx * 17)
        out_lines.append(f"=== KATEGORI: {cat.upper()} ({len(samples)} sampel acak) ===")
        for lineno, q, a in samples:
            out_lines.append(f"[Baris {lineno}] U: {q}")
            out_lines.append(f"          A: {a}")
            out_lines.append("-" * 60)

    report_text = "\n".join(out_lines)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(report_text + "\n")
        print(f"Tersimpan {len(out_lines)} baris audit ke {args.out}")
    else:
        print(report_text)


if __name__ == "__main__":
    main()
