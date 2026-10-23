"""Tambahan contoh `kode.jsonl` teruji untuk Nara-Allegretto-2.

Semua cuplikan <= 8 baris dan diuji otomatis oleh CodeVerifier sebelum masuk.
Fokus: kasus praktis sehari-hari di Python, JavaScript, TypeScript, HTML, CSS,
C++, dan SQL (format Rupiah, keranjang belanja, validasi teks, komponen UI, dll.).
"""
from __future__ import annotations

import json

from .code_verifier import CodeVerifier
from .core_v2 import CategoryCollector, pick_det
from .gen_kode import (
    CPP_INTROS,
    CSS_INTROS,
    HTML_INTROS,
    JS_INTROS,
    PY_INTROS,
    TS_INTROS,
    _wrap_code,
)


def build_kode_extra(
    col: CategoryCollector,
    ver: CodeVerifier,
    limit: int | None = None,
) -> None:
    q_py = [
        "contoh kode Python praktis untuk {task}",
        "gimana cara {task} di Python?",
        "nara, bikinin skrip Python pendek buat {task} dong",
        "tolong bantu potongan Python untuk {task}",
        "cara {task} pakai Python yang simpel gimana?",
    ]
    # 1. Python praktis sehari-hari (~2.400 contoh teruji)
    items_names = [
        "Roti", "Susu", "Telur", "Kopi", "Teh", "Beras", "Gula", "Sabun", "Buku", "Pulpen"
    ]
    for i in range(2400):
        if limit and len(col.rows) >= limit:
            return
        key = f"py-ex-{i}"
        intro = pick_det(PY_INTROS, key)
        mode = i % 6
        if mode == 0:
            nominal = (i + 12) * 1500
            expected = f"Rp{nominal:,}".replace(",", ".")
            code = f"nominal = {nominal}\nteks = f'Rp{{nominal:,}}'.replace(',', '.')\nprint(teks)"
            task = f"memformat angka {nominal} menjadi tampilan Rupiah bertitik ribuan"
            outro = f"Format `{{nominal:,}}` memberi pemisah ribuan lalu diganti titik menjadi `{expected}`."
        elif mode == 1:
            it1 = items_names[i % len(items_names)]
            it2 = items_names[(i + 3) % len(items_names)]
            p1 = ((i % 20) + 2) * 1000
            p2 = (((i * 3) % 25) + 3) * 1000 + (i // 20) * 500
            tot = p1 + p2
            code = (
                f"keranjang = {{{it1!r}: {p1}, {it2!r}: {p2}}}\n"
                "total = sum(keranjang.values())\n"
                "print(total)"
            )
            expected = str(tot)
            task = f"menjumlahkan harga belanja `{it1}` ({p1}) dan `{it2}` ({p2}) di dictionary"
            outro = f"`.values()` mengambil semua harga di dictionary lalu `sum()` menghasilkan `{expected}`."
        elif mode == 2:
            kal = f"Belajar Python hari ke {i + 1} bareng Nara"
            jml_kata = len(kal.split())
            code = f"kalimat = {kal!r}\nkata = kalimat.split()\nprint(len(kata), kata[-1])"
            expected = f"{jml_kata} Nara"
            task = f"menghitung jumlah kata dan mengambil kata terakhir dari '{kal}'"
            outro = f"`.split()` memecah kalimat berdasarkan spasi; total katanya dan kata terakhirnya `{expected}`."
        elif mode == 3:
            kode_brg = f"BRG-{1000 + i}"
            bersih_num = str(1000 + i)
            code = f"import re\nteks = 'Kode pesanan {kode_brg}'\nangka = re.findall(r'\\d+', teks)\nprint(angka[0])"
            expected = bersih_num
            task = f"mengambil deretan angka saja dari teks `'Kode pesanan {kode_brg}'` pakai regex"
            outro = f"Pola `r'\\d+'` pada `re.findall` mengekstrak angka berurutan sehingga didapat `{expected}`."
        elif mode == 4:
            n_siswa = ["Budi", "Siti", "Raka", "Nadia", "Dewi", "Fajar"][i % 6]
            skor_a = 70 + (i % 30)
            skor_b = 65 + ((i * 5) % 35)
            kode_id = i + 101
            code = (
                "import json\n"
                f"data = {{'id': {kode_id}, 'nama': {n_siswa!r}, 'rata': ({skor_a} + {skor_b}) / 2}}\n"
                "print(json.dumps(data))"
            )
            expected = json.dumps({"id": kode_id, "nama": n_siswa, "rata": (skor_a + skor_b) / 2})
            task = f"mengubah dictionary nilai {n_siswa} (ID {kode_id}, skor {skor_a} & {skor_b}) ke teks JSON"
            outro = f"`json.dumps()` mengubah objek Python menjadi string JSON: `{expected}`."
        else:
            start = (i % 15) + 1
            step = (i % 5) + 2
            arr = [start + k * step for k in range(4)]
            idx_val = i % 4
            code = (
                f"tugas = {arr}\n"
                "for idx, nilai in enumerate(tugas, start=1):\n"
                f"  if idx == {idx_val + 1}:\n"
                "    print(f'{idx}:{nilai}')"
            )
            expected = f"{idx_val + 1}:{arr[idx_val]}"
            task = f"menampilkan nomor urut ke-{idx_val + 1} beserta nilainya dari list {arr} pakai `enumerate`"
            outro = f"`enumerate(..., start=1)` memberi nomor urut mulai dari 1 dan mencetak `{expected}`."

        ok, _ = ver.verify_python(code, expected_out=expected)
        if ok:
            q = pick_det(q_py, key).format(task=task)
            col.add(q, _wrap_code(intro, "python", code, outro))

    # 2. JavaScript & TypeScript praktis sehari-hari (~2.400 contoh teruji)
    q_js = [
        "contoh kode JavaScript ringkas buat {task}",
        "gimana cara {task} pakai JS modern?",
        "nara, bantu potongan JavaScript untuk {task} dong",
        "cara {task} di JavaScript gimana contohnya?",
    ]
    for i in range(1300):
        if limit and len(col.rows) >= limit:
            return
        key = f"js-ex-{i}"
        intro = pick_det(JS_INTROS, key)
        mode = i % 4
        if mode == 0:
            nums = [i % 12 + 2, (i // 10) + 5, (i * 3) % 19 + 4]
            code = (
                f"const harga = {json.dumps(nums)};\n"
                "const denganPajak = harga.filter((h) => h > 4).map((h) => h * 1000);\n"
                "console.log(denganPajak);"
            )
            exp = json.dumps([h * 1000 for h in nums if h > 4], separators=(",", ":"))
            task = f"menyaring angka di atas 4 dari {nums} lalu mengalikannya 1000 secara berantai"
            outro = f"Penggabungan `.filter()` lalu `.map()` menghasilkan array baru `{exp}`."
        elif mode == 1:
            teks = f"  pesanan-{100 + i}  "
            exp = f"PESANAN-{100 + i}"
            code = f"const mentah = {json.dumps(teks)};\nconst rapi = mentah.trim().toUpperCase();\nconsole.log(rapi);"
            task = f"menghapus spasi tepi pada `'{teks}'` sekaligus mengubahnya ke huruf kapital"
            outro = f"`.trim()` membuang spasi di ujung kiri-kanan, lalu `.toUpperCase()` menghasilkan `{exp}`."
        elif mode == 2:
            kode_urut = str(i + 1).zfill(4)
            code = f"const nomor = {i + 1};\nconst kode = String(nomor).padStart(4, '0');\nconsole.log(`INV-${{kode}}`);"
            exp = f"INV-{kode_urut}"
            task = f"membuat nomor nota 4 digit berawalan nol untuk urutan ke-{i + 1}"
            outro = f"`.padStart(4, '0')` melengkapi nol di depan angka hingga mencetak `{exp}`."
        else:
            a_val = 10 + (i % 40)
            b_val = 12 + ((i * 3) % 45)
            c_val = 8 + (i // 15)
            code = f"const skor = [{a_val}, {b_val}, {c_val}];\nconsole.log(Math.max(...skor), Math.min(...skor));"
            exp = f"{max(a_val, b_val, c_val)} {min(a_val, b_val, c_val)}"
            task = f"mencari angka tertinggi dan terendah dari `[{a_val}, {b_val}, {c_val}]` pakai `Math.max`"
            outro = f"Spread `...skor` memecah isi array menjadi argumen sehingga tercetak `{exp}`."

        ok, _ = ver.verify_js_or_ts(code, lang="js", run=True, expected_out=exp)
        if ok:
            q = pick_det(q_js, key).format(task=task)
            col.add(q, _wrap_code(intro, "javascript", code, outro.lstrip()))

    q_ts = [
        "contoh kode TypeScript praktis buat {task}",
        "gimana nulis {task} di TypeScript?",
        "nara, bikinin potongan TS singkat untuk {task} dong",
        "cara membuat {task} pakai tipe TypeScript gimana?",
    ]
    for i in range(1100):
        if limit and len(col.rows) >= limit:
            return
        key = f"ts-ex-{i}"
        intro = pick_det(TS_INTROS, key)
        mode = i % 3
        if mode == 0:
            brg = f"Produk-{i + 1}"
            hrg = ((i % 30) + 5) * 2000
            code = (
                "interface Barang { nama: string; harga: number; diskon?: number; }\n"
                "function hargaAkhir(b: Barang): number {\n"
                "  return b.harga - (b.diskon ?? 0);\n"
                "}\n"
                f"console.log(hargaAkhir({{ nama: {json.dumps(brg)}, harga: {hrg}, diskon: 1500 }}));"
            )
            exp = str(hrg - 1500)
            task = f"interface `Barang` dengan properti opsional `diskon?` untuk `{brg}` seharga {hrg}"
            outro = f"Operator `?? 0` memberi nilai cadangan nol saat `diskon` kosong; di sini hasilnya `{exp}`."
        elif mode == 1:
            k1 = f"apel_{i}"
            v1 = (i % 15) + 3
            v2 = (i % 10) + 2
            code = (
                "const stokGudang: Record<string, number> = {\n"
                f"  {json.dumps(k1)}: {v1},\n"
                f"  jeruk: {v2},\n"
                "};\n"
                f"console.log(stokGudang[{json.dumps(k1)}] + stokGudang.jeruk);"
            )
            exp = str(v1 + v2)
            task = f"objek `Record<string, number>` yang menyimpan stok `{k1}` ({v1}) dan `jeruk` ({v2})"
            outro = f"`Record<string, number>` memastikan setiap kunci string berpasangan dengan angka; totalnya `{exp}`."
        else:
            teks = f"user_{i + 10}"
            code = (
                "function formatId(id: string | number): string {\n"
                "  return `ID-${String(id).toUpperCase()}`;\n"
                "}\n"
                f"console.log(formatId({json.dumps(teks)}));"
            )
            exp = f"ID-{teks.upper()}"
            task = f"fungsi parameter union `string | number` untuk memformat `'{teks}'`"
            outro = f"Parameter union menerima angka maupun teks lalu memformatnya secara seragam menjadi `{exp}`."

        ok, _ = ver.verify_js_or_ts(code, lang="ts", run=True, expected_out=exp)
        if ok:
            q = pick_det(q_ts, key).format(task=task)
            col.add(q, _wrap_code(intro, "ts", code, outro))

    # 3. HTML & CSS komponen praktis (~1.400 contoh teruji)
    for i in range(700):
        if limit and len(col.rows) >= limit:
            return
        key = f"html-ex-{i}"
        intro = pick_det(HTML_INTROS, key)
        if i % 2 == 0:
            persen = (i % 95) + 5
            judul = f"Target Belajar Modul {i + 1}"
            code = (
                f"<section id=\"progres-{i}\">\n"
                f"  <label for=\"bar-{i}\">{judul} ({persen}%)</label>\n"
                f"  <progress id=\"bar-{i}\" value=\"{persen}\" max=\"100\">{persen}%</progress>\n"
                "</section>"
            )
            task = f"bilah progres (`progress`) untuk '{judul}' sebesar {persen}%"
            outro = f"Elemen `<progress>` bawaan HTML menampilkan capaian `{persen}` dari batas `100`."
        else:
            plh = f"Cari materi ke-{i + 1}..."
            code = (
                f"<form role=\"search\" action=\"/cari-{i}\">\n"
                f"  <input type=\"search\" name=\"q\" placeholder=\"{plh}\">\n"
                "  <button type=\"submit\">Cari</button>\n"
                "</form>"
            )
            task = f"kotak pencarian HTML dengan placeholder '{plh}'"
            outro = "`type=\"search\"` memberi perilaku kolom pencarian semantik lengkap dengan tombol hapus cepat di banyak browser."

        if ver.verify_html(code)[0]:
            q = f"contoh HTML ringkas untuk membuat {task} gimana nara?"
            col.add(q, _wrap_code(intro, "html", code, outro))

    palette = ["#0284c7", "#059669", "#d97706", "#e11d48", "#4f46e5", "#334155"]
    for i in range(700):
        if limit and len(col.rows) >= limit:
            return
        key = f"css-ex-{i}"
        intro = pick_det(CSS_INTROS, key)
        hex_c = palette[i % len(palette)]
        pad_h = 12 + (i % 10) * 2
        cls = f"navbar-atas-{i}"
        code = (
            f".{cls} {{\n"
            "  display: flex;\n"
            "  justify-content: space-between;\n"
            "  align-items: center;\n"
            f"  padding: 10px {pad_h}px;\n"
            f"  background-color: {hex_c};\n"
            "  color: #ffffff;\n"
            "}"
        )
        task = f"bilah navigasi `.{cls}` dengan logo di kiri dan menu di kanan (warna `{hex_c}`, padding samping `{pad_h}px`)"
        outro = f"Pada `.{cls}`, `justify-content: space-between` mendorong kelompok kiri dan kanan ke ujung berlawanan."
        if ver.verify_css(code)[0]:
            q = f"gimana aturan CSS buat menyusun {task}?"
            col.add(q, _wrap_code(intro, "css", code, outro))

    # 4. C++ tambahan teruji (~600 contoh)
    cpp_items: list[tuple[str, str, str, str]] = []
    target_n = 600 if limit is None else min(60, limit)
    for i in range(target_n):
        key = f"cpp-ex-{i}"
        a = (i % 35) + 10
        b = ((i * 3) % 40) + 12
        c = ((i * 7) % 30) + 8
        tot = a + b + c
        code = (
            "#include <iostream>\n"
            "using namespace std;\n"
            "int main() {\n"
            f"  int s1 = {a}, s2 = {b}, s3 = {c};\n"
            "  cout << (s1 + s2 + s3) << endl;\n"
            "  return 0;\n"
            "}"
        )
        task = f"menjumlahkan tiga skor `{a}`, `{b}`, dan `{c}` di C++"
        outro = f"Ketiga variabel `int` dijumlahkan lalu dicetak ke output standar dengan hasil `{tot}`."
        cpp_items.append((key, code, str(tot), f"{task}||{outro}"))

    cpp_checked = ver.verify_cpp_batch([(x[1], x[2]) for x in cpp_items])
    for (key, code, _, meta), (ok, _) in zip(cpp_items, cpp_checked):
        if limit and len(col.rows) >= limit:
            return
        if ok:
            task, outro = meta.split("||", 1)
            intro = pick_det(CPP_INTROS, key)
            col.add(f"tolong contoh kode C++ singkat untuk {task}", _wrap_code(intro, "cpp", code, outro))
