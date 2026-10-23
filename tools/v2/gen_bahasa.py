"""Generator kategori `bahasa.jsonl` untuk Nara-Allegretto-2.

Menggabungkan materi ejaan/kosakata/tata bahasa tervalidasi dari v1 dengan
materi tambahan bahasa Indonesia sehari-hari: ungkapan/idiom, penulisan kata
depan 'di-' vs 'di ', serta terjemahan kalimat percakapan harian ID <-> EN.
"""
from __future__ import annotations

import os
import random
import sys

TOOLS_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if TOOLS_DIR not in sys.path:
    sys.path.insert(0, TOOLS_DIR)

import data_bahasa  # noqa: E402
import data_language  # noqa: E402
from nara_core import Builder  # noqa: E402

from .core_v2 import CategoryCollector, pick_det

IDIOMS = [
    ("banting tulang", "bekerja sangat keras", "Ayah rela banting tulang demi membiayai sekolah adik."),
    ("buah tangan", "oleh-oleh yang dibawa sepulang bepergian", "Kakak membawa lumpia sebagai buah tangan dari Semarang."),
    ("ringan tangan", "suka menolong atau cepat membantu orang lain", "Raka dikenal ringan tangan saat ada tetangga yang kerepotan."),
    ("kepala dingin", "tenang dan sabar saat menghadapi masalah", "Sebaiknya selesaikan salah paham itu dengan kepala dingin."),
    ("angkat tangan", "menyerah karena merasa sudah tidak sanggup", "Soal teka-teki terakhir itu bikin banyak peserta angkat tangan."),
    ("besar kepala", "sombong atau terlalu membanggakan diri", "Walaupun juara kelas, Siti tidak pernah besar kepala."),
    ("rendah hati", "tidak sombong dan menghargai orang lain", "Sikapnya yang rendah hati membuat banyak teman nyaman mengobrol."),
    ("panjang tangan", "suka mencuri barang milik orang lain", "Jangan sampai ada kebiasaan panjang tangan di lingkungan kos."),
    ("kambing hitam", "pihak yang disalahkan atas kesalahan orang lain", "Ia menolak dijadikan kambing hitam atas keterlambatan laporan itu."),
    ("meja hijau", "pengadilan", "Sengketa tanah tersebut akhirnya dibawa ke meja hijau."),
    ("naik daun", "sedang terkenal atau populer", "Lagu dari grup musik independen itu sedang naik daun bulan ini."),
    ("gulung tikar", "bangkrut atau menutup usaha", "Warung itu terpaksa gulung tikar karena biaya sewa naik tinggi."),
    ("buah bibir", "bahan pembicaraan banyak orang", "Kemenangan tim sekolah kita jadi buah bibir sepanjang minggu."),
    ("tangan kanan", "orang kepercayaan utama", "Dimas menjadi tangan kanan ketua panitia selama acara kampus."),
    ("berat hati", "kurang rela atau sedih saat harus melakukan sesuatu", "Dengan berat hati ia berpamitan untuk merantau ke kota seberang."),
    ("lapang dada", "ikhlas dan menerima keadaan dengan sabar", "Ia menerima kritik dari juri dengan lapang dada."),
    ("cuci tangan", "lepas tanggung jawab dari masalah yang ikut dibuat", "Jangan langsung cuci tangan kalau rencana kelompok belum beres."),
    ("bunga tidur", "mimpi saat tidur", "Anggap saja mimpi buruk semalam cuma bunga tidur."),
    ("adu mulut", "bertengkar dengan kata-kata", "Untung mereka segera dilerai sebelum adu mulut makin panjang."),
    ("titik terang", "petunjuk menuju penyelesaian masalah", "Diskusi sore tadi mulai menunjukkan titik terang untuk proyek kita."),
    ("darah daging", "anak kandung atau keluarga sedarah", "Bagaimanapun juga, adik tetap darah daging sendiri."),
    ("makan hati", "sedih atau tertekan batin karena ulah orang lain", "Jangan mau terus-terusan makan hati menghadapi komentar kasar."),
    ("kutu buku", "orang yang sangat gemar membaca buku", "Sejak SMP, Nadia memang kutu buku yang betah berjam-jam di perpustakaan."),
    ("kabar burung", "berita yang belum jelas kebenarannya", "Cek dulu sumbernya supaya kamu nggak tertipu kabar burung."),
    ("jalan tengah", "keputusan kompromi yang adil bagi kedua pihak", "Setelah berunding lama, mereka sepakat mengambil jalan tengah."),
    ("buka suara", "mulai memberikan pernyataan atau pendapat", "Saksi kejadian akhirnya berani buka suara kepada petugas."),
    ("tulang punggung", "penopang utama kehidupan keluarga atau tim", "Sejak lulus kuliah, ia ikut menjadi tulang punggung keluarganya."),
    ("tinggi hati", "angkuh atau merasa lebih hebat dari orang lain", "Ilmu setinggi apa pun bakal kurang dihargai kalau orangnya tinggi hati."),
    ("bermuka dua", "tidak jujur karena bersikap beda di depan dan di belakang", "Susah mempercayai teman yang suka bermuka dua."),
    ("gigit jari", "kecewa karena gagal mendapatkan sesuatu", "Penonton yang terlambat beli tiket terpaksa gigit jari karena sudah habis."),
]

DI_LOCATIONS = [
    "rumah", "sekolah", "kampus", "kantor", "pasar", "dapur", "kamar", "perpustakaan",
    "stasiun", "bandara", "taman", "warung", "kelas", "lapangan", "halte", "apotek",
    "klinik", "toko", "meja", "lemari", "kulkas", "beranda", "halaman", "seberang",
    "pojok", "lantai dua", "luar ruangan", "dalam tas", "atas rak", "bawah pohon",
]

DI_PASSIVES = [
    ("baca", "dibaca"), ("tulis", "ditulis"), ("masak", "dimasak"), ("cuci", "dicuci"),
    ("beli", "dibeli"), ("simpan", "disimpan"), ("kirim", "dikirim"), ("buka", "dibuka"),
    ("tutup", "ditutup"), ("pakai", "dipakai"), ("rapikan", "dirapikan"), ("periksa", "diperiksa"),
    ("hitung", "dihitung"), ("catat", "dicatat"), ("jemur", "dijemur"), ("lipat", "dilipat"),
    ("potong", "dipotong"), ("aduk", "diaduk"), ("rebus", "direbus"), ("goreng", "digoreng"),
    ("panggang", "dipanggang"), ("hapus", "dihapus"), ("unduh", "diunduh"), ("cetak", "dicetak"),
    ("kunci", "dikunci"), ("antar", "diantar"), ("jemput", "dijemput"), ("rawat", "dirawat"),
]

DAILY_TRANSLATIONS = [
    ("Aku lagi di jalan, tunggu sebentar ya.", "I am on my way, please wait a moment."),
    ("Hari ini cuacanya mendung banget.", "It is very cloudy today."),
    ("Jangan lupa bawa payung sebelum berangkat.", "Do not forget to bring an umbrella before leaving."),
    ("Kamu sudah sarapan pagi ini?", "Have you had breakfast this morning?"),
    ("Maaf aku baru sempat membalas pesanmu.", "Sorry I just got a chance to reply to your message."),
    ("Baterai HP-ku hampir habis.", "My phone battery is almost dead."),
    ("Bisa tolong jelaskan sekali lagi pelan-pelan?", "Could you please explain it once more slowly?"),
    ("Aku butuh istirahat sebentar karena agak pusing.", "I need a short rest because I feel a bit dizzy."),
    ("Kapan batas pengumpulan tugas ini?", "When is the deadline for this assignment?"),
    ("Terima kasih banyak atas bantuannya hari ini.", "Thank you so much for your help today."),
    ("Di mana stasiun kereta terdekat dari sini?", "Where is the nearest train station from here?"),
    ("Aku belum pernah mencoba makanan ini sebelumnya.", "I have never tried this food before."),
    ("Mari kita bahas lagi besok pagi.", "Let us discuss it again tomorrow morning."),
    ("Koneksi internet di kamarku sedang lambat.", "The internet connection in my room is slow right now."),
    ("Tolong kecilkan sedikit volume musiknya.", "Please turn down the music volume a little."),
    ("Aku setuju dengan usulanmu tadi.", "I agree with your suggestion earlier."),
    ("Jam berapa toko buku itu tutup?", "What time does that bookstore close?"),
    ("Semoga perjalananmu lancar dan selamat sampai tujuan.", "Have a smooth trip and arrive safely."),
    ("Aku sedang belajar bahasa pemrograman dasar.", "I am learning basic programming languages."),
    ("Harga barang ini sudah termasuk pajak atau belum?", "Does this item price include tax or not?"),
    ("Kita ketemu di depan pintu masuk jam empat sore ya.", "Let us meet in front of the entrance at four in the afternoon."),
    ("Aku lupa menaruh kacamata bacaku di mana.", "I forgot where I put my reading glasses."),
    ("Jangan begadang terus, jaga kesehatanmu.", "Do not stay up late all the time, take care of your health."),
    ("Kopi ini rasanya pas, nggak terlalu manis.", "This coffee tastes just right, not too sweet."),
    ("Apakah kursi di sebelahmu kosong?", "Is the seat next to you empty?"),
]


def _gen_idioms(col: CategoryCollector, limit: int | None) -> None:
    q_styles = [
        "apa arti ungkapan '{idiom}'?",
        "maksud dari istilah '{idiom}' dalam bahasa Indonesia apa ya?",
        "nara, '{idiom}' itu artinya apa sih?",
        "kasih arti sekaligus contoh kalimat ungkapan '{idiom}' dong",
        "kalau orang bilang '{idiom}', maksudnya gimana?",
        "jelasin makna ungkapan '{idiom}' pakai bahasa santai dong",
    ]
    a_styles = [
        "Ungkapan '{idiom}' artinya {meaning}. Contoh pemakaiannya: \"{ex}\"",
        "Dalam bahasa Indonesia, '{idiom}' bermakna {meaning}. Misalnya pada kalimat: \"{ex}\"",
        "Maksud dari '{idiom}' adalah {meaning}, bukan makna harfiah kata per katanya. Contohnya: \"{ex}\"",
        "Kalau ada yang menyebut '{idiom}', artinya {meaning}. Contoh kalimat sehari-harinya: \"{ex}\"",
        "Secara kiasan, '{idiom}' berarti {meaning}. Kamu bisa memakainya seperti ini: \"{ex}\"",
        "Itu termasuk idiom yang artinya {meaning}. Biar kebayang konteksnya, lihat kalimat ini: \"{ex}\"",
    ]
    for idiom, meaning, ex in IDIOMS:
        for idx, qs in enumerate(q_styles):
            if limit and len(col.rows) >= limit:
                return
            q = qs.format(idiom=idiom)
            a = a_styles[idx % len(a_styles)].format(idiom=idiom, meaning=meaning, ex=ex)
            col.add(q, a)


def _gen_di_rules(col: CategoryCollector, limit: int | None) -> None:
    # Tempat -> dipisah
    for i, loc in enumerate(DI_LOCATIONS):
        wrong = "di" + loc.replace(" ", "")
        right = f"di {loc}"
        qs = [
            f"penulisan yang benar '{right}' atau '{wrong}'?",
            f"nara, kata '{right}' itu 'di'-nya dipisah atau digabung?",
            f"beneran '{right}' pakai spasi atau '{wrong}' tanpa spasi?",
            f"gimana penulisan baku untuk keterangan tempat '{right}'?",
        ]
        ans_list = [
            f"Yang benar adalah '{right}' (dipisah pakai spasi), karena `{loc}` menunjukkan tempat atau lokasi, bukan kata kerja pasif.",
            f"Tulis terpisah menjadi '{right}' ya. Aturannya mudah: kalau menjawab pertanyaan 'di mana?', kata depan `di` selalu dipisah dari kata tempatnya.",
            f"Pakai spasi: '{right}'. Bentuk '{wrong}' kurang tepat sebab `{loc}` adalah keterangan lokasi.",
            f"Penulisan bakunya '{right}'. Kata depan `di` wajib dipisah saat diikuti nama tempat atau posisi seperti `{loc}`.",
        ]
        for k in range(len(qs)):
            if limit and len(col.rows) >= limit:
                return
            col.add(qs[k], ans_list[k])

    # Kata kerja pasif -> disambung
    for base, joined in DI_PASSIVES:
        wrong = f"di {base}"
        qs = [
            f"penulisan yang baku '{joined}' atau '{wrong}'?",
            f"kalau kata kerja pasif dari '{base}', tulisnya '{joined}' atau '{wrong}'?",
            f"nara, '{joined}' itu digabung atau dipisah ya?",
            f"mana yang tepat menurut EYD: '{joined}' atau '{wrong}'?",
        ]
        ans_list = [
            f"Yang baku adalah '{joined}' (digabung tanpa spasi), karena `di-` di sini berfungsi sebagai awalan pembentuk kata kerja pasif dari `{base}`.",
            f"Digabung menjadi '{joined}' ya. Cirinya gampang: kalau bisa diubah ke bentuk aktif `me-` (dari kata dasar `{base}`), penulisannya selalu serangkai.",
            f"Tulis serangkai: '{joined}', bukan '{wrong}'. Pemisahan spasi hanya dipakai untuk keterangan tempat atau waktu.",
            f"Menurut ejaan baku, yang benar '{joined}'. Karena `{base}` adalah tindakan, imbuhan `di-` melekat langsung pada kata dasarnya.",
        ]
        for k in range(len(qs)):
            if limit and len(col.rows) >= limit:
                return
            col.add(qs[k], ans_list[k])


def _gen_daily_translations(col: CategoryCollector, limit: int | None) -> None:
    for idx, (id_sent, en_sent) in enumerate(DAILY_TRANSLATIONS):
        q_to_en = [
            f"bahasa Inggrisnya \"{id_sent}\" apa ya?",
            f"nara, terjemahin ke bahasa Inggris dong: \"{id_sent}\"",
            f"gimana ngomong \"{id_sent}\" dalam bahasa Inggris?",
            f"bantu translate kalimat ini ke Inggris: \"{id_sent}\"",
        ]
        a_to_en = [
            f"Dalam bahasa Inggris, kamu bisa bilang: \"{en_sent}\". Kalimat ini terdengar wajar untuk percakapan sehari-hari.",
            f"Terjemahan alaminya adalah: \"{en_sent}\". Cocok dipakai saat ngobrol langsung maupun lewat pesan singkat.",
            f"Kamu bisa menyampaikannya begini: \"{en_sent}\". Susunan katanya sederhana dan mudah dipahami lawan bicara.",
            f"Versi bahasa Inggrisnya: \"{en_sent}\". Tinggal sesuaikan nada bicaranya dengan situasi obrolanmu.",
        ]
        for k in range(len(q_to_en)):
            if limit and len(col.rows) >= limit:
                return
            col.add(q_to_en[k], a_to_en[k], allow_english=True)

        q_to_id = [
            f"arti kalimat Inggris \"{en_sent}\" dalam bahasa Indonesia apa?",
            f"nara, terjemahin \"{en_sent}\" ke bahasa Indonesia yang santai dong",
            f"maksud dari \"{en_sent}\" kalau diartiin ke Indonesia apa ya?",
        ]
        a_to_id = [
            f"Artinya kurang lebih: \"{id_sent}\". Kalimat itu biasa dipakai dalam obrolan harian.",
            f"Kalau diterjemahkan secara luwes ke bahasa Indonesia, maksudnya: \"{id_sent}\".",
            f"Makna kalimat tersebut adalah: \"{id_sent}\".",
        ]
        for k in range(len(q_to_id)):
            if limit and len(col.rows) >= limit:
                return
            col.add(q_to_id[k], a_to_id[k], allow_english=True)


def build_bahasa_v2(
    col: CategoryCollector,
    *,
    seed: int = 20261023,
    limit: int | None = None,
) -> None:
    # Utamakan materi sehari-hari baru terlebih dahulu
    _gen_idioms(col, limit)
    _gen_di_rules(col, limit)
    _gen_daily_translations(col, limit)
    if limit and len(col.rows) >= limit:
        return

    # Tambahkan kosakata, kata baku, sinonim, antonim, peribahasa, dan struktur kata dari v1
    legacy = Builder(seed=seed)
    rng = random.Random(seed)
    data_bahasa.build_language_content(legacy)
    if limit is None or len(legacy.rows) + len(col.rows) < limit:
        data_language.build_language_puzzles(legacy, rng)

    rows = list(legacy.rows)
    rng.shuffle(rows)
    for row in rows:
        if limit and len(col.rows) >= limit:
            break
        q = row["messages"][0]["content"]
        a = row["messages"][1]["content"]
        col.add(q, a, min_answer=34, allow_english=("inggris" in q.lower()))
