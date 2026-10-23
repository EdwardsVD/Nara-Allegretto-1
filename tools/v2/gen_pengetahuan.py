"""Generator kategori `pengetahuan.jsonl` untuk Nara-Allegretto-2.

Memakai basis fakta terkurasi (negara, 38 provinsi Indonesia, kuliner Nusantara,
budaya, gunung, tokoh, peristiwa sejarah, unsur kimia, teknologi, sains,
kesehatan, satuan ukur, dan panduan praktis) dengan variasi gaya tanya-jawab
santai khas percakapan sehari-hari.
"""
from __future__ import annotations

import os
import random
import sys

TOOLS_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if TOOLS_DIR not in sys.path:
    sys.path.insert(0, TOOLS_DIR)

import data_facts  # noqa: E402
import data_world  # noqa: E402
from nara_core import Builder, fmt_id  # noqa: E402

from .core_v2 import CategoryCollector

EXTRA_UNITS = [
    ("1 lusin", "12 buah", "dipakai saat membeli piring, gelas, buku tulis, atau pensil"),
    ("1 kodi", "20 potong atau helai", "sering dipakai pedagang pakaian, kain, atau batik"),
    ("1 gros", "144 buah (12 lusin)", "dipakai untuk barang kecil dalam jumlah banyak seperti kancing atau peniti"),
    ("1 rim", "500 lembar", "standar ukuran kertas cetak HVS A4 atau F4"),
    ("1 kuintal", "100 kilogram", "biasa dipakai untuk menimbang hasil panen beras, jagung, atau gula"),
    ("1 ton", "1.000 kilogram (10 kuintal)", "dipakai untuk muatan truk, kapal, atau hasil panen besar"),
    ("1 hektare", "10.000 meter persegi", "ukuran umum untuk luas sawah, kebun, atau lahan"),
    ("1 kilometer", "1.000 meter", "dipakai untuk menyatakan jarak antarwilayah atau jalan raya"),
    ("1 liter", "1.000 mililiter (setara 1 desimeter kubik)", "dipakai untuk takaran air, susu, minyak goreng, atau bensin"),
    ("1 jam", "60 menit atau 3.600 detik", "satuan waktu standar dalam kegiatan sehari-hari"),
    ("1 minggu", "7 hari", "siklus hari dari Senin sampai Minggu"),
    ("1 abad", "100 tahun", "dipakai saat membahas periode sejarah panjang"),
    ("1 windu", "8 tahun", "satuan waktu tradisional yang dikenal di Nusantara"),
    ("1 dasawarsa", "10 tahun (1 dekade)", "sering dipakai untuk evaluasi pembangunan atau peringatan sepuluh tahunan"),
    ("1 mil laut", "1.852 meter", "dipakai pada pelayaran kapal dan penerbangan"),
]

EXTRA_VITAMINS = [
    ("Vitamin A", "menjaga kesehatan mata, kulit, dan daya tahan tubuh", "wortel, ubi jalar, bayam, dan hati ayam"),
    ("Vitamin B12", "membantu pembentukan sel darah merah dan fungsi saraf", "ikan, telur, susu, dan daging sapi"),
    ("Vitamin C", "membantu daya tahan tubuh, penyerapan zat besi, dan kesehatan gusi", "jeruk, jambu biji, pepaya, dan paprika"),
    ("Vitamin D", "membantu penyerapan kalsium agar tulang dan gigi tetap kuat", "sinar matahari pagi, ikan berlemak, dan kuning telur"),
    ("Vitamin E", "berperan sebagai antioksidan yang melindungi sel tubuh", "kacang almond, biji bunga matahari, dan alpukat"),
    ("Vitamin K", "membantu proses pembekuan darah saat terjadi luka", "kangkung, brokoli, bayam, dan sawi hijau"),
    ("Zat besi", "membentuk hemoglobin pembawa oksigen di dalam darah", "daging merah tanpa lemak, bayam, dan kacang hijau"),
    ("Kalsium", "menjaga kepadatan tulang, gigi, serta kerja otot", "susu, tempe, tahu, dan ikan teri"),
    ("Serat pangan", "melancarkan pencernaan dan membantu kenyang lebih lama", "oatmeal, pepaya, sayur hijau, dan kacang-kacangan"),
    ("Protein", "membangun serta memperbaiki jaringan otot dan sel tubuh", "telur, tempe, tahu, ikan, dan dada ayam"),
]

INDO_LAKES_RIVERS = [
    ("Danau Toba", "danau vulkanik terbesar di Indonesia", "Sumatera Utara", "memiliki Pulau Samosir tepat di tengahnya"),
    ("Danau Singkarak", "danau tektonik terkenal di ranah Minang", "Sumatera Barat", "menjadi habitat ikan bilih yang khas"),
    ("Danau Maninjau", "danau kaldera dengan pemandangan perbukitan curam", "Sumatera Barat", "dikenal lewat jalur Kelok 44 menuju tepiannya"),
    ("Danau Sentani", "danau luas di kaki Pegunungan Cyclops", "Papua", "memiliki puluhan pulau kecil dan festival budaya tahunan"),
    ("Danau Kelimutu", "danau kawah tiga warna di puncak gunung", "Nusa Tenggara Timur", "warna airnya bisa berubah seiring aktivitas mineral"),
    ("Danau Poso", "danau jernih berpasir keemasan di bagian tengah pulau", "Sulawesi Tengah", "termasuk salah satu danau terdalam di Indonesia"),
    ("Danau Towuti", "danau tektonik luas di kawasan Luwu Timur", "Sulawesi Selatan", "menjadi bagian sistem danau purba Malili"),
    ("Sungai Kapuas", "sungai terpanjang di Indonesia", "Kalimantan Barat", "membentang sekitar 1.143 km dan menjadi jalur transportasi utama"),
    ("Sungai Mahakam", "sungai besar yang bermuara ke Selat Makassar", "Kalimantan Timur", "menjadi habitat pesut Mahakam yang langka"),
    ("Sungai Musi", "sungai besar yang membelah Kota Palembang", "Sumatera Selatan", "terkenal dengan Jembatan Ampera di atasnya"),
    ("Sungai Bengawan Solo", "sungai terpanjang di Pulau Jawa", "Jawa Tengah dan Jawa Timur", "berhulu di Pegunungan Sewu dan bermuara ke Laut Jawa"),
    ("Sungai Barito", "sungai lebar yang ramai dilalui kapal dan pasar terapung", "Kalimantan Selatan dan Kalimantan Tengah", "menjadi urat nadi ekonomi warga tepian sungai"),
]


def build_pengetahuan_v2(
    col: CategoryCollector,
    *,
    seed: int = 20261023,
    limit: int | None = None,
) -> None:
    rng = random.Random(seed)

    # 1. Basis v1 terkurasi penuh
    legacy = Builder(seed=seed)
    data_world.build_world(legacy)
    data_facts.build_facts(legacy)
    base_rows = list(legacy.rows)
    rng.shuffle(base_rows)
    for row in base_rows:
        if limit and len(col.rows) >= limit:
            return
        col.add(row["messages"][0]["content"], row["messages"][1]["content"], min_answer=34)

    # 2. Variasi santai untuk 87 negara
    for country, capital, continent, currency, lang in data_world.COUNTRIES:
        pairs = [
            (
                f"nara, ibu kota sama mata uang negara {country} apa ya?",
                f"Ibu kota {country} adalah {capital}, sedangkan mata uang resminya {currency}. Negara ini berada di kawasan {continent}.",
            ),
            (
                f"kalau jalan-jalan ke {country}, di sana pakai bahasa dan mata uang apa?",
                f"Di {country}, bahasa yang digunakan adalah {lang} dan transaksinya memakai {currency}. Pusat pemerintahannya ada di kota {capital}.",
            ),
            (
                f"kota {capital} itu ibu kota dari negara mana sih?",
                f"{capital} adalah ibu kota dari {country}, sebuah negara di {continent} yang memakai mata uang {currency}.",
            ),
            (
                f"kasih info singkat soal negara {country} dong",
                f"{country} terletak di {continent} dengan ibu kota {capital}. Warga di sana menggunakan {lang} serta mata uang {currency}.",
            ),
        ]
        for q, a in pairs:
            if limit and len(col.rows) >= limit:
                return
            col.add(q, a)

    # 3. Variasi santai untuk 38 provinsi Indonesia
    for prov, cap, island in data_world.PROVINCES:
        pairs = [
            (
                f"ibu kota provinsi {prov} itu di kota mana ya?",
                f"Ibu kota Provinsi {prov} berada di {cap}. Provinsi ini terletak di kawasan {island}.",
            ),
            (
                f"provinsi {prov} letaknya di pulau apa dan ibu kotanya mana?",
                f"Provinsi {prov} berada di {island}, dengan pusat pemerintahan atau ibu kota di {cap}.",
            ),
            (
                f"kalau kota {cap}, itu pusat pemerintahan provinsi apa?",
                f"{cap} merupakan ibu kota dari Provinsi {prov} yang berada di wilayah {island}.",
            ),
        ]
        for q, a in pairs:
            if limit and len(col.rows) >= limit:
                return
            col.add(q, a)

    # 4. Kuliner khas, budaya, gunung, unsur kimia, dan hewan dengan gaya beragam
    for dish, origin, main_ing in data_world.FOODS:
        pairs = [
            (
                f"makanan {dish} berasal dari daerah mana dan bahan utamanya apa?",
                f"Kuliner {dish} berasal dari {origin}. Hidangan ini dikenal memakai bahan utama seperti {main_ing}.",
            ),
            (
                f"nara, {dish} itu kuliner khas mana sih?",
                f"{dish.capitalize()} adalah makanan khas dari {origin} yang diolah dengan bahan utama {main_ing}.",
            ),
            (
                f"kalau suka olahan {main_ing}, {dish} dari {origin} itu kayak gimana?",
                f"{dish.capitalize()} merupakan sajian populer asal {origin}. Ciri utamanya memang memadukan {main_ing} sehingga rasanya khas.",
            ),
        ]
        for q, a in pairs:
            if limit and len(col.rows) >= limit:
                return
            col.add(q, a)

    for item, kind, region, desc in data_world.CULTURE:
        pairs = [
            (
                f"apa yang kamu tahu soal {item} dari {region}?",
                f"{item} adalah {kind} tradisional asal {region}. Keunikannya terletak pada ciri bahwa ia {desc}.",
            ),
            (
                f"nara, {item} itu {kind} dari daerah mana?",
                f"{item} berasal dari {region}. Sebagai warisan budaya berupa {kind}, ia dikenal karena {desc}.",
            ),
        ]
        for q, a in pairs:
            if limit and len(col.rows) >= limit:
                return
            col.add(q, a)

    for mt, height, loc in data_world.MOUNTAINS:
        h_str = fmt_id(height)
        pairs = [
            (
                f"berapa meter tinggi {mt} dan letaknya di mana?",
                f"{mt} memiliki ketinggian sekitar {h_str} meter di atas permukaan laut dan berada di {loc}.",
            ),
            (
                f"nara, {mt} itu ada di daerah mana sih?",
                f"{mt} terletak di wilayah {loc}, dengan puncak mencapai kurang lebih {h_str} mdpl.",
            ),
        ]
        for q, a in pairs:
            if limit and len(col.rows) >= limit:
                return
            col.add(q, a)

    for elem, sym, num in data_world.ELEMENTS:
        pairs = [
            (
                f"lambang kimia dan nomor atom dari unsur {elem} apa?",
                f"Unsur {elem} memiliki lambang kimia `{sym}` dengan nomor atom {num} pada tabel periodik.",
            ),
            (
                f"unsur dengan lambang `{sym}` dan nomor atom {num} itu apa namanya?",
                f"Lambang `{sym}` bernomor atom {num} pada tabel periodik merujuk pada unsur {elem}.",
            ),
        ]
        for q, a in pairs:
            if limit and len(col.rows) >= limit:
                return
            col.add(q, a)

    for animal, diet, habitat, trait in data_world.ANIMALS:
        pairs = [
            (
                f"hewan {animal} biasanya hidup di mana dan makan apa?",
                f"{animal.capitalize()} umumnya hidup di {habitat} dan memakan {diet}. Ciri khas yang mudah dikenali adalah {trait}.",
            ),
            (
                f"apa ciri khas dari hewan {animal}?",
                f"Ciri menonjol {animal} adalah {trait}. Hewan pemakan {diet} ini banyak ditemukan di {habitat}.",
            ),
        ]
        for q, a in pairs:
            if limit and len(col.rows) >= limit:
                return
            col.add(q, a)

    # 5. Tokoh, peristiwa sejarah, teknologi, kesehatan, satuan ukur, vitamin, dan danau/sungai
    for fig, field, role in data_world.FIGURES:
        pairs = [
            (
                f"siapa itu {fig} dan apa jasanya?",
                f"{fig} adalah tokoh di bidang {field} yang dikenal karena {role}.",
            ),
            (
                f"nara, kenalin singkat tokoh {fig} dong",
                f"Dalam sejarah dan bidang {field}, {fig} dikenang luas karena perannya {role}.",
            ),
        ]
        for q, a in pairs:
            if limit and len(col.rows) >= limit:
                return
            col.add(q, a)

    for ev, yr, detail in data_world.EVENTS:
        pairs = [
            (
                f"tahun berapa {ev} terjadi dan gimana ringkasannya?",
                f"{ev} terjadi pada tahun {yr}. Saat itu, {detail}.",
            ),
            (
                f"peristiwa {ev} ({yr}) itu tentang apa ya?",
                f"Pada tahun {yr} berlangsung {ev}, yakni ketika {detail}.",
            ),
        ]
        for q, a in pairs:
            if limit and len(col.rows) >= limit:
                return
            col.add(q, a)

    for term, desc, ex in data_facts.TECH:
        pairs = [
            (
                f"jelasin pakai bahasa gampang dong, apa itu {term}?",
                f"Secara sederhana, {term} adalah {desc}. Contoh sehari-harinya bisa kamu temui pada {ex}.",
            ),
            (
                f"nara, fungsi {term} di dunia komputer/internet buat apa?",
                f"{term} berperan sebagai {desc}. Contoh paling dekatnya adalah {ex}.",
            ),
            (
                f"kasih contoh nyata dari {term} dong",
                f"Contoh pemakaian {term} adalah {ex}. Istilah ini sendiri merujuk pada {desc}.",
            ),
        ]
        for q, a in pairs:
            if limit and len(col.rows) >= limit:
                return
            col.add(q, a)

    for unit, eq, usage in EXTRA_UNITS:
        qs = [
            f"{unit} itu sama dengan berapa sih?",
            f"nara, ukuran {unit} isinya berapa?",
            f"kalau orang bilang {unit}, itu setara berapa dan buat apa?",
            f"jelasin konversi satuan {unit} dong",
        ]
        ans = [
            f"Ukuran {unit} setara dengan {eq}. Satuan ini lazim {usage}.",
            f"Nilainya sama dengan {eq}. Dalam keseharian, takaran {unit} {usage}.",
            f"Kalau dihitung, {unit} berarti {eq}. Biasanya satuan tersebut {usage}.",
            f"Konversinya mudah: {unit} adalah {eq}, yang umumnya {usage}.",
        ]
        for q, a in zip(qs, ans):
            if limit and len(col.rows) >= limit:
                return
            col.add(q, a)

    for vit, benefit, sources in EXTRA_VITAMINS:
        qs = [
            f"apa manfaat {vit} buat tubuh dan ada di makanan apa aja?",
            f"nara, kalau mau cukup {vit} sebaiknya makan apa?",
            f"fungsi utama {vit} bagi kesehatan kita apa ya?",
            f"makanan sehari-hari yang kaya {vit} contohnya apa?",
        ]
        ans = [
            f"{vit} bermanfaat untuk {benefit}. Sumber alaminya mudah didapat dari {sources}.",
            f"Kamu bisa memperoleh {vit} dari {sources}. Zat gizi ini penting untuk {benefit}.",
            f"Peran utama {vit} di tubuh adalah {benefit}. Contoh sumber hariannya meliputi {sources}.",
            f"Beberapa sumber {vit} yang gampang dicari antara lain {sources}, bagus buat {benefit}.",
        ]
        for q, a in zip(qs, ans):
            if limit and len(col.rows) >= limit:
                return
            col.add(q, a)

    for name, kind, loc, fact in INDO_LAKES_RIVERS:
        qs = [
            f"di mana letak {name} dan apa keunikannya?",
            f"nara, ceritain singkat soal {name} dong",
            f"{name} itu ada di provinsi mana sih?",
        ]
        ans = [
            f"{name} berada di {loc}. Tempat ini dikenal sebagai {kind} yang {fact}.",
            f"{name} merupakan {kind} di wilayah {loc}. Salah satu hal menariknya, ia {fact}.",
            f"Letak {name} ada di {loc}; ia adalah {kind} dan populer karena {fact}.",
        ]
        for q, a in zip(qs, ans):
            if limit and len(col.rows) >= limit:
                return
            col.add(q, a)

    # 6. Julukan kota di Indonesia, rumah adat, alat musik daerah, organ tubuh, dan penemuan penting
    city_nicknames = [
        ("Bandung", "Kota Kembang", "Jawa Barat", "udaranya sejuk serta sejarah taman dan budayanya kuat"),
        ("Surabaya", "Kota Pahlawan", "Jawa Timur", "perjuangan besar warga pada peristiwa 10 November 1945"),
        ("Yogyakarta", "Kota Pelajar", "DI Yogyakarta", "banyaknya kampus, sekolah, dan pusat kebudayaan"),
        ("Semarang", "Kota Lumpia", "Jawa Tengah", "kuliner lumpia rebung khas yang melegenda"),
        ("Bogor", "Kota Hujan", "Jawa Barat", "curah hujannya tinggi hampir sepanjang tahun"),
        ("Malang", "Kota Apel", "Jawa Timur", "kawasan dataran tingginya terkenal menghasilkan apel"),
        ("Solo", "Kota Batik", "Jawa Tengah", "tradisi membatik dan kampung batiknya sangat hidup"),
        ("Pekalongan", "Kota Batik Pesisir", "Jawa Tengah", "motif batik pesisirnya berwarna cerah dan mendunia"),
        (" Palembang", "Bumi Sriwijaya", "Sumatera Selatan", "pernah menjadi pusat Kerajaan maritim Sriwijaya"),
        ("Padang", "Kota Bengkuang", "Sumatera Barat", "hasil bengkuang yang melimpah dan jadi ikon daerah"),
        ("Ambon", "Kota Musik", "Maluku", "bakat musik warganya diakui sampai tingkat dunia"),
        ("Makassar", "Kota Daeng", "Sulawesi Selatan", "sapaan penghormatan adat Bugis-Makassar dan kuliner pantainya"),
        ("Banda Aceh", "Serambi Mekkah", "Aceh", "sejarah awal penyebaran Islam di kepulauan Nusantara"),
        ("Pontianak", "Kota Khatulistiwa", "Kalimantan Barat", "dilalui tepat oleh garis lintang nol derajat"),
        ("Samarinda", "Kota Tepian", "Kalimantan Timur", "tumbuh memanjang di tepi aliran Sungai Mahakam"),
        ("Banjarmasin", "Kota Seribu Sungai", "Kalimantan Selatan", "banyaknya sungai dan budaya pasar terapungnya"),
        ("Jayapura", "Kota Port Numbay", "Papua", "letaknya menghadap teluk indah di ujung timur Indonesia"),
        ("Magelang", "Kota Sejuta Bunga", "Jawa Tengah", "kotanya rapi, asri, dan dikelilingi banyak gunung"),
        ("Cirebon", "Kota Udang", "Jawa Barat", "hasil laut pesisir utara khususnya udang dan terasi"),
        ("Madiun", "Kota Gadis", "Jawa Timur", "singkatan dari perdagangan, pendidikan, dan perindustrian serta nasi pecelnya"),
        ("Kudus", "Kota Kretek", "Jawa Tengah", "sejarah panjang industri kretek dan Menara Kudus"),
        ("Jepara", "Kota Ukir", "Jawa Tengah", "kerajinan ukir kayu jatinya terkenal halus hingga mancanegara"),
        ("Garut", "Kota Intan", "Jawa Barat", "dikenal lewat dodol Garut dan panorama pegunungan Priangan"),
        ("Bukittinggi", "Kota Jam Gadang", "Sumatera Barat", "menara Jam Gadang ikonik di pusat kotanya"),
        ("Manado", "Kota Tinutuan", "Sulawesi Utara", "bubur Manado atau tinutuan serta keindahan laut Bunaken"),
        ("Balikpapan", "Kota Minyak", "Kalimantan Timur", "sejarah pengolahan minyak bumi dan kota pesisir yang bersih"),
        ("kupang", "Kota Kasih", "Nusa Tenggara Timur", "kerukunan warganya di pesisir Pulau Timor"),
        ("Mataram", "Kota Seribu Masjid", "Nusa Tenggara Barat", "berada di Pulau Lombok yang kental dengan tradisi religius"),
        ("batam", "Kota Industri", "Kepulauan Riau", "kawasan industri dan pelabuhan dekat jalur selat internasional"),
        ("Ternate", "Kota Rempah", "Maluku Utara", "sejarah penghasil cengkeh utama di kepulauan Maluku"),
    ]
    for raw_city, nick, prov, reason in city_nicknames:
        city = raw_city.strip().title() if raw_city.strip().islower() else raw_city.strip()
        pairs = [
            (
                f"kenapa kota {city} dijuluki {nick}?",
                f"Kota {city} di {prov} mendapat julukan {nick} karena {reason}.",
            ),
            (
                f"julukan populer untuk kota {city} di {prov} apa ya?",
                f"Kota {city} akrab dijuluki sebagai {nick}. Sebutan itu muncul karena {reason}.",
            ),
            (
                f"kota mana di Indonesia yang punya julukan {nick}?",
                f"Julukan {nick} merujuk pada Kota {city} di Provinsi {prov}, sebab {reason}.",
            ),
            (
                f"nara, ceritain singkat ciri khas kota {city} dong",
                f"{city} terletak di {prov} dan dikenal luas dengan sebutan {nick} berkat {reason}.",
            ),
        ]
        for q, a in pairs:
            if limit and len(col.rows) >= limit:
                return
            col.add(q, a)

    # Rumah adat & alat musik tradisional Nusantara
    trad_houses = [
        ("Rumah Gadang", "Sumatera Barat", "atapnya melengkung runcing menyerupai tanduk kerbau"),
        ("Rumah Joglo", "Jawa Tengah dan DI Yogyakarta", "memiliki empat tiang utama bernama soko guru di tengah bangunan"),
        ("Rumah Tongkonan", "Sulawesi Selatan (Toraja)", "atapnya melengkung tinggi mirip perahu dan penuh ukiran adat"),
        ("Rumah Honai", "Papua Pegunungan", "berbentuk bundar beratap jerami tebal agar tetap hangat di udara dingin"),
        ("Rumah Betang", "Kalimantan Tengah", "berbentuk rumah panggung sangat panjang yang dihuni keluarga besar suku Dayak"),
        ("Rumah Limas", "Sumatera Selatan", "memiliki lantai bertingkat-tingkat yang melambangkan tatanan adat Palembang"),
        ("Rumah Bolon", "Sumatera Utara", "rumah panggung kayu suku Batak dengan atap pelana berujung lancip"),
        ("Rumah Krong Bade", "Aceh", "berbentuk panggung tinggi untuk melindungi penghuni dari banjir dan hewan liar"),
        ("Rumah Baileo", "Maluku", "bangunan terbuka tanpa dinding yang dipakai untuk musyawarah adat"),
        ("Rumah Sasadu", "Maluku Utara", "dibangun oleh suku Sahu memakai pasak kayu tanpa paku besi"),
        ("Rumah Dulohupa", "Gorontalo", "merupakan rumah panggung kayu dengan tangga kembar di sisi kiri dan kanan"),
        ("Rumah Lamin", "Kalimantan Timur", "berupa rumah panjang berukir warna kuning, hitam, dan putih khas Dayak Kenyah"),
        ("Rumah Kebaya", "DKI Jakarta", "memiliki teras depan luas yang akrab buat menerima tamu khas masyarakat Betawi"),
        ("Rumah Baduy (Sulamah Nyanda)", "Banten", "dibangun mengikuti kontur tanah tanpa meratakan bukit demi menjaga alam"),
        ("Bale Tani", "Nusa Tenggara Barat", "berlantai tanah liat campuran dan beratap alang-alang yang sejuk"),
    ]
    for house, region, feat in trad_houses:
        pairs = [
            (
                f"{house} itu rumah adat dari daerah mana dan apa cirinya?",
                f"{house} berasal dari {region}. Ciri khas utamanya, bangunan ini {feat}.",
            ),
            (
                f"apa nama rumah adat terkenal dari {region}?",
                f"Salah satu rumah adat paling dikenal dari {region} adalah {house}, yang khas karena {feat}.",
            ),
            (
                f"nara, jelasin keunikan {house} dong",
                f"{house} merupakan arsitektur tradisional asal {region}. Keistimewaannya, bangunan ini {feat}.",
            ),
        ]
        for q, a in pairs:
            if limit and len(col.rows) >= limit:
                return
            col.add(q, a)

    organs = [
        ("jantung", "memompa darah kaya oksigen dan nutrisi ke seluruh jaringan tubuh tanpa henti"),
        ("paru-paru", "menukar oksigen dari udara yang dihirup dengan karbon dioksida dari darah"),
        ("hati (liver)", "menyaring zat racun di darah, menghasilkan empedu, dan menyimpan cadangan glikogen"),
        ("ginjal", "menyaring limbah metabolisme dari darah lalu membuangnya bersama kelebihan air sebagai urine"),
        ("lambung", "mencerna makanan secara mekanik dan kimiawi menggunakan asam lambung serta enzim pepsin"),
        ("usus halus", "menyerap sari-sari makanan seperti glukosa, asam amino, vitamin, dan mineral ke aliran darah"),
        ("usus besar", "menyerap sisa air dari ampas pencernaan sebelum dikeluarkan dari tubuh"),
        ("otak", "mengatur pikiran, ingatan, gerak tubuh, emosi, hingga fungsi otomatis seperti bernapas"),
        ("pankreas", "menghasilkan enzim pencernaan sekaligus hormon insulin pengatur kadar gula darah"),
        ("limpa", "membantu sistem kekebalan tubuh dan mendaur ulang sel darah merah yang sudah tua"),
        ("kornea mata", "membiaskan cahaya yang masuk ke mata agar fokus tepat menuju lensa dan retina"),
        ("gendang telinga", "menangkap gelombang suara dari luar lalu mengubahnya menjadi getaran ke tulang pendengaran"),
    ]
    for organ, fn in organs:
        pairs = [
            (
                f"apa fungsi utama organ {organ} pada tubuh manusia?",
                f"Di dalam tubuh manusia, {organ} bertugas utama untuk {fn}.",
            ),
            (
                f"nara, kerja {organ} di badan kita itu ngapain sih?",
                f"Peran {organ} sangat penting, yaitu {fn}.",
            ),
            (
                f"jelasin tugas {organ} dengan bahasa sederhana dong",
                f"Secara ringkas, tugas {organ} adalah {fn}.",
            ),
        ]
        for q, a in pairs:
            if limit and len(col.rows) >= limit:
                return
            col.add(q, a)

    # Sains & pengetahuan praktis rumah tangga sehari-hari
    daily_science = [
        ("kenapa es batu bisa mengapung di atas air?", "Saat membeku menjadi es, molekul air membentuk struktur kristal berongga sehingga massa jenis es lebih kecil daripada air cair. Karena lebih ringan per satuan volumenya, es pun mengapung."),
        ("kenapa bawang merah bikin mata perih dan berair waktu diiris?", "Ketika sel bawang terpotong, enzim di dalamnya melepaskan gas sulfur ringan yang menguap ke udara. Saat gas itu menyentuh permukaan mata yang lembap, kelenjar air mata otomatis membilasnya."),
        ("kenapa baju warna hitam terasa lebih panas saat dipakai di bawah terik matahari?", "Warna gelap menyerap hampir seluruh spektrum cahaya matahari dan mengubahnya menjadi panas, sedangkan warna putih atau terang memantulkan sebagian besar cahaya tersebut."),
        ("kenapa suara petir terdengar belakangan setelah kilat terlihat?", "Cahaya merambat sekitar 300.000 km per detik, jauh lebih cepat daripada bunyi di udara yang hanya sekitar 340 meter per detik. Akibatnya kilat sampai ke mata lebih dulu sebelum guruh sampai ke telinga."),
        ("kenapa telinga terasa berdengung atau penuh saat naik pesawat atau ke puncak gunung?", "Tekanan udara di ketinggian lebih rendah daripada tekanan di ruang telinga tengah. Menelan ludah atau menguap membantu membuka saluran tuba eustachius agar tekanannya kembali seimbang."),
        ("kenapa panci logam cepat panas tapi gagang kayunya tetap adem?", "Logam seperti aluminium dan baja adalah konduktor panas yang menghantarkan kalor dengan cepat, sedangkan kayu atau plastik tahan panas termasuk isolator yang menghambat aliran panas."),
        ("kenapa roti bisa mengembang empuk kalau diberi ragi?", "Ragi memfermentasi gula di dalam adonan tepung dan menghasilkan gelembung gas karbon dioksida. Gelembung gas yang terperangkap di jaringan gluten itulah yang membuat adonan mengembang."),
        ("kenapa besi yang kehujanan lama-lama berkarat?", "Besi bereaksi dengan oksigen di udara dan uap air dalam proses oksidasi membentuk besi oksida yang berwarna cokelat kemerahan dan rapuh, yang sehari-hari kita sebut karat."),
        ("kenapa air di kendi tanah liat terasa lebih sejuk?", "Dinding tanah liat memiliki pori-pori halus tempat sedikit air merembes lalu menguap. Proses penguapan itu menyerap panas dari air di dalam kendi sehingga suhunya turun alami."),
        ("kenapa sabun bisa mengangkat minyak di piring kotor sedangkan air saja nggak bisa?", "Molekul sabun punya dua ujung berbeda: satu ujung mengikat lemak atau minyak, dan ujung lainnya mengikat air. Saat dibilas, minyak yang sudah terikat sabun ikut hanyut bersama air."),
    ]
    q_sci_variants = [
        "{q}",
        "nara, jelasin dong {q}",
        "aku penasaran, {q}",
        "secara sains sederhana, {q}",
    ]
    a_sci_prefixes = [
        "",
        "Penjelasan sederhananya begini: ",
        "Hal itu terjadi karena alasan fisika/kimia sehari-hari. ",
        "Menarik nih kalau dilihat proses alaminya. ",
    ]
    for base_q, base_a in daily_science:
        for idx in range(4):
            if limit and len(col.rows) >= limit:
                return
            col.add(q_sci_variants[idx].format(q=base_q), a_sci_prefixes[idx] + base_a)

    # Hari peringatan nasional Indonesia (fakta tetap)
    national_days = [
        ("2 Mei", "Hari Pendidikan Nasional", "mengenang kelahiran tokoh pendidikan Ki Hadjar Dewantara"),
        ("20 Mei", "Hari Kebangkitan Nasional", "memperingati berdirinya organisasi Budi Utomo pada tahun 1908"),
        ("1 Juni", "Hari Lahir Pancasila", "mengenang pidato rumusan dasar negara Pancasila pada tahun 1945"),
        ("17 Agustus", "Hari Kemerdekaan Republik Indonesia", "memperingati Proklamasi Kemerdekaan Indonesia tahun 1945"),
        ("2 Oktober", "Hari Batik Nasional", "merayakan pengakuan batik Indonesia sebagai warisan budaya dunia UNESCO"),
        ("28 Oktober", "Hari Sumpah Pemuda", "mengenang ikrar persatuan pemuda Nusantara pada Kongres Pemuda II tahun 1928"),
        ("10 November", "Hari Pahlawan", "mengenang keberanian pejuang dalam pertempuran Surabaya tahun 1945"),
        ("21 April", "Hari Kartini", "mengenang perjuangan R.A. Kartini dalam memajukan pendidikan dan kesetaraan perempuan"),
        ("25 November", "Hari Guru Nasional", "memberi penghormatan atas pengabdian para guru di seluruh Indonesia"),
        ("12 November", "Hari Kesehatan Nasional", "mengajak masyarakat menjaga pola hidup bersih dan sehat"),
    ]
    for dt, name, desc in national_days:
        pairs = [
            (
                f"tanggal {dt} di Indonesia diperingati sebagai hari apa?",
                f"Setiap tanggal {dt}, Indonesia memperingati {name} untuk {desc}.",
            ),
            (
                f"kapan {name} diperingati dan apa maknanya?",
                f"{name} diperingati setiap tanggal {dt}. Momen ini bertujuan untuk {desc}.",
            ),
            (
                f"nara, kenapa tanggal {dt} jadi {name}?",
                f"Tanggal {dt} ditetapkan sebagai {name} guna {desc}.",
            ),
        ]
        for q, a in pairs:
            if limit and len(col.rows) >= limit:
                return
            col.add(q, a)

    # 7. Taman Nasional Indonesia, Alat Musik Daerah, Kerajaan Nusantara, & Sains Dasar
    national_parks = [
        ("Taman Nasional Komodo", "Nusa Tenggara Timur", "habitat asli kadal purba komodo serta perairan karang kepulauan yang kaya biota laut"),
        ("Taman Nasional Ujung Kulon", "Banten", "suaka terakhir badak jawa bercula satu di ujung barat Pulau Jawa"),
        ("Taman Nasional Gunung Leuser", "Aceh dan Sumatera Utara", "hutan hujan tropis tempat hidup orangutan sumatera, gajah, harimau, dan badak sumatera"),
        ("Taman Nasional Lorentz", "Papua", "kawasan konservasi terluas di Asia Tenggara yang membentang dari gletser puncak salju hingga laut tropis"),
        ("Taman Nasional Tanjung Puting", "Kalimantan Tengah", "pusat pelestarian orangutan kalimantan di ekosistem hutan rawa gambut"),
        ("Taman Nasional Bromo Tengger Semeru", "Jawa Timur", "bentang kaldera lautan pasir luas serta puncak tertinggi Pulau Jawa yaitu Gunung Semeru"),
        ("Taman Nasional Bunaken", "Sulawesi Utara", "taman laut dengan dinding terumbu karang vertikal yang sangat kaya spesies ikan tropis"),
        ("Taman Nasional Way Kambas", "Lampung", "kawasan konservasi gajah sumatera dan badak sumatera di dataran rendah berawa"),
        ("Taman Nasional Wakatobi", "Sulawesi Tenggara", "gugusan kepulauan karang di jantung segitiga terumbu karang dunia"),
        ("Taman Nasional Baluran", "Jawa Timur", "hamparan padang sabana luas berlatar Gunung Baluran tempat banteng dan rusa merumput"),
        ("Taman Nasional Kerinci Seblat", "Sumatera (Jambi, Sumbar, Bengkulu, Sumsel)", "bentang pegunungan Bukit Barisan tempat berdirinya Gunung Kerinci dan bunga raksasa Rafflesia"),
        ("Taman Nasional Bali Barat", "Bali", "habitat alami burung curik bali atau jalak bali putih yang dilindungi ketat"),
    ]
    for park, loc, feat in national_parks:
        for q, a in [
            (f"di mana letak {park} dan apa keunikannya?", f"{park} terletak di wilayah {loc}. Kawasan konservasi ini terkenal sebagai {feat}."),
            (f"apa yang dilindungi di {park}?", f"Di {park} ({loc}), fokus utamanya menjaga {feat}."),
            (f"nara, kenalin singkat tentang {park} dong", f"{park} berada di {loc} dan dikenal luas karena perannya sebagai {feat}."),
            (f"kalau membahas {feat}, itu ciri khas taman nasional apa?", f"Ciri khas {feat} merujuk pada {park} yang berlokasi di {loc}."),
        ]:
            if limit and len(col.rows) >= limit:
                return
            col.add(q, a)

    trad_instruments = [
        ("Angklung", "Jawa Barat", "bambu yang digoyangkan hingga menghasilkan nada bergetar harmonis"),
        ("Sasando", "Nusa Tenggara Timur (Pulau Rote)", "alat musik petik berdawai dengan tabung bambu dan resonator daun lontar melengkung"),
        ("Tifa", "Maluku dan Papua", "alat musik pukul berbentuk tabung kayu berukir yang ditutup kulit hewan di salah satu ujungnya"),
        ("Kolintang", "Sulawesi Utara", "bilah-bilah kayu ringan bernada yang dimainkan dengan cara dipukul menggunakan stik berlapis"),
        ("Gamelan", "Jawa dan Bali", "ansambel instrumen pukul logam perunggu, gong, kendang, dan bilah nada tradisional"),
        ("Saluang", "Sumatera Barat", "alat musik tiup tradisional Minangkabau yang terbuat dari bambu tipis atau talang"),
        ("Sampe (Sape)", "Kalimantan Timur", "alat musik petik tradisional suku Dayak berbadan kayu lebar dengan ukiran khas"),
        ("Kecapi", "Sunda (Jawa Barat)", "kotak kayu memanjang berdawai sejajar yang dipetik lembut mengiringi tembang"),
        ("Gordang Sambilan", "Sumatera Utara (Mandailing)", "sembilan gendang besar bertingkat ukuran yang ditabuh bersama dalam upacara adat"),
        ("Serunai", "Sumatera Barat dan Melayu", "alat musik tiup kayu berlidah getar dengan ujung mengembang seperti terompet kecil"),
    ]
    for inst, origin, how_play in trad_instruments:
        for q, a in [
            (f"alat musik tradisional {inst} berasal dari daerah mana dan gimana memainkannya?", f"Alat musik {inst} berasal dari {origin}, yaitu {how_play}."),
            (f"apa ciri khas alat musik {inst} dari {origin}?", f"Dari daerah {origin}, {inst} dikenal sebagai {how_play}."),
            (f"nara, jelasin singkat alat musik {inst} dong", f"{inst} merupakan warisan musik daerah {origin} berupa {how_play}."),
        ]:
            if limit and len(col.rows) >= limit:
                return
            col.add(q, a)

    kingdoms = [
        ("Kerajaan Kutai", "Kalimantan Timur (tepi Sungai Mahakam)", "abad ke-4 Masehi", "dikenal sebagai salah satu kerajaan Hindu tertua di Nusantara lewat peninggalan tujuh prasasti Yupa"),
        ("Kerajaan Tarumanagara", "Jawa Barat", "abad ke-4 hingga ke-7 Masehi", "meninggalkan prasasti batu seperti Ciaruteun dan Tugu yang mencatat pembangunan saluran air oleh Raja Purnawarman"),
        ("Kerajaan Sriwijaya", "Sumatera Selatan (Palembang)", "abad ke-7 hingga ke-12 Masehi", "tumbuh menjadi kemaharajaan maritim besar pengendali jalur pelayaran Selat Malaka dan pusat studi agama Buddha"),
        ("Kerajaan Mataram Kuno", "Jawa Tengah dan Yogyakarta", "abad ke-8 hingga ke-10 Masehi", "mewariskan mahakarya arsitektur batu Candi Borobudur bercorak Buddha dan Candi Prambanan bercorak Hindu"),
        ("Kerajaan Majapahit", "Jawa Timur (Trowulan)", "abad ke-13 hingga ke-15 Masehi", "mencapai puncak kejayaan pada masa Raja Hayam Wuruk dan Mahapatih Gajah Mada dengan Sumpah Palapa"),
        ("Kesultanan Samudera Pasai", "Aceh bagian utara", "abad ke-13 Masehi", "tercatat sebagai kesultanan Islam awal yang ramai dikunjungi pedagang mancanegara di pesisir Sumatera"),
        ("Kesultanan Demak", "pesisir utara Jawa Tengah", "akhir abad ke-15 Masehi", "menjadi pusat penyebaran Islam awal di Pulau Jawa bersama peran para Wali Songo"),
        ("Kesultanan Gowa-Tallo", "Sulawesi Selatan (Makassar)", "abad ke-16 hingga ke-17 Masehi", "dikenal sebagai poros pelayaran niaga rempah Indonesia bagian timur dengan tokoh gigih Sultan Hasanuddin"),
        ("Kesultanan Ternate dan Tidore", "Kepulauan Maluku Utara", "abad ke-15 hingga ke-17 Masehi", "termasyhur sebagai pusat penghasil cengkih dan pala yang dicari pelayar dari seluruh penjuru dunia"),
        ("Kesultanan Banten", "ujung barat Pulau Jawa", "abad ke-16 hingga ke-17 Masehi", "berkembang pesat sebagai bandar perdagangan lada internasional di tepi Selat Sunda"),
    ]
    for kg, loc, era, note in kingdoms:
        for q, a in [
            (f"di mana pusat {kg} dan apa peninggalan atau ciri sejarahnya?", f"{kg} berpusat di {loc} sekitar {era}, serta {note}."),
            (f"nara, ceritain ringkas sejarah {kg} dong", f"Sekitar {era} di wilayah {loc}, berdiri {kg} yang dalam sejarah {note}."),
            (f"kapan masa berkembangnya {kg}?", f"{kg} berkembang sekitar {era} di kawasan {loc} dan {note}."),
        ]:
            if limit and len(col.rows) >= limit:
                return
            col.add(q, a)

    si_quantities = [
        ("panjang", "meter", "m", "mengukur jarak antara dua titik di ruang"),
        ("massa", "kilogram", "kg", "mengukur banyaknya materi yang terkandung dalam suatu benda"),
        ("waktu", "sekon (detik)", "s", "mengukur selang berlangsungnya suatu peristiwa"),
        ("kuat arus listrik", "ampere", "A", "mengukur laju aliran muatan listrik tiap satuan waktu"),
        ("suhu termodinamika", "kelvin", "K", "mengukur derajat energi panas rata-rata partikel benda dalam skala mutlak"),
        ("intensitas cahaya", "kandela", "cd", "mengukur kekuatan pancaran cahaya dari sumber ke arah tertentu"),
        ("jumlah zat", "mol", "mol", "mengukur banyaknya partikel elementer seperti atom atau molekul"),
        ("gaya", "newton", "N", "besaran turunan hasil kali massa dan percepatan yang menyebabkan perubahan gerak"),
        ("energi atau usaha", "joule", "J", "besaran turunan kemampuan melakukan kerja atau memindahkan benda dengan gaya"),
        ("daya", "watt", "W", "besaran turunan laju penggunaan atau perubahan energi tiap satu detik"),
        ("tekanan", "pascal", "Pa", "besaran turunan besarnya gaya yang bekerja tegak lurus tiap satu meter persegi luas bidang"),
        ("frekuensi", "hertz", "Hz", "besaran turunan banyaknya getaran atau gelombang yang terjadi dalam satu detik"),
    ]
    for qname, unit, sym, desc in si_quantities:
        for q, a in [
            (f"apa satuan SI dan lambang untuk besaran {qname}?", f"Dalam Sistem Internasional (SI), besaran {qname} menggunakan satuan {unit} dengan lambang `{sym}` untuk {desc}."),
            (f"satuan `{unit}` (`{sym}`) dipakai untuk mengukur besaran apa?", f"Satuan {unit} (`{sym}`) pada standar SI dipakai untuk besaran {qname}, yakni guna {desc}."),
            (f"jelasin singkat besaran fisika {qname} beserta satuannya dong", f"Besaran {qname} berfungsi {desc}, dan satuan bakunya dalam SI adalah {unit} (`{sym}`)."),
        ]:
            if limit and len(col.rows) >= limit:
                return
            col.add(q, a)
