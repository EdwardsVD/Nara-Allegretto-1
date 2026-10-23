"""Generator tambahan kategori `math` untuk Nara-Allegretto-3 (v3).

Strategi anti-salah:
- Memakai ulang pembangun matematika v1/v2 (`data_math.build_math`) yang semua
  jawabannya dihitung langsung oleh Python, tetapi dengan banyak benih acak
  baru secara berurutan. Registri duplikat global sudah diisi seluruh isi
  `Nara-Allegretto-2.jsonl`, jadi hanya soal yang benar-benar baru yang lolos.
- Berhenti begitu target byte kategori tercapai (atau sumber benih habis),
  supaya porsi matematika di v3 tetap terkendali dan tidak mendominasi.
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

from .core_v3 import CategoryCollector


def build_math_v3(
    col: CategoryCollector,
    *,
    target_bytes: int,
    seeds: tuple[int, ...] = (20261024, 20261025, 20261026, 20261027, 20261028),
    scale: float = 0.95,
) -> dict:
    """Tambahkan soal matematika baru sampai `target_bytes` (estimasi) tercapai."""
    per_seed: dict[str, int] = {}
    for seed in seeds:
        if col.total_bytes_est >= target_bytes:
            break
        before = len(col.rows)
        legacy = Builder(seed=seed)
        rng = random.Random(seed)
        data_math.build_math(legacy, rng, scale)
        rows = list(legacy.rows)
        rng.shuffle(rows)
        for row in rows:
            if col.total_bytes_est >= target_bytes:
                break
            q = row["messages"][0]["content"]
            a = row["messages"][1]["content"]
            col.add(q, a, min_answer=34)
        per_seed[str(seed)] = len(col.rows) - before
    return {"per_seed_new_rows": per_seed, "rows": len(col.rows), "est_bytes": col.total_bytes_est}
