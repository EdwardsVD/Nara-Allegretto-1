"""Pembuat utama dataset Nara-Allegretto-3 (v3, target 100-102 MiB).

Alur (cermin pipeline v2, semua serialisasi lewat `json.dumps`):
1. Muat `Nara-Allegretto-2.jsonl` utuh sebagai basis. Sepuluh baris identitas
   versi-2 dimigrasi MANUAL satu per satu menjadi identitas Nara-Allegretto-3
   (tidak ada penggantian massal buta yang bisa merusak makna).
2. Registri duplikat global diisi dengan seluruh baris basis termigrasi,
   sehingga semua generator v3 hanya bisa menambahkan contoh yang
   pertanyaan & jawabannya benar-benar baru terhadap v2.
3. Setiap kategori dibangun ke berkas terpisah di `build/v3/*_new.jsonl`,
   divalidasi, lalu digabung dengan basis dan diacak deterministik menjadi
   `Nara-Allegretto-3.jsonl`.
4. Mode `--pilot` membangun versi kecil dari contoh baru saja untuk uji awal.

Target byte di bawah adalah estimasi per kategori BARU; ukuran akhir berkas
gabungan diukur persis dari berkas yang benar-benar tertulis.
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

from v3.core_v3 import (  # noqa: E402
    DEFAULT_OUTPUT,
    DEFAULT_SPLIT_DIR,
    CategoryCollector,
    norm_key,
    trim_lower_key,
)
from v3.gen_bahasa_v3 import build_bahasa_v3  # noqa: E402
from v3.gen_chat_v3 import build_chat_v3  # noqa: E402
from v3.gen_kode_v3 import build_kode_v3  # noqa: E402
from v3.gen_math_v3 import build_math_v3  # noqa: E402
from v3.gen_pengetahuan_v3 import build_pengetahuan_v3  # noqa: E402
from v3.validate_v3 import validate_file  # noqa: E402

ROOT = os.path.dirname(TOOLS_DIR)
BASE_V2 = os.path.join(ROOT, "Nara-Allegretto-2.jsonl")
SEED = 20261024
MIB = 1024 * 1024

# Batas keras berkas gabungan: 100 MiB persis. Batas ini adalah batas transfer
# satu berkas platform/Google Drive (terukur: 104.857.600 byte diterima,
# lebih dari itu ditolak), jadi dataset v3 dikalibrasi tepat di bawahnya.
MAX_MERGED_BYTES = 100 * MIB

# Target estimasi byte contoh BARU per kategori (total baru +-51 MiB).
# Target math dikurangi 540.000 byte dari porsi awalnya agar total gabungan
# mendarat tepat di bawah MAX_MERGED_BYTES (kalibrasi terukur dari build
# pertama: 105.392.693 byte).
TARGETS_NEW = {
    "chat": int(12.2 * MIB),
    "kode": int(9.0 * MIB),
    "pengetahuan": int(1.9 * MIB),
    "bahasa": int(13.2 * MIB),
    "math": int(14.7 * MIB) - 540_000,
}

# Migrasi identitas manual: pertanyaan lama -> (pertanyaan baru, jawaban baru).
# Hanya 10 baris di seluruh v2 yang menyebut "Nara-Allegretto-2".
IDENTITY_MIGRATION: dict[str, tuple[str, str]] = {
    "kenapa gaya ngomongmu pakai aku kamu?": (
        "kenapa gaya ngomongmu pakai aku kamu?",
        "Biar obrolannya terasa hangat, akrab, dan nggak kaku kayak surat dinas! Sejak awal Nara-Allegretto-3 memang dirancang jadi teman diskusi santai, tapi tetap sopan.",
    ),
    "nama lengkap kamu apa?": (
        "nama lengkap kamu apa?",
        "Nama lengkapku Nara-Allegretto-3. Kepanjangan ya kalau diketik terus? Makanya sehari-hari cukup panggil Nara aja.",
    ),
    "kamu siapa sih sebenarnya?": (
        "kamu siapa sih sebenarnya?",
        "Aku program kecerdasan buatan berukuran ringkas yang diberi nama Nara-Allegretto-3. Aku bukan manusia, nggak punya wujud fisik, tapi dirancang supaya enak diajak diskusi pakai bahasa sehari-hari.",
    ),
    "apa bedanya kamu sama Nara-Allegretto-1?": (
        "apa bedanya kamu sama Nara-Allegretto-1?",
        "Dibanding Nara-Allegretto-1 yang dulu kebanyakan latihan soal matematika, generasiku sebagai Nara-Allegretto-3 membawa bekal latihan yang jauh lebih besar, dengan fokus kuat ke obrolan sehari-hari dan contoh coding sederhana yang diuji otomatis.",
    ),
    "apa batasan atau kekurangan kamu?": (
        "apa batasan atau kekurangan kamu?",
        "Karena aku model kecil bernama Nara-Allegretto-3, aku nggak terhubung ke internet, nggak bisa lihat gambar atau dengar suara, dan kadang masih bisa keliru. Jadi untuk hal krusial, tetap cek ulang ya.",
    ),
    "versi kamu sekarang versi berapa?": (
        "versi kamu sekarang versi berapa?",
        "Sekarang aku jalan sebagai Nara-Allegretto-3, alias versi ketiga di keluarga Allegretto. Fokus utamaku ngobrol santai sehari-hari dan bantu dasar-dasar ngoding.",
    ),
    "kenalin diri kamu dong": (
        "kenalin diri kamu dong",
        "Kenalin, panggil aja aku Nara! Versi lengkapku Nara-Allegretto-3. Gaya ngobrolku santai, dan aku paling senang bantu obrolan harian, bahasa Indonesia, hitungan dasar, sampai potongan kode pendek.",
    ),
    "siapa kamu?": (
        "siapa kamu?",
        "Aku Nara, nama lengkapku Nara-Allegretto-3. Aku model AI kecil berbahasa Indonesia yang dibuat buat nemenin ngobrol sehari-hari, bantu belajar, dan ngasih contoh coding sederhana.",
    ),
    "kamu manusia atau robot?": (
        "kamu manusia atau robot?",
        "Bukan manusia dan nggak punya badan robot juga. Aku murni perangkat lunak model bahasa bernama Nara-Allegretto-3 yang memproses teks di komputer.",
    ),
    "apa itu Nara-Allegretto-2?": (
        "apa itu Nara-Allegretto-3?",
        "Nara-Allegretto-3 itu generasi ketiga dari model bahasa kecil seri Nara. Di generasi ini, bekal latihannya diperbesar lagi buat percakapan sehari-hari yang luwes, bahasa Indonesia, hitungan praktis, dan contoh pemrograman dasar yang rapi.",
    ),
}


def load_base_migrated(path: str = BASE_V2) -> tuple[list[dict], dict]:
    rows: list[dict] = []
    patched = 0
    with open(path, encoding="utf-8") as f:
        for line in f:
            rec = json.loads(line)
            q = rec["messages"][0]["content"]
            a = rec["messages"][1]["content"]
            if q in IDENTITY_MIGRATION:
                new_q, new_a = IDENTITY_MIGRATION[q]
                rec = {
                    "messages": [
                        {"role": "user", "content": new_q},
                        {"role": "assistant", "content": new_a},
                    ]
                }
                patched += 1
            rows.append(rec)
    if patched != len(IDENTITY_MIGRATION):
        raise RuntimeError(
            f"Migrasi identitas menemukan {patched} baris, seharusnya {len(IDENTITY_MIGRATION)}. Pembangunan dibatalkan."
        )
    bad = []
    for i, rec in enumerate(rows, start=1):
        a = rec["messages"][1]["content"]
        if "Nara-Allegretto-2" in a or "generasi kedua" in a.lower() or "versi kedua" in a.lower():
            bad.append(i)
    if bad:
        raise RuntimeError(f"Masih ada identitas versi lama pada basis di baris {bad[:5]}. Pembangunan dibatalkan.")
    est_bytes = sum(
        len((json.dumps(r, ensure_ascii=False, separators=(", ", ": ")) + "\n").encode("utf-8")) for r in rows
    )
    return rows, {"rows": len(rows), "identity_rows_migrated": patched, "est_bytes": est_bytes}


def seed_seen(rows: list[dict]):
    seen_qn: set[str] = set()
    seen_qt: set[str] = set()
    seen_an: set[str] = set()
    seen_at: set[str] = set()
    for rec in rows:
        q = rec["messages"][0]["content"]
        a = rec["messages"][1]["content"]
        seen_qn.add(norm_key(q))
        seen_qt.add(trim_lower_key(q))
        seen_an.add(norm_key(a))
        seen_at.add(trim_lower_key(a))
    if len(seen_qn) != len(rows) or len(seen_an) != len(rows):
        raise RuntimeError("Basis v2 termigrasi mengandung duplikat. Pembangunan dibatalkan.")
    return seen_qn, seen_qt, seen_an, seen_at


def build_all(*, pilot: bool = False, out: str = DEFAULT_OUTPUT, split_dir: str = DEFAULT_SPLIT_DIR) -> dict:
    started = time.time()
    os.makedirs(split_dir, exist_ok=True)

    base_rows, base_info = load_base_migrated()
    print(f"[basis] {base_info}", flush=True)
    seen = seed_seen(base_rows)

    if pilot:
        targets = {k: 140_000 for k in TARGETS_NEW}
    else:
        targets = dict(TARGETS_NEW)

    specs = [
        ("chat", 660, 4000, lambda c: build_chat_v3(c, target_bytes=targets["chat"], seed=SEED)),
        ("kode", 700, 2500, lambda c: build_kode_v3(c, target_bytes=targets["kode"], seed=SEED)),
        ("pengetahuan", 640, 3000, lambda c: build_pengetahuan_v3(c, target_bytes=targets["pengetahuan"], seed=SEED)),
        ("bahasa", 640, 6000, lambda c: build_bahasa_v3(c, target_bytes=targets["bahasa"], seed=SEED)),
        ("math", 640, 4000, lambda c: build_math_v3(c, target_bytes=targets["math"])),
    ]

    split_reports: dict[str, dict] = {}
    gen_stats: dict[str, dict] = {}
    new_rows: list[dict] = []
    for idx, (name, max_ans, max_pref, fn) in enumerate(specs):
        t0 = time.time()
        col = CategoryCollector(
            name, seen[0], seen[1], seen[2], seen[3], max_answer=max_ans, max_prefix_repeat=max_pref
        )
        gen_stats[name] = fn(col)
        split_path = os.path.join(split_dir, f"{name}_new.jsonl")
        w_rep = col.write_jsonl(split_path, shuffle_seed=SEED + idx)
        v_rep = validate_file(split_path, check_code=(name == "kode"))
        if v_rep["issues_count"] > 0:
            raise RuntimeError(f"Validasi split {name} gagal: {v_rep['sample_issues']}")
        w_rep["validation_issues"] = v_rep["issues_count"]
        w_rep["seconds"] = round(time.time() - t0, 1)
        split_reports[name] = w_rep
        new_rows.extend(col.rows)
        print(f"[{name}] rows={len(col.rows)} estMiB={col.total_bytes_est / MIB:.2f} fileMiB={w_rep['size_mib']} {w_rep['seconds']}s", flush=True)

    all_rows = list(new_rows) if pilot else (base_rows + new_rows)
    rng = random.Random(SEED + 999)
    rng.shuffle(all_rows)
    with open(out, "w", encoding="utf-8", newline="\n") as handle:
        for rec in all_rows:
            handle.write(json.dumps(rec, ensure_ascii=False, separators=(", ", ": ")) + "\n")
    merged_size = os.path.getsize(out)
    if not pilot and merged_size > MAX_MERGED_BYTES:
        raise RuntimeError(
            f"Berkas gabungan {merged_size} byte melebihi batas {MAX_MERGED_BYTES} byte (100 MiB)."
        )

    return {
        "out": out,
        "pilot": pilot,
        "base": base_info,
        "new_total_rows": len(new_rows),
        "merged_rows": len(all_rows),
        "merged_size_bytes": merged_size,
        "merged_size_mib": round(merged_size / MIB, 2),
        "merged_size_mb_decimal": round(merged_size / 1_000_000, 2),
        "splits": split_reports,
        "generators": gen_stats,
        "seconds": round(time.time() - started, 1),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pilot", action="store_true")
    parser.add_argument("--out", default="")
    parser.add_argument("--split-dir", default="")
    parser.add_argument("--report", default="")
    args = parser.parse_args()

    if args.pilot:
        split_dir = args.split_dir or os.path.join(ROOT, "build", "v3_pilot")
        out = args.out or os.path.join(split_dir, "pilot_merged.jsonl")
    else:
        split_dir = args.split_dir or DEFAULT_SPLIT_DIR
        out = args.out or DEFAULT_OUTPUT

    summary = build_all(pilot=args.pilot, out=out, split_dir=split_dir)
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    if args.report:
        with open(args.report, "w", encoding="utf-8") as f:
            json.dump(summary, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
