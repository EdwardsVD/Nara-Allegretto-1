"""Materi bahasa Indonesia: latihan ejaan dan huruf.

Daftar kata diambil dari kata dasar KBBI (lewat Sastrawi), lalu disaring ke kata
yang umum dipakai. Semua jawaban dihitung langsung dari huruf kata, jadi akurat.
"""
from __future__ import annotations

import os
import random

from nara_core import Builder, count_consonants, count_vowels

HERE = os.path.dirname(os.path.abspath(__file__))
WORDS_FILE = os.path.join(HERE, "words_id.txt")


def load_words() -> list[str]:
    with open(WORDS_FILE, encoding="utf-8") as handle:
        words = [w.strip().lower() for w in handle if w.strip()]
    return sorted(set(w for w in words if w.isalpha() and 3 <= len(w) <= 12))


def _letters(word: str) -> str:
    return "-".join(word)


def _unique(items: list[str]) -> list[str]:
    seen: list[str] = []
    for item in items:
        if item not in seen:
            seen.append(item)
    return seen


def _vowel_report(word: str) -> str:
    vowels = count_vowels(word)
    unique = _unique(vowels)
    parts = []
    for v in unique:
        count = vowels.count(v)
        parts.append(f"{v} ({count} kali)" if count > 1 else v)
    return ", ".join(parts)


def _consonant_report(word: str) -> str:
    consonants = count_consonants(word)
    unique = _unique(consonants)
    parts = []
    for c in unique:
        count = consonants.count(c)
        parts.append(f"{c} ({count} kali)" if count > 1 else c)
    return ", ".join(parts)


def gen_spelling(b: Builder, words: list[str]) -> None:
    for word in words:
        n = len(word)
        vowels = count_vowels(word)
        consonants = count_consonants(word)
        key = f"eja-{word}"
        question = b.pick(
            [
                "gimana ejaan kata '{w}'?",
                "eja kata '{w}' dong",
                "'{w}' itu ditulis gimana sih?",
                "tolong eja '{w}'",
                "aku mau tahu ejaan '{w}', gimana?",
            ],
            key,
        ).format(w=word)
        answer = b.pick(
            [
                f"Ejaan kata '{word}' adalah {_letters(word)}. Ada {n} huruf, terdiri dari {len(vowels)} vokal ({', '.join(vowels)}) dan {len(consonants)} konsonan ({', '.join(consonants)}).",
                f"'{word}' ditulis {_letters(word)}, totalnya {n} huruf. Vokalnya {len(vowels)} huruf, yaitu {', '.join(vowels)}, dan konsonannya {len(consonants)} huruf.",
                f"Ejaannya {_letters(word)}. Kalau dihitung, {n} huruf dengan {len(vowels)} vokal dan {len(consonants)} konsonan. Nggak ada huruf yang terlewat.",
                f"Kata '{word}' dieja {_letters(word)}, jadi {n} huruf semuanya. Huruf vokalnya {', '.join(vowels) or 'tidak ada'}, sisanya konsonan.",
            ],
            key,
        )
        b.add(question, answer, "bahasa", fact=key)


def gen_letter_count(b: Builder, words: list[str]) -> None:
    for word in words:
        n = len(word)
        vowels = count_vowels(word)
        consonants = count_consonants(word)
        key = f"jumlah-huruf-{word}"
        question = b.pick(
            [
                "ada berapa huruf dalam kata '{w}'?",
                "'{w}' jumlah hurufnya berapa?",
                "hitung jumlah huruf kata '{w}'",
                "kata '{w}' terdiri dari berapa huruf?",
            ],
            key,
        ).format(w=word)
        answer = b.pick(
            [
                f"Kata '{word}' punya {n} huruf: {', '.join(word)}. Dari jumlah itu, {len(vowels)} vokal dan {len(consonants)} konsonan.",
                f"Jumlah hurufnya {n}. Kalau diurutkan: {', '.join(word)}. Vokalnya {len(vowels)} huruf, konsonannya {len(consonants)} huruf.",
                f"Ada {n} huruf di kata '{word}'. Aku hitung satu per satu: {_letters(word)}. Jadi totalnya {n}, bukan {n + 1}.",
                f"Panjang kata '{word}' {n} huruf. Rinciannya {len(vowels)} vokal dan {len(consonants)} konsonan, kalau dijumlahkan pas {n}.",
            ],
            key,
        )
        b.add(question, answer, "bahasa", fact=key)


def gen_first_last(b: Builder, words: list[str]) -> None:
    for word in words:
        first, last = word[0], word[-1]
        key = f"awal-akhir-{word}"
        question = b.pick(
            [
                "huruf pertama dan terakhir dari kata '{w}' apa?",
                "kata '{w}' diawali dan diakhiri huruf apa?",
                "'{w}' huruf depannya apa dan belakangnya apa?",
            ],
            key,
        ).format(w=word)
        answer = b.pick(
            [
                f"Kata '{word}' diawali huruf {first} dan diakhiri huruf {last}. Total ada {len(word)} huruf.",
                f"Huruf pertamanya {first}, huruf terakhirnya {last}. Kata '{word}' panjangnya {len(word)} huruf.",
                f"Depannya {first}, belakangnya {last}. Kalau dieja dari awal sampai akhir: {_letters(word)}.",
            ],
            key,
        )
        b.add(question, answer, "bahasa", fact=key)


def gen_reverse(b: Builder, words: list[str]) -> None:
    for word in words:
        rev = word[::-1]
        key = f"balik-{word}"
        question = b.pick(
            [
                "kalau kata '{w}' dibalik, jadi apa?",
                "'{w}' dibaca dari belakang jadi kata apa?",
                "coba balik kata '{w}'",
            ],
            key,
        ).format(w=word)
        answer = b.pick(
            [
                f"Kalau dibalik, '{word}' menjadi '{rev}'. Urutan hurufnya jadi {_letters(rev)}.",
                f"Hasilnya '{rev}'. Aku baca '{word}' dari huruf terakhir sampai pertama, jadinya {_letters(rev)}.",
                f"Dibalik jadi '{rev}', karena huruf terakhir '{word}' adalah {word[-1]} dan huruf pertamanya {word[0]}.",
            ],
            key,
        )
        b.add(question, answer, "bahasa", fact=key)


def gen_nth_letter(b: Builder, words: list[str], rng: random.Random) -> None:
    for word in words:
        if len(word) > 3:
            n = rng.randint(2, len(word) - 1)
        else:
            n = rng.randint(1, len(word))
        letter = word[n - 1]
        key = f"huruf-{word}-{n}"
        question = b.pick(
            [
                "huruf ke-{n} dari kata '{w}' apa?",
                "di kata '{w}', huruf urutan ke-{n} itu huruf apa?",
                "'{w}' huruf ke-{n}-nya apa ya?",
            ],
            key,
        ).format(w=word, n=n)
        answer = b.pick(
            [
                f"Huruf ke-{n} dari '{word}' adalah {letter}. Urutannya: {', '.join(f'{ch}({i + 1})' for i, ch in enumerate(word))}.",
                f"Jawabannya {letter}. Di kata '{word}' yang dieja {_letters(word)}, huruf urutan ke-{n} memang {letter}.",
                f"Hurufnya {letter}. Aku hitung dari depan sampai urutan ke-{n}, ketemunya huruf {letter} pada kata '{word}'.",
            ],
            key,
        )
        b.add(question, answer, "bahasa", fact=key)


def gen_vowel_list(b: Builder, words: list[str]) -> None:
    for word in words:
        vowels = count_vowels(word)
        if not vowels:
            continue
        key = f"vokal-{word}"
        question = b.pick(
            [
                "huruf vokal apa saja yang ada di kata '{w}'?",
                "'{w}' punya vokal apa aja?",
                "sebutkan huruf vokal dalam kata '{w}'",
            ],
            key,
        ).format(w=word)
        answer = b.pick(
            [
                f"Vokal yang muncul di kata '{word}' adalah {_vowel_report(word)}. Total ada {len(vowels)} huruf vokal dari {len(word)} huruf.",
                f"Kata '{word}' mengandung vokal {_vowel_report(word)}. Sisanya {len(count_consonants(word))} huruf konsonan.",
                f"Vokalnya {_vowel_report(word)}. Jadi dari {len(word)} huruf, {len(vowels)} di antaranya vokal.",
            ],
            key,
        )
        b.add(question, answer, "bahasa", fact=key)


def gen_consonant_list(b: Builder, words: list[str]) -> None:
    for word in words:
        consonants = count_consonants(word)
        if not consonants:
            continue
        key = f"konsonan-{word}"
        question = b.pick(
            [
                "huruf konsonan apa saja yang ada di kata '{w}'?",
                "'{w}' punya konsonan apa aja?",
                "sebutkan huruf konsonan dalam kata '{w}'",
            ],
            key,
        ).format(w=word)
        answer = b.pick(
            [
                f"Konsonan di kata '{word}' adalah {_consonant_report(word)}. Totalnya {len(consonants)} huruf konsonan dari {len(word)} huruf.",
                f"Kata '{word}' punya konsonan {_consonant_report(word)}. Sisa {len(count_vowels(word))} huruf lainnya adalah vokal.",
                f"Konsonannya {_consonant_report(word)}. Kalau dihitung, ada {len(consonants)} konsonan di kata '{word}'.",
            ],
            key,
        )
        b.add(question, answer, "bahasa", fact=key)


def gen_uppercase(b: Builder, words: list[str]) -> None:
    for word in words:
        key = f"kapital-{word}"
        question = b.pick(
            [
                "kalau '{w}' ditulis pakai huruf kapital semua, jadi apa?",
                "'{w}' huruf besarnya semua gimana?",
                "ubah '{w}' ke huruf kapital semua dong",
            ],
            key,
        ).format(w=word)
        answer = b.pick(
            [
                f"Kalau ditulis kapital semua, '{word}' menjadi '{word.upper()}'. Jumlah hurufnya tetap {len(word)}.",
                f"Bentuk kapitalnya '{word.upper()}'. Isinya sama, cuma semua hurufnya diubah ke huruf besar.",
                f"Hasilnya '{word.upper()}'. Huruf vokalnya jadi {', '.join(v.upper() for v in count_vowels(word)) or 'tidak ada'}, konsonannya {', '.join(c.upper() for c in count_consonants(word)) or 'tidak ada'}.",
            ],
            key,
        )
        b.add(question, answer, "bahasa", fact=key)


def gen_length_compare(b: Builder, words: list[str], rng: random.Random, quota: int) -> None:
    added = 0
    tries = 0
    while added < quota and tries < quota * 20:
        tries += 1
        a, c = rng.sample(words, 2)
        if len(a) == len(c):
            continue
        long_word, short_word = (a, c) if len(a) > len(c) else (c, a)
        key = f"banding-kata-{long_word}-{short_word}"
        question = b.pick(
            [
                "mana yang lebih panjang, '{a}' atau '{b}'?",
                "antara '{a}' dan '{b}', kata mana yang lebih panjang?",
                "'{a}' sama '{b}', mana yang lebih panjang?",
            ],
            key,
        ).format(a=a, b=c)
        answer = b.pick(
            [
                f"'{long_word}' lebih panjang, karena punya {len(long_word)} huruf sedangkan '{short_word}' hanya {len(short_word)} huruf. Selisihnya {len(long_word) - len(short_word)} huruf.",
                f"Yang lebih panjang adalah '{long_word}'. Kata itu {len(long_word)} huruf, '{short_word}' cuma {len(short_word)} huruf.",
                f"'{long_word}' yang lebih panjang. Kalau dihitung, {len(long_word)} huruf dibanding {len(short_word)} huruf, selisih {len(long_word) - len(short_word)}.",
            ],
            key,
        )
        if b.add(question, answer, "bahasa", fact=key):
            added += 1


def gen_missing_letter(b: Builder, words: list[str], rng: random.Random) -> None:
    counts: dict[str, int] = {}
    for w in words:
        for i in range(len(w)):
            pat = w[:i] + "_" + w[i + 1:]
            counts[pat] = counts.get(pat, 0) + 1
    for word in words:
        index = rng.randrange(len(word))
        missing = word[index]
        masked = word[:index] + "_" + word[index + 1:]
        if counts.get(masked, 0) != 1:
            continue
        key = f"hilang-{word}-{index}"
        question = b.pick(
            [
                "huruf apa yang hilang dari kata '{m}'?",
                "'{m}' kurang huruf apa ya?",
                "lengkapi kata '{m}', huruf apa yang kosong?",
            ],
            key,
        ).format(m=masked)
        answer = b.pick(
            [
                f"Huruf yang hilang adalah {missing}. Kata lengkapnya '{word}', yang terdiri dari {len(word)} huruf.",
                f"Bagian yang kosong diisi huruf {missing}, jadi kata utuhnya '{word}'. Posisinya ada di urutan ke-{index + 1}.",
                f"Jawabannya {missing}. Kalau disusun lengkap, kata itu menjadi {_letters(word)}.",
            ],
            key,
        )
        b.add(question, answer, "bahasa", fact=key)


def gen_letter_frequency(b: Builder, words: list[str], rng: random.Random) -> None:
    for word in words:
        letter = rng.choice(sorted(set(word)))
        positions = [str(i + 1) for i, ch in enumerate(word) if ch == letter]
        key = f"frekuensi-{word}-{letter}"
        question = b.pick(
            [
                "ada berapa huruf '{l}' dalam kata '{w}'?",
                "di kata '{w}', huruf '{l}' muncul berapa kali?",
                "hitung jumlah huruf '{l}' pada kata '{w}'",
            ],
            key,
        ).format(w=word, l=letter)
        answer = b.pick(
            [
                f"Ada {len(positions)} huruf {letter} di kata '{word}', yaitu di urutan {', '.join(positions)}. Total panjang katanya {len(word)} huruf.",
                f"Huruf {letter} muncul {len(positions)} kali. Posisinya di urutan {', '.join(positions)} dari {len(word)} huruf.",
                f"Jumlahnya {len(positions)}. Kalau kata '{word}' dieja {_letters(word)}, huruf {letter} terlihat di urutan {', '.join(positions)}.",
            ],
            key,
        )
        b.add(question, answer, "bahasa", fact=key)


def gen_alphabetical(b: Builder, words: list[str]) -> None:
    for word in words:
        ordered = "-".join(sorted(word))
        key = f"urut-{word}"
        question = b.pick(
            [
                "kalau huruf-huruf kata '{w}' diurutkan dari a sampai z, jadi apa?",
                "urutkan huruf kata '{w}' sesuai abjad",
                "'{w}' kalau hurufnya diurutkan abjad jadi apa?",
            ],
            key,
        ).format(w=word)
        answer = b.pick(
            [
                f"Kalau diurutkan dari a sampai z, huruf kata '{word}' menjadi {ordered}. Kata aslinya tetap '{word}'.",
                f"Urutan abjadnya {ordered}. Jumlah hurufnya tetap {len(word)}, cuma posisinya diubah.",
                f"Hasilnya {ordered}. Aku susun ulang {len(word)} huruf '{word}' berdasarkan abjad.",
            ],
            key,
        )
        b.add(question, answer, "bahasa", fact=key)



def gen_sort_letters(b: Builder, words: list[str]) -> None:
    for word in words:
        ordered = "".join(sorted(word))
        key = f"urut-{word}"
        question = b.pick(
            [
                "kalau huruf kata '{w}' diurutkan dari a sampai z, jadi apa?",
                "urutkan huruf kata '{w}' sesuai abjad",
                "susun ulang huruf kata '{w}' dari a ke z",
            ],
            key,
        ).format(w=word)
        answer = b.pick(
            [
                f"Kalau diurutkan, hurufnya menjadi {_letters(ordered)}. Kata aslinya tetap '{word}'.",
                f"Hasil urutannya {ordered}, berasal dari kata '{word}' yang hurufnya disusun dari a sampai z.",
                f"Urutan abjadnya {_letters(ordered)}, sedangkan kata aslinya '{word}'.",
            ],
            key,
        )
        b.add(question, answer, "bahasa", fact=key)


def gen_letter_position(b: Builder, words: list[str], rng: random.Random) -> None:
    for word in words:
        unique = [i for i in range(len(word)) if word.count(word[i]) == 1]
        if not unique:
            continue
        index = rng.choice(unique)
        letter = word[index]
        key = f"posisi-{word}-{index}"
        question = b.pick(
            [
                "huruf '{l}' ada di urutan berapa pada kata '{w}'?",
                "di kata '{w}', huruf '{l}' menempati urutan ke berapa?",
                "posisi huruf '{l}' dalam kata '{w}' nomor berapa?",
            ],
            key,
        ).format(l=letter, w=word)
        answer = b.pick(
            [
                f"Huruf {letter} ada di urutan ke-{index + 1} dari {len(word)} huruf. Kata '{word}' dieja {_letters(word)}.",
                f"Posisinya urutan {index + 1}. Kalau '{word}' dieja, huruf {letter} muncul setelah {index} huruf sebelumnya.",
                f"Jawabannya urutan {index + 1}, karena urutan lengkapnya {_letters(word)}.",
            ],
            key,
        )
        b.add(question, answer, "bahasa", fact=key)


def gen_vowel_count(b: Builder, words: list[str]) -> None:
    for word in words:
        count = len(count_vowels(word))
        key = f"jumlah-vokal-{word}"
        question = b.pick(
            [
                "ada berapa vokal dalam kata '{w}'?",
                "berapa jumlah huruf vokal pada kata '{w}'?",
                "hitung banyaknya vokal di kata '{w}'",
            ],
            key,
        ).format(w=word)
        answer = b.pick(
            [
                f"Ada {count} vokal di kata '{word}' dari total {len(word)} huruf. Sisanya {len(word) - count} huruf konsonan.",
                f"Jumlahnya {count}. Kata '{word}' terdiri dari {len(word)} huruf, dan {len(word) - count} di antaranya konsonan.",
                f"Vokalnya ada {count} di kata '{word}', karena dari {len(word)} huruf, hanya {count} yang termasuk a, i, u, e, atau o.",
            ],
            key,
        )
        b.add(question, answer, "bahasa", fact=key)


def gen_consonant_count(b: Builder, words: list[str]) -> None:
    for word in words:
        count = len(count_consonants(word))
        key = f"jumlah-konsonan-{word}"
        question = b.pick(
            [
                "ada berapa konsonan dalam kata '{w}'?",
                "berapa jumlah huruf konsonan pada kata '{w}'?",
                "hitung banyaknya konsonan di kata '{w}'",
            ],
            key,
        ).format(w=word)
        answer = b.pick(
            [
                f"Ada {count} konsonan di kata '{word}' dari total {len(word)} huruf. Sisanya {len(word) - count} huruf vokal.",
                f"Jumlahnya {count}. Dari {len(word)} huruf pada '{word}', {len(word) - count} di antaranya vokal.",
                f"Konsonannya ada {count} di kata '{word}', karena {len(word) - count} huruf lainnya termasuk vokal.",
            ],
            key,
        )
        b.add(question, answer, "bahasa", fact=key)


def build_language_puzzles(b: Builder, rng: random.Random, limit: int | None = None) -> None:
    words = load_words()
    if limit:
        words = words[:limit]
    gen_spelling(b, words)
    gen_letter_count(b, words)
    gen_first_last(b, words)
    gen_reverse(b, words)
    gen_nth_letter(b, words, rng)
    gen_vowel_list(b, words)
    gen_consonant_list(b, words)
    gen_uppercase(b, words)
    gen_missing_letter(b, words, rng)
    gen_letter_frequency(b, words, rng)
    gen_alphabetical(b, words)
    gen_length_compare(b, words, rng, 3000)
    gen_sort_letters(b, words)
    gen_letter_position(b, words, rng)
    gen_vowel_count(b, words)
    gen_consonant_count(b, words)
