"""Generator tambahan kategori `kode` untuk Nara-Allegretto-3 (v3).

Semua cuplikan baru di berkas ini:
- dibatasi maksimal 8 baris (diperiksa `CodeVerifier`),
- Python & JavaScript/TypeScript dieksekusi sungguhan dan outputnya dicocokkan
  dengan hasil yang dihitung generator,
- HTML/CSS divalidasi strukturnya, SQL dijalankan di sqlite3 in-memory,
  Bash dicek dengan `bash -n`, dan JSON diparsing dengan `json.loads`.
Parameter (angka, kata, nama, warna, tabel) diacak dari ruang kombinasi lebar
dengan benih tetap, lalu disaring registri duplikat global terhadap v2.
"""
from __future__ import annotations

import json
import os
import random
import sys

TOOLS_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if TOOLS_DIR not in sys.path:
    sys.path.insert(0, TOOLS_DIR)

import data_language  # noqa: E402

from .core_v3 import CategoryCollector, pick_det
from v2.code_verifier import CodeVerifier  # noqa: E402
from v2.gen_kode import (  # noqa: E402
    CSS_INTROS,
    HTML_INTROS,
    JS_INTROS,
    PY_INTROS,
    TS_INTROS,
    _wrap_code,
)

NAMES = ["Raka", "Siti", "Bima", "Nadia", "Eka", "Dimas", "Tania", "Fajar", "Lala", "Yuda", "Wulan", "Galih"]
CITIES = ["Magelang", "Semarang", "Yogyakarta", "Bandung", "Surabaya", "Malang", "Solo", "Bogor", "Denpasar", "Makassar", "Medan", "Palembang"]
ITEMS = ["buku tulis", "pulpen", "kopi sachet", "roti tawar", "susu kotak", "telur ayam", "sabun mandi", "baterai", "kaos kaki", "mie instan", "air mineral", "pensil"]
COLORS = ["#1d4ed8", "#047857", "#b45309", "#be185d", "#6d28d9", "#0f766e", "#b91c1c", "#334155", "#ea580c", "#15803d", "#0369a1", "#a21caf"]
CLASS_NAMES = ["kartu-profil", "tombol-utama", "judul-besar", "kotak-info", "menu-samping", "galeri-item", "label-harga", "panel-form", "daftar-tugas", "kepala-halaman"]

PY_Q = [
    "contoh kode Python pendek buat {task} dong",
    "gimana cara {task} pakai Python?",
    "nara, tolong bikinin skrip Python sederhana untuk {task}",
    "ada contoh Python singkat untuk {task}?",
    "ajarin aku {task} di Python lewat contoh kecil dong",
]
JS_Q = [
    "contoh kode JavaScript ringkas buat {task} dong",
    "gimana cara {task} pakai JavaScript?",
    "nara, tolong bikinin potongan JS sederhana untuk {task}",
    "ada contoh JavaScript singkat untuk {task}?",
]
TS_Q = [
    "contoh kode TypeScript pendek buat {task} dong",
    "gimana cara {task} pakai TypeScript bertipe jelas?",
    "nara, bikinin contoh TS sederhana untuk {task} ya",
]
HTML_Q = [
    "contoh markup HTML sederhana untuk {task} dong",
    "gimana struktur HTML buat {task}?",
    "nara, bikinin potongan HTML ringkas untuk {task}",
]
CSS_Q = [
    "contoh CSS sederhana untuk {task} dong",
    "gimana cara {task} pakai CSS?",
    "nara, bikinin aturan CSS ringkas buat {task}",
]
SQL_Q = [
    "contoh query SQL untuk {task} dong",
    "gimana perintah SQL buat {task}?",
    "nara, bantu tuliskan SQL sederhana untuk {task}",
]
BASH_Q = [
    "contoh skrip bash singkat buat {task} dong",
    "gimana cara {task} lewat terminal bash?",
    "nara, kasih perintah bash untuk {task} ya",
]
JSON_Q = [
    "contoh JSON yang valid untuk {task} dong",
    "gimana format JSON buat {task}?",
    "nara, bikinin objek JSON sederhana untuk {task}",
]

# Tabel contoh bawaan CodeVerifier.verify_sql (disalin agar hasil SELECT bisa
# dihitung persis oleh generator dan dicocokkan ke database sungguhan).
SISWA = [(1, "Budi", "10A", 85, 16), (2, "Siti", "10A", 92, 15), (3, "Raka", "10B", 78, 16), (4, "Nadia", "10B", 95, 16)]
PRODUK = [(1, "Buku Tulis", "Alat Tulis", 5000, 40), (2, "Pulpen", "Alat Tulis", 3500, 80), (3, "Tas Sekolah", "Tas", 120000, 12), (4, "Botol Minum", "Aksesoris", 45000, 25)]


def _rp(n: int) -> str:
    return "Rp" + f"{n:,}".replace(",", ".")


class _KodeV3:
    def __init__(self, col: CategoryCollector, ver: CodeVerifier, rng: random.Random):
        self.col = col
        self.ver = ver
        self.rng = rng
        words = [w for w in data_language.load_words() if 4 <= len(w) <= 9 and w.isalpha()]
        rng.shuffle(words)
        self.words = words
        self.i = 0

    def _word_phrase(self) -> tuple[str, str]:
        a = self.words[self.rng.randrange(len(self.words))]
        b = self.words[self.rng.randrange(len(self.words))]
        return a, b

    # ------------------------------- Python ------------------------------- #
    def add_python(self) -> bool:
        self.i += 1
        i, rng = self.i, self.rng
        mode = i % 8
        key = f"v3py-{mode}-{i}"
        intro = pick_det(PY_INTROS, key)
        if mode == 0:  # total belanja
            item = rng.choice(ITEMS)
            qty = rng.randint(2, 15)
            price = rng.randint(2, 60) * 500
            total = qty * price
            code = f"jumlah = {qty}\nharga_satuan = {price}\ntotal_bayar = jumlah * harga_satuan\nprint(total_bayar)"
            exp = str(total)
            task = f"menghitung total bayar untuk {qty} buah {item} seharga {_rp(price)} per buah"
            outro = f"Perkalian `jumlah * harga_satuan` pada program mencetak total `{exp}`."
        elif mode == 1:  # operasi list angka
            nums = [rng.randint(3, 99) for _ in range(rng.randint(4, 6))]
            op = rng.choice(["sum", "max", "min", "sorted"])
            if op == "sum":
                code = f"angka = {nums}\nprint(sum(angka))"
                exp = str(sum(nums))
                task = f"menjumlahkan semua isi list `{nums}`"
                outro = f"Fungsi `sum()` menambahkan seluruh anggota list dan mencetak `{exp}`."
            elif op == "max":
                code = f"angka = {nums}\nprint(max(angka))"
                exp = str(max(nums))
                task = f"mencari nilai terbesar dari list `{nums}`"
                outro = f"Fungsi `max()` mengambil nilai paling besar dari list, yaitu `{exp}`."
            elif op == "min":
                code = f"angka = {nums}\nprint(min(angka))"
                exp = str(min(nums))
                task = f"mencari nilai terkecil dari list `{nums}`"
                outro = f"Fungsi `min()` mengambil nilai paling kecil dari list, yaitu `{exp}`."
            else:
                code = f"angka = {nums}\nprint(sorted(angka))"
                exp = str(sorted(nums))
                task = f"mengurutkan list `{nums}` dari kecil ke besar"
                outro = f"`sorted()` menghasilkan list baru yang terurut naik: `{exp}`."
        elif mode == 2:  # operasi string dari dua kata acak
            a, b = self._word_phrase()
            phrase = f"{a} {b}"
            op = rng.choice(["title", "upper", "ganti", "iris", "hitung"])
            if op == "title":
                code = f"teks = {phrase!r}\nprint(teks.title())"
                exp = phrase.title()
                task = f"mengubah awal tiap kata pada teks `{phrase}` menjadi huruf kapital"
                outro = f"Method `.title()` mengapitalkan huruf pertama tiap kata menjadi `{exp}`."
            elif op == "upper":
                code = f"teks = {phrase!r}\nprint(teks.upper())"
                exp = phrase.upper()
                task = f"mengubah teks `{phrase}` menjadi huruf besar semua"
                outro = f"Method `.upper()` mengubah seluruh huruf menjadi kapital: `{exp}`."
            elif op == "ganti":
                code = f"teks = {phrase!r}\nprint(teks.replace(' ', '-'))"
                exp = phrase.replace(" ", "-")
                task = f"mengganti spasi pada teks `{phrase}` dengan tanda hubung"
                outro = f"Method `.replace(' ', '-')` menukar spasi menjadi tanda hubung: `{exp}`."
            elif op == "iris":
                n = rng.randint(3, 6)
                code = f"teks = {phrase!r}\nprint(teks[:{n}])"
                exp = phrase[:n]
                task = f"mengambil {n} karakter pertama dari teks `{phrase}`"
                outro = f"Irisan `teks[:{n}]` membaca {n} karakter terdepan dan mencetak `{exp}`."
            else:
                ch = rng.choice(sorted(set(phrase.replace(" ", ""))))
                code = f"teks = {phrase!r}\nprint(teks.count({ch!r}))"
                exp = str(phrase.count(ch))
                task = f"menghitung kemunculan huruf `{ch}` pada teks `{phrase}`"
                outro = f"Method `.count({ch!r})` menghitung huruf itu dan mencetak `{exp}`."
        elif mode == 3:  # kembalian
            price = rng.randint(5, 95) * 1000
            pay = ((price // 50000) + 1) * 50000
            back = pay - price
            code = f"harga = {price}\nuang = {pay}\nkembalian = uang - harga\nprint(kembalian)"
            exp = str(back)
            task = f"menghitung kembalian dari uang {_rp(pay)} untuk belanjaan senilai {_rp(price)}"
            outro = f"Pengurangan `uang - harga` pada program menghasilkan kembalian `{exp}`."
        elif mode == 4:  # genap/ganjil atau lulus
            if rng.random() < 0.5:
                n = rng.randint(2, 500)
                label = "genap" if n % 2 == 0 else "ganjil"
                code = f"angka = {n}\nstatus = 'genap' if angka % 2 == 0 else 'ganjil'\nprint(status)"
                exp = label
                task = f"mengecek apakah angka {n} termasuk genap atau ganjil"
                outro = f"Sisa bagi `angka % 2` menentukan statusnya, dan hasilnya tercetak `{exp}`."
            else:
                name = rng.choice(NAMES)
                score = rng.randint(45, 100)
                label = "lulus" if score >= 75 else "remedial"
                code = f"nama = {name!r}\nnilai = {score}\nstatus = 'lulus' if nilai >= 75 else 'remedial'\nprint(nama, status)"
                exp = f"{name} {label}"
                task = f"menentukan status kelulusan {name} dari nilai {score} (batas lulus 75)"
                outro = f"Perbandingan `nilai >= 75` memilih label status dan mencetak `{exp}`."
        elif mode == 5:  # loop jumlah deret
            start = rng.randint(1, 9)
            stop = start + rng.randint(4, 9)
            total = sum(range(start, stop + 1))
            code = f"total = 0\nfor n in range({start}, {stop + 1}):\n    total += n\nprint(total)"
            exp = str(total)
            task = f"menjumlahkan bilangan dari {start} sampai {stop} dengan perulangan `for`"
            outro = f"Perulangan mengakumulasikan tiap bilangan ke variabel `total` sampai tercetak `{exp}`."
        elif mode == 6:  # dictionary stok
            i1, i2 = rng.sample(ITEMS, 2)
            s1, s2 = rng.randint(2, 40), rng.randint(2, 40)
            code = f"stok = {{{i1!r}: {s1}, {i2!r}: {s2}}}\nprint(stok[{i2!r}], sum(stok.values()))"
            exp = f"{s2} {s1 + s2}"
            task = f"mengambil stok `{i2}` dan total stok dari dictionary berisi `{i1}` ({s1}) serta `{i2}` ({s2})"
            outro = f"Akses kunci dictionary mengambil stok barang kedua, lalu `sum(stok.values())` mencetak pasangan hasil `{exp}`."
        else:  # f-string profil
            name = rng.choice(NAMES)
            city = rng.choice(CITIES)
            age = rng.randint(13, 45)
            code = f"nama = {name!r}\nkota = {city!r}\numur = {age}\nprint(f'{{nama}} tinggal di {{kota}} dan berumur {{umur}} tahun.')"
            exp = f"{name} tinggal di {city} dan berumur {age} tahun."
            task = f"mencetak kalimat perkenalan untuk {name} dari {city} berumur {age} tahun pakai f-string"
            outro = "F-string menyisipkan isi variabel langsung ke dalam teks yang dicetak."
        ok, _ = self.ver.verify_python(code, expected_out=exp)
        if not ok:
            return False
        q = pick_det(PY_Q, key).format(task=task)
        return self.col.add(q, _wrap_code(intro, "python", code, outro))

    # --------------------------- JavaScript / TS -------------------------- #
    def add_js(self, ts: bool = False) -> bool:
        self.i += 1
        i, rng = self.i, self.rng
        mode = i % 6
        lang = "ts" if ts else "js"
        key = f"v3{lang}-{mode}-{i}"
        intro = pick_det(TS_INTROS if ts else JS_INTROS, key)
        tnum = ": number" if ts else ""
        tstr = ": string" if ts else ""
        if mode == 0:
            a, b = rng.randint(7, 400), rng.randint(3, 250)
            op = rng.choice(["+", "-", "*"])
            val = {"+" : a + b, "-": a - b, "*": a * b}[op]
            name_op = {"+" : "menjumlahkan", "-": "mengurangkan", "*": "mengalikan"}[op]
            code = f"const a{tnum} = {a};\nconst b{tnum} = {b};\nconsole.log(a {op} b);"
            exp = str(val)
            task = f"{name_op} {a} dan {b}"
            outro = f"Kode menyimpan angka di variabel konstanta lalu mencetak hasil operasinya, yaitu `{exp}`."
        elif mode == 1:
            w = self.words[rng.randrange(len(self.words))]
            code = f"const kata{tstr} = {w!r};\nconsole.log(kata.toUpperCase(), kata.length);".replace("'", '"')
            exp = f"{w.upper()} {len(w)}"
            task = f"mengubah kata `{w}` menjadi huruf besar dan menghitung panjangnya"
            outro = f"`.toUpperCase()` mengapitalkan teks, sedangkan `.length` menghitung karakternya sehingga tercetak `{exp}`."
        elif mode == 2:
            name = rng.choice(NAMES)
            city = rng.choice(CITIES)
            code = f'const nama{tstr} = "{name}";\nconst kota{tstr} = "{city}";\nconsole.log(`Halo, ${{nama}} dari ${{kota}}!`);'
            exp = f"Halo, {name} dari {city}!"
            task = f"membuat sapaan untuk {name} dari {city} dengan template literal"
            outro = f"Template literal berbacktick menyisipkan variabel ke kalimat dan mencetak `{exp}`."
        elif mode == 3:
            nums = [rng.randint(2, 90) for _ in range(5)]
            total = sum(nums)
            arr = json.dumps(nums).replace(" ", "")
            code = f"const angka{(': number[]' if ts else '')} = {arr};\nconst total = angka.reduce((s, n) => s + n, 0);\nconsole.log(total);"
            exp = str(total)
            task = f"menjumlahkan array `[{', '.join(map(str, nums))}]` dengan metode `reduce`"
            outro = f"Metode `.reduce()` melipat seluruh anggota array menjadi satu jumlah, yaitu `{exp}`."
        elif mode == 4:
            price = rng.randint(8, 120) * 1000
            pct = rng.choice([5, 10, 15, 20, 25, 30, 40])
            pay = price - (price * pct // 100)
            code = f"const harga{tnum} = {price};\nconst bayar = harga - Math.floor(harga * {pct} / 100);\nconsole.log(bayar);"
            exp = str(pay)
            task = f"menghitung harga bayar dari {_rp(price)} setelah diskon {pct}%"
            outro = f"Potongan harga dihitung lebih dulu lalu dikurangkan, dan console mencetak `{exp}`."
        else:
            nums = [rng.randint(2, 30) for _ in range(5)]
            doubled = [n * 2 for n in nums]
            arr = json.dumps(nums).replace(" ", "")
            code = f"const nilai{(': number[]' if ts else '')} = {arr};\nconst ganda = nilai.map(n => n * 2);\nconsole.log(ganda.join('-'));"
            exp = "-".join(map(str, doubled))
            task = f"menggandakan setiap isi array `[{', '.join(map(str, nums))}]` dengan metode `map`"
            outro = f"Metode `.map()` membuat array baru berisi hasil kali dua, lalu `.join('-')` mencetak `{exp}`."
        ok, _ = self.ver.verify_js_or_ts(code, lang=lang, run=True, expected_out=exp)
        if not ok:
            return False
        q = pick_det(TS_Q if ts else JS_Q, key).format(task=task)
        return self.col.add(q, _wrap_code(intro, "typescript" if ts else "javascript", code, outro))

    # ------------------------------ HTML/CSS ------------------------------ #
    def add_html(self) -> bool:
        self.i += 1
        i, rng = self.i, self.rng
        mode = i % 5
        key = f"v3html-{mode}-{i}"
        intro = pick_det(HTML_INTROS, key)
        menu = rng.choice(["nasi goreng", "mie ayam", "sate ayam", "bakso sapi", "gado-gado", "soto ayam", "rendang", "pecel lele"])
        place = rng.choice(CITIES)
        if mode == 0:
            title = f"Wisata Kuliner {place}"
            code = f"<section>\n  <h2>{title}</h2>\n  <p>Jangan lewatkan {menu} khas daerah ini.</p>\n</section>"
            task = f"membuat bagian promosi berjudul `{title}` dengan satu paragraf"
            outro = "Elemen `<section>` mengelompokkan judul `<h2>` dan paragraf `<p>` sebagai satu bagian halaman."
        elif mode == 1:
            items = rng.sample(ITEMS, 3)
            lis = "\n".join(f"  <li>{x}</li>" for x in items)
            code = f"<ul>\n{lis}\n</ul>"
            task = f"membuat daftar belanja berisi {', '.join(items)}"
            outro = "Daftar tidak berurutan dibungkus `<ul>`, dan tiap butir belanja ditulis dengan `<li>`."
        elif mode == 2:
            label = rng.choice(["Pesan Sekarang", "Lihat Jadwal", "Mulai Belajar", "Simpan Catatan", "Buka Galeri", "Daftar Gratis", "Unduh Materi", "Hubungi Kami", "Cek Lokasi", "Tambah ke Keranjang", "Baca Selengkapnya", "Ikuti Kelasnya"])
            cls = rng.choice(CLASS_NAMES)
            code = f'<button type="button" class="{cls}">{label}</button>'
            task = f"membuat tombol berlabel `{label}` dengan kelas CSS `{cls}`"
            outro = f'Atribut `type="button"` mencegah pengiriman formulir otomatis, dan kelas `{cls}` siap diberi gaya lewat CSS.'
        elif mode == 3:
            name = rng.choice(NAMES)
            score = rng.randint(70, 100)
            code = f"<table>\n  <tr><th>Nama</th><th>Nilai</th></tr>\n  <tr><td>{name}</td><td>{score}</td></tr>\n</table>"
            task = f"membuat tabel nilai sederhana berisi {name} dengan nilai {score}"
            outro = "Baris dibuat dengan `<tr>`, sel judul memakai `<th>`, dan sel data memakai `<td>`."
        else:
            art = rng.choice(["Tips Belajar Efektif", "Resep Sarapan Cepat", "Panduan Anak Kos", "Jelajah Kota Tua", "Merawat Tanaman Hias", "Dasar Fotografi HP", "Mengatur Uang Saku", "Olahraga Ringan di Rumah", "Memilih Buku Bacaan", "Sejarah Pasar Tradisional", "Belajar Bahasa Daerah", "Menulis Catatan Harian", "Berkebun di Lahan Sempit", "Mengenal Transportasi Umum"])
            author = rng.choice(NAMES)
            code = f"<article>\n  <h3>{art}</h3>\n  <p>Tulisan {author} untuk pembaca dari {place}.</p>\n</article>"
            task = f"membuat kartu artikel berjudul `{art}` karya {author} untuk pembaca {place}"
            outro = "Elemen `<article>` cocok untuk konten mandiri seperti kartu artikel atau unggahan blog."
        ok, _ = self.ver.verify_html(code)
        if not ok:
            return False
        q = pick_det(HTML_Q, key).format(task=task)
        return self.col.add(q, _wrap_code(intro, "html", code, outro))

    def add_css(self) -> bool:
        self.i += 1
        i, rng = self.i, self.rng
        key = f"v3css-{i}"
        intro = pick_det(CSS_INTROS, key)
        cls = rng.choice(CLASS_NAMES)
        color = rng.choice(COLORS)
        bg = rng.choice(["#f8fafc", "#fefce8", "#ecfdf5", "#eff6ff", "#fdf2f8", "#fff7ed"])
        pad = rng.choice([8, 10, 12, 14, 16, 20, 24])
        radius = rng.choice([4, 6, 8, 10, 12, 16])
        size = rng.choice([14, 15, 16, 18, 20, 22, 24])
        mode = i % 3
        if mode == 0:
            code = f".{cls} {{\n  color: {color};\n  background-color: {bg};\n  padding: {pad}px;\n  border-radius: {radius}px;\n}}"
            task = f"menata kelas `.{cls}` dengan teks berwarna {color}, latar {bg}, padding {pad}px, dan sudut membulat {radius}px"
            outro = f"Selektor `.{cls}` menargetkan elemen berkelas sama, lalu empat deklarasi di dalamnya mengatur warna, latar, ruang dalam, dan lengkungan sudut."
        elif mode == 1:
            code = f".{cls} {{\n  font-size: {size}px;\n  font-weight: bold;\n  text-align: center;\n  color: {color};\n}}"
            task = f"membuat teks kelas `.{cls}` berukuran {size}px, tebal, rata tengah, dan berwarna {color}"
            outro = "Kombinasi `font-size`, `font-weight: bold`, dan `text-align: center` membuat teks tampil menonjol di tengah wadahnya."
        else:
            gap = rng.choice([6, 8, 10, 12, 16])
            code = f".{cls} {{\n  display: flex;\n  gap: {gap}px;\n  align-items: center;\n  padding: {pad}px;\n}}"
            task = f"menyusun isi kelas `.{cls}` sebaris dengan flexbox berjarak {gap}px"
            outro = f"`display: flex` menyusun anak elemen sebaris, sedangkan `gap: {gap}px` memberi jarak rapi di antara mereka."
        ok, _ = self.ver.verify_css(code)
        if not ok:
            return False
        q = pick_det(CSS_Q, key).format(task=task)
        return self.col.add(q, _wrap_code(intro, "css", code, outro))

    # --------------------------- SQL / Bash / JSON ------------------------ #
    def add_sql(self) -> bool:
        self.i += 1
        i, rng = self.i, self.rng
        mode = i % 5
        key = f"v3sql-{mode}-{i}"
        expected = None
        if mode == 0:
            batas = rng.choice([70, 75, 80, 82, 85, 88, 90, 93])
            code = f"SELECT nama, kelas, nilai\nFROM siswa\nWHERE nilai > {batas}\nORDER BY nilai DESC;"
            expected = [(n, k, v) for (_id, n, k, v, _u) in sorted(SISWA, key=lambda r: -r[3]) if v > batas]
            task = f"mengambil nama, kelas, dan nilai siswa bernilai di atas {batas} dari tabel `siswa` terurut menurun"
            outro = "Klausa `WHERE` menyaring nilai, dan `ORDER BY nilai DESC` menampilkan yang tertinggi lebih dulu."
        elif mode == 1:
            kelas = rng.choice(["10A", "10B"])
            code = f"SELECT nama, nilai\nFROM siswa\nWHERE kelas = '{kelas}';"
            expected = [(n, v) for (_id, n, k, v, _u) in SISWA if k == kelas]
            task = f"menampilkan nama dan nilai semua siswa dari kelas {kelas}"
            outro = f"Kondisi `WHERE kelas = '{kelas}'` hanya mengembalikan baris siswa dari kelas tersebut."
        elif mode == 2:
            stok_min = rng.choice([10, 15, 20, 30, 45, 60])
            code = f"SELECT nama, stok\nFROM produk\nWHERE stok >= {stok_min}\nORDER BY stok DESC;"
            expected = [(n, s) for (_id, n, _k, _h, s) in sorted(PRODUK, key=lambda r: -r[4]) if s >= stok_min]
            task = f"mencari produk dengan stok minimal {stok_min} diurutkan dari stok terbanyak"
            outro = "Penyaringan `stok >= ...` digabung pengurutan menurun agar produk paling siap jual tampil teratas."
        elif mode == 3:
            harga = rng.choice([4000, 6000, 10000, 50000, 100000])
            code = f"SELECT COUNT(*) AS jumlah\nFROM produk\nWHERE harga < {harga};"
            expected = [(sum(1 for r in PRODUK if r[3] < harga),)]
            task = f"menghitung banyak produk berharga di bawah {_rp(harga)}"
            outro = "Fungsi agregat `COUNT(*)` menghitung baris yang lolos syarat harga pada klausa `WHERE`."
        else:
            pid = rng.randint(1, 4)
            baru = rng.randint(5, 90)
            code = f"UPDATE produk\nSET stok = stok + {baru}\nWHERE id = {pid};"
            task = f"menambah stok produk ber-id {pid} sebanyak {baru} buah"
            outro = "Bentuk `SET stok = stok + ...` menambah stok lama, dan `WHERE id` memastikan hanya satu produk berubah."
        ok, _ = self.ver.verify_sql(code, expected_rows=expected)
        if not ok:
            return False
        q = pick_det(SQL_Q, key).format(task=task)
        return self.col.add(q, _wrap_code("Ini contoh query SQL yang bisa langsung dicoba:", "sql", code, outro))

    def add_bash(self) -> bool:
        self.i += 1
        i, rng = self.i, self.rng
        mode = i % 4
        key = f"v3bash-{mode}-{i}"
        if mode == 0:
            a, b = rng.randint(3, 200), rng.randint(2, 90)
            code = f"a={a}\nb={b}\ntotal=$((a + b))\necho \"Total: $total\""
            exp = a + b
            task = f"menjumlahkan {a} dan {b} memakai variabel bash lalu mencetak hasilnya"
            outro = f"Ekspansi aritmetika `$((a + b))` menghitung di dalam shell sehingga tercetak `Total: {exp}`."
        elif mode == 1:
            n = rng.randint(3, 9)
            code = f"for i in $(seq 1 {n}); do\n  echo \"Baris ke-$i\"\ndone"
            task = f"mencetak tulisan `Baris ke-...` sebanyak {n} kali dengan perulangan"
            outro = f"Perintah `seq 1 {n}` menghasilkan urutan angka yang diulang oleh loop `for` satu per satu."
        elif mode == 2:
            folder = f"arsip_{rng.choice(['senin', 'rabu', 'jumat', 'pekan1', 'pekan2'])}_{i % 97}"
            code = f"mkdir -p {folder}\ncd {folder}\npwd"
            task = f"membuat folder `{folder}`, masuk ke dalamnya, lalu menampilkan lokasinya"
            outro = "Opsi `-p` aman dipakai berulang, dan `pwd` memastikan posisi terminal sudah berada di folder baru."
        else:
            fname = f"laporan_{i % 389}.log"
            word = rng.choice(["BERHASIL", "GAGAL", "PERINGATAN", "SELESAI"])
            code = f"grep -c \"{word}\" {fname} || true"
            task = f"menghitung jumlah baris berisi kata `{word}` pada berkas `{fname}`"
            outro = "Opsi `-c` pada grep hanya menampilkan hitungan baris yang cocok, bukan isi barisnya."
        ok, _ = self.ver.verify_bash(code)
        if not ok:
            return False
        q = pick_det(BASH_Q, key).format(task=task)
        return self.col.add(q, _wrap_code("Kamu bisa memakai skrip bash singkat ini:", "bash", code, outro))

    def add_json(self) -> bool:
        self.i += 1
        i, rng = self.i, self.rng
        key = f"v3json-{i}"
        mode = i % 3
        if mode == 0:
            name = rng.choice(NAMES)
            city = rng.choice(CITIES)
            age = rng.randint(12, 40)
            obj = {"nama": name, "kota": city, "umur": age, "pelajar": age <= 25}
            task = f"data profil {name} dari {city} yang berumur {age} tahun"
            outro = "Objek JSON memakai pasangan key dan value di dalam kurung kurawal, dengan semua key berquote ganda."
        elif mode == 1:
            item = rng.choice(ITEMS)
            price = rng.randint(3, 150) * 1000
            stock = rng.randint(0, 60)
            obj = {"produk": item, "harga": price, "stok": stock, "tersedia": stock > 0}
            task = f"data produk `{item}` seharga {_rp(price)} dengan stok {stock}"
            outro = "Angka pada JSON ditulis tanpa quote, sedangkan teks seperti nama produk wajib memakai quote ganda."
        else:
            day = rng.choice(["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"])
            lesson = rng.choice(["Matematika", "Bahasa Indonesia", "IPA", "IPS", "Bahasa Inggris", "Informatika"])
            hour = rng.randint(7, 15)
            obj = {"hari": day, "pelajaran": lesson, "jam_mulai": hour, "ruang": f"R{rng.randint(1, 30)}"}
            task = f"jadwal pelajaran {lesson} pada hari {day} pukul {hour:02d}.00"
            outro = "Satu objek JSON seperti ini mudah dibaca program karena setiap informasi punya key yang jelas."
        code = json.dumps(obj, ensure_ascii=False, indent=2)
        ok, _ = self.ver.verify_json(code)
        if not ok:
            return False
        q = pick_det(JSON_Q, key).format(task=task)
        return self.col.add(q, _wrap_code("Ini contoh penulisan JSON yang valid:", "json", code, outro))


_SEQUENCE = (
    ["python"] * 16 + ["js"] * 8 + ["ts"] * 4 + ["html"] * 4
    + ["css"] * 4 + ["sql"] * 2 + ["bash"] * 1 + ["json"] * 1
)


def build_kode_v3(
    col: CategoryCollector,
    *,
    target_bytes: int,
    seed: int = 20261024,
    max_attempts: int = 90000,
) -> dict:
    rng = random.Random(seed)
    ver = CodeVerifier()
    gen = _KodeV3(col, ver, rng)
    dispatch = {
        "python": gen.add_python,
        "js": lambda: gen.add_js(False),
        "ts": lambda: gen.add_js(True),
        "html": gen.add_html,
        "css": gen.add_css,
        "sql": gen.add_sql,
        "bash": gen.add_bash,
        "json": gen.add_json,
    }
    attempts = 0
    try:
        while col.total_bytes_est < target_bytes and attempts < max_attempts:
            kind = _SEQUENCE[attempts % len(_SEQUENCE)]
            attempts += 1
            dispatch[kind]()
        node_ok, node_err = ver.flush_node_cli_check()
        if not node_ok:
            raise RuntimeError(f"node --check batch gagal: {node_err}")
        return {"attempts": attempts, "rows": len(col.rows), "est_bytes": col.total_bytes_est, "verifier": dict(ver.stats)}
    finally:
        ver.close()
