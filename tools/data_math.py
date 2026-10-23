"""Generator materi matematika dasar untuk Nara-Allegretto-1.

Semua jawaban dihitung dengan Python, jadi tidak ada angka yang salah.
Setiap fakta (operasi + angka) hanya dipakai sekali agar tidak duplikat.
"""
from __future__ import annotations

import math
import random
from typing import Callable

from nara_core import Builder, fmt_id, fmt_rp, norm


def norm_key(text: str) -> str:
    return norm(text).replace(" ", "-")

# --------------------------------------------------------------------------- #
# Kumpulan varian bahasa
# --------------------------------------------------------------------------- #
Q_ADD = [
    "berapa {a} + {b}?",
    "hasil dari {a} + {b} berapa?",
    "tolong hitung {a} + {b}",
    "{a} + {b} = ?",
    "kak, {a} + {b} berapa ya?",
    "coba jumlahkan {a} dengan {b}",
    "berapa jumlah {a} dan {b}?",
    "hitung cepat: {a} + {b}",
    "{a} ditambah {b} hasilnya berapa?",
    "aku mau nanya, {a} + {b} itu berapa?",
    "bantu hitung {a} tambah {b} dong",
    "kalau {a} + {b}, hasilnya?",
    "berapa ya {a} tambah {b}?",
    "jujur aku lupa, {a} + {b} sama dengan berapa?",
    "coba tebak hasil {a} + {b}",
]
Q_SUB = [
    "berapa {a} - {b}?",
    "hasil dari {a} - {b} berapa?",
    "tolong hitung {a} - {b}",
    "{a} - {b} = ?",
    "kak, {a} dikurangi {b} berapa?",
    "coba kurangi {a} dengan {b}",
    "berapa sisa kalau {a} dikurangi {b}?",
    "hitung cepat: {a} - {b}",
    "{a} minus {b} hasilnya berapa?",
    "aku mau nanya, {a} - {b} itu berapa?",
    "bantu hitung {a} kurang {b} dong",
    "kalau {a} - {b}, hasilnya?",
    "berapa ya {a} dikurangi {b}?",
    "jujur aku lupa, {a} - {b} sama dengan berapa?",
    "coba tebak hasil {a} - {b}",
]
Q_MUL = [
    "berapa {a} x {b}?",
    "hasil dari {a} x {b} berapa?",
    "tolong hitung {a} x {b}",
    "{a} x {b} = ?",
    "kak, {a} dikali {b} berapa?",
    "coba kalikan {a} dengan {b}",
    "berapa hasil {a} kali {b}?",
    "hitung cepat: {a} x {b}",
    "{a} dikali {b} hasilnya berapa?",
    "aku mau nanya, {a} x {b} itu berapa?",
    "bantu hitung {a} kali {b} dong",
    "kalau {a} x {b}, hasilnya?",
    "berapa ya {a} kali {b}?",
    "jujur aku lupa, {a} x {b} sama dengan berapa?",
    "coba tebak hasil {a} x {b}",
]
Q_DIV = [
    "berapa {a} : {b}?",
    "hasil dari {a} : {b} berapa?",
    "tolong hitung {a} dibagi {b}",
    "{a} : {b} = ?",
    "kak, {a} dibagi {b} berapa?",
    "coba bagi {a} dengan {b}",
    "berapa hasil {a} dibagi {b}?",
    "hitung cepat: {a} : {b}",
    "{a} dibagi {b} hasilnya berapa?",
    "aku mau nanya, {a} : {b} itu berapa?",
    "bantu hitung {a} dibagi {b} dong",
    "kalau {a} : {b}, hasilnya?",
    "berapa ya {a} dibagi {b}?",
    "jujur aku lupa, {a} : {b} sama dengan berapa?",
    "coba tebak hasil {a} : {b}",
]

NAMES = [
    "Nia", "Budi", "Siti", "Rizky", "Eka", "Andi", "Dewi", "Hendra", "Lina",
    "Bayu", "Putri", "Fajar", "Intan", "Dimas", "Ayu", "Raka", "Sari", "Tono",
    "Maya", "Yoga", "Nadia", "Reza", "Vina", "Adit", "Citra", "Gilang", "Hana",
    "Ivan", "Joko", "Kiki", "Lukman", "Mira", "Nanda", "Oki", "Prita", "Qori",
    "Rina", "Sinta", "Tia", "Umar", "Wulan", "Yuni", "Zaki", "Alfi", "Bella",
]

OBJECTS = [
    ("apel", "buah"), ("jeruk", "buah"), ("mangga", "buah"), ("pisang", "buah"),
    ("permen", "butir"), ("kelereng", "butir"), ("buku", "buku"), ("pensil", "batang"),
    ("stiker", "lembar"), ("roti", "potong"), ("telur", "butir"), ("donat", "buah"),
    ("koin", "keping"), ("kue", "potong"), ("bola", "buah"), ("kartu", "lembar"),
    ("manggis", "buah"), ("salak", "buah"), ("durian", "buah"), ("rambutan", "buah"),
    ("jambu", "buah"), ("semangka", "buah"), ("nanas", "buah"), ("pepaya", "buah"),
    ("susu", "kotak"), ("air", "gelas"), ("nasi", "porsi"), ("mi", "porsi"),
    ("baju", "potong"), ("sepatu", "pasang"), ("tas", "buah"), ("topi", "buah"),
    ("bunga", "tangkai"), ("daun", "lembar"), ("ikan", "ekor"), ("ayam", "ekor"),
    ("kambing", "ekor"), ("sapi", "ekor"), ("mobil", "unit"), ("motor", "unit"),
]


def _split_last_place(n: int) -> tuple[int, int]:
    """Pecah n menjadi (puluhan, satuan), mis. 74 -> (70, 4)."""
    return n // 10 * 10, n % 10


def _answer_add(b: Builder, a: int, bb: int, key: str) -> str:
    result = a + bb
    tens, units = _split_last_place(bb)
    if tens:
        step = f"Aku jumlahkan {fmt_id(a)} dengan {fmt_id(tens)} dulu, dapat {fmt_id(a + tens)}, lalu ditambah {units} jadi {fmt_id(result)}."
    else:
        step = f"Tinggal tambahkan {units} ke {fmt_id(a)}, hasilnya {fmt_id(result)}."
    return b.pick(
        [
            f"{fmt_id(a)} + {fmt_id(bb)} = {fmt_id(result)}. {step}",
            f"Hasilnya {fmt_id(result)}. Caranya, {fmt_id(a)} ditambah {fmt_id(bb)} sama dengan {fmt_id(result)}.",
            f"{fmt_id(a)} + {fmt_id(bb)} = {fmt_id(result)}. Kalau dicek mundur, {fmt_id(result)} - {fmt_id(bb)} = {fmt_id(a)}, jadi jawabannya pas.",
            f"Jumlahnya {fmt_id(result)}. {step}",
            f"Itu sama dengan {fmt_id(result)}. {fmt_id(a)} + {fmt_id(bb)} = {fmt_id(result)}, nggak ada sisa.",
            f"Jawabannya {fmt_id(result)}. Kalau {fmt_id(bb)} ditambah {fmt_id(a)}, hasilnya juga {fmt_id(result)} karena urutan penjumlahan boleh dibalik.",
            f"{fmt_id(result)}, itu hasilnya. Aku jumlahkan {fmt_id(a)} dengan {fmt_id(bb)} dan dapat {fmt_id(result)}.",
            f"Hasil penjumlahannya {fmt_id(result)}. Coba bayangkan {fmt_id(a)} langkah lalu {fmt_id(bb)} langkah lagi, totalnya {fmt_id(result)}.",
        ],
        key,
    )


def _answer_sub(b: Builder, a: int, bb: int, key: str) -> str:
    result = a - bb
    tens, units = _split_last_place(bb)
    if tens:
        step = f"Aku kurangi {fmt_id(a)} dengan {fmt_id(tens)} dulu, dapat {fmt_id(a - tens)}, lalu dikurangi {units} jadi {fmt_id(result)}."
    else:
        step = f"Tinggal kurangi {units} dari {fmt_id(a)}, hasilnya {fmt_id(result)}."
    return b.pick(
        [
            f"{fmt_id(a)} - {fmt_id(bb)} = {fmt_id(result)}. {step}",
            f"Hasilnya {fmt_id(result)}. Kalau {fmt_id(a)} dikurangi {fmt_id(bb)}, yang tersisa {fmt_id(result)}.",
            f"{fmt_id(a)} - {fmt_id(bb)} = {fmt_id(result)}. Cek pakai {fmt_id(result)} + {fmt_id(bb)} = {fmt_id(a)}, jadi benar.",
            f"Jawabannya {fmt_id(result)}. {step}",
            f"Sisanya {fmt_id(result)}. {fmt_id(a)} dikurangi {fmt_id(bb)} memang {fmt_id(result)}.",
            f"{fmt_id(result)}, itu hasilnya. Kalau {fmt_id(result)} ditambah {fmt_id(bb)} lagi, balik ke {fmt_id(a)}.",
            f"Hasil pengurangannya {fmt_id(result)}. Angka {fmt_id(a)} kalau diambil {fmt_id(bb)} tinggal {fmt_id(result)}.",
            f"Jawabannya {fmt_id(result)}. {fmt_id(a)} - {fmt_id(bb)} = {fmt_id(result)}, dan nggak ada sisa yang tertinggal.",
        ],
        key,
    )


def _answer_mul(b: Builder, a: int, bb: int, key: str) -> str:
    result = a * bb
    tens, units = _split_last_place(a)
    if tens and units:
        p1 = tens * bb
        p2 = units * bb
        step = (
            f"Aku pecah {a} jadi {fmt_id(tens)} + {units}. "
            f"{fmt_id(tens)} x {bb} = {fmt_id(p1)}, lalu {units} x {bb} = {p2}, "
            f"dan {fmt_id(p1)} + {p2} = {fmt_id(result)}."
        )
    elif bb <= 5:
        step = f"Kalau dijumlah berulang, {' + '.join([str(a)] * bb)} = {fmt_id(result)}."
    else:
        step = f"Tinggal kalikan {a} dengan {bb}, hasilnya {fmt_id(result)}."
    return b.pick(
        [
            f"{a} x {bb} = {fmt_id(result)}. {step}",
            f"Hasilnya {fmt_id(result)}. {a} dikali {bb} sama dengan {fmt_id(result)}.",
            f"{a} x {bb} = {fmt_id(result)}. Kalau dibalik, {bb} x {a} juga {fmt_id(result)}, jadi hasilnya tetap.",
            f"Jawabannya {fmt_id(result)}. {step}",
            f"{fmt_id(result)}, itu hasilnya. Aku kalikan {a} dengan {bb} dan dapat {fmt_id(result)}.",
            f"Hasil perkaliannya {fmt_id(result)}. Bayangkan {bb} kelompok yang masing-masing berisi {a}, totalnya {fmt_id(result)}.",
            f"{a} x {bb} = {fmt_id(result)}. {step}",
        ],
        key,
    )


def _answer_div(b: Builder, a: int, bb: int, key: str) -> str:
    result = a // bb
    return b.pick(
        [
            f"{fmt_id(a)} : {bb} = {result}. Karena {bb} x {result} = {fmt_id(a)}, hasilnya {result}.",
            f"Hasilnya {result}. Aku cek pakai perkalian: {result} x {bb} = {fmt_id(a)}, cocok.",
            f"{fmt_id(a)} dibagi {bb} = {result}. Nggak ada sisa, jadi pembagiannya pas.",
            f"Jawabannya {result}. Kalau {result} dikali {bb}, balik lagi ke {fmt_id(a)}.",
            f"{fmt_id(a)} : {bb} = {result}. Jadi kalau dibagi rata ke {bb} bagian, tiap bagian isinya {result}.",
            f"{result}, itu hasilnya. Aku bagi {fmt_id(a)} jadi {bb} bagian sama besar, isinya {result}.",
        ],
        key,
    )


def gen_arithmetic(b: Builder, rng: random.Random, scale: float = 1.0) -> None:
    """Penjumlahan, pengurangan, perkalian, pembagian."""
    specs: list[tuple[str, Callable, Callable, int, int, int]] = [
        ("tambah", Q_ADD, _answer_add, 10, 989, int(2400 * scale)),
        ("kurang", Q_SUB, _answer_sub, 50, 999, int(2400 * scale)),
        ("kali", Q_MUL, _answer_mul, 2, 99, int(4200 * scale)),
        ("bagi", Q_DIV, _answer_div, 2, 40, int(3000 * scale)),
    ]
    for name, questions, answer_fn, lo, hi, quota in specs:
        added = 0
        tries = 0
        while added < quota and tries < quota * 30:
            tries += 1
            if name == "bagi":
                divisor = rng.randint(lo, hi)
                quotient = rng.randint(3, 60)
                a = divisor * quotient
                if a > 2400:
                    continue
                c = divisor
            else:
                a = rng.randint(lo, hi)
                c = rng.randint(lo, hi)
                if name == "kurang":
                    if c >= a:
                        continue
                elif name == "kali":
                    c = rng.randint(3, 30)
                if a == c:
                    continue
            key = f"{name}-{a}-{c}"
            question = b.pick(questions, key).format(a=fmt_id(a), b=fmt_id(c))
            answer = answer_fn(b, a, c, key)
            if b.add(question, answer, "matematika", fact=f"op:{name}:{a}:{c}"):
                added += 1


def gen_remainder(b: Builder, quota: int, rng: random.Random) -> None:
    variants = [
        "berapa hasil {a} dibagi {b}? Kasih tahu sisanya juga.",
        "{a} dibagi {b} berapa, sisa berapa?",
        "hitung {a} : {b} lengkap dengan sisanya",
        "kalau {a} dibagi {b}, hasil dan sisanya berapa?",
        "aku mau bagi {a} ke {b} orang, tiap orang dapat berapa dan sisanya?",
    ]
    added = 0
    tries = 0
    while added < quota and tries < quota * 40:
        tries += 1
        divisor = rng.randint(3, 19)
        quotient = rng.randint(2, 30)
        remainder = rng.randint(1, divisor - 1)
        a = divisor * quotient + remainder
        key = f"sisa-{a}-{divisor}"
        question = b.pick(variants, key).format(a=a, b=divisor)
        answer = b.pick(
            [
                f"{a} : {divisor} hasilnya {quotient} dengan sisa {remainder}. Karena {divisor} x {quotient} = {divisor * quotient}, lalu {a} - {divisor * quotient} = {remainder}.",
                f"Hasilnya {quotient}, sisanya {remainder}. Cek: {divisor} x {quotient} + {remainder} = {a}, jadi hitungannya pas.",
                f"{a} dibagi {divisor} dapat {quotient} dan sisa {remainder}. Sisanya nggak bisa dibagi lagi karena lebih kecil dari {divisor}.",
                f"Jawabannya {quotient} sisa {remainder}. Kalau {remainder} masih dibagi {divisor}, hasilnya pecahan, jadi cukup ditulis sebagai sisa.",
            ],
            key,
        )
        if b.add(question, answer, "matematika", fact=f"sisa:{a}:{divisor}"):
            added += 1


def gen_percent(b: Builder, quota: int, rng: random.Random) -> None:
    percents = [5, 10, 15, 20, 25, 30, 40, 50, 60, 75, 80]
    qs = [
        "berapa {p} persen dari {n}?",
        "hitung {p}% dari {n}",
        "{p}% dari {n} itu berapa?",
        "tolong cari {p} persen dari {n}",
        "kalau {p}% dari {n}, hasilnya berapa?",
    ]
    added = 0
    tries = 0
    while added < quota and tries < quota * 40:
        tries += 1
        p = rng.choice(percents)
        result = rng.randint(3, 900)
        if (result * 100) % p != 0:
            continue
        n = result * 100 // p
        if n > 20000 or n < 20:
            continue
        key = f"persen-{p}-{n}"
        question = b.pick(qs, key).format(p=p, n=fmt_id(n))
        answer = b.pick(
            [
                f"{p}% dari {fmt_id(n)} adalah {fmt_id(result)}. Caranya, {fmt_id(n)} x {p} : 100 = {fmt_id(result)}.",
                f"Hasilnya {fmt_id(result)}. Aku ubah {p}% jadi {p}/100, lalu {fmt_id(n)} x {p}/100 = {fmt_id(result)}.",
                f"{fmt_id(result)}, itu jawabannya. Karena {p}% sama dengan {p} per seratus, hasilnya {fmt_id(n)} x {p} : 100 = {fmt_id(result)}.",
                f"Nilainya {fmt_id(result)}. Karena {p}% itu {p} dari 100 bagian, aku hitung {fmt_id(n)} x {p} = {fmt_id(n * p)}, lalu dibagi 100 jadi {fmt_id(result)}.",
            ],
            key,
        )
        if b.add(question, answer, "matematika", fact=f"persen:{p}:{n}"):
            added += 1


def gen_rounding(b: Builder, quota: int, rng: random.Random) -> None:
    units = [(10, "puluhan"), (100, "ratusan"), (1000, "ribuan")]
    qs = [
        "bulatkan {n} ke {unit} terdekat",
        "{n} kalau dibulatkan ke {unit} terdekat jadi berapa?",
        "tolong bulatkan {n} ke {unit} terdekat",
        "berapa hasil pembulatan {n} ke {unit}?",
    ]
    added = 0
    tries = 0
    while added < quota and tries < quota * 20:
        tries += 1
        unit, label = rng.choice(units)
        n = rng.randint(11, 9999)
        rounded = (n + unit // 2) // unit * unit
        if rounded == n:
            continue
        key = f"bulat-{n}-{unit}"
        question = b.pick(qs, key).format(n=fmt_id(n), unit=label)
        look = (n // (unit // 10)) % 10
        other = rounded - unit if n < rounded else rounded + unit
        if abs(rounded - n) == abs(other - n):
            second = f"Hasilnya {fmt_id(rounded)}. Karena angkanya tepat di tengah, pembulatan dilakukan ke atas."
        else:
            second = f"Hasilnya {fmt_id(rounded)}. Karena {fmt_id(n)} lebih dekat ke {fmt_id(rounded)} daripada ke {fmt_id(other)}."
        answer = b.pick(
            [
                f"{fmt_id(n)} dibulatkan ke {label} terdekat menjadi {fmt_id(rounded)}. Angka di belakang {label} adalah {look}, jadi hasilnya {fmt_id(rounded)}.",
                second,
                f"Jadi {fmt_id(rounded)}. Aku lihat angka di belakang {label}, lalu bulatkan ke atas atau ke bawah sesuai jarak terdekat.",
                f"Pembulatannya {fmt_id(rounded)}. Selisihnya cuma {fmt_id(abs(rounded - n))}, jadi {fmt_id(rounded)} adalah pilihan terdekat.",
            ],
            key,
        )
        if b.add(question, answer, "matematika", fact=f"bulat:{n}:{unit}"):
            added += 1


def gen_compare(b: Builder, quota: int, rng: random.Random) -> None:
    added = 0
    tries = 0
    while added < quota and tries < quota * 20:
        tries += 1
        a = rng.randint(10, 9999)
        c = rng.randint(10, 9999)
        if a == c:
            continue
        big, small = max(a, c), min(a, c)
        key = f"banding-{big}-{small}"
        if rng.random() < 0.5:
            question = b.pick(
                [
                    "mana yang lebih besar, {a} atau {b}?",
                    "antara {a} dan {b}, mana yang lebih besar?",
                    "{a} sama {b}, mana yang lebih gede?",
                ],
                key,
            ).format(a=fmt_id(a), b=fmt_id(c))
            answer = b.pick(
                [
                    f"{fmt_id(big)} lebih besar daripada {fmt_id(small)}. Selisihnya {fmt_id(big - small)}, jadi jelas {fmt_id(big)} yang lebih besar.",
                    f"Yang lebih besar adalah {fmt_id(big)}. Kalau dibandingkan, {fmt_id(big)} - {fmt_id(small)} = {fmt_id(big - small)}.",
                    f"{fmt_id(big)}, karena posisinya lebih ke kanan di garis bilangan dan selisihnya {fmt_id(big - small)}.",
                ],
                key,
            )
        else:
            question = b.pick(
                [
                    "mana yang lebih kecil, {a} atau {b}?",
                    "antara {a} dan {b}, mana yang lebih kecil?",
                    "{a} sama {b}, mana yang lebih kecil?",
                ],
                key,
            ).format(a=fmt_id(a), b=fmt_id(c))
            answer = b.pick(
                [
                    f"{fmt_id(small)} lebih kecil daripada {fmt_id(big)}. Selisihnya {fmt_id(big - small)}, jadi {fmt_id(small)} yang lebih kecil.",
                    f"Yang lebih kecil adalah {fmt_id(small)}. Kalau {fmt_id(big)} dikurangi {fmt_id(small)}, selisihnya {fmt_id(big - small)}.",
                    f"{fmt_id(small)}, karena nilainya lebih rendah {fmt_id(big - small)} dari {fmt_id(big)}.",
                ],
                key,
            )
        if b.add(question, answer, "matematika", fact=f"banding:{big}:{small}"):
            added += 1


def gen_sequence(b: Builder, quota: int, rng: random.Random) -> None:
    added = 0
    tries = 0
    qs = [
        "lanjutkan deret ini: {seq}",
        "deret berikutnya berapa: {seq}",
        "coba lanjutkan pola angka ini: {seq}",
        "pola bilangan ini lanjutannya apa: {seq}",
        "tebak dua angka selanjutnya dari deret {seq}",
    ]
    while added < quota and tries < quota * 30:
        tries += 1
        kind = rng.choice(["aritmetika", "geometri", "kuadrat", "ganjil", "genap"])
        if kind == "aritmetika":
            start = rng.randint(1, 40)
            step = rng.randint(2, 15)
            seq = [start + i * step for i in range(5)]
            nxt = [seq[-1] + step, seq[-1] + 2 * step]
            rule = f"polanya ditambah {step} setiap langkah"
        elif kind == "geometri":
            start = rng.randint(1, 6)
            ratio = rng.choice([2, 3, 4, 5])
            seq = [start * ratio ** i for i in range(5)]
            if seq[-1] * ratio > 100000:
                continue
            nxt = [seq[-1] * ratio, seq[-1] * ratio * ratio]
            rule = f"polanya dikali {ratio} setiap langkah"
        elif kind == "kuadrat":
            start = rng.randint(1, 8)
            seq = [(start + i) ** 2 for i in range(5)]
            nxt = [(start + 5) ** 2, (start + 6) ** 2]
            rule = "polanya bilangan kuadrat berurutan"
        elif kind == "ganjil":
            start = rng.randint(1, 4) * 2 - 1
            seq = [start + 2 * i for i in range(6)]
            nxt = [seq[-1] + 2, seq[-1] + 4]
            rule = "polanya bilangan ganjil, jadi naik 2 setiap langkah"
        else:
            start = rng.randint(1, 4) * 2
            seq = [start + 2 * i for i in range(6)]
            nxt = [seq[-1] + 2, seq[-1] + 4]
            rule = "polanya bilangan genap, jadi naik 2 setiap langkah"
        seq_text = ", ".join(fmt_id(x) for x in seq)
        key = f"deret-{'-'.join(map(str, seq))}"
        question = b.pick(qs, key).format(seq=seq_text)
        answer = b.pick(
            [
                f"Lanjutannya {fmt_id(nxt[0])} lalu {fmt_id(nxt[1])}, karena {rule}.",
                f"Dua angka berikutnya {fmt_id(nxt[0])} dan {fmt_id(nxt[1])}. Aku cek selisihnya, ternyata {rule}.",
                f"Jawabannya {fmt_id(nxt[0])}, {fmt_id(nxt[1])}. Dari deret itu kelihatan {rule}.",
                f"Setelah {fmt_id(seq[-1])} datang {fmt_id(nxt[0])} dan {fmt_id(nxt[1])}. {rule.capitalize()}.",
            ],
            key,
        )
        if b.add(question, answer, "matematika", fact=f"deret:{'-'.join(map(str, seq))}"):
            added += 1


def gen_average(b: Builder, quota: int, rng: random.Random) -> None:
    added = 0
    tries = 0
    qs = [
        "rata-rata dari {nums} berapa?",
        "hitung rata-rata bilangan ini: {nums}",
        "kalau nilainya {nums}, rata-ratanya berapa?",
        "tolong cari rata-rata dari {nums}",
    ]
    while added < quota and tries < quota * 30:
        tries += 1
        count = rng.randint(3, 5)
        mean = rng.randint(20, 95)
        nums = [mean + rng.randint(-15, 15) for _ in range(count)]
        if sum(nums) != mean * count:
            nums[-1] += mean * count - sum(nums)
        if any(n < 0 for n in nums):
            continue
        key = f"rata-{'-'.join(map(str, nums))}"
        text = ", ".join(str(n) for n in nums)
        question = b.pick(qs, key).format(nums=text)
        answer = b.pick(
            [
                f"Rata-ratanya {mean}. Jumlah semua angkanya {sum(nums)}, lalu dibagi {count} hasilnya {mean}.",
                f"Hasilnya {mean}. Caranya, {' + '.join(map(str, nums))} = {sum(nums)}, terus {sum(nums)} : {count} = {mean}.",
                f"Rata-ratanya {fmt_id(mean)}. Totalnya {sum(nums)} dan banyak datanya {count}, jadi {sum(nums)} : {count} = {mean}.",
                f"Nilainya {mean}. Aku jumlahkan dulu semua bilangan, lalu bagi dengan jumlah data, hasilnya {mean}.",
            ],
            key,
        )
        if b.add(question, answer, "matematika", fact=f"rata:{key}"):
            added += 1


def _is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    for d in range(3, int(n ** 0.5) + 1, 2):
        if n % d == 0:
            return False
    return True


def _smallest_factor(n: int) -> int:
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            return d
    return n


def gen_prime(b: Builder, quota: int, rng: random.Random) -> None:
    added = 0
    tries = 0
    qs = [
        "apa {n} itu bilangan prima?",
        "{n} bilangan prima atau bukan?",
        "cek dong, {n} prima bukan?",
        "menurut kamu {n} termasuk bilangan prima?",
    ]
    while added < quota and tries < quota * 20:
        tries += 1
        n = rng.randint(2, 200)
        key = f"prima-{n}"
        prime = _is_prime(n)
        question = b.pick(qs, key).format(n=n)
        if prime:
            answer = b.pick(
                [
                    f"Iya, {n} bilangan prima. Faktornya cuma 1 dan {n}, nggak ada bilangan lain yang bisa membaginya habis.",
                    f"Betul, {n} prima. Coba bagi dengan 2, 3, 5, dan seterusnya sampai akar {n}, nggak ada yang pas.",
                    f"{n} termasuk bilangan prima, karena hanya bisa dibagi 1 dan {n} tanpa sisa.",
                ],
                key,
            )
        else:
            d = _smallest_factor(n)
            answer = b.pick(
                [
                    f"Bukan, {n} bukan bilangan prima. Pembagi terkecilnya {d}, karena {d} x {n // d} = {n}.",
                    f"{n} bukan prima. Angka itu bisa dibagi {d}, jadi punya faktor selain 1 dan {n}.",
                    f"Bukan prima. {n} habis dibagi {d}, hasilnya {n // d}.",
                ],
                key,
            )
        if b.add(question, answer, "matematika", fact=key):
            added += 1


def gen_factors(b: Builder, quota: int, rng: random.Random) -> None:
    added = 0
    tries = 0
    qs = [
        "sebutkan semua faktor dari {n}",
        "faktor bilangan {n} apa saja?",
        "apa saja faktor dari {n}?",
        "tolong daftar faktor dari {n}",
    ]
    while added < quota and tries < quota * 20:
        tries += 1
        n = rng.randint(6, 120)
        factors = [d for d in range(1, n + 1) if n % d == 0]
        if len(factors) < 4:
            continue
        key = f"faktor-{n}"
        question = b.pick(qs, key).format(n=n)
        answer = b.pick(
            [
                f"Faktor dari {n} ada {len(factors)}, yaitu {', '.join(map(str, factors))}. Semuanya membagi {n} tanpa sisa.",
                f"Faktornya {', '.join(map(str, factors))}. Jumlahnya {len(factors)} faktor, dari 1 sampai {n}.",
                f"Bilangan yang bisa membagi {n} habis adalah {', '.join(map(str, factors))}. Total ada {len(factors)}.",
            ],
            key,
        )
        if b.add(question, answer, "matematika", fact=key):
            added += 1


def gen_gcd_lcm(b: Builder, quota: int, rng: random.Random) -> None:
    added = 0
    tries = 0
    while added < quota and tries < quota * 30:
        tries += 1
        a = rng.randint(4, 72)
        c = rng.randint(4, 72)
        if a == c:
            continue
        g = math.gcd(a, c)
        l = a * c // g
        key = f"kpk-{min(a, c)}-{max(a, c)}" if rng.random() < 0.5 else f"fpb-{min(a, c)}-{max(a, c)}"
        if key.startswith("kpk"):
            question = b.pick(
                ["berapa KPK dari {a} dan {b}?", "cari KPK {a} dan {b} dong", "KPK {a} dan {b} berapa ya?"],
                key,
            ).format(a=a, b=c)
            answer = b.pick(
                [
                    f"KPK dari {a} dan {c} adalah {l}. Karena {l} adalah kelipatan terkecil yang sama-sama muncul di kelipatan {a} dan {c}.",
                    f"Hasilnya {l}. Aku pakai hubungan KPK x FPB = {a} x {c}, dengan FPB {g}, jadi KPK = {a * c} : {g} = {l}.",
                    f"KPK-nya {l}. Kelipatan {a} dan {c} pertama kali bertemu di angka {l}.",
                ],
                key,
            )
        else:
            question = b.pick(
                ["berapa FPB dari {a} dan {b}?", "cari FPB {a} dan {b} dong", "FPB {a} dan {b} berapa ya?"],
                key,
            ).format(a=a, b=c)
            answer = b.pick(
                [
                    f"FPB dari {a} dan {c} adalah {g}. Itu bilangan terbesar yang bisa membagi habis keduanya.",
                    f"Hasilnya {g}. Aku cari faktor persekutuan terbesar dari {a} dan {c}, ketemunya {g}.",
                    f"FPB-nya {g}. Cek: {a} : {g} = {a // g} dan {c} : {g} = {c // g}, dua-duanya bulat.",
                ],
                key,
            )
        if b.add(question, answer, "matematika", fact=key):
            added += 1


def gen_powers(b: Builder, quota: int, rng: random.Random) -> None:
    added = 0
    tries = 0
    while added < quota and tries < quota * 30:
        tries += 1
        kind = rng.choice(["kuadrat", "akar", "kubik", "pangkat"])
        if kind == "kuadrat":
            n = rng.randint(2, 40)
            key = f"kuadrat-{n}"
            question = b.pick(
                ["berapa {n} kuadrat?", "{n} pangkat 2 hasilnya berapa?", "hitung {n} kuadrat dong"], key
            ).format(n=n)
            answer = f"{n} kuadrat adalah {n * n}. Artinya {n} dikali {n}, hasilnya {n * n}."
        elif kind == "akar":
            n = rng.randint(2, 40)
            key = f"akar-{n}"
            question = b.pick(
                ["berapa akar kuadrat dari {sq}?", "akar dari {sq} berapa?", "hitung akar kuadrat {sq}"], key
            ).format(sq=n * n)
            answer = f"Akar kuadrat dari {n * n} adalah {n}, karena {n} x {n} = {n * n}."
        elif kind == "kubik":
            n = rng.randint(2, 12)
            key = f"kubik-{n}"
            question = b.pick(
                ["berapa {n} pangkat 3?", "hitung {n} kubik dong", "{n} pangkat tiga hasilnya berapa?"], key
            ).format(n=n)
            answer = f"{n} pangkat 3 adalah {n ** 3}. Caranya, {n} x {n} = {n * n}, lalu {n * n} x {n} = {n ** 3}."
        else:
            base = rng.randint(2, 9)
            exp = rng.randint(3, 6)
            value = base ** exp
            if value > 500000:
                continue
            key = f"pangkat-{base}-{exp}"
            question = b.pick(
                ["berapa {a} pangkat {b}?", "hitung {a}^{b} dong", "{a} dipangkatkan {b} hasilnya berapa?"], key
            ).format(a=base, b=exp)
            answer = f"{base} pangkat {exp} adalah {fmt_id(value)}. Artinya {base} dikali dirinya sendiri sebanyak {exp} kali, hasilnya {fmt_id(value)}."
        if b.add(question, answer, "matematika", fact=key):
            added += 1


def gen_conversion(b: Builder, quota: int, rng: random.Random) -> None:
    specs = [
        ("km", "m", 1000, "panjang"),
        ("m", "cm", 100, "panjang"),
        ("cm", "mm", 10, "panjang"),
        ("kg", "g", 1000, "berat"),
        ("g", "mg", 1000, "berat"),
        ("liter", "ml", 1000, "volume"),
        ("jam", "menit", 60, "waktu"),
        ("menit", "detik", 60, "waktu"),
        ("hari", "jam", 24, "waktu"),
        ("minggu", "hari", 7, "waktu"),
    ]
    added = 0
    tries = 0
    while added < quota and tries < quota * 20:
        tries += 1
        src, dst, factor, kind = rng.choice(specs)
        n = rng.randint(2, 60)
        key = f"konversi-{src}-{dst}-{n}"
        question = b.pick(
            [
                "{n} {src} berapa {dst}?",
                "tolong ubah {n} {src} ke {dst}",
                "{n} {src} itu sama dengan berapa {dst}?",
                "kalau {n} {src}, berapa {dst}?",
            ],
            key,
        ).format(n=n, src=src, dst=dst)
        answer = b.pick(
            [
                f"{n} {src} = {fmt_id(n * factor)} {dst}. Karena 1 {src} sama dengan {fmt_id(factor)} {dst}, tinggal dikali {fmt_id(factor)}.",
                f"Hasilnya {fmt_id(n * factor)} {dst}. Caranya, {n} x {fmt_id(factor)} = {fmt_id(n * factor)}.",
                f"{n} {src} sama dengan {fmt_id(n * factor)} {dst}. Satu {src} itu {fmt_id(factor)} {dst}, jadi {n} kali {fmt_id(factor)}.",
            ],
            key,
        )
        if b.add(question, answer, "matematika", fact=key):
            added += 1


def gen_discount(b: Builder, quota: int, rng: random.Random) -> None:
    added = 0
    tries = 0
    qs = [
        "harga barang {price} didiskon {p}%. Berapa harga setelah diskon?",
        "sebuah baju harganya {price}, dapat diskon {p}%. Jadi berapa yang harus dibayar?",
        "{price} diskon {p} persen, berapa potongannya dan harga akhirnya?",
        "kalau harga {price} turun {p}%, harga barunya berapa?",
    ]
    while added < quota and tries < quota * 30:
        tries += 1
        price = rng.randrange(20, 400) * 1000
        p = rng.choice([10, 15, 20, 25, 30, 40, 50])
        cut = price * p // 100
        final = price - cut
        if cut <= 0:
            continue
        key = f"diskon-{price}-{p}"
        question = b.pick(qs, key).format(price=fmt_rp(price), p=p)
        answer = b.pick(
            [
                f"Potongannya {fmt_rp(cut)}, jadi harga akhirnya {fmt_rp(final)}. Caranya, {fmt_rp(price)} x {p}% = {fmt_rp(cut)}, lalu dikurangkan.",
                f"Harga setelah diskon {fmt_rp(final)}. Diskon {p}% dari {fmt_rp(price)} adalah {fmt_rp(cut)}.",
                f"Yang perlu dibayar {fmt_rp(final)}. Aku hitung {fmt_rp(price)} - {fmt_rp(cut)} = {fmt_rp(final)}.",
                f"Harga barunya {fmt_rp(final)}. Kalau diskonnya {p}%, berarti yang dibayar {100 - p}% dari harga awal, yaitu {fmt_rp(final)}.",
            ],
            key,
        )
        if b.add(question, answer, "matematika", fact=key):
            added += 1


def gen_money_change(b: Builder, quota: int, rng: random.Random) -> None:
    added = 0
    tries = 0
    qs = [
        "{name} membeli {item} seharga {price} dan membayar dengan {pay}. Berapa kembaliannya?",
        "harga {item} {price}, dibayar pakai uang {pay}. Kembaliannya berapa?",
        "{name} belanja {item} {price} lalu menyerahkan {pay}. Berapa uang kembalinya?",
    ]
    while added < quota and tries < quota * 30:
        tries += 1
        price = rng.randrange(5, 95) * 1000
        pay = rng.choice([20000, 50000, 100000])
        if pay <= price:
            continue
        name = rng.choice(NAMES)
        item = rng.choice(["buku", "pensil", "tas", "sepatu", "mainan", "kue", "minuman", "baju"])
        change = pay - price
        key = f"kembali-{price}-{pay}-{name}-{item}"
        question = b.pick(qs, key).format(name=name, item=item, price=fmt_rp(price), pay=fmt_rp(pay))
        answer = b.pick(
            [
                f"Kembaliannya {fmt_rp(change)}. Caranya, {fmt_rp(pay)} - {fmt_rp(price)} = {fmt_rp(change)}.",
                f"Uang kembalinya {fmt_rp(change)}. Karena dibayar {fmt_rp(pay)} dan belanjanya {fmt_rp(price)}.",
                f"Kembalian {name} adalah {fmt_rp(change)}. Selisih uang bayar dan harga barang segitu.",
            ],
            key,
        )
        if b.add(question, answer, "matematika", fact=key):
            added += 1


def gen_time(b: Builder, quota: int, rng: random.Random) -> None:
    added = 0
    tries = 0
    qs = [
        "film mulai jam {h}.{m:02d} dan durasinya {dur} menit. Selesai jam berapa?",
        "acara dimulai pukul {h}.{m:02d}, lama acara {dur} menit. Jam berapa selesai?",
        "kalau mulai jam {h}.{m:02d} lalu berlangsung {dur} menit, selesainya kapan?",
    ]
    while added < quota and tries < quota * 30:
        tries += 1
        h = rng.randint(6, 20)
        m = rng.choice([0, 10, 15, 20, 30, 40, 45, 50])
        dur = rng.choice([30, 45, 60, 75, 90, 120, 135, 150])
        total = h * 60 + m + dur
        if total >= 24 * 60:
            continue
        eh, em = divmod(total, 60)
        key = f"waktu-{h}-{m}-{dur}"
        question = b.pick(qs, key).format(h=h, m=m, dur=dur)
        answer = b.pick(
            [
                f"Selesai jam {eh}.{em:02d}. Caranya, {h}.{m:02d} ditambah {dur} menit, hasilnya {eh}.{em:02d}.",
                f"Jam {eh}.{em:02d}. Jam {h}.{m:02d} itu {h * 60 + m} menit sejak tengah malam, ditambah {dur} menit jadi {total} menit, atau {eh}.{em:02d}.",
                f"Berakhir pukul {eh}.{em:02d}. Durasi {dur} menit itu setara {dur // 60} jam {dur % 60} menit, lalu ditambahkan ke jam mulai.",
            ],
            key,
        )
        if b.add(question, answer, "matematika", fact=key):
            added += 1


def gen_geometry(b: Builder, quota: int, rng: random.Random) -> None:
    added = 0
    tries = 0
    while added < quota and tries < quota * 30:
        tries += 1
        kind = rng.choice(["persegi_panjang_luas", "persegi_panjang_keliling", "persegi_luas", "segitiga_luas"])
        if kind == "persegi_panjang_luas":
            p = rng.randint(3, 40)
            l = rng.randint(2, 30)
            key = f"pp-luas-{p}-{l}"
            question = b.pick(
                [
                    "persegi panjang punya panjang {p} cm dan lebar {l} cm. Berapa luasnya?",
                    "hitung luas persegi panjang dengan panjang {p} cm dan lebar {l} cm",
                    "luas persegi panjang {p} cm x {l} cm berapa?",
                ],
                key,
            ).format(p=p, l=l)
            answer = f"Luas persegi panjang itu {p * l} cm persegi. Caranya, panjang x lebar = {p} x {l} = {p * l}."
        elif kind == "persegi_panjang_keliling":
            p = rng.randint(3, 40)
            l = rng.randint(2, 30)
            key = f"pp-keliling-{p}-{l}"
            question = b.pick(
                [
                    "persegi panjang {p} cm x {l} cm, berapa kelilingnya?",
                    "hitung keliling persegi panjang dengan panjang {p} cm dan lebar {l} cm",
                    "keliling persegi panjang {p} cm dan {l} cm berapa?",
                ],
                key,
            ).format(p=p, l=l)
            answer = f"Kelilingnya {2 * (p + l)} cm. Caranya, 2 x (panjang + lebar) = 2 x ({p} + {l}) = {2 * (p + l)} cm."
        elif kind == "persegi_luas":
            s = rng.randint(2, 30)
            key = f"persegi-{s}"
            question = b.pick(
                ["persegi dengan sisi {s} cm, luasnya berapa?", "hitung luas persegi bersisi {s} cm", "luas persegi sisi {s} cm berapa?"],
                key,
            ).format(s=s)
            answer = f"Luasnya {s * s} cm persegi, karena sisi x sisi = {s} x {s} = {s * s}."
        else:
            a = rng.randrange(2, 30)
            t = rng.randrange(2, 25)
            area_num = a * t
            if area_num % 2 != 0:
                continue
            key = f"segitiga-{a}-{t}"
            question = b.pick(
                [
                    "segitiga punya alas {a} cm dan tinggi {t} cm. Berapa luasnya?",
                    "hitung luas segitiga dengan alas {a} cm dan tinggi {t} cm",
                    "luas segitiga alas {a} cm tinggi {t} cm berapa?",
                ],
                key,
            ).format(a=a, t=t)
            answer = f"Luasnya {area_num // 2} cm persegi. Caranya, setengah x alas x tinggi = 1/2 x {a} x {t} = {area_num // 2}."
        if b.add(question, answer, "matematika", fact=key):
            added += 1


def gen_fraction(b: Builder, quota: int, rng: random.Random) -> None:
    added = 0
    tries = 0
    fracs = [(1, 2), (1, 3), (2, 3), (1, 4), (3, 4), (2, 5), (3, 5), (1, 5)]
    while added < quota and tries < quota * 30:
        tries += 1
        num, den = rng.choice(fracs)
        base = den * rng.randint(4, 60)
        value = base * num // den
        key = f"pecahan-{num}-{den}-{base}"
        question = b.pick(
            [
                "berapa {num}/{den} dari {base}?",
                "hitung {num}/{den} dari {base}",
                "{num}/{den} bagian dari {base} itu berapa?",
            ],
            key,
        ).format(num=num, den=den, base=base)
        answer = b.pick(
            [
                f"{num}/{den} dari {base} adalah {value}. Caranya, {base} : {den} = {base // den}, lalu dikali {num} jadi {value}.",
                f"Hasilnya {value}. Aku bagi {base} jadi {den} bagian, tiap bagian {base // den}, lalu ambil {num} bagian.",
                f"{value}, itu jawabannya. Karena {base} x {num} : {den} = {value}.",
            ],
            key,
        )
        if b.add(question, answer, "matematika", fact=key):
            added += 1


def gen_ratio(b: Builder, quota: int, rng: random.Random) -> None:
    added = 0
    tries = 0
    while added < quota and tries < quota * 40:
        tries += 1
        r1 = rng.randint(1, 5)
        r2 = rng.randint(1, 5)
        if r1 == r2:
            continue
        total = (r1 + r2) * rng.randint(5, 40) * 1000
        part1 = total * r1 // (r1 + r2)
        part2 = total - part1
        if part1 <= 0 or part2 <= 0:
            continue
        key = f"rasio-{r1}-{r2}-{total}"
        question = b.pick(
            [
                "uang {total} dibagi ke dua orang dengan perbandingan {r1}:{r2}. Berapa bagian masing-masing?",
                "total {total} dibagi dengan rasio {r1}:{r2}. Berapa nilai tiap bagian?",
                "ada {total} yang harus dibagi {r1}:{r2}. Masing-masing dapat berapa?",
            ],
            key,
        ).format(total=fmt_rp(total), r1=r1, r2=r2)
        answer = b.pick(
            [
                f"Bagiannya {fmt_rp(part1)} dan {fmt_rp(part2)}. Karena total perbandingannya {r1 + r2} bagian, satu bagiannya {fmt_rp(total // (r1 + r2))}.",
                f"Yang pertama dapat {fmt_rp(part1)}, yang kedua {fmt_rp(part2)}. Caranya, {fmt_rp(total)} : {r1 + r2} = {fmt_rp(total // (r1 + r2))}, lalu dikali {r1} dan {r2}.",
                f"Masing-masing {fmt_rp(part1)} dan {fmt_rp(part2)}. Kalau dijumlahkan, hasilnya balik ke {fmt_rp(total)}.",
            ],
            key,
        )
        if b.add(question, answer, "matematika", fact=key):
            added += 1


FOODS = [
    ("apel", "buah"), ("jeruk", "buah"), ("mangga", "buah"), ("pisang", "buah"),
    ("permen", "butir"), ("roti", "potong"), ("donat", "buah"), ("kue", "potong"),
    ("manggis", "buah"), ("salak", "buah"), ("durian", "buah"), ("rambutan", "buah"),
    ("jambu", "buah"), ("semangka", "buah"), ("nanas", "buah"), ("pepaya", "buah"),
]

ITEMS = [
    ("buku", "buku"), ("pensil", "batang"), ("stiker", "lembar"), ("kelereng", "butir"),
    ("kartu", "lembar"), ("koin", "keping"), ("bola", "buah"), ("topi", "buah"),
    ("tas", "buah"), ("baju", "potong"), ("sepatu", "pasang"), ("bunga", "tangkai"),
]

PACKED = [
    ("permen", "butir"), ("kelereng", "butir"), ("stiker", "lembar"), ("kartu", "lembar"),
    ("telur", "butir"), ("koin", "keping"), ("pensil", "batang"), ("buku", "buku"),
    ("kue", "potong"), ("donat", "buah"),
]


def _noun(n: int, obj: str, unit: str) -> str:
    if unit == "buah":
        return f"{fmt_id(n)} {obj}"
    return f"{fmt_id(n)} {unit} {obj}"


def gen_word_problems(b: Builder, quota: int, rng: random.Random) -> None:
    added = 0
    tries = 0
    while added < quota and tries < quota * 50:
        tries += 1
        name = rng.choice(NAMES)
        name2 = rng.choice([n for n in NAMES if n != name])
        kind = rng.choice(["sisa", "tambah", "kali", "bagi", "umur", "kelas", "tali"])

        if kind == "sisa":
            obj, unit = rng.choice(FOODS)
            start = rng.randint(8, 60)
            used = rng.randint(2, start - 1)
            a_txt, b_txt = _noun(start, obj, unit), _noun(used, obj, unit)
            key = f"cerita-sisa-{name}-{obj}-{start}-{used}"
            question = b.pick(
                [
                    "{name} punya {a}, lalu {b} dimakan. Berapa {obj} yang tersisa?",
                    "{name} membawa {a} ke sekolah, lalu {b} diberikan ke temannya. Berapa sisa {obj} {name}?",
                    "di meja ada {a} milik {name}, kemudian {b} diambil. Berapa {obj} yang masih ada?",
                ],
                key,
            ).format(name=name, obj=obj, a=a_txt, b=b_txt)
            answer = b.pick(
                [
                    f"Sisa {obj} {name} {start - used}. Caranya, {start} - {used} = {start - used}.",
                    f"Tinggal {start - used} {obj}. Aku kurangi {start} dengan {used}, hasilnya {start - used}.",
                    f"Jumlah akhirnya {start - used} {obj}. Karena {start} diambil {used}, sisanya {start - used}.",
                    f"Yang tersisa {start - used} {obj}. Cek pakai {start - used} + {used} = {start}, jadi benar.",
                ],
                key,
            )
        elif kind == "tambah":
            obj, unit = rng.choice(ITEMS)
            start = rng.randint(3, 40)
            more = rng.randint(2, 40)
            a_txt, b_txt = _noun(start, obj, unit), _noun(more, obj, unit)
            key = f"cerita-tambah-{name}-{obj}-{start}-{more}"
            question = b.pick(
                [
                    "{name} punya {a}, lalu membeli {b} lagi. Berapa jumlah {obj} {name} sekarang?",
                    "{name} sudah punya {a}, lalu mendapat hadiah {b}. Totalnya berapa?",
                    "di rak ada {a}, lalu {name} menambah {b}. Sekarang berapa {obj} di rak?",
                ],
                key,
            ).format(name=name, obj=obj, a=a_txt, b=b_txt)
            answer = b.pick(
                [
                    f"Jumlahnya {start + more} {obj}. Caranya, {start} + {more} = {start + more}.",
                    f"Sekarang {name} punya {start + more} {obj}. Aku jumlahkan {start} dengan {more}.",
                    f"Totalnya {start + more} {obj}. Karena {start} ditambah {more} sama dengan {start + more}.",
                    f"Jadi {start + more} {obj}. Cek mundur: {start + more} - {more} = {start}, hasilnya balik.",
                ],
                key,
            )
        elif kind == "kali":
            obj, unit = rng.choice(PACKED)
            per = rng.randint(2, 25)
            count = rng.randint(3, 20)
            key = f"cerita-kali-{obj}-{per}-{count}"
            question = b.pick(
                [
                    "satu wadah berisi {a}. Kalau ada {b} wadah, berapa jumlah {obj} semuanya?",
                    "setiap kantong berisi {a}. Ada {b} kantong, total {obj} berapa?",
                    "{name} membeli {b} paket, tiap paket berisi {a}. Berapa {obj} seluruhnya?",
                ],
                key,
            ).format(name=name, obj=obj, a=_noun(per, obj, unit), b=count)
            answer = b.pick(
                [
                    f"Totalnya {per * count} {obj}. Caranya, {per} x {count} = {per * count}.",
                    f"Semuanya ada {per * count} {obj}. Aku kalikan isi tiap wadah {per} dengan jumlah wadah {count}.",
                    f"Jumlah seluruhnya {per * count} {obj}. Karena {count} wadah berisi {per} {obj}, hasilnya {per * count}.",
                    f"Jadi {per * count} {obj}. Kalau dipecah lagi jadi {count} bagian, tiap bagian {per} {obj}.",
                ],
                key,
            )
        elif kind == "bagi":
            obj, unit = rng.choice(FOODS + ITEMS)
            divisor = rng.choice([2, 3, 4, 5, 6, 8, 10])
            each = rng.randint(2, 30)
            total = divisor * each
            key = f"cerita-bagi-{obj}-{total}-{divisor}"
            question = b.pick(
                [
                    "{total} {obj} dibagi rata ke {b} anak. Setiap anak mendapat berapa {obj}?",
                    "ada {total} {obj} yang akan dibagikan sama banyak ke {b} orang. Tiap orang dapat berapa?",
                    "{name} membagi {total} {obj} ke {b} temannya dengan jumlah sama. Berapa bagian masing-masing?",
                ],
                key,
            ).format(name=name, obj=obj, total=fmt_id(total), b=divisor)
            answer = b.pick(
                [
                    f"Setiap anak mendapat {each} {obj}. Caranya, {total} : {divisor} = {each}.",
                    f"Bagiannya {each} {obj} per orang. Aku bagi {total} dengan {divisor}, hasilnya {each}.",
                    f"Masing-masing dapat {each} {obj}. Karena {divisor} x {each} = {total}.",
                    f"Tiap orang dapat {each} {obj}. Kalau dikembalikan, {each} x {divisor} = {total}, jadi pas.",
                ],
                key,
            )
        elif kind == "umur":
            age = rng.randint(10, 45)
            diff = rng.randint(2, 20)
            older = rng.random() < 0.5
            if not older and age <= diff:
                continue
            key = f"cerita-umur-{name}-{name2}-{age}-{diff}-{older}"
            if older:
                question = f"umur {name} {age} tahun. {name2} {diff} tahun lebih tua. Berapa umur {name2}?"
                answer = f"Umur {name2} {age + diff} tahun. Karena {age} + {diff} = {age + diff}, jadi {name2} lebih tua {diff} tahun."
            else:
                question = f"umur {name} {age} tahun. {name2} {diff} tahun lebih muda. Berapa umur {name2}?"
                answer = f"Umur {name2} {age - diff} tahun. Aku kurangi {age} dengan {diff}, hasilnya {age - diff}."
        elif kind == "kelas":
            total = rng.randint(20, 45)
            absent = rng.randint(2, 8)
            key = f"cerita-kelas-{name}-{total}-{absent}"
            question = f"kelas {name} punya {total} siswa. Hari ini {absent} siswa izin. Berapa siswa yang hadir?"
            answer = b.pick(
                [
                    f"Siswa yang hadir {total - absent} orang. Caranya, {total} - {absent} = {total - absent}.",
                    f"Yang hadir {total - absent} siswa. Karena dari {total} siswa, {absent} di antaranya izin.",
                    f"Hadir {total - absent} orang. Cek: {total - absent} + {absent} = {total}, jadi benar.",
                ],
                key,
            )
        else:
            length = rng.choice([60, 72, 90, 120, 150, 180])
            parts = rng.choice([3, 4, 5, 6])
            if length % parts != 0:
                continue
            key = f"cerita-tali-{length}-{parts}"
            question = f"tali sepanjang {length} cm dipotong jadi {parts} bagian sama panjang. Tiap bagian berapa cm?"
            answer = b.pick(
                [
                    f"Tiap bagian {length // parts} cm. Karena {length} : {parts} = {length // parts}, jadi panjangnya sama semua.",
                    f"Panjangnya {length // parts} cm per bagian. Aku bagi {length} dengan {parts}, hasilnya {length // parts}.",
                    f"Masing-masing {length // parts} cm. Kalau disambung lagi, {length // parts} x {parts} = {length} cm.",
                ],
                key,
            )

        if b.add(question, answer, "matematika", fact=key):
            added += 1


def gen_missing_number(b: Builder, quota: int, rng: random.Random) -> None:
    added = 0
    tries = 0
    while added < quota and tries < quota * 30:
        tries += 1
        kind = rng.choice(["tambah", "kurang", "kali", "bagi"])
        if kind == "tambah":
            a = rng.randint(2, 500)
            missing = rng.randint(2, 500)
            result = a + missing
            question = b.pick(
                [
                    "lengkapi: {a} + ? = {r}. Angka yang kosong berapa?",
                    "berapa angka yang hilang dari {a} + ... = {r}?",
                    "kalau {a} + ? = {r}, isi titik-titiknya berapa?",
                ],
                f"hilang-tambah-{a}-{result}",
            ).format(a=fmt_id(a), r=fmt_id(result))
            answer = f"Angka yang kosong adalah {fmt_id(missing)}. Caranya, {fmt_id(result)} - {fmt_id(a)} = {fmt_id(missing)}, jadi {fmt_id(a)} + {fmt_id(missing)} = {fmt_id(result)}."
        elif kind == "kurang":
            missing = rng.randint(20, 600)
            c = rng.randint(2, missing - 1)
            result = missing - c
            question = b.pick(
                [
                    "lengkapi: ? - {c} = {r}. Angka yang kosong berapa?",
                    "berapa angka awal kalau ? - {c} = {r}?",
                    "isi titik-titik: ... - {c} = {r}",
                ],
                f"hilang-kurang-{c}-{result}",
            ).format(c=fmt_id(c), r=fmt_id(result))
            answer = f"Angka yang kosong adalah {fmt_id(missing)}. Caranya, {fmt_id(result)} + {fmt_id(c)} = {fmt_id(missing)}, jadi {fmt_id(missing)} - {fmt_id(c)} = {fmt_id(result)}."
        elif kind == "kali":
            a = rng.randint(2, 30)
            missing = rng.randint(2, 30)
            result = a * missing
            question = b.pick(
                [
                    "lengkapi: {a} x ? = {r}. Angka yang kosong berapa?",
                    "berapa angka yang hilang dari {a} x ... = {r}?",
                    "kalau {a} x ? = {r}, isinya berapa?",
                ],
                f"hilang-kali-{a}-{result}",
            ).format(a=a, r=fmt_id(result))
            answer = f"Angka yang kosong adalah {missing}. Caranya, {fmt_id(result)} : {a} = {missing}, karena {a} x {missing} = {fmt_id(result)}."
        else:
            quotient = rng.randint(2, 20)
            divisor = rng.randint(2, 20)
            dividend = quotient * divisor
            question = b.pick(
                [
                    "lengkapi: ? : {c} = {q}. Angka yang kosong berapa?",
                    "berapa angka awal kalau ? : {c} = {q}?",
                    "isi titik-titik: ... : {c} = {q}",
                ],
                f"hilang-bagi-{divisor}-{quotient}",
            ).format(c=divisor, q=quotient)
            answer = f"Angka yang kosong adalah {fmt_id(dividend)}. Caranya, {quotient} x {divisor} = {fmt_id(dividend)}, jadi {fmt_id(dividend)} : {divisor} = {quotient}."
        if b.add(question, answer, "matematika", fact="hilang-" + norm_key(question)):
            added += 1


def gen_chain(b: Builder, quota: int, rng: random.Random) -> None:
    added = 0
    tries = 0
    while added < quota and tries < quota * 30:
        tries += 1
        kind = rng.choice(["tambah-tambah", "kurang-kurang", "tambah-kurang"])
        a = rng.randint(10, 200)
        c = rng.randint(5, 100)
        d = rng.randint(5, 100)
        if kind == "tambah-tambah":
            result = a + c + d
            expr = f"{fmt_id(a)} + {fmt_id(c)} + {fmt_id(d)}"
            mid = a + c
            work = f"{fmt_id(a)} + {fmt_id(c)} = {fmt_id(mid)}, lalu {fmt_id(mid)} + {fmt_id(d)} = {fmt_id(result)}"
        elif kind == "kurang-kurang":
            if a <= c + d:
                continue
            result = a - c - d
            expr = f"{fmt_id(a)} - {fmt_id(c)} - {fmt_id(d)}"
            mid = a - c
            work = f"{fmt_id(a)} - {fmt_id(c)} = {fmt_id(mid)}, lalu {fmt_id(mid)} - {fmt_id(d)} = {fmt_id(result)}"
        else:
            result = a + c - d
            if result <= 0:
                continue
            expr = f"{fmt_id(a)} + {fmt_id(c)} - {fmt_id(d)}"
            mid = a + c
            work = f"{fmt_id(a)} + {fmt_id(c)} = {fmt_id(mid)}, lalu {fmt_id(mid)} - {fmt_id(d)} = {fmt_id(result)}"
        key = "rantai-" + norm_key(expr)
        question = b.pick(
            [
                "berapa hasil dari {e}?",
                "hitung {e} dong",
                "tolong selesaikan {e}",
                "coba hitung {e} pelan-pelan",
            ],
            key,
        ).format(e=expr)
        answer = b.pick(
            [
                f"Hasilnya {fmt_id(result)}. Aku kerjakan berurutan: {work}.",
                f"Jawabannya {fmt_id(result)}. {work.capitalize()}, jadi hasil akhirnya {fmt_id(result)}.",
                f"{fmt_id(result)}, itu hasilnya. Aku hitung dari kiri ke kanan: {work}.",
            ],
            key,
        )
        if b.add(question, answer, "matematika", fact=key):
            added += 1


def gen_two_digit_mul(b: Builder, quota: int, rng: random.Random) -> None:
    added = 0
    tries = 0
    while added < quota and tries < quota * 25:
        tries += 1
        a = rng.randint(11, 99)
        c = rng.randint(11, 99)
        result = a * c
        tens, units = (a // 10) * 10, a % 10
        p1, p2 = tens * c, units * c
        key = f"kali2-{a}-{c}"
        question = b.pick(
            [
                "berapa {a} x {c}?",
                "hitung perkalian {a} x {c}",
                "hasil dari {a} x {c} berapa?",
                "{a} dikali {c} sama dengan berapa?",
            ],
            key,
        ).format(a=a, c=c)
        answer = b.pick(
            [
                f"{a} x {c} = {fmt_id(result)}. Aku pecah {a} jadi {tens} + {units}: {tens} x {c} = {fmt_id(p1)}, lalu {units} x {c} = {p2}, dan {fmt_id(p1)} + {p2} = {fmt_id(result)}.",
                f"Hasilnya {fmt_id(result)}. Caranya, {a} x {c} = ({tens} + {units}) x {c} = {fmt_id(p1)} + {p2} = {fmt_id(result)}.",
                f"{a} x {c} = {fmt_id(result)}. Kalau dicek dengan pembagian, {fmt_id(result)} : {c} = {a}, jadi hasilnya benar.",
            ],
            key,
        )
        if b.add(question, answer, "matematika", fact=key):
            added += 1


def gen_big_div(b: Builder, quota: int, rng: random.Random) -> None:
    added = 0
    tries = 0
    while added < quota and tries < quota * 40:
        tries += 1
        divisor = rng.randint(3, 25)
        quotient = rng.randint(10, 99)
        remainder = 0 if rng.random() < 0.6 else rng.randint(1, divisor - 1)
        dividend = divisor * quotient + remainder
        key = f"bagi2-{dividend}-{divisor}"
        question = b.pick(
            [
                "berapa {a} : {b}?",
                "hitung {a} dibagi {b}",
                "hasil dari {a} : {b} berapa?",
                "{a} dibagi {b} sama dengan berapa?",
            ],
            key,
        ).format(a=fmt_id(dividend), b=divisor)
        if remainder == 0:
            answer = b.pick(
                [
                    f"{fmt_id(dividend)} : {divisor} = {quotient}. Karena {divisor} x {quotient} = {fmt_id(dividend)}, pembagiannya pas tanpa sisa.",
                    f"Hasilnya {quotient}. Aku cek dengan perkalian: {quotient} x {divisor} = {fmt_id(dividend)}, jadi jawabannya benar.",
                    f"{fmt_id(dividend)} dibagi {divisor} hasilnya {quotient}. Nggak ada sisa karena {fmt_id(dividend)} habis dibagi {divisor}.",
                ],
                key,
            )
        else:
            answer = b.pick(
                [
                    f"{fmt_id(dividend)} : {divisor} hasilnya {quotient} dengan sisa {remainder}. Karena {divisor} x {quotient} = {fmt_id(dividend - remainder)}, lalu {fmt_id(dividend)} - {fmt_id(dividend - remainder)} = {remainder}.",
                    f"Hasilnya {quotient}, sisanya {remainder}. Cek: {divisor} x {quotient} + {remainder} = {fmt_id(dividend)}.",
                    f"Jawabannya {quotient} sisa {remainder}. Sisa ini lebih kecil dari {divisor}, jadi sudah tidak bisa dibagi lagi.",
                ],
                key,
            )
        if b.add(question, answer, "matematika", fact=key):
            added += 1


TIPS = {
    "tambah": [
        "Tips: jumlahkan ratusan, puluhan, lalu satuan supaya nggak ada angka yang terlewat.",
        "Kalau angkanya besar, bulatkan dulu ke puluhan terdekat lalu koreksi selisihnya.",
        "Ingat, hasil penjumlahan tidak berubah walau urutan angkanya dibalik.",
        "Cek ulang dengan mengurangi hasilnya dengan salah satu angka; kalau balik ke angka lain, berarti benar.",
    ],
    "kurang": [
        "Tips: kurangi puluhan dulu, baru satuannya, biar lebih gampang.",
        "Cek hasilnya dengan menambahkan kembali angka yang dikurangkan.",
        "Kalau perlu meminjam, ambil satu puluhan lalu ubah jadi sepuluh satuan.",
        "Pengurangan adalah kebalikan penjumlahan, jadi bisa dicek dari arah sebaliknya.",
    ],
    "kali": [
        "Tips: pecah angka besar jadi puluhan dan satuan, lalu kalikan satu per satu.",
        "Perkalian kecil bisa diubah jadi penjumlahan berulang.",
        "Cek hasilnya dengan membagi ke salah satu angka; kalau pas, hasilnya benar.",
        "Ingat, urutan perkalian boleh dibalik tanpa mengubah hasil.",
    ],
    "bagi": [
        "Tips: pembagian adalah kebalikan perkalian, jadi cek dengan mengalikan kembali.",
        "Kalau ada sisa, tulis hasil bulatnya dulu, lalu sisanya.",
        "Bayangkan membagi kue ke beberapa orang supaya lebih mudah dipahami.",
        "Pastikan pembaginya bukan nol, karena pembagian dengan nol tidak terdefinisi.",
    ],
    "persen": [
        "Tips: persen artinya per seratus, jadi selalu bagi 100 di langkah terakhir.",
        "Kalau persennya bulat, hitung dulu 10% lalu kalikan sesuai kebutuhan.",
        "Persen bisa diubah jadi pecahan, misalnya 25% sama dengan 1/4.",
        "Cek kewajaran hasilnya: persentase kecil pasti menghasilkan angka yang lebih kecil dari total.",
    ],
    "bulat": [
        "Tips: lihat angka di sebelah kanan posisi yang dituju; 5 ke atas dibulatkan naik.",
        "Pembulatan dipakai supaya angka lebih mudah dibaca, bukan supaya nilainya berubah banyak.",
        "Kalau angka yang dilihat kurang dari 5, bulatkan ke bawah.",
        "Selisih hasil pembulatan paling besar setengah dari satuan yang dipakai.",
    ],
    "banding": [
        "Tips: bandingkan dulu jumlah digitnya; angka dengan digit lebih banyak biasanya lebih besar.",
        "Kalau jumlah digitnya sama, bandingkan dari angka paling depan.",
        "Selisih dua angka didapat dari angka besar dikurangi angka kecil.",
        "Garis bilangan membantu: angka yang lebih ke kanan selalu lebih besar.",
    ],
    "deret": [
        "Tips: cek dulu selisih antar angka; kalau selisihnya tetap, itu deret aritmetika.",
        "Kalau selisihnya berubah, coba cek hasil bagi antar angka.",
        "Pola deret bisa berupa penjumlahan, pengurangan, perkalian, atau bilangan kuadrat.",
        "Tulis dua angka berikutnya, lalu pastikan polanya tetap konsisten.",
    ],
    "rata": [
        "Tips: rata-rata didapat dari jumlah semua data dibagi banyaknya data.",
        "Nilai rata-rata selalu berada di antara angka terkecil dan terbesar.",
        "Kalau ada data yang jauh berbeda, rata-rata bisa terpengaruh nilai itu.",
        "Cek dengan mengalikan rata-rata dengan jumlah data; hasilnya harus sama dengan total.",
    ],
    "prima": [
        "Tips: bilangan prima hanya punya dua faktor, yaitu 1 dan dirinya sendiri.",
        "Cek pembagi mulai dari 2, 3, 5, dan seterusnya sampai akar angkanya.",
        "Angka genap di atas 2 pasti bukan prima karena bisa dibagi 2.",
        "Angka yang berakhiran 0 atau 5 di atas 5 pasti bukan prima.",
    ],
    "faktor": [
        "Tips: faktor selalu berpasangan, misalnya 2 x 6 = 12.",
        "Cukup cek pembagi sampai akar angkanya, sisanya pasangan otomatis.",
        "Faktor 1 dan angka itu sendiri selalu ada.",
        "Kalau jumlah faktornya ganjil, berarti angka itu bilangan kuadrat.",
    ],
    "kpk": [
        "Tips: FPB adalah pembagi bersama terbesar, KPK adalah kelipatan bersama terkecil.",
        "Hubungannya: KPK x FPB = hasil kali kedua angka.",
        "Untuk angka besar, pakai faktorisasi prima supaya lebih cepat.",
        "KPK selalu lebih besar atau sama dengan angka terbesar di antara keduanya.",
    ],
    "pangkat": [
        "Tips: pangkat berarti perkalian berulang, bukan dikali angka pangkatnya.",
        "Kuadrat adalah pangkat dua, kubik adalah pangkat tiga.",
        "Akar kuadrat adalah kebalikan dari kuadrat.",
        "Cek hasil pangkat dengan mengalikan berulang sesuai jumlah pangkatnya.",
    ],
    "konversi": [
        "Tips: turun satu tangga satuan dikali 10, naik satu tangga dibagi 10.",
        "Untuk waktu, ingat 1 jam = 60 menit dan 1 menit = 60 detik.",
        "Tulis dulu faktor konversinya supaya nggak salah kali atau bagi.",
        "Pastikan satuan akhirnya sesuai dengan yang diminta soal.",
    ],
    "diskon": [
        "Tips: potongan dihitung dari harga awal, bukan dari harga setelah diskon.",
        "Harga akhir sama dengan harga awal dikurangi potongan.",
        "Diskon 50% berarti membayar setengah dari harga awal.",
        "Kalau diskonnya bertingkat, hitung satu per satu secara berurutan.",
    ],
    "kembali": [
        "Tips: kembalian dihitung dari uang yang dibayar dikurangi harga barang.",
        "Pastikan uang yang dibayar lebih besar dari harga barang.",
        "Hitung harga total dulu kalau barangnya lebih dari satu.",
        "Cek ulang dengan menambahkan kembalian ke harga barang.",
    ],
    "waktu": [
        "Tips: ingat, 1 jam itu 60 menit, bukan 100 menit.",
        "Kalau menitnya lewat 60, pindahkan 60 menit menjadi 1 jam.",
        "Untuk durasi panjang, ubah semuanya ke menit dulu supaya mudah.",
        "Cek hasilnya dengan mengurangi jam selesai dengan jam mulai.",
    ],
    "geometri": [
        "Tips: pastikan satuan luas memakai cm persegi, bukan cm biasa.",
        "Tulis rumusnya dulu, baru masukkan angkanya.",
        "Keliling adalah jumlah semua sisi, luas adalah ukuran daerah di dalamnya.",
        "Kalau satuannya berbeda, samakan dulu sebelum menghitung.",
    ],
    "pecahan": [
        "Tips: pecahan berarti bagian dari keseluruhan.",
        "Bagi dulu totalnya dengan penyebut, lalu kalikan dengan pembilang.",
        "Pecahan senilai didapat dengan mengali atas dan bawah dengan angka yang sama.",
        "Cek kewajaran hasilnya: 1/2 dari 100 pasti 50, bukan 200.",
    ],
    "rasio": [
        "Tips: jumlahkan dulu semua angka perbandingan untuk mencari nilai satu bagian.",
        "Setelah nilai satu bagian ketemu, kalikan dengan masing-masing angka rasio.",
        "Cek dengan menjumlahkan semua bagian; hasilnya harus balik ke total awal.",
        "Rasio 1:2 berarti bagian kedua dua kali lipat bagian pertama.",
    ],
    "cerita": [
        "Tips: tulis dulu angka yang diketahui, lalu tentukan operasi yang tepat.",
        "Cek kembali angkanya sebelum menghitung supaya tidak ada yang terlewat.",
        "Pastikan jawaban akhirnya menjawab pertanyaan dengan satuan yang benar.",
        "Kalau ragu, hitung ulang dari arah sebaliknya untuk memastikan hasilnya.",
    ],
}


def _math_topic(question: str) -> str:
    q = question.lower()
    if "%" in q or "persen" in q:
        return "persen"
    if "bulatkan" in q or "pembulatan" in q:
        return "bulat"
    if "lebih besar" in q or "lebih kecil" in q or "mana yang lebih" in q:
        return "banding"
    if "deret" in q or "pola" in q:
        return "deret"
    if "rata-rata" in q:
        return "rata"
    if "prima" in q:
        return "prima"
    if "faktor" in q:
        return "faktor"
    if "kpk" in q or "fpb" in q:
        return "kpk"
    if "kuadrat" in q or "akar" in q or "pangkat" in q or "kubik" in q:
        return "pangkat"
    if "diskon" in q or "didiskon" in q:
        return "diskon"
    if "kembalian" in q or "kembalinya" in q:
        return "kembali"
    if "luas" in q or "keliling" in q:
        return "geometri"
    if "bagian dari" in q:
        return "pecahan"
    if "perbandingan" in q or "rasio" in q:
        return "rasio"
    if "jam " in q or "pukul" in q or "menit" in q:
        return "waktu"
    if any(unit in q for unit in (" km", " cm", " mm", " kg", " mg", " ml", "liter", "detik", "hari", "minggu")):
        return "konversi"
    if " + " in q or "tambah" in q or "jumlah" in q or "dijumlah" in q:
        return "tambah"
    if " - " in q or "kurang" in q or "minus" in q or "selisih" in q:
        return "kurang"
    if " x " in q or "kali" in q:
        return "kali"
    if " : " in q or "dibagi" in q or "pembagian" in q:
        return "bagi"
    return "cerita"


def _decorate(b: Builder) -> None:
    """Tambahkan satu kalimat tips supaya jawaban lebih menjelaskan cara kerja."""
    for row in b.rows:
        question = row["messages"][0]["content"]
        answer = row["messages"][1]["content"]
        topic = _math_topic(question)
        tip = b.pick(TIPS[topic], question)
        row["messages"][1]["content"] = answer + " " + tip


def build_math(b: Builder, rng: random.Random, scale: float = 1.0) -> None:
    gen_arithmetic(b, rng, scale)
    gen_remainder(b, int(900 * scale), rng)
    gen_percent(b, int(2400 * scale), rng)
    gen_rounding(b, int(1600 * scale), rng)
    gen_compare(b, int(1200 * scale), rng)
    gen_sequence(b, int(1400 * scale), rng)
    gen_average(b, int(1000 * scale), rng)
    gen_prime(b, int(350 * scale), rng)
    gen_factors(b, int(350 * scale), rng)
    gen_gcd_lcm(b, int(700 * scale), rng)
    gen_powers(b, int(600 * scale), rng)
    gen_conversion(b, int(1200 * scale), rng)
    gen_discount(b, int(1000 * scale), rng)
    gen_money_change(b, int(700 * scale), rng)
    gen_time(b, int(500 * scale), rng)
    gen_geometry(b, int(800 * scale), rng)
    gen_fraction(b, int(700 * scale), rng)
    gen_ratio(b, int(500 * scale), rng)
    gen_word_problems(b, int(2200 * scale), rng)
    gen_missing_number(b, int(5000 * scale), rng)
    gen_chain(b, int(5000 * scale), rng)
    gen_two_digit_mul(b, int(3500 * scale), rng)
    gen_big_div(b, int(3000 * scale), rng)
    _decorate(b)
