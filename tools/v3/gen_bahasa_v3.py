"""Generator tambahan kategori `bahasa` untuk Nara-Allegretto-3 (v3).

Dua sumber, semuanya dihitung/diturunkan langsung oleh Python (anti-salah):
1. Teka-teki kata v1/v2 (`data_language.build_language_puzzles`) dengan benih
   baru berurutan — hanya kombinasi kata/tugas yang belum ada di v2 yang lolos
   registri duplikat global.
2. Tugas analisis kata baru di berkas ini atas `tools/words_id.txt`:
   huruf unik, awalan/akhiran 2 huruf, kata tanpa huruf pertama/terakhir,
   huruf tengah, frekuensi + posisi huruf, urutan huruf a-z, topeng vokal,
   posisi alfabet huruf pertama, serta perbandingan dua kata (panjang dan
   urutan kamus). Setiap jawaban menyertakan kata sumbernya agar unik.
"""
from __future__ import annotations

import os
import random
import re
import sys

TOOLS_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if TOOLS_DIR not in sys.path:
    sys.path.insert(0, TOOLS_DIR)

import data_language  # noqa: E402
from nara_core import Builder  # noqa: E402

from .core_v3 import CategoryCollector, pick_det, stable_hash

WORD_RE = re.compile(r"^[a-z]{4,}$")
VOWELS = "aeiou"


def _spell(word: str) -> str:
    return "-".join(word)


def _positions(word: str, ch: str) -> list[int]:
    return [i + 1 for i, c in enumerate(word) if c == ch]


def _legacy_reseed(col: CategoryCollector, *, target_bytes: int, seeds: tuple[int, ...]) -> dict:
    per_seed: dict[str, int] = {}
    for seed in seeds:
        if col.total_bytes_est >= target_bytes:
            break
        before = len(col.rows)
        legacy = Builder(seed=seed)
        rng = random.Random(seed)
        data_language.build_language_puzzles(legacy, rng)
        rows = list(legacy.rows)
        rng.shuffle(rows)
        for row in rows:
            if col.total_bytes_est >= target_bytes:
                break
            q = row["messages"][0]["content"]
            a = row["messages"][1]["content"]
            col.add(q, a, min_answer=34, allow_english=("inggris" in q.lower()))
        per_seed[str(seed)] = len(col.rows) - before
    return per_seed


# --------------------------------------------------------------------------- #
# Tugas kata baru. Setiap fungsi menerima daftar kata yang sudah diacak
# deterministik dan menambahkan paling banyak `quota` contoh.
# --------------------------------------------------------------------------- #

def _task_unique_letters(col, words, quota, target_bytes):
    qs = [
        "buat kata '{w}', huruf berbeda apa saja yang menyusunnya?",
        "nara, kalau huruf yang sama dihitung sekali, kata '{w}' tersusun dari huruf apa?",
        "sebutkan himpunan huruf penyusun kata '{w}' dong",
    ]
    ans = [
        "Kata '{w}' tersusun dari {n} huruf berbeda, yaitu {lst}. Ejaan lengkapnya adalah {spell}.",
        "Kalau huruf kembar dihitung satu kali, kata '{w}' memakai {n} huruf berbeda: {lst}. Urutan aslinya dieja {spell}.",
        "Himpunan huruf penyusun '{w}' ada {n} macam, yakni {lst}. Bentuk utuh kata itu dieja {spell}.",
    ]
    made = 0
    for w in words:
        if made >= quota or col.total_bytes_est >= target_bytes:
            return
        uniq = sorted(set(w))
        key = f"uniq-{w}"
        q = pick_det(qs, key).format(w=w)
        a = pick_det(ans, key + "a").format(w=w, n=len(uniq), lst=", ".join(uniq), spell=_spell(w))
        if col.add(q, a):
            made += 1


def _task_prefix_suffix(col, words, quota, target_bytes):
    qs = [
        "dua huruf pertama dan dua huruf terakhir dari kata '{w}' apa saja?",
        "nara, awalan dua huruf serta akhiran dua huruf kata '{w}' itu apa?",
        "potong kata '{w}': ambil 2 huruf terdepan dan 2 huruf paling belakang dong",
    ]
    ans = [
        "Kata '{w}' diawali oleh '{pre}' dan diakhiri oleh '{suf}'. Panjang kata ini {n} huruf dan dieja {spell}.",
        "Dua huruf terdepannya adalah '{pre}', sedangkan dua huruf terakhirnya '{suf}' untuk kata '{w}' ({n} huruf, dieja {spell}).",
        "Buat '{w}', potongan depannya '{pre}' dan potongan belakangnya '{suf}'. Ejaan lengkapnya {spell}.",
    ]
    made = 0
    for w in words:
        if made >= quota or col.total_bytes_est >= target_bytes:
            return
        if len(w) < 5:
            continue
        key = f"presuf-{w}"
        q = pick_det(qs, key).format(w=w)
        a = pick_det(ans, key + "a").format(w=w, pre=w[:2], suf=w[-2:], n=len(w), spell=_spell(w))
        if col.add(q, a):
            made += 1


def _task_drop_edges(col, words, quota, target_bytes):
    made = 0
    for w in words:
        if made >= quota or col.total_bytes_est >= target_bytes:
            return
        if len(w) < 5:
            continue
        mode = stable_hash(f"drop-{w}") % 2
        if mode == 0:
            q = pick_det(
                [
                    "kalau huruf pertama kata '{w}' dibuang, sisa katanya jadi apa?",
                    "nara, hilangkan huruf paling depan dari '{w}', hasilnya bagaimana?",
                    "tulis kata '{w}' tanpa huruf pertamanya dong",
                ],
                f"dropq-{w}",
            ).format(w=w)
            a = pick_det(
                [
                    "Huruf pertama '{w}' adalah '{c}', jadi kalau dibuang sisa katanya menjadi '{rest}' dengan panjang {n} huruf.",
                    "Setelah huruf depan '{c}' dihilangkan, kata '{w}' berubah menjadi '{rest}' ({n} huruf).",
                    "Tanpa huruf pertamanya yang berupa '{c}', kata '{w}' tinggal berbunyi '{rest}'.",
                ],
                f"dropa-{w}",
            ).format(w=w, c=w[0], rest=w[1:], n=len(w) - 1)
        else:
            q = pick_det(
                [
                    "kalau huruf terakhir kata '{w}' dibuang, sisa katanya jadi apa?",
                    "nara, hilangkan huruf paling belakang dari '{w}', hasilnya bagaimana?",
                    "tulis kata '{w}' tanpa huruf terakhirnya dong",
                ],
                f"dropq-{w}",
            ).format(w=w)
            a = pick_det(
                [
                    "Huruf terakhir '{w}' adalah '{c}', jadi kalau dibuang sisa katanya menjadi '{rest}' dengan panjang {n} huruf.",
                    "Setelah huruf belakang '{c}' dihilangkan, kata '{w}' berubah menjadi '{rest}' ({n} huruf).",
                    "Tanpa huruf terakhirnya yang berupa '{c}', kata '{w}' tinggal berbunyi '{rest}'.",
                ],
                f"dropa-{w}",
            ).format(w=w, c=w[-1], rest=w[:-1], n=len(w) - 1)
        if col.add(q, a):
            made += 1


def _task_middle(col, words, quota, target_bytes):
    made = 0
    for w in words:
        if made >= quota or col.total_bytes_est >= target_bytes:
            return
        n = len(w)
        if n < 5:
            continue
        if n % 2 == 1:
            mid = w[n // 2]
            tengah = f"huruf tunggal '{mid}' di urutan ke-{n // 2 + 1}"
        else:
            mid = w[n // 2 - 1 : n // 2 + 1]
            tengah = f"dua huruf '{mid}' di urutan ke-{n // 2} dan ke-{n // 2 + 1}"
        q = pick_det(
            [
                "huruf yang persis di tengah kata '{w}' itu apa?",
                "nara, bagian tengah dari kata '{w}' hurufnya apa saja?",
                "cari huruf tengah kata '{w}' dong",
            ],
            f"midq-{w}",
        ).format(w=w)
        a = pick_det(
            [
                "Kata '{w}' punya {n} huruf, jadi bagian tengahnya adalah {tengah}. Ejaannya adalah {spell}.",
                "Dengan panjang {n} huruf, kata '{w}' memiliki {tengah} sebagai bagian tengahnya (dieja {spell}).",
                "Bagian tengah dari '{w}' ({n} huruf) berupa {tengah}. Ejaan lengkap kata ini {spell}.",
            ],
            f"mida-{w}",
        ).format(w=w, n=n, tengah=tengah, spell=_spell(w))
        if col.add(q, a):
            made += 1


def _task_letter_freq_positions(col, words, quota, target_bytes):
    made = 0
    for w in words:
        if made >= quota or col.total_bytes_est >= target_bytes:
            return
        # pilih huruf yang pasti ada: huruf dengan frekuensi tertinggi (seri -> hash)
        freq: dict[str, int] = {}
        for c in w:
            freq[c] = freq.get(c, 0) + 1
        best = max(freq.values())
        cands = [c for c, f in freq.items() if f == best]
        ch = cands[stable_hash(f"freq-{w}") % len(cands)]
        pos = _positions(w, ch)
        pos_txt = " dan ".join(str(p) for p in pos) if len(pos) <= 2 else ", ".join(str(p) for p in pos[:-1]) + f", dan {pos[-1]}"
        q = pick_det(
            [
                "pada kata '{w}', huruf '{c}' muncul berapa kali dan di urutan mana saja?",
                "nara, hitung kemunculan huruf '{c}' di kata '{w}' beserta posisinya dong",
                "di kata '{w}' ada berapa huruf '{c}'? posisinya di mana saja?",
            ],
            f"freqq-{w}-{ch}",
        ).format(w=w, c=ch)
        a = pick_det(
            [
                "Di kata '{w}', huruf '{c}' muncul sebanyak {k} kali, tepatnya pada urutan ke-{pos}. Kata itu dieja {spell}.",
                "Huruf '{c}' pada '{w}' berjumlah {k} dan menempati urutan ke-{pos}. Ejaan lengkapnya adalah {spell}.",
                "Kalau dihitung dari ejaan {spell}, huruf '{c}' di kata '{w}' tampil {k} kali pada posisi ke-{pos}.",
            ],
            f"freqa-{w}-{ch}",
        ).format(w=w, c=ch, k=len(pos), pos=pos_txt, spell=_spell(w))
        if col.add(q, a):
            made += 1


def _task_sorted_letters(col, words, quota, target_bytes):
    made = 0
    for w in words:
        if made >= quota or col.total_bytes_est >= target_bytes:
            return
        sorted_w = "".join(sorted(w))
        q = pick_det(
            [
                "kalau huruf-huruf kata '{w}' diurutkan dari a sampai z, hasilnya apa?",
                "nara, susun huruf penyusun '{w}' menurut urutan alfabet dong",
                "urutkan semua huruf pada kata '{w}' secara alfabetis ya",
            ],
            f"sortq-{w}",
        ).format(w=w)
        a = pick_det(
            [
                "Huruf-huruf kata '{w}' bila disusun alfabetis menjadi '{sorted_w}'. Jumlah hurufnya tetap {n}, hanya urutannya yang berubah.",
                "Hasil pengurutan alfabet untuk '{w}' adalah '{sorted_w}', terdiri dari {n} huruf yang sama dengan kata aslinya.",
                "Susunan a-z dari huruf penyusun '{w}' berbunyi '{sorted_w}' ({n} huruf, dari ejaan asli {spell}).",
            ],
            f"sorta-{w}",
        ).format(w=w, sorted_w=sorted_w, n=len(w), spell=_spell(w))
        if col.add(q, a):
            made += 1


def _task_vowel_mask(col, words, quota, target_bytes):
    made = 0
    for w in words:
        if made >= quota or col.total_bytes_est >= target_bytes:
            return
        masked = "".join("_" if c in VOWELS else c for c in w)
        n_v = sum(1 for c in w if c in VOWELS)
        if n_v == 0:
            continue
        q = pick_det(
            [
                "tulis kata '{w}' dengan semua huruf vokalnya diganti garis bawah dong",
                "nara, samarkan huruf vokal pada kata '{w}' pakai tanda garis bawah ya",
                "ganti setiap vokal di kata '{w}' menjadi karakter '_' dong",
            ],
            f"maskq-{w}",
        ).format(w=w)
        a = pick_det(
            [
                "Kata '{w}' memiliki {k} huruf vokal, jadi bentuk samarannya adalah '{masked}'. Huruf konsonannya dibiarkan apa adanya.",
                "Setelah {k} vokalnya ditutup garis bawah, kata '{w}' tampil sebagai '{masked}'. Pola konsonannya tetap bisa kamu baca.",
                "Hasil penyamaran vokal untuk '{w}' adalah '{masked}', karena ada {k} huruf vokal di dalamnya.",
            ],
            f"maska-{w}",
        ).format(w=w, k=n_v, masked=masked)
        if col.add(q, a):
            made += 1


def _task_first_letter_alphabet_pos(col, words, quota, target_bytes):
    made = 0
    for w in words:
        if made >= quota or col.total_bytes_est >= target_bytes:
            return
        pos = ord(w[0]) - ord("a") + 1
        q = pick_det(
            [
                "huruf pertama kata '{w}' menempati urutan ke berapa di alfabet a-z?",
                "nara, huruf awal '{w}' itu huruf ke berapa dalam abjad latin?",
                "di deretan alfabet, huruf pertama kata '{w}' nomor urut berapa?",
            ],
            f"alposq-{w}",
        ).format(w=w)
        a = pick_det(
            [
                "Kata '{w}' diawali huruf '{c}', dan huruf '{c}' adalah huruf ke-{pos} dalam alfabet a-z. Kata itu sendiri panjangnya {n} huruf.",
                "Huruf awal '{w}' berupa '{c}', yang menempati urutan ke-{pos} di abjad latin (a adalah ke-1 dan z adalah ke-26).",
                "Jawabannya urutan ke-{pos}, karena kata '{w}' dimulai dengan huruf '{c}'. Ejaan lengkapnya adalah {spell}.",
            ],
            f"alposa-{w}",
        ).format(w=w, c=w[0], pos=pos, n=len(w), spell=_spell(w))
        if col.add(q, a):
            made += 1


def _task_contains_letter(col, words, quota, target_bytes, rng: random.Random):
    made = 0
    attempts = 0
    pool = list(words)
    while made < quota and col.total_bytes_est < target_bytes and attempts < quota * 3:
        attempts += 1
        w = pool[attempts % len(pool)]
        ch = chr(ord("a") + (stable_hash(f"cont-{w}-{attempts}") % 26))
        pos = _positions(w, ch)
        key = f"cont-{w}-{ch}-{attempts}"
        q = pick_det(
            [
                "apakah kata '{w}' mengandung huruf '{c}'?",
                "nara, di dalam kata '{w}' ada huruf '{c}' nggak sih?",
                "cek dong, kata '{w}' memakai huruf '{c}' atau tidak?",
            ],
            key + "q",
        ).format(w=w, c=ch)
        if pos:
            pos_txt = " dan ".join(str(p) for p in pos) if len(pos) <= 3 else ", ".join(str(p) for p in pos)
            a = pick_det(
                [
                    "Ada. Kata '{w}' mengandung huruf '{c}' pada urutan ke-{pos}, seperti terlihat dari ejaannya {spell}.",
                    "Iya, huruf '{c}' dipakai di kata '{w}', tepatnya di urutan ke-{pos}. Ejaan lengkapnya adalah {spell}.",
                    "Betul, '{c}' termasuk huruf penyusun '{w}' dan berada pada urutan ke-{pos} dari {n} huruf.",
                ],
                key + "a",
            ).format(w=w, c=ch, pos=pos_txt, spell=_spell(w), n=len(w))
        else:
            a = pick_det(
                [
                    "Tidak ada. Kata '{w}' dieja {spell}, dan di antara {n} hurufnya tidak terdapat huruf '{c}'.",
                    "Nggak ada huruf '{c}' di kata '{w}'. Huruf penyusunnya hanya {lst}, sesuai ejaan {spell}.",
                    "Setelah dicek dari ejaan {spell}, kata '{w}' ternyata tidak memakai huruf '{c}' sama sekali.",
                ],
                key + "a",
            ).format(w=w, c=ch, pos="", spell=_spell(w), n=len(w), lst=", ".join(sorted(set(w))))
        if col.add(q, a):
            made += 1


def _task_compare_pairs(col, words, quota, target_bytes, rng: random.Random):
    made = 0
    attempts = 0
    while made < quota and col.total_bytes_est < target_bytes and attempts < quota * 4:
        attempts += 1
        w1, w2 = rng.sample(words, 2)
        if stable_hash(f"cmp-{w1}-{w2}") % 2 == 0:
            # banding panjang
            if len(w1) == len(w2):
                continue
            longer, shorter = (w1, w2) if len(w1) > len(w2) else (w2, w1)
            diff = len(longer) - len(shorter)
            q = pick_det(
                [
                    "antara kata '{a}' dan '{b}', mana yang hurufnya lebih banyak?",
                    "nara, bandingkan panjang kata '{a}' dengan kata '{b}' dong",
                    "dari dua kata '{a}' serta '{b}', yang lebih panjang yang mana?",
                ],
                f"cmpq-{w1}-{w2}",
            ).format(a=w1, b=w2)
            a = pick_det(
                [
                    "Kata '{longer}' lebih panjang dengan {nl} huruf, sedangkan '{shorter}' hanya {ns} huruf. Selisih panjang keduanya adalah {diff} huruf.",
                    "Yang lebih banyak hurufnya adalah '{longer}' ({nl} huruf) dibanding '{shorter}' ({ns} huruf), jadi bedanya {diff} huruf.",
                    "Kalau dihitung, '{a}' berisi {na} huruf dan '{b}' berisi {nb} huruf, sehingga '{longer}' unggul {diff} huruf.",
                ],
                f"cmpa-{w1}-{w2}",
            ).format(longer=longer, shorter=shorter, nl=len(longer), ns=len(shorter), diff=diff, a=w1, b=w2, na=len(w1), nb=len(w2))
        else:
            # urutan kamus
            first, second = sorted([w1, w2])
            q = pick_det(
                [
                    "kalau di kamus, kata '{a}' atau '{b}' yang muncul lebih dulu?",
                    "nara, urutkan dua kata ini secara alfabetis: '{a}' dan '{b}'",
                    "menurut urutan alfabet, '{a}' dan '{b}' mana yang posisinya lebih awal?",
                ],
                f"dictq-{w1}-{w2}",
            ).format(a=w1, b=w2)
            a = pick_det(
                [
                    "Yang muncul lebih dulu adalah '{first}', baru kemudian '{second}'. Urutan kamusnya ditentukan oleh huruf awal '{fc}' yang mendahului '{sc}'.",
                    "Urutan alfabetisnya adalah '{first}' lalu '{second}', karena huruf pertama '{fc}' berada sebelum '{sc}' di alfabet.",
                    "Di kamus, '{first}' terletak lebih awal daripada '{second}'. Kuncinya ada pada huruf awal masing-masing kata.",
                ],
                f"dicta-{w1}-{w2}",
            ).format(first=first, second=second, fc=first[0], sc=second[0])
        if col.add(q, a):
            made += 1


def _task_concat_words(col, words, quota, target_bytes, rng: random.Random):
    made = 0
    attempts = 0
    while made < quota and col.total_bytes_est < target_bytes and attempts < quota * 3:
        attempts += 1
        w1, w2 = rng.sample(words, 2)
        joined = w1 + w2
        q = pick_det(
            [
                "kalau kata '{a}' ditempel langsung dengan kata '{b}' tanpa spasi, jadinya apa dan berapa huruf?",
                "nara, gabungkan '{a}' dan '{b}' jadi satu rangkaian huruf dong",
                "sambung kata '{a}' lalu '{b}' tanpa spasi, hasilnya bagaimana?",
            ],
            f"catq-{w1}-{w2}",
        ).format(a=w1, b=w2)
        a = pick_det(
            [
                "Gabungan tanpa spasinya adalah '{joined}' dengan total {n} huruf, yaitu {na} huruf dari '{a}' ditambah {nb} huruf dari '{b}'.",
                "Kalau ditempel langsung, hasilnya berbunyi '{joined}' ({n} huruf seluruhnya dari gabungan {na} + {nb} huruf).",
                "Rangkaian hurufnya menjadi '{joined}'. Panjangnya {n} huruf karena '{a}' menyumbang {na} huruf dan '{b}' menyumbang {nb} huruf.",
            ],
            f"cata-{w1}-{w2}",
        ).format(joined=joined, n=len(joined), a=w1, b=w2, na=len(w1), nb=len(w2))
        if col.add(q, a):
            made += 1


def build_bahasa_v3(
    col: CategoryCollector,
    *,
    target_bytes: int,
    seed: int = 20261024,
) -> dict:
    rng = random.Random(seed)
    stats: dict[str, object] = {}

    # Sumber 1: teka-teki kata lama dengan benih baru (dibatasi 45% target)
    legacy_cap = int(target_bytes * 0.45)
    stats["legacy_per_seed"] = _legacy_reseed(
        col, target_bytes=legacy_cap, seeds=(seed, seed + 1, seed + 2)
    )

    # Sumber 2: tugas analisis kata baru
    all_words = [w for w in data_language.load_words() if WORD_RE.match(w)]
    rng.shuffle(all_words)

    n_tasks = 10
    per_task = max(400, int((target_bytes - col.total_bytes_est) / 230 / n_tasks) + 200)
    _task_unique_letters(col, all_words, per_task, target_bytes)
    _task_prefix_suffix(col, all_words, per_task, target_bytes)
    _task_drop_edges(col, all_words, per_task, target_bytes)
    _task_middle(col, all_words, per_task, target_bytes)
    _task_letter_freq_positions(col, all_words, per_task, target_bytes)
    _task_sorted_letters(col, all_words, per_task, target_bytes)
    _task_vowel_mask(col, all_words, per_task, target_bytes)
    _task_first_letter_alphabet_pos(col, all_words, per_task, target_bytes)
    _task_contains_letter(col, all_words, per_task, target_bytes, rng)
    _task_compare_pairs(col, all_words, per_task * 2, target_bytes, rng)
    _task_concat_words(col, all_words, per_task, target_bytes, rng)

    stats["rows"] = len(col.rows)
    stats["est_bytes"] = col.total_bytes_est
    return stats
