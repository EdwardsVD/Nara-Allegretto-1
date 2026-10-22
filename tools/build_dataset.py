"""Bangun data_Nara_Allegretto_1.jsonl dari semua modul materi."""
from __future__ import annotations

import argparse
import json
import random
import time

from nara_core import Builder, OUTPUT
import data_math
import data_language
import data_bahasa
import data_world
import data_facts
import data_chat


def build(scale: float, out: str) -> dict:
    started = time.time()
    b = Builder()
    rng = random.Random(20261022)

    data_math.build_math(b, rng, scale)
    data_language.build_language_puzzles(b, rng)
    data_bahasa.build_language_content(b)
    data_world.build_world(b)
    data_facts.build_facts(b)
    data_chat.build_chat(b)

    report = b.write(out)
    report["seconds"] = round(time.time() - started, 2)
    report["scale"] = scale
    return report


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--scale", type=float, default=1.0)
    parser.add_argument("--out", default=OUTPUT)
    parser.add_argument("--report", default="")
    args = parser.parse_args()

    report = build(args.scale, args.out)
    print(json.dumps(report, ensure_ascii=False, indent=1))
    if args.report:
        with open(args.report, "w", encoding="utf-8") as handle:
            json.dump(report, handle, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
