"""Generator kategori `math.jsonl` untuk Nara-Allegretto-2.

Target v2 (Point 5): matematika diturunkan ke kisaran 30.000 - 40.000 contoh
(dari 84.096 di v1) agar fokus utama beralih ke percakapan sehari-hari dan kode.
Semua hitungan dihitung langsung dengan Python sehingga 100% akurat.
"""
from __future__ import annotations

import os
import random
import sys

TOOLS_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if TOOLS_DIR not in sys.path:
    sys.path.insert(0, TOOLS_DIR)

import data_math  # noqa: E402
from nara_core import Builder  # noqa: E402

from .core_v2 import CategoryCollector


def build_math_v2(
    col: CategoryCollector,
    *,
    seed: int = 20261023,
    target_rows: int = 35500,
    limit: int | None = None,
) -> None:
    cap = target_rows if limit is None else min(limit, target_rows)
    scale = 0.05 if (limit is not None and limit <= 1000) else 0.88

    legacy_builder = Builder(seed=seed)
    rng = random.Random(seed)
    data_math.build_math(legacy_builder, rng, scale)

    rows = list(legacy_builder.rows)
    rng.shuffle(rows)
    for row in rows:
        if len(col.rows) >= cap:
            break
        q = row["messages"][0]["content"]
        a = row["messages"][1]["content"]
        col.add(q, a, min_answer=34)
