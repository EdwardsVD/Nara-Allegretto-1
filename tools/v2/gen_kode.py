"""Generator kategori `kode.jsonl` untuk Nara-Allegretto-2.

Mencakup Python, JavaScript, TypeScript, HTML, CSS, C++, C, SQL, Bash/Git, dan JSON.
Setiap cuplikan kode:
1. Maksimal 8 baris (agar model kecil tidak kewalahan).
2. Diuji otomatis oleh CodeVerifier (ast.parse + exec, node --check + vm,
   stripTypeScriptTypes + vm, g++, gcc, sqlite3, HTMLParser, CSS parser, bash -n, json.loads).
3. Yang gagal otomatis dibuang.
"""
from __future__ import annotations

import json
import math
import random

from .code_verifier import CodeVerifier
from .core_v2 import CategoryCollector, pick_det

PY_INTROS = [
    "Ini contoh singkatnya di Python:",
    "Kamu bisa pakai kode Python pendek ini:",
    "Coba tulis seperti ini di Python:",
    "Begini cara sederhananya pakai Python:",
    "Di Python, kodenya cukup ringkas kayak gini:",
    "Ini potongan kode Python yang bisa langsung kamu coba:",
    "Bisa banget, ini contoh Python sederhananya:",
    "Kurang lebih bentuknya begini di Python:",
]

JS_INTROS = [
    "Ini contoh ringkasnya di JavaScript:",
    "Kamu bisa nulisnya pakai JavaScript seperti ini:",
    "Di JavaScript, caranya cukup singkat:",
    "Coba potongan kode JavaScript berikut:",
    "Begini contoh sederhananya di JS:",
    "Untuk JavaScript, kamu bisa pakai pola ini:",
    "Ini kode JS pendek yang langsung jalan:",
    "Kurang lebih begini kalau ditulis di JavaScript:",
]

TS_INTROS = [
    "Di TypeScript, tambahkan tipe datanya seperti ini:",
    "Ini contoh TypeScript sederhananya:",
    "Kamu bisa menulis tipe yang jelas di TypeScript kayak gini:",
    "Begini versi TypeScript yang rapi dan aman tipenya:",
    "Coba contoh singkat TypeScript berikut:",
    "Kalau pakai TypeScript, bentuk kodenya seperti ini:",
]

HTML_INTROS = [
    "Ini struktur HTML sederhananya:",
    "Kamu bisa menyusun tag HTML-nya seperti ini:",
    "Coba contoh HTML ringkas berikut:",
    "Di HTML, cukup pakai elemen seperti ini:",
    "Begini penulisan HTML yang rapi dan tag-nya lengkap:",
    "Untuk kebutuhan itu, potongan HTML ini sudah cukup:",
]

CSS_INTROS = [
    "Ini aturan CSS sederhananya:",
    "Kamu bisa atur tampilannya pakai CSS seperti ini:",
    "Coba gaya CSS ringkas berikut:",
    "Di CSS, properti yang dipakai kurang lebih begini:",
    "Begini contoh CSS biar tampilannya rapi:",
    "Untuk efek itu, tulis CSS seperti ini:",
]

CPP_INTROS = [
    "Ini contoh program C++ sederhananya:",
    "Di C++, kamu bisa menulisnya seperti ini:",
    "Coba kode C++ singkat berikut:",
    "Begini bentuk program dasarnya di C++:",
    "Untuk C++, kodenya cukup ringkas seperti ini:",
    "Ini contoh C++ yang bisa langsung dikompilasi pakai g++:",
]


def _wrap_code(intro: str, lang: str, code: str, outro: str) -> str:
    return f"{intro}\n```{lang}\n{code.strip()}\n```\n{outro}"


def _gen_python(col: CategoryCollector, ver: CodeVerifier, rng: random.Random, limit: int | None) -> None:
    q_styles = [
        "contoh kode Python buat {task} dong",
        "gimana cara {task} di Python?",
        "nara, bikinin kode py sederhana untuk {task}",
        "tolong kasih contoh Python untuk {task}",
        "cara {task} pakai Python gimana ya?",
        "bantu kode Python singkat buat {task}",
        "ada contoh skrip Python pendek untuk {task}?",
        "ajarin {task} di Python pakai contoh singkat dong",
    ]

    # 1. Operasi hitung, diskon, suhu, waktu, rata-rata di Python
    var_pairs = [
        ("skor_a", "skor_b"), ("harga_awal", "ongkir"), ("apel", "jeruk"),
        ("poin_1", "poin_2"), ("tugas", "ujian"), ("pemasukan", "bonus"),
        ("jarak_pagi", "jarak_sore"), ("halaman_a", "halaman_b"),
    ]
    for i in range(650):
        if limit and len(col.rows) >= limit:
            return
        v1, v2 = var_pairs[i % len(var_pairs)]
        a = rng.randint(12, 240)
        b = rng.randint(5, 130)
        mode = i % 5
        key = f"py-num-{i}-{a}-{b}"
        intro = pick_det(PY_INTROS, key)
        if mode == 0:
            code = f"{v1} = {a}\n{v2} = {b}\ntotal = {v1} + {v2}\nprint(total)"
            exp = str(a + b)
            task = f"menjumlahkan {a} dan {b} di variabel `{v1}` serta `{v2}`"
            outro = f"Operator `+` menjumlahkan kedua variabel, lalu `print(total)` mencetak `{exp}`."
        elif mode == 1:
            harga = (i + 8) * 5000
            persen = [10, 15, 20, 25, 30, 40, 50][i % 7]
            bayar = harga - (harga * persen // 100)
            code = f"harga = {harga}\ndiskon = {persen}\nbayar = harga - (harga * diskon // 100)\nprint(bayar)"
            exp = str(bayar)
            task = f"menghitung harga akhir dari {harga} setelah diskon {persen}%"
            outro = f"Potongannya dihitung dulu lalu dikurangkan dari `harga`, sehingga tercetak `{exp}`."
        elif mode == 2:
            c_val = (i % 45) * 5 - 10
            f_val = c_val * 9 / 5 + 32
            code = f"celsius = {c_val}\nfahrenheit = celsius * 9 / 5 + 32\nprint(fahrenheit)"
            exp = str(f_val)
            task = f"mengubah suhu {c_val} derajat Celsius ke Fahrenheit"
            outro = f"Rumus `celsius * 9 / 5 + 32` mengubah suhu ke Fahrenheit dan menghasilkan `{exp}`."
        elif mode == 3:
            total_menit = 65 + i * 7
            jam = total_menit // 60
            sisa = total_menit % 60
            code = f"menit = {total_menit}\njam = menit // 60\nsisa = menit % 60\nprint(f'{{jam}} jam {{sisa}} menit')"
            exp = f"{jam} jam {sisa} menit"
            task = f"mengubah {total_menit} menit menjadi format jam dan menit"
            outro = f"`// 60` mengambil jam bulat dan `% 60` mengambil sisanya, hasilnya `{exp}`."
        else:
            p = rng.randint(4, 35)
            l = rng.randint(3, 28)
            code = f"panjang = {p}\nlebar = {l}\nluas = panjang * lebar\nkeliling = 2 * (panjang + lebar)\nprint(luas, keliling)"
            exp = f"{p * l} {2 * (p + l)}"
            task = f"menghitung luas dan keliling persegi panjang ukuran {p} x {l}"
            outro = f"Program mencetak luas dan keliling secara berurutan, yaitu `{exp}`."

        ok, _ = ver.verify_python(code, expected_out=exp)
        if ok:
            q = pick_det(q_styles, key).format(task=task)
            col.add(q, _wrap_code(intro, "python", code, outro))

    # 2. Manipulasi string Python
    words_pool = [
        "allegretto", "nusantara", "matahari", "pelangi", "semangat", "belajar",
        "komputer", "indonesia", "sahabat", "petualang", "perpustakaan", "kopi susu",
        "nasi goreng", "selamat pagi", "hujan rintik", "coding santai", "anak rantau",
        "kebun teh", "angin sore", "bintang malam", "layar biru", "catatan kecil",
        "roti bakar", "kereta cepat", "musik akustik", "taman kota", "jembatan merah",
    ]
    for idx, phrase in enumerate(words_pool):
        for op in range(8):
            if limit and len(col.rows) >= limit:
                return
            key = f"py-str-{idx}-{op}"
            intro = pick_det(PY_INTROS, key)
            if op == 0:
                code = f"teks = {phrase!r}\nprint(teks[::-1])"
                exp = phrase[::-1]
                task = f"membalik urutan karakter pada teks '{phrase}'"
                outro = f"Slicing `[::-1]` membaca string dari belakang, jadi hasilnya `{exp}`."
            elif op == 1:
                code = f"teks = {phrase!r}\nprint(teks.upper())"
                exp = phrase.upper()
                task = f"mengubah teks '{phrase}' menjadi huruf besar semua"
                outro = f"Method `.upper()` mengubah seluruh huruf menjadi kapital: `{exp}`."
            elif op == 2:
                code = f"teks = {phrase!r}\nvokal = sum(1 for h in teks.lower() if h in 'aeiou')\nprint(vokal)"
                exp = str(sum(1 for h in phrase.lower() if h in "aeiou"))
                task = f"menghitung banyaknya huruf vokal pada teks '{phrase}'"
                outro = f"Setiap huruf dicek apakah termasuk `aeiou`, sehingga total vokalnya `{exp}`."
            elif op == 3:
                code = f"teks = {phrase!r}\nprint(len(teks))"
                exp = str(len(phrase))
                task = f"mengecek panjang karakter dari teks '{phrase}'"
                outro = f"`len(teks)` menghitung semua karakter termasuk spasi, hasilnya `{exp}`."
            elif op == 4:
                code = f"teks = {phrase!r}\nprint(teks.title())"
                exp = phrase.title()
                task = f"membuat huruf awal tiap kata pada '{phrase}' jadi kapital"
                outro = f"`.title()` mengubah huruf pertama setiap kata menjadi kapital: `{exp}`."
            elif op == 5:
                code = f"teks = {phrase!r}\nbersih = teks.replace(' ', '_')\nprint(bersih)"
                exp = phrase.replace(" ", "_")
                task = f"mengganti spasi dengan garis bawah pada '{phrase}'"
                outro = f"`.replace(' ', '_')` menukar spasi menjadi underscore, hasilnya `{exp}`."
            elif op == 6:
                target_ch = phrase[0]
                cnt = phrase.count(target_ch)
                code = f"teks = {phrase!r}\nprint(teks.count({target_ch!r}))"
                exp = str(cnt)
                task = f"menghitung kemunculan huruf '{target_ch}' di dalam '{phrase}'"
                outro = f"`.count({target_ch!r})` menghitung berapa kali karakter itu muncul, yaitu `{exp}`."
            else:
                clean_p = phrase.replace(" ", "")
                is_pal = clean_p == clean_p[::-1]
                code = f"kata = {phrase!r}.replace(' ', '')\nprint(kata == kata[::-1])"
                exp = str(is_pal)
                task = f"mengecek apakah '{phrase}' termasuk palindrom atau bukan"
                outro = f"Setelah spasi dihapus, string dibandingkan dengan kebalikannya dan menghasilkan `{exp}`."

            ok, _ = ver.verify_python(code, expected_out=exp)
            if ok:
                q = pick_det(q_styles, key).format(task=task)
                col.add(q, _wrap_code(intro, "python", code, outro))

    # 3. List, comprehension, filter, agregasi, set, dan dict di Python
    for i in range(1100):
        if limit and len(col.rows) >= limit:
            return
        nums = [rng.randint(2, 49) for _ in range(5)]
        # Pastikan cukup bervariasi
        nums[0] = i % 37 + 3
        nums[1] = (i * 3) % 41 + 2
        key = f"py-list-{i}-{nums}"
        intro = pick_det(PY_INTROS, key)
        mode = i % 9
        if mode == 0:
            res = [x for x in nums if x % 2 == 0]
            code = f"data = {nums}\ngenap = [x for x in data if x % 2 == 0]\nprint(genap)"
            exp = str(res)
            task = f"menyaring angka genap dari list {nums}"
            outro = f"List comprehension menyaring elemen yang habis dibagi 2, hasilnya `{exp}`."
        elif mode == 1:
            res = [x * x for x in nums[:4]]
            code = f"angka = {nums[:4]}\nkuadrat = [x ** 2 for x in angka]\nprint(kuadrat)"
            exp = str(res)
            task = f"membuat list kuadrat dari {nums[:4]}"
            outro = f"Setiap angka dipangkatkan dua memakai `x ** 2`, sehingga tercetak `{exp}`."
        elif mode == 2:
            avg = round(sum(nums) / len(nums), 2)
            code = f"nilai = {nums}\nrata = round(sum(nilai) / len(nilai), 2)\nprint(rata)"
            exp = str(avg)
            task = f"menghitung rata-rata dari list nilai {nums}"
            outro = f"`sum()` dibagi `len()` menghitung rata-rata, lalu dibulatkan 2 desimal menjadi `{exp}`."
        elif mode == 3:
            mx, mn = max(nums), min(nums)
            code = f"data = {nums}\nprint(min(data), max(data))"
            exp = f"{mn} {mx}"
            task = f"mencari nilai terkecil dan terbesar pada list {nums}"
            outro = f"`min()` dan `max()` langsung menemukan batas bawah serta atasnya, yaitu `{exp}`."
        elif mode == 4:
            srt = sorted(nums, reverse=True)
            code = f"angka = {nums}\nterurut = sorted(angka, reverse=True)\nprint(terurut)"
            exp = str(srt)
            task = f"mengurutkan list {nums} dari terbesar ke terkecil"
            outro = f"Argumen `reverse=True` membalik urutan dari besar ke kecil: `{exp}`."
        elif mode == 5:
            dup_list = [nums[0], nums[1], nums[0], nums[2], nums[1], nums[3]]
            uniq = list(dict.fromkeys(dup_list))
            code = f"data = {dup_list}\nunik = list(dict.fromkeys(data))\nprint(unik)"
            exp = str(uniq)
            task = f"menghapus angka duplikat dari {dup_list} tanpa mengubah urutan"
            outro = f"`dict.fromkeys()` membuang duplikat sambil mempertahankan urutan kemunculan: `{exp}`."
        elif mode == 6:
            thresh = nums[2]
            cnt = sum(1 for x in nums if x > thresh)
            code = f"data = {nums}\nbanyak = sum(1 for x in data if x > {thresh})\nprint(banyak)"
            exp = str(cnt)
            task = f"menghitung berapa angka di {nums} yang lebih besar dari {thresh}"
            outro = f"Generator menghitung setiap elemen di atas `{thresh}`, totalnya `{exp}`."
        elif mode == 7:
            names = ["Budi", "Siti", "Raka", "Nadia", "Dewi", "Fajar", "Putri", "Andi"]
            n1, n2 = names[i % len(names)], names[(i + 3) % len(names)]
            s1, s2 = 70 + (i % 28), 65 + ((i * 5) % 33)
            code = f"skor = {{{n1!r}: {s1}, {n2!r}: {s2}}}\ntertinggi = max(skor, key=skor.get)\nprint(tertinggi)"
            exp = max({n1: s1, n2: s2}, key={n1: s1, n2: s2}.get)
            task = f"mencari pemilik skor tertinggi di dictionary {n1}:{s1} dan {n2}:{s2}"
            outro = f"`max(skor, key=skor.get)` membandingkan nilainya lalu mengembalikan kuncinya, yaitu `{exp}`."
        else:
            k = (i % 5) + 2
            kel = [x for x in nums if x % k == 0]
            code = f"data = {nums}\nhasil = [x for x in data if x % {k} == 0]\nprint(hasil)"
            exp = str(kel)
            task = f"mengambil kelipatan {k} dari list {nums}"
            outro = f"Syarat `x % {k} == 0` memilih angka yang habis dibagi {k}, hasilnya `{exp}`."

        ok, _ = ver.verify_python(code, expected_out=exp)
        if ok:
            q = pick_det(q_styles, key).format(task=task)
            col.add(q, _wrap_code(intro, "python", code, outro))

    # 4. Fungsi Python (def), faktor, prima, FPB/KPK, faktorial, deret
    for i in range(950):
        if limit and len(col.rows) >= limit:
            return
        key = f"py-fn-{i}"
        intro = pick_det(PY_INTROS, key)
        mode = i % 6
        if mode == 0:
            n = (i % 9) + 3
            fact_val = math.factorial(n)
            code = (
                "def faktorial(n):\n"
                "  hasil = 1\n"
                "  for i in range(2, n + 1):\n"
                "    hasil *= i\n"
                "  return hasil\n"
                f"print(faktorial({n}))"
            )
            exp = str(fact_val)
            task = f"membuat fungsi faktorial dan menghitung faktorial({n})"
            outro = f"Fungsi mengalikan angka 2 sampai `{n}` secara berurutan, hasilnya `{exp}`."
        elif mode == 1:
            n = i + 4
            is_p = n >= 2 and all(n % d != 0 for d in range(2, int(n**0.5) + 1))
            code = (
                "def cek_prima(n):\n"
                "  if n < 2:\n"
                "    return False\n"
                "  return all(n % i != 0 for i in range(2, int(n**0.5) + 1))\n"
                f"print(cek_prima({n}))"
            )
            exp = str(is_p)
            task = f"mengecek apakah angka {n} bilangan prima lewat fungsi"
            outro = f"Cukup uji pembagi sampai akar kuadratnya saja; untuk `{n}` hasilnya `{exp}`."
        elif mode == 2:
            a = (i % 24) + 6
            b = ((i * 7) % 30) + 8
            g = math.gcd(a, b)
            l = a * b // g
            code = f"import math\na, b = {a}, {b}\nfpb = math.gcd(a, b)\nkpk = a * b // fpb\nprint(fpb, kpk)"
            exp = f"{g} {l}"
            task = f"mencari FPB dan KPK dari {a} serta {b}"
            outro = f"`math.gcd()` menghitung FPB, lalu KPK didapat dari `a * b // fpb`, hasilnya `{exp}`."
        elif mode == 3:
            n = (i % 45) + 6
            divs = [d for d in range(1, n + 1) if n % d == 0]
            code = f"n = {n}\nfaktor = [i for i in range(1, n + 1) if n % i == 0]\nprint(faktor)"
            exp = str(divs)
            task = f"mencari semua faktor pembagi dari angka {n}"
            outro = f"Semua pembagi bulat dari 1 sampai `{n}` dikumpulkan ke list: `{exp}`."
        elif mode == 4:
            start = (i % 10) + 1
            step = (i % 6) + 2
            cnt = 5
            seq = [start + k * step for k in range(cnt)]
            code = f"awal, beda = {start}, {step}\nderet = [awal + i * beda for i in range({cnt})]\nprint(deret)"
            exp = str(seq)
            task = f"membuat 5 suku deret aritmetika mulai dari {start} dengan beda {step}"
            outro = f"Setiap suku bertambah `{step}` dari nilai awal `{start}`, menghasilkan `{exp}`."
        else:
            berat = 48 + (i % 38)
            tinggi_cm = 152 + ((i * 3) % 30)
            bmi = round(berat / ((tinggi_cm / 100) ** 2), 1)
            code = f"berat = {berat}\ntinggi_m = {tinggi_cm} / 100\nbmi = round(berat / (tinggi_m ** 2), 1)\nprint(bmi)"
            exp = str(bmi)
            task = f"menghitung IMT/BMI untuk berat {berat} kg dan tinggi {tinggi_cm} cm"
            outro = f"Tinggi diubah ke meter dulu sebelum dikuadratkan, sehingga IMT-nya `{exp}`."

        ok, _ = ver.verify_python(code, expected_out=exp)
        if ok:
            q = pick_det(q_styles, key).format(task=task)
            col.add(q, _wrap_code(intro, "python", code, outro))

    # 5. Tebak output & debugging Python
    trace_q_styles = [
        "apa output dari kode Python `{inline}`?",
        "kalau kode Python `{inline}` dijalankan, hasilnya apa?",
        "nara, tebak hasil print dari `{inline}` di Python dong",
        "bantu jelasin output kode Python ini: `{inline}`",
        "hasil eksekusi `{inline}` di Python itu berapa/apa ya?",
    ]
    for i in range(850):
        if limit and len(col.rows) >= limit:
            return
        key = f"py-trace-{i}"
        mode = i % 5
        if mode == 0:
            a, b, c = (i % 9) + 2, ((i * 3) % 7) + 2, (i % 5) + 1
            inline = f"x = {a}; y = {b}; print(x + y * {c})"
            code = f"x = {a}\ny = {b}\nprint(x + y * {c})"
            val = a + b * c
            ans = (
                f"Outputnya adalah `{val}`.\n```python\n{code}\n```\n"
                f"Di Python, perkalian `y * {c}` ({b} * {c} = {b * c}) dihitung lebih dulu sebelum ditambah `x` ({a}), jadi hasilnya `{val}`."
            )
            exp = str(val)
        elif mode == 1:
            word = ["informatika", " nusantara", "allegretto", "pemrograman", "matematika"][i % 5].strip()
            s = i % 3
            e = s + 4 + (i % 3)
            inline = f"s = '{word}'; print(s[{s}:{e}])"
            code = f"s = {word!r}\nprint(s[{s}:{e}])"
            val = word[s:e]
            ans = (
                f"Kode itu mencetak `{val}`.\n```python\n{code}\n```\n"
                f"Slicing `s[{s}:{e}]` mengambil karakter dari indeks ke-{s} sampai sebelum indeks ke-{e}."
            )
            exp = val
        elif mode == 2:
            n = (i % 6) + 3
            mult = (i % 4) + 2
            inline = f"total = 0\nfor i in range(1, {n}): total += i * {mult}\nprint(total)".replace("\n", "; ")
            inline = f"print(sum(i * {mult} for i in range(1, {n})))"
            code = f"hasil = sum(i * {mult} for i in range(1, {n}))\nprint(hasil)"
            val = sum(k * mult for k in range(1, n))
            ans = (
                f"Hasil yang tercetak adalah `{val}`.\n```python\n{code}\n```\n"
                f"`range(1, {n})` menghasilkan angka 1 sampai {n - 1}, masing-masing dikali `{mult}` lalu dijumlahkan."
            )
            exp = str(val)
        elif mode == 3:
            a = (i % 25) + 10
            b = (i % 6) + 3
            inline = f"print({a} // {b}, {a} % {b})"
            code = f"print({a} // {b}, {a} % {b})"
            exp = f"{a // b} {a % b}"
            ans = (
                f"Outputnya `{exp}`.\n```python\n{code}\n```\n"
                f"`{a} // {b}` adalah pembagian bulat ({a // b}), sedangkan `{a} % {b}` adalah sisa baginya ({a % b})."
            )
        else:
            lst = [(i + 1) % 10, (i + 4) % 10, (i + 7) % 10]
            inline = f"a = {lst}; a.append({i % 9}); print(len(a), a[-1])"
            code = f"a = {lst}\na.append({i % 9})\nprint(len(a), a[-1])"
            exp = f"4 {i % 9}"
            ans = (
                f"Hasilnya `{exp}`.\n```python\n{code}\n```\n"
                f"Setelah `.append({i % 9})`, panjang list jadi 4 dan elemen terakhir `a[-1]` bernilai `{i % 9}`."
            )

        ok, _ = ver.verify_python(code, expected_out=exp)
        if ok:
            q = pick_det(trace_q_styles, key).format(inline=inline)
            col.add(q, ans)

    # 6. Debugging / perbaiki error Python sehari-hari
    bug_q_styles = [
        "kenapa kode Python `{bad}` error ya?",
        "nara, bantu benerin bug Python ini dong: `{bad}`",
        "kok `{bad}` di Python malah error? gimana benerinnya?",
        "cara memperbaiki error pada kode Python `{bad}` gimana?",
    ]
    for i in range(450):
        if limit and len(col.rows) >= limit:
            return
        key = f"py-bug-{i}"
        mode = i % 5
        if mode == 0:
            umur = 15 + (i % 25)
            bad = f"umur = {umur}; print('Umur: ' + umur)"
            fix = f"umur = {umur}\nprint(f'Umur: {{umur}}')"
            exp = f"Umur: {umur}"
            why = f"Itu kena `TypeError` karena string nggak bisa langsung digabung dengan integer `{umur}` memakai `+`. Pakai f-string seperti ini:"
            outro = f"Dengan f-string, angka `{umur}` otomatis diubah ke teks dan mencetak `{exp}`."
        elif mode == 1:
            arr = [10 + i % 7, 20 + i % 5, 30 + i % 9]
            bad = f"data = {arr}; print(data[3])"
            fix = f"data = {arr}\nprint(data[-1])"
            exp = str(arr[-1])
            why = "Muncul `IndexError` karena list isi 3 elemen hanya punya indeks `0, 1, 2`. Untuk ambil elemen terakhir dengan aman, pakai `data[-1]`:"
            outro = f"Indeks `-1` selalu menunjuk elemen paling belakang, yaitu `{exp}`."
        elif mode == 2:
            skor = 70 + (i % 25)
            bad = f"skor = {skor}; if skor = 100: print('Sempurna')"
            fix = f"skor = {skor}\nif skor == 100:\n  print('Sempurna')\nelse:\n  print('Belum 100')"
            exp = "Belum 100"
            why = "Tanda `=` tunggal dipakai untuk mengisi variabel, bukan membandingkan nilai, sehingga muncul `SyntaxError`. Gunakan `==`:"
            outro = f"Karena `skor` bernilai `{skor}`, kondisi bernilai salah dan mencetak `{exp}`."
        elif mode == 3:
            angka_str = str(120 + i)
            tambah = (i % 9) + 5
            bad = f"teks = '{angka_str}'; print(teks + {tambah})"
            fix = f"teks = '{angka_str}'\nprint(int(teks) + {tambah})"
            exp = str(int(angka_str) + tambah)
            why = f"Variabel `teks` masih bertipe `str`, jadi gagal dijumlahkan dengan angka `{tambah}`. Ubah dulu pakai `int()`:"
            outro = f"Setelah dikonversi menjadi bilangan bulat, hasilnya `{exp}`."
        else:
            k_name = ["nama", "kota", "hobi", "kelas"][i % 4]
            v_val = f"user_{i}"
            bad = f"profil = {{'{k_name}': '{v_val}'}}; print(profil['alamat'])"
            fix = f"profil = {{{k_name!r}: {v_val!r}}}\nprint(profil.get('alamat', 'Belum diisi'))"
            exp = "Belum diisi"
            why = "Mengakses key `'alamat'` yang belum ada dengan `profil['alamat']` memicu `KeyError`. Lebih aman pakai `.get()` dengan nilai cadangan:"
            outro = f"Kalau key tidak ditemukan, `.get()` mengembalikan `{exp}` tanpa membuat program berhenti."

        ok, _ = ver.verify_python(fix, expected_out=exp)
        if ok:
            q = pick_det(bug_q_styles, key).format(bad=bad)
            col.add(q, _wrap_code(why, "python", fix, outro))


def _gen_js(col: CategoryCollector, ver: CodeVerifier, rng: random.Random, limit: int | None) -> None:
    q_styles = [
        "contoh kode JavaScript untuk {task}",
        "gimana cara {task} di JS?",
        "nara, bikinin kode JS pendek buat {task} dong",
        "cara {task} pakai JavaScript gimana?",
        "tolong kasih contoh JavaScript sederhana untuk {task}",
        "bantu potongan kode JS buat {task}",
    ]

    for i in range(1600):
        if limit and len(col.rows) >= limit:
            return
        key = f"js-core-{i}"
        intro = pick_det(JS_INTROS, key)
        mode = i % 10
        run_flag = True
        exp: str | None = None

        if mode == 0:
            nums = [(i % 13) + 2, ((i * 3) % 17) + 3, ((i * 5) % 19) + 4, (i % 11) + 1 + (i // 40)]
            total = sum(nums)
            code = f"const angka = {json.dumps(nums)};\nconst total = angka.reduce((acc, x) => acc + x, 0);\nconsole.log(total);"
            exp = str(total)
            task = f"menjumlahkan isi array {nums}"
            outro = f"`.reduce()` mengakumulasi semua elemen dari nilai awal `0`, jadi hasilnya `{exp}`."
        elif mode == 1:
            nums = [i % 20 + 3, (i * 2) % 25 + 4, (i * 3) % 29 + 5, (i // 10) + 6]
            batas = 12 + (i % 7)
            filtered = [x for x in nums if x >= batas]
            code = f"const skor = {json.dumps(nums)};\nconst lulus = skor.filter((n) => n >= {batas});\nconsole.log(lulus);"
            exp = json.dumps(filtered, separators=(",", ":"))
            task = f"menyaring angka minimal {batas} dari array {nums}"
            outro = f"`.filter()` menyisakan elemen yang memenuhi syarat `>= {batas}`, yaitu `{exp}`."
        elif mode == 2:
            nums = [(i % 15) + 1, ((i + 3) % 17) + 2, (i // 12) + 3]
            faktor = (i % 6) + 2
            mapped = [x * faktor for x in nums]
            code = f"const awal = {json.dumps(nums)};\nconst hasil = awal.map((x) => x * {faktor});\nconsole.log(hasil);"
            exp = json.dumps(mapped, separators=(",", ":"))
            task = f"mengalikan setiap elemen array {nums} dengan {faktor}"
            outro = f"`.map()` membuat array baru hasil perkalian tiap elemen, yaitu `{exp}`."
        elif mode == 3:
            nama = ["Nara", "Budi", "Siti", "Raka", "Dewi", "Fajar", "Nadia", "Putri", "Andi", "Lina"][i % 10]
            poin = 50 + i
            code = f"const nama = {json.dumps(nama)};\nconst poin = {poin};\nconsole.log(`Halo ${{nama}}, poinmu ${{poin}}!`);"
            exp = f"Halo {nama}, poinmu {poin}!"
            task = f"menyusun template literal sapaan untuk {nama} dengan poin {poin}"
            outro = f"Backtick dan `${{...}}` menyisipkan variabel langsung ke teks sehingga mencetak `{exp}`."
        elif mode == 4:
            nums = [(i * 7) % 45 + 5, (i * 3) % 37 + 1, (i // 8) + 2, (i % 19) + 8]
            srt = sorted(nums)
            code = f"const data = {json.dumps(nums)};\nconst urut = [...data].sort((a, b) => a - b);\nconsole.log(urut);"
            exp = json.dumps(srt, separators=(",", ":"))
            task = f"mengurutkan angka {nums} dari kecil ke besar tanpa merusak array asli"
            outro = f"Pembanding `(a, b) => a - b` wajib dipakai agar JS mengurutkan nilai angka (`{exp}`), bukan urutan teks."
        elif mode == 5:
            kata = f"belajar-js-{i}"
            code = f"const slug = {json.dumps(kata)};\nconst bagian = slug.split('-');\nconsole.log(bagian.join(' '));"
            exp = kata.replace("-", " ")
            task = f"memecah teks '{kata}' berdasarkan tanda hubung lalu menggabungkannya dengan spasi"
            outro = f"`.split('-')` memecah string jadi array, lalu `.join(' ')` menyatukannya menjadi `{exp}`."
        elif mode == 6:
            harga = (i + 5) * 2500
            qty = (i % 8) + 2
            code = f"const hitungTotal = (harga, jumlah) => harga * jumlah;\nconsole.log(hitungTotal({harga}, {qty}));"
            exp = str(harga * qty)
            task = f"membuat arrow function perkalian harga {harga} dan jumlah {qty}"
            outro = f"Arrow function langsung mengembalikan hasil kali tanpa kata kunci `return`, yaitu `{exp}`."
        elif mode == 7:
            produk = f"Item-{i}"
            stok = (i % 40) + 1
            code = f"const barang = {{ nama: {json.dumps(produk)}, stok: {stok} }};\nconst {{ nama, stok }} = barang;\nconsole.log(`${{nama}}: ${{stok}}`);"
            exp = f"{produk}: {stok}"
            task = f"mengambil properti objek `{produk}` (stok {stok}) memakai destructuring"
            outro = f"Destructuring `const {{ nama, stok }} = barang` mengambil properti ke variabel lokal dan mencetak `{exp}`."
        elif mode == 8:
            btn_id = f"tombol-{i}"
            pesan = f"Data ke-{i} tersimpan!"
            code = (
                f"const btn = document.getElementById({json.dumps(btn_id)});\n"
                "btn.addEventListener('click', () => {\n"
                f"  console.log({json.dumps(pesan)});\n"
                "});"
            )
            run_flag = False
            task = f"menangani klik pada tombol ber-id '{btn_id}' untuk mencetak '{pesan}'"
            outro = f"`addEventListener('click', ...)` pada `#{btn_id}` menjalankan fungsi setiap kali tombol diklik."
        else:
            arr_a = [i % 13 + 1, (i // 10) + 2]
            arr_b = [(i + 4) % 17 + 1, i % 13 + 1]
            merged = list(dict.fromkeys(arr_a + arr_b))
            code = f"const gabung = [...new Set([...{json.dumps(arr_a)}, ...{json.dumps(arr_b)}])];\nconsole.log(gabung);"
            exp = json.dumps(merged, separators=(",", ":"))
            task = f"menggabungkan array {arr_a} dan {arr_b} sekaligus membuang duplikat"
            outro = f"`Set` hanya menyimpan nilai unik, lalu spread `[...]` mengubahnya kembali jadi array `{exp}`."

        ok, _ = ver.verify_js_or_ts(code, lang="js", run=run_flag, expected_out=exp)
        if ok:
            q = pick_det(q_styles, key).format(task=task)
            col.add(q, _wrap_code(intro, "javascript", code, outro))

    # Tebak output & perbaiki bug JS
    for i in range(600):
        if limit and len(col.rows) >= limit:
            return
        key = f"js-trace-{i}"
        mode = i % 3
        if mode == 0:
            n = (i % 40) + 10
            code = f"const a = '{n}';\nconst b = {i % 9 + 2};\nconsole.log(Number(a) + b);"
            exp = str(n + (i % 9 + 2))
            q = f"gimana cara menjumlahkan string angka `'{n}'` dengan `{i % 9 + 2}` di JS supaya nggak jadi gabung teks?"
            ans = _wrap_code(
                f"Kalau langsung `'${n}' + {i % 9 + 2}`, JS akan menggabungkan teks. Ubah dulu pakai `Number()`:",
                "javascript",
                code,
                f"Setelah dikonversi ke tipe angka, penjumlahannya menghasilkan `{exp}`.",
            )
        elif mode == 1:
            a = (i % 30) + 5
            code = f"const nilai = {a};\nconsole.log(nilai === {a}, nilai === '{a}');"
            exp = "true false"
            q = f"apa output `const nilai = {a}; console.log(nilai === {a}, nilai === '{a}')` di JavaScript?"
            ans = _wrap_code(
                f"Output yang keluar adalah `{exp}`:",
                "javascript",
                code,
                "`===` mengecek nilai sekaligus tipe datanya, jadi angka dan string dianggap berbeda (`false`).",
            )
        else:
            words = [f"kata{i}", "belajar", "nara"]
            code = f"const kata = {json.dumps(words)};\nconsole.log(kata.includes('nara'), kata.length);"
            exp = "true 3"
            q = f"apa hasil dari kode JS `const kata = {json.dumps(words)}; console.log(kata.includes('nara'), kata.length)`?"
            ans = _wrap_code(
                f"Hasil yang tercetak di konsol adalah `{exp}`:",
                "javascript",
                code,
                "`.includes('nara')` bernilai `true` karena ada di array, dan `.length` mengembalikan jumlah elemen `3`.",
            )

        ok, _ = ver.verify_js_or_ts(code, lang="js", run=True, expected_out=exp)
        if ok:
            col.add(q, ans)


def _gen_ts(col: CategoryCollector, ver: CodeVerifier, rng: random.Random, limit: int | None) -> None:
    q_styles = [
        "contoh kode TypeScript sederhana untuk {task}",
        "gimana cara nulis {task} di TypeScript?",
        "nara, kasih contoh TS singkat buat {task} dong",
        "cara membuat {task} pakai TypeScript gimana?",
        "tolong bikinin potongan TypeScript untuk {task}",
    ]

    roles = ["admin", "member", "editor", "tamu"]
    names = ["Nara", "Budi", "Siti", "Raka", "Nadia", "Fajar", "Dewi", "Andi", "Putri", "Dimas"]

    for i in range(1350):
        if limit and len(col.rows) >= limit:
            return
        key = f"ts-core-{i}"
        intro = pick_det(TS_INTROS, key)
        mode = i % 6
        nm = names[i % len(names)]

        if mode == 0:
            a, b = (i % 30) + 4, ((i * 3) % 25) + 2
            code = (
                "function tambah(a: number, b: number): number {\n"
                "  return a + b;\n"
                "}\n"
                f"console.log(tambah({a}, {b}));"
            )
            exp = str(a + b)
            task = f"fungsi penjumlahan bertipe `number` untuk angka {a} dan {b}"
            outro = f"Tipe parameter dan nilai balik dikunci sebagai `number`, hasilnya `{exp}`."
        elif mode == 1:
            umur = 16 + (i % 30)
            aktif = "true" if i % 2 == 0 else "false"
            code = (
                "interface Pengguna {\n"
                "  nama: string;\n"
                "  umur: number;\n"
                "  aktif: boolean;\n"
                "}\n"
                f"const u: Pengguna = {{ nama: {json.dumps(nm)}, umur: {umur}, aktif: {aktif} }};\n"
                "console.log(`${u.nama} (${u.umur})`);"
            )
            exp = f"{nm} ({umur})"
            task = f"interface `Pengguna` untuk data {nm} berumur {umur} tahun"
            outro = f"`interface` memastikan struktur objek lengkap sebelum dipakai; outputnya `{exp}`."
        elif mode == 2:
            role = roles[i % len(roles)]
            uid = 100 + i
            code = (
                "type Peran = 'admin' | 'member' | 'editor' | 'tamu';\n"
                f"const peranUser: Peran = {json.dumps(role)};\n"
                f"const idAkun: number = {uid};\n"
                "console.log(`${idAkun}:${peranUser}`);"
            )
            exp = f"{uid}:{role}"
            task = f"union type `Peran` untuk akun ID {uid} berperannya '{role}'"
            outro = f"Union type mencegah salah ketik di luar pilihan yang diizinkan, mencetak `{exp}`."
        elif mode == 3:
            arr = [i % 15 + 2, (i + 5) % 20 + 3, (i + 9) % 18 + 4]
            code = (
                "function totalAngka(daftar: number[]): number {\n"
                "  return daftar.reduce((s, n) => s + n, 0);\n"
                "}\n"
                f"console.log(totalAngka({json.dumps(arr)}));"
            )
            exp = str(sum(arr))
            task = f"fungsi bertipe array `number[]` yang menjumlahkan {arr}"
            outro = f"`number[]` menjaga agar array hanya berisi angka; hasilnya `{exp}`."
        elif mode == 4:
            harga = (i + 3) * 7500
            pajak_pct = [5, 10, 11, 12][i % 4]
            total_h = harga + (harga * pajak_pct // 100)
            code = (
                f"function hitungBayar(harga: number, pajak: number = {pajak_pct}): number {{\n"
                "  return harga + Math.floor((harga * pajak) / 100);\n"
                "}\n"
                f"console.log(hitungBayar({harga}));"
            )
            exp = str(total_h)
            task = f"fungsi dengan parameter default pajak {pajak_pct}% untuk harga {harga}"
            outro = f"Jika argumen kedua dikosongkan, nilai bawaan `{pajak_pct}` dipakai dan mencetak `{exp}`."
        else:
            item_val = f" paket-{i}" .strip()
            code = (
                "function ambilPertama<T>(data: T[]): T {\n"
                "  return data[0];\n"
                "}\n"
                f"console.log(ambilPertama<string>([{json.dumps(item_val)}, 'cadangan']));"
            )
            exp = item_val
            task = f"fungsi generic `<T>` untuk mengambil elemen pertama `'{item_val}'`"
            outro = f"Generic `<T>` membuat fungsi tetap fleksibel tanpa kehilangan tipe datanya (`{exp}`)."

        ok, _ = ver.verify_js_or_ts(code, lang="ts", run=True, expected_out=exp)
        if ok:
            q = pick_det(q_styles, key).format(task=task)
            col.add(q, _wrap_code(intro, "ts", code, outro))


def _gen_html_css(col: CategoryCollector, ver: CodeVerifier, rng: random.Random, limit: int | None) -> None:
    html_q = [
        "contoh HTML sederhana untuk {task}",
        "gimana cara bikin {task} pakai HTML?",
        "nara, tolong bikinin tag HTML buat {task}",
        "struktur HTML singkat untuk {task} gimana ya?",
        "bantu potongan kode HTML untuk {task} dong",
    ]
    css_q = [
        "contoh CSS sederhana untuk {task}",
        "gimana cara {task} pakai CSS?",
        "nara, kasih kode CSS singkat buat {task} dong",
        "aturan CSS biar bisa {task} gimana?",
        "tolong bantu CSS untuk {task}",
    ]

    # HTML (~1,450 examples)
    menus = [
        ("Nasi Goreng", "Teh Hangat", "Pisang Bakar"),
        ("Soto Ayam", "Jeruk Peras", "Tempe Mendoan"),
        ("Mie Ayam", "Es Cincau", "Tahu Isi"),
        ("Gado-Gado", "Air Mineral", "Kerupuk"),
        ("Bakso Urat", "Es Teh", "Pangsit"),
    ]
    for i in range(1450):
        if limit and len(col.rows) >= limit:
            return
        key = f"html-{i}"
        intro = pick_det(HTML_INTROS, key)
        mode = i % 7
        if mode == 0:
            judul = f"Catatan Belajar Minggu {i + 1}"
            isi = f"Hari ini fokus latihan bagian ke-{i + 1} sampai paham."
            code = (
                f"<article class=\"catatan-{i % 20}\">\n"
                f"  <h2>{judul}</h2>\n"
                f"  <p>{isi}</p>\n"
                "</article>"
            )
            task = f"kartu artikel berjudul '{judul}'"
            outro = "Tag `<article>` membungkus judul `<h2>` dan paragraf `<p>` secara semantik."
        elif mode == 1:
            m1, m2, m3 = menus[i % len(menus)]
            code = (
                f"<ul id=\"menu-{i}\">\n"
                f"  <li>{m1}</li>\n"
                f"  <li>{m2}</li>\n"
                f"  <li>{m3}</li>\n"
                "</ul>"
            )
            task = f"daftar tidak berurutan (`ul`) berisi {m1}, {m2}, dan {m3} (id `menu-{i}`)"
            outro = "Gunakan `<ul>` untuk daftar poin dan `<li>` untuk setiap item di dalamnya."
        elif mode == 2:
            field = ["username", "email", "nama_lengkap", "kota_asal", "kode_pos"][i % 5]
            itype = "email" if field == "email" else "text"
            code = (
                f"<form action=\"/simpan-{i}\" method=\"post\">\n"
                f"  <label for=\"{field}-{i}\">Isi {field}:</label>\n"
                f"  <input id=\"{field}-{i}\" name=\"{field}\" type=\"{itype}\" required>\n"
                "  <button type=\"submit\">Kirim</button>\n"
                "</form>"
            )
            task = f"form input `{field}` wajib isi dengan tombol kirim (endpoint `/simpan-{i}`)"
            outro = "Atribut `for` pada `<label>` dihubungkan ke `id` input agar aksesibel, dan `required` mencegah kiriman kosong."
        elif mode == 3:
            img_name = f"foto-kegiatan-{i}.jpg"
            alt_txt = f"Dokumentasi kegiatan nomor {i}"
            code = (
                "<figure>\n"
                f"  <img src=\"/aset/{img_name}\" alt=\"{alt_txt}\" width=\"320\">\n"
                f"  <figcaption>{alt_txt}</figcaption>\n"
                "</figure>"
            )
            task = f"gambar `/aset/{img_name}` lengkap dengan teks alternatif dan keterangan bawah"
            outro = "Selalu isi atribut `alt` supaya pembaca layar dan browser tetap paham isi gambarnya."
        elif mode == 4:
            barang = f"Buku Seri {i + 1}"
            harga_s = f"Rp{(i % 15 + 3) * 10}.000"
            code = (
                "<table>\n"
                "  <tr><th>Produk</th><th>Harga</th></tr>\n"
                f"  <tr><td>{barang}</td><td>{harga_s}</td></tr>\n"
                "</table>"
            )
            task = f"tabel dua kolom yang menampilkan '{barang}' dengan harga {harga_s}"
            outro = "`<tr>` membuat baris tabel, `<th>` untuk judul kolom, dan `<td>` untuk sel datanya."
        elif mode == 5:
            tanya = f"Bagaimana jadwal kelas batch {i + 1}?"
            jawab = f"Kelas batch {i + 1} dimulai setiap pukul 19.00 WIB."
            code = (
                "<details>\n"
                f"  <summary>{tanya}</summary>\n"
                f"  <p>{jawab}</p>\n"
                "</details>"
            )
            task = f"elemen buka-tutup (accordion) FAQ untuk '{tanya}'"
            outro = "`<details>` dan `<summary>` membuat kotak tanya-jawab lipat bawaan HTML tanpa perlu JavaScript."
        else:
            hal = f"materi-{i + 1}.html"
            label = f"Buka Materi {i + 1}"
            code = (
                "<nav>\n"
                "  <a href=\"index.html\">Beranda</a>\n"
                f"  <a href=\"{hal}\">{label}</a>\n"
                "</nav>"
            )
            task = f"menu navigasi menuju Beranda dan `{hal}`"
            outro = "Tag `<nav>` menandai bagian tautan navigasi utama di halaman web."

        ok, _ = ver.verify_html(code)
        if ok:
            q = pick_det(html_q, key).format(task=task)
            col.add(q, _wrap_code(intro, "html", code, outro))

    # CSS (~1,450 examples)
    colors = ["#2563eb", "#16a34a", "#dc2626", "#7c3aed", "#ea580c", "#0f766e", "#1e293b", "#be123c"]
    for i in range(1450):
        if limit and len(col.rows) >= limit:
            return
        key = f"css-{i}"
        intro = pick_det(CSS_INTROS, key)
        mode = i % 6
        col_hex = colors[i % len(colors)]

        if mode == 0:
            pad_y = 6 + (i % 9) * 2
            pad_x = 12 + (i % 11) * 2
            rad = 4 + (i % 10) * 2
            cls = f"btn-aksi-{i}"
            code = (
                f".{cls} {{\n"
                f"  background-color: {col_hex};\n"
                "  color: #ffffff;\n"
                f"  padding: {pad_y}px {pad_x}px;\n"
                f"  border-radius: {rad}px;\n"
                "  border: none;\n"
                "}"
            )
            task = f"membuat tombol `.{cls}` berwarna `{col_hex}` dengan sudut membulat `{rad}px` dan padding `{pad_y}px {pad_x}px`"
            outro = f"Pada `.{cls}`, `padding` memberi ruang dalam tombol sedangkan `border-radius` menghaluskan sudutnya."
        elif mode == 1:
            gap_px = 8 + (i % 15) * 2
            min_h = 180 + (i % 25) * 10
            cls = f"wadah-tengah-{i}"
            code = (
                f".{cls} {{\n"
                "  display: flex;\n"
                "  justify-content: center;\n"
                "  align-items: center;\n"
                f"  gap: {gap_px}px;\n"
                f"  min-height: {min_h}px;\n"
                "}"
            )
            task = f"meratakan isi `.{cls}` tepat di tengah memakai Flexbox (tinggi minimal `{min_h}px`, jarak `{gap_px}px`)"
            outro = f"Pada `.{cls}`, `justify-content: center` dan `align-items: center` menengahkan elemen mendatar sekaligus tegak."
        elif mode == 2:
            cols = (i % 5) + 2
            gap_px = 8 + (i % 14) * 2
            cls = f"galeri-{i}"
            code = (
                f".{cls} {{\n"
                "  display: grid;\n"
                f"  grid-template-columns: repeat({cols}, 1fr);\n"
                f"  gap: {gap_px}px;\n"
                "}"
            )
            task = f"menyusun `.{cls}` menjadi {cols} kolom sama lebar dengan jarak `{gap_px}px` pakai CSS Grid"
            outro = f"Pada `.{cls}`, `repeat({cols}, 1fr)` membagi ruang menjadi {cols} kolom seimbang."
        elif mode == 3:
            max_w = 480 + (i % 30) * 20
            pad = 12 + (i % 9) * 4
            cls = f"kontainer-{i}"
            code = (
                f".{cls} {{\n"
                f"  max-width: {max_w}px;\n"
                "  margin: 0 auto;\n"
                f"  padding: {pad}px;\n"
                "  box-sizing: border-box;\n"
                "}"
            )
            task = f"membatasi lebar `.{cls}` maksimal `{max_w}px` di tengah layar dengan padding `{pad}px`"
            outro = f"Pada `.{cls}`, `margin: 0 auto` menaruh blok di tengah halaman saat lebarnya dibatasi `max-width`."
        elif mode == 4:
            fsize = 14 + (i % 15)
            lh = round(1.4 + (i % 6) * 0.1, 1)
            cls = f"teks-baca-{i}"
            code = (
                f".{cls} {{\n"
                f"  font-size: {fsize}px;\n"
                f"  line-height: {lh};\n"
                f"  color: {col_hex};\n"
                "}"
            )
            task = f"mengatur ukuran huruf `{fsize}px`, jarak baris `{lh}`, dan warna `{col_hex}` pada `.{cls}`"
            outro = f"Pada `.{cls}`, `line-height: {lh}` membuat paragraf panjang jauh lebih nyaman dibaca."
        else:
            rad = 6 + (i % 9) * 2
            pad = 12 + (i % 8) * 2
            cls = f"kartu-{i}"
            code = (
                f".{cls} {{\n"
                "  background-color: #ffffff;\n"
                f"  padding: {pad}px;\n"
                f"  border-radius: {rad}px;\n"
                "  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);\n"
                "}"
            )
            task = f"memberi bayangan halus, radius `{rad}px`, dan padding `{pad}px` pada `.{cls}`"
            outro = f"Pada `.{cls}`, `box-shadow` tipis memberi kesan kartu terangkat dari latar halaman."

        ok, _ = ver.verify_css(code)
        if ok:
            q = pick_det(css_q, key).format(task=task)
            col.add(q, _wrap_code(intro, "css", code, outro))


def _gen_cpp_and_c(col: CategoryCollector, ver: CodeVerifier, limit: int | None) -> None:
    cpp_q = [
        "contoh program C++ sederhana untuk {task}",
        "gimana cara {task} di C++?",
        "nara, bikinin kode C++ singkat buat {task} dong",
        "tolong kasih contoh C++ untuk {task}",
        "cara nulis program {task} pakai C++ gimana?",
    ]
    c_q = [
        "contoh program bahasa C sederhana untuk {task}",
        "gimana cara {task} pakai bahasa C?",
        "nara, kasih contoh kode C singkat buat {task} dong",
        "cara membuat {task} di bahasa C gimana?",
    ]

    cpp_candidates: list[tuple[str, str, str, str, str]] = []
    target_cpp = 1100 if limit is None else min(limit, 120)
    for i in range(target_cpp):
        key = f"cpp-{i}"
        intro = pick_det(CPP_INTROS, key)
        mode = i % 6
        if mode == 0:
            a, b = (i % 45) + 5, ((i * 3) % 40) + 4
            code = (
                "#include <iostream>\n"
                "using namespace std;\n"
                "int main() {\n"
                f"  int a = {a}, b = {b};\n"
                "  cout << a + b << endl;\n"
                "  return 0;\n"
                "}"
            )
            exp = str(a + b)
            task = f"menjumlahkan bilangan {a} dan {b}"
            outro = f"`cout` mencetak hasil `a + b` ke layar, yaitu `{exp}`."
        elif mode == 1:
            n = i + 11
            label = "genap" if n % 2 == 0 else "ganjil"
            code = (
                "#include <iostream>\n"
                "using namespace std;\n"
                "int main() {\n"
                f"  int n = {n};\n"
                "  cout << (n % 2 == 0 ? \"genap\" : \"ganjil\") << endl;\n"
                "  return 0;\n"
                "}"
            )
            exp = label
            task = f"mengecek apakah angka {n} genap atau ganjil"
            outro = f"Operator ternary memeriksa sisa bagi `n % 2`, dan untuk `{n}` mencetak `{exp}`."
        elif mode == 2:
            batas = (i % 15) + 4
            total = batas * (batas + 1) // 2
            code = (
                "#include <iostream>\n"
                "using namespace std;\n"
                "int main() {\n"
                "  int total = 0;\n"
                f"  for (int i = 1; i <= {batas}; i++) total += i;\n"
                "  cout << total << endl;\n"
                "  return 0;\n"
                "}"
            )
            exp = str(total)
            task = f"menjumlahkan deret angka 1 sampai {batas} memakai perulangan `for`"
            outro = f"Perulangan menambah `total` dari 1 hingga `{batas}` sehingga menghasilkan `{exp}`."
        elif mode == 3:
            v1, v2, v3, v4 = (i % 30) + 3, ((i * 5) % 40) + 2, ((i * 7) % 35) + 9, (i % 20) + 1
            mx = max(v1, v2, v3, v4)
            code = (
                "#include <iostream>\n"
                "#include <vector>\n"
                "#include <algorithm>\n"
                "using namespace std;\n"
                "int main() {\n"
                f"  vector<int> v = {{{v1}, {v2}, {v3}, {v4}}};\n"
                "  cout << *max_element(v.begin(), v.end()) << endl;\n"
                "}"
            )
            exp = str(mx)
            task = f"mencari nilai terbesar di `vector` {{{v1}, {v2}, {v3}, {v4}}}"
            outro = f"`max_element` dari `<algorithm>` menunjuk elemen terbesar di vector, yaitu `{exp}`."
        elif mode == 4:
            p, l = (i % 22) + 3, ((i * 3) % 18) + 2
            code = (
                "#include <iostream>\n"
                "using namespace std;\n"
                f"int luas(int p, int l) {{ return p * l; }}\n"
                "int main() {\n"
                f"  cout << luas({p}, {l}) << endl;\n"
                "  return 0;\n"
                "}"
            )
            exp = str(p * l)
            task = f"membuat fungsi `luas` persegi panjang untuk ukuran {p} dan {l}"
            outro = f"Fungsi `luas({p}, {l})` mengembalikan hasil kali kedua sisi, yaitu `{exp}`."
        else:
            kata = f"NaraCpp{i}"
            code = (
                "#include <iostream>\n"
                "#include <string>\n"
                "using namespace std;\n"
                "int main() {\n"
                f"  string teks = {json.dumps(kata)};\n"
                "  cout << teks.length() << endl;\n"
                "}"
            )
            exp = str(len(kata))
            task = f"menghitung panjang string `{kata}` memakai `std::string`"
            outro = f"Method `.length()` mengembalikan jumlah karakter pada string, yaitu `{exp}`."

        cpp_candidates.append((key, intro, code, exp, f"{task}||{outro}"))

    cpp_verified = ver.verify_cpp_batch([(c[2], c[3]) for c in cpp_candidates])
    for (key, intro, code, _, meta), (ok, _) in zip(cpp_candidates, cpp_verified):
        if limit and len(col.rows) >= limit:
            return
        if ok:
            task, outro = meta.split("||", 1)
            q = pick_det(cpp_q, key).format(task=task)
            col.add(q, _wrap_code(intro, "cpp", code, outro))

    # Bahasa C (~400 examples)
    c_candidates: list[tuple[str, str, str, str]] = []
    target_c = 400 if limit is None else min(limit, 50)
    for i in range(target_c):
        key = f"c-lang-{i}"
        mode = i % 3
        if mode == 0:
            a, b = (i % 50) + 6, ((i * 3) % 30) + 4
            code = (
                "#include <stdio.h>\n"
                "int main(void) {\n"
                f"  int a = {a}, b = {b};\n"
                "  printf(\"%d\\n\", a * b);\n"
                "  return 0;\n"
                "}"
            )
            exp = str(a * b)
            task = f"mengalikan {a} dan {b} lalu menampilkannya dengan `printf`"
            outro = f"Format `%d` pada `printf` mencetak bilangan bulat `{exp}`."
        elif mode == 1:
            n = (i % 12) + 3
            s = sum(range(1, n + 1))
            code = (
                "#include <stdio.h>\n"
                "int main(void) {\n"
                "  int jml = 0;\n"
                f"  for (int i = 1; i <= {n}; i++) jml += i;\n"
                "  printf(\"%d\\n\", jml);\n"
                "  return 0;\n"
                "}"
            )
            exp = str(s)
            task = f"menghitung jumlah angka 1 sampai {n} memakai loop `for`"
            outro = f"Variabel `jml` bertambah setiap iterasi hingga mencetak `{exp}`."
        else:
            x, y, z = (i % 20) + 2, ((i + 5) % 25) + 3, ((i + 9) % 30) + 1
            code = (
                "#include <stdio.h>\n"
                "int main(void) {\n"
                f"  int arr[3] = {{{x}, {y}, {z}}};\n"
                "  printf(\"%d\\n\", arr[0] + arr[1] + arr[2]);\n"
                "  return 0;\n"
                "}"
            )
            exp = str(x + y + z)
            task = f"menjumlahkan isi array C `{{{x}, {y}, {z}}}`"
            outro = f"Ketiga elemen array diakses lewat indeks `0..2`, menghasilkan `{exp}`."
        c_candidates.append((key, code, exp, f"{task}||{outro}"))

    c_verified = ver.verify_c_batch([(c[1], c[2]) for c in c_candidates])
    for (key, code, _, meta), (ok, _) in zip(c_candidates, c_verified):
        if limit and len(col.rows) >= limit:
            return
        if ok:
            task, outro = meta.split("||", 1)
            q = pick_det(c_q, key).format(task=task)
            col.add(q, _wrap_code("Ini contoh sederhananya dalam bahasa C:", "c", code, outro))


def _gen_sql_bash_json(col: CategoryCollector, ver: CodeVerifier, limit: int | None) -> None:
    sql_q = [
        "contoh query SQL untuk {task}",
        "gimana cara {task} pakai SQL?",
        "nara, bantu query SQL buat {task} dong",
        "tuliskan perintah SQL sederhana untuk {task}",
    ]
    for i in range(550):
        if limit and len(col.rows) >= limit:
            return
        key = f"sql-{i}"
        mode = i % 5
        if mode == 0:
            batas = 75 + (i % 20)
            code = f"SELECT nama, nilai\nFROM siswa\nWHERE nilai >= {batas}\nORDER BY nilai DESC;"
            task = f"mengambil nama dan nilai dari tabel `siswa` yang nilainya minimal {batas} (urut tertinggi)"
            outro = f"`WHERE nilai >= {batas}` menyaring baris, lalu `ORDER BY nilai DESC` mengurutkannya dari tertinggi."
        elif mode == 1:
            harga_max = (i % 25 + 2) * 5000
            code = f"SELECT nama, harga\nFROM produk\nWHERE harga <= {harga_max} AND stok > 10;"
            task = f"mencari produk dengan harga maksimal {harga_max} dan stok di atas 10"
            outro = "Operator `AND` memastikan kedua syarat harga serta stok terpenuhi sekaligus."
        elif mode == 2:
            lim = (i % 5) + 1
            code = f"SELECT divisi, COUNT(*) AS jumlah, AVG(gaji) AS rata_gaji\nFROM pegawai\nGROUP BY divisi\nLIMIT {lim};"
            task = f"menghitung jumlah pegawai dan rata-rata gaji per divisi (ambil {lim} baris teratas)"
            outro = "`GROUP BY divisi` mengelompokkan baris sebelum dihitung oleh `COUNT(*)` dan `AVG(gaji)`."
        elif mode == 3:
            stok_baru = 30 + (i % 50)
            pid = (i % 4) + 1
            code = f"UPDATE produk\nSET stok = {stok_baru}\nWHERE id = {pid};"
            task = f"mengubah stok produk ber-id {pid} menjadi {stok_baru}"
            outro = "Selalu sertakan `WHERE id = ...` pada `UPDATE` agar tidak mengubah seluruh baris tabel."
        else:
            nm = f"Siswa_{i}"
            nilai = 70 + (i % 30)
            code = f"INSERT INTO siswa (id, nama, kelas, nilai, umur)\nVALUES ({100 + i}, '{nm}', '10A', {nilai}, 16);"
            task = f"menambahkan data `{nm}` dengan nilai {nilai} ke tabel `siswa`"
            outro = "`INSERT INTO` menyebutkan kolom tujuan lalu mengisi nilainya lewat `VALUES`."

        ok, _ = ver.verify_sql(code)
        if ok:
            q = pick_det(sql_q, key).format(task=task)
            col.add(q, _wrap_code("Ini contoh query SQL-nya:", "sql", code, outro))

    # Bash & JSON (~550 examples)
    bash_q = [
        "contoh perintah bash untuk {task}",
        "gimana cara {task} di terminal Linux/bash?",
        "nara, kasih skrip bash singkat buat {task} dong",
    ]
    for i in range(300):
        if limit and len(col.rows) >= limit:
            return
        key = f"bash-{i}"
        mode = i % 3
        if mode == 0:
            folder = f"proyek_{i}"
            code = f"mkdir -p {folder}/src\ncd {folder}\nls -la"
            task = f"membuat folder `{folder}/src` lalu masuk dan melihat isinya"
            outro = "Opsi `-p` membuat folder induk sekaligus tanpa error kalau foldernya sudah ada."
        elif mode == 1:
            fname = f"catatan_{i}.txt"
            code = f"if [ -f \"{fname}\" ]; then\n  wc -l \"{fname}\"\nelse\n  echo \"File belum ada\"\nfi"
            task = f"mengecek apakah file `{fname}` ada lalu menghitung jumlah barisnya"
            outro = "`[ -f ... ]` memeriksa keberadaan file biasa, dan `wc -l` menghitung barisnya."
        else:
            kata = f"error_{i}"
            code = f"grep -rn \"{kata}\" ./logs"
            task = f"mencari teks `{kata}` beserta nomor barisnya di dalam folder `./logs`"
            outro = "Flag `-r` mencari secara rekursif ke subfolder dan `-n` menampilkan nomor barisnya."

        ok, _ = ver.verify_bash(code)
        if ok:
            q = pick_det(bash_q, key).format(task=task)
            col.add(q, _wrap_code("Kamu bisa jalankan perintah bash ini:", "bash", code, outro))

    json_q = [
        "contoh format JSON valid untuk {task}",
        "gimana penulisan JSON untuk {task}?",
        "nara, bikinin contoh objek JSON buat {task} dong",
    ]
    for i in range(300):
        if limit and len(col.rows) >= limit:
            return
        key = f"json-{i}"
        obj = {
            "id": i + 1,
            "judul": f"Tugas Harian {i + 1}",
            "selesai": bool(i % 2 == 0),
            "prioritas": ["rendah", "sedang", "tinggi"][i % 3],
        }
        code = json.dumps(obj, ensure_ascii=False, indent=2)
        task = f"data tugas id {i + 1} berjudul '{obj['judul']}' dengan prioritas '{obj['prioritas']}'"
        outro = "Di JSON, semua nama key wajib memakai tanda kutip ganda `\"...\"` dan boolean ditulis huruf kecil (`true`/`false`)."
        ok, _ = ver.verify_json(code)
        if ok:
            q = pick_det(json_q, key).format(task=task)
            col.add(q, _wrap_code("Ini contoh format JSON yang valid:", "json", code, outro))

    # Konsep pemrograman & Git dasar sehari-hari (dengan contoh diuji)
    concept_seeds = [
        (
            [
                "apa bedanya let dan const di JavaScript?",
                "kapan harus pakai let atau const di JS?",
                "nara, jelasin beda let sama const dong",
                "di JS bedanya variabel let dan const apa ya?",
                "kenapa orang sering pakai const daripada let di JS?",
            ],
            "js",
            "const pi = 3.14;\nlet skor = 10;\nskor = 15;\nconsole.log(pi, skor);",
            "3.14 15",
            "`const` dipakai untuk variabel yang referensinya nggak diganti ulang, sedangkan `let` dipakai kalau nilainya bakal berubah.",
            "Biasakan pakai `const` dulu supaya kode lebih aman dari perubahan nggak sengaja.",
        ),
        (
            [
                "apa bedanya == dan === di JavaScript?",
                "kenapa di JS disarankan pakai === daripada ==?",
                "jelasin perbedaan == sama === di JS dong",
                "di JavaScript hasil 5 == '5' sama 5 === '5' beda ya?",
                "nara, kapan pakai === di JavaScript?",
            ],
            "js",
            "console.log(5 == '5');\nconsole.log(5 === '5');",
            "true\nfalse",
            "`==` menyamakan tipe data secara otomatis sebelum dibandingkan, sedangkan `===` membandingkan nilai sekaligus tipe datanya.",
            "Pakai `===` biar terhindar dari bug konversi tipe otomatis yang membingungkan.",
        ),
        (
            [
                "apa bedanya list dan tuple di Python?",
                "kapan pakai tuple dibanding list di Python?",
                "nara, jelasin beda list sama tuple di py dong",
                "list `[1, 2]` dan tuple `(1, 2)` di Python bedanya apa?",
                "kenapa tuple di Python nggak bisa diubah isinya?",
            ],
            "py",
            "daftar = [1, 2]\ndaftar.append(3)\ntetap = (1, 2)\nprint(daftar, tetap)",
            "[1, 2, 3] (1, 2)",
            "`list` bersifat *mutable* (isinya bisa ditambah, diubah, atau dihapus), sedangkan `tuple` bersifat *immutable* (isinya tetap setelah dibuat).",
            "Gunakan `tuple` untuk data tetap seperti koordinat `(x, y)` dan `list` untuk kumpulan data dinamis.",
        ),
        (
            [
                "apa bedanya fungsi return dan print di Python?",
                "kenapa fungsi Python tanpa return hasilnya None?",
                "nara, beda print() sama return di fungsi Python apa?",
                "kapan harus pakai return di dalam def Python?",
                "jelasin perbedaan return dan print buat pemula dong",
            ],
            "py",
            "def tambah(a, b):\n  return a + b\nhasil = tambah(4, 6)\nprint(hasil * 2)",
            "20",
            "`print()` hanya menampilkan teks ke layar, sedangkan `return` mengirimkan nilai keluar dari fungsi supaya bisa disimpan atau dihitung lagi.",
            "Kalau fungsi nggak menulis `return`, Python otomatis mengembalikan `None`.",
        ),
        (
            [
                "apa bedanya class dan id di HTML serta CSS?",
                "kapan pakai .class dan kapan pakai #id di CSS?",
                "nara, bedanya selektor titik dan pagar di CSS apa?",
                "jelasin beda atribut id sama class di HTML dong",
                "kenapa id di HTML nggak boleh kembar sedangkan class boleh?",
            ],
            "css",
            "#judul-utama {\n  font-size: 24px;\n}\n.kartu-info {\n  padding: 12px;\n}",
            None,
            "`id` (ditulis `#nama` di CSS) bersifat unik untuk satu elemen saja di halaman, sedangkan `class` (ditulis `.nama`) boleh dipakai berulang pada banyak elemen.",
            "Untuk mengatur tampilan komponen yang seragam, utamakan `class`.",
        ),
        (
            [
                "apa fungsi interface di TypeScript?",
                "kenapa di TypeScript sering bikin interface dulu?",
                "nara, jelasin kegunaan interface di TS dong",
                "interface pada TypeScript itu gunanya buat apa?",
                "contoh pemakaian interface sederhana di TS gimana?",
            ],
            "ts",
            "interface Buku {\n  judul: string;\n  halaman: number;\n}\nconst b: Buku = { judul: 'Logika Dasar', halaman: 120 };\nconsole.log(b.judul);",
            "Logika Dasar",
            "`interface` menentukan kontrak bentuk sebuah objek, mulai dari nama properti sampai tipe datanya.",
            "Kalau ada properti yang kurang atau salah tipe, TypeScript langsung memberi peringatan sebelum kode dijalankan.",
        ),
        (
            [
                "gimana urutan perintah Git dasar buat simpan perubahan?",
                "cara git add commit push yang bener gimana?",
                "nara, ajarin langkah dasar nyimpen kode pakai Git dong",
                "perintah Git sehari-hari buat commit kode apa aja?",
                "contoh alur git status sampai git push gimana?",
            ],
            "bash",
            "git status\ngit add .\ngit commit -m \"Perbaiki tampilan tombol\"\ngit push origin main",
            None,
            "Alur paling dasarnya adalah cek perubahan, masukkan ke staging, beri pesan commit yang jelas, lalu kirim ke repositori.",
            "Biasakan cek `git status` dulu supaya nggak ada file sementara yang ikut ter-commit.",
        ),
    ]

    ans_variants = [
        "{exp1}\n```{lang}\n{code}\n```\n{exp2}",
        "Singkatnya begini: {exp1}\n```{lang}\n{code}\n```\nCatatan kecil: {exp2}",
        "Biar gampang kebayang, lihat perbandingan ini dulu. {exp1}\n```{lang}\n{code}\n```\nIntinya, {exp2}",
        "Pertanyaan bagus buat dasar coding! {exp1}\n```{lang}\n{code}\n```\nTips praktisnya: {exp2}",
        "Yuk kita bedah singkat. {exp1}\n```{lang}\n{code}\n```\nJadi {exp2}",
    ]
    for q_list, lang, code, exp, exp1, exp2 in concept_seeds:
        if lang == "py":
            ok, _ = ver.verify_python(code, expected_out=exp)
            fence = "python"
        elif lang == "js":
            ok, _ = ver.verify_js_or_ts(code, lang="js", run=True, expected_out=exp)
            fence = "javascript"
        elif lang == "ts":
            ok, _ = ver.verify_js_or_ts(code, lang="ts", run=True, expected_out=exp)
            fence = "ts"
        elif lang == "css":
            ok, _ = ver.verify_css(code)
            fence = "css"
        else:
            ok, _ = ver.verify_bash(code)
            fence = "bash"
        if not ok:
            continue
        for idx, q in enumerate(q_list):
            if limit and len(col.rows) >= limit:
                return
            tmpl = ans_variants[idx % len(ans_variants)]
            ans = tmpl.format(
                exp1=exp1,
                lang=fence,
                code=code,
                exp2=exp2[0].lower() + exp2[1:] if tmpl.endswith("Jadi {exp2}") else exp2,
            )
            col.add(q, ans)


def build_kode(
    col: CategoryCollector,
    *,
    seed: int = 20261023,
    limit: int | None = None,
) -> dict:
    """Bangun seluruh contoh kategori kode dan kembalikan ringkasan verifikasi."""
    rng = random.Random(seed)
    ver = CodeVerifier()
    try:
        if limit is not None:
            per_sub = max(1, limit // 5)
            _gen_python(col, ver, rng, per_sub)
            _gen_js(col, ver, rng, per_sub * 2)
            _gen_ts(col, ver, rng, per_sub * 3)
            _gen_html_css(col, ver, rng, per_sub * 4)
            _gen_cpp_and_c(col, ver, limit)
            _gen_sql_bash_json(col, ver, limit)
        else:
            _gen_python(col, ver, rng, None)
            _gen_js(col, ver, rng, None)
            _gen_ts(col, ver, rng, None)
            _gen_html_css(col, ver, rng, None)
            _gen_cpp_and_c(col, ver, None)
            _gen_sql_bash_json(col, ver, None)
            from .gen_kode_extra import build_kode_extra
            build_kode_extra(col, ver, None)

        node_ok, node_err = ver.flush_node_cli_check()
        if not node_ok:
            raise RuntimeError(f"node --check batch gagal: {node_err}")
        return dict(ver.stats)
    finally:
        ver.close()
