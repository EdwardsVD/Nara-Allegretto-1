"""Generator tambahan kategori `pengetahuan` untuk Nara-Allegretto-3 (v3).

Hanya memakai basis fakta terkurasi yang sama dengan v1/v2 (`data_world`,
`data_facts`) dengan gaya tanya baru, ditambah fakta yang bisa dihitung
langsung oleh Python (kalender, hari, tahun kabisat, perbandingan tinggi
gunung/nomor atom/tahun peristiwa dari daftar terkurasi, urutan planet,
bulan, arah mata angin, dan sila Pancasila). Tidak ada fakta karangan baru
yang belum terkurasi.
"""
from __future__ import annotations

import datetime as dt
import os
import random
import sys

TOOLS_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if TOOLS_DIR not in sys.path:
    sys.path.insert(0, TOOLS_DIR)

import data_facts  # noqa: E402
import data_world  # noqa: E402
from nara_core import fmt_id  # noqa: E402

from .core_v3 import CategoryCollector, pick_det

MONTHS = [
    ("Januari", 31), ("Februari", 28), ("Maret", 31), ("April", 30),
    ("Mei", 31), ("Juni", 30), ("Juli", 31), ("Agustus", 31),
    ("September", 30), ("Oktober", 31), ("November", 30), ("Desember", 31),
]
MONTH_NAMES = [m for m, _ in MONTHS]
WEEKDAYS = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
PLANETS = [
    ("Merkurius", "planet terdekat dari Matahari sekaligus yang paling kecil"),
    ("Venus", "planet yang tampak sangat terang dan dijuluki Bintang Kejora"),
    ("Bumi", "planet tempat manusia hidup dengan air cair melimpah di permukaannya"),
    ("Mars", "planet berwarna kemerahan karena debu besi di permukaannya"),
    ("Jupiter", "planet terbesar di tata surya, jauh lebih besar dari Bumi"),
    ("Saturnus", "planet yang terkenal dengan cincin lebar mengelilingi tubuhnya"),
    ("Uranus", "planet yang berputar miring seperti menggelinding mengelilingi Matahari"),
    ("Neptunus", "planet terjauh dari Matahari di antara delapan planet tata surya"),
]
DIRECTIONS = ["utara", "timur-laut", "timur", "tenggara", "selatan", "barat-daya", "barat", "barat-laut"]
PANCASILA = [
    "Ketuhanan Yang Maha Esa",
    "Kemanusiaan yang adil dan beradab",
    "Persatuan Indonesia",
    "Kerakyatan yang dipimpin oleh hikmat kebijaksanaan dalam permusyawaratan/perwakilan",
    "Keadilan sosial bagi seluruh rakyat Indonesia",
]
COLOR_MIX = [
    ("merah", "kuning", "jingga (oranye)"),
    ("merah", "biru", "ungu"),
    ("biru", "kuning", "hijau"),
    ("merah", "putih", "merah muda"),
    ("hitam", "putih", "abu-abu"),
    ("biru", "putih", "biru muda"),
    ("kuning", "putih", "kuning muda"),
    ("hitam", "kuning", "hijau kehitaman yang gelap"),
]
CONTINENTS_BY_AREA = ["Asia", "Afrika", "Amerika Utara", "Amerika Selatan", "Antarktika", "Eropa", "Australia"]
TIMEZONES_ID = [
    ("WIB (Waktu Indonesia Barat)", "UTC+7", "Sumatra, Jawa, Kalimantan Barat, dan Kalimantan Tengah"),
    ("WITA (Waktu Indonesia Tengah)", "UTC+8", "Bali, Nusa Tenggara, Sulawesi, Kalimantan Selatan, dan Kalimantan Timur"),
    ("WIT (Waktu Indonesia Timur)", "UTC+9", "Maluku dan Papua"),
]


def _done(col, quota_made: int, quota: int, target_bytes: int) -> bool:
    return quota_made >= quota or col.total_bytes_est >= target_bytes


def _countries(col, target_bytes, rng):
    for country, capital, continent, currency, lang in data_world.COUNTRIES:
        if col.total_bytes_est >= target_bytes:
            return
        key = f"neg-{country}"
        if country == "Indonesia":
            pairs = [
                (
                    "ibu kota Indonesia sekarang di mana sih, nara?",
                    "Jakarta masih menjadi pusat pemerintahan dan ekonomi Indonesia sampai sekarang. Nusantara di Kalimantan Timur sedang disiapkan sebagai ibu kota baru, tetapi perpindahannya dilakukan secara bertahap.",
                ),
                (
                    "negara kita Indonesia pakai mata uang dan bahasa resmi apa?",
                    "Indonesia memakai mata uang Rupiah untuk transaksi sehari-hari. Bahasa resminya adalah Bahasa Indonesia, yang dipakai sebagai bahasa persatuan di seluruh daerah.",
                ),
            ]
        else:
            pairs = [
                (
                    pick_det(
                        [
                            f"sebutkan benua dan bahasa yang dipakai di negara {country} dong",
                            f"nara, {country} itu ada di kawasan mana dan bahasanya apa?",
                            f"kalau berkunjung ke {country}, aku bakal dengar orang bicara bahasa apa?",
                        ],
                        key + "q1",
                    ),
                    f"Negara {country} berada di kawasan {continent} dan bahasa yang digunakan di sana adalah {lang}. Ibu kotanya adalah {capital}.",
                ),
                (
                    pick_det(
                        [
                            f"mata uang apa yang beredar di {country} dan ibu kotanya di mana?",
                            f"nara, orang {country} belanja pakai uang apa ya?",
                            f"kota {capital} adalah ibu kota negara apa dan mata uangnya apa?",
                        ],
                        key + "q2",
                    ),
                    f"Mata uang yang beredar di {country} adalah {currency}. Pusat pemerintahan negara di kawasan {continent} itu berada di kota {capital}.",
                ),
            ]
        for q, a in pairs:
            if col.total_bytes_est >= target_bytes:
                return
            col.add(q, a)
    # Kelompok negara sekawasan (dihitung dari daftar terkurasi)
    by_cont: dict[str, list[str]] = {}
    for country, _c, continent, _cur, _l in data_world.COUNTRIES:
        by_cont.setdefault(continent, []).append(country)
    made = 0
    attempts = 0
    pool = list(data_world.COUNTRIES)
    while not _done(col, made, 700, target_bytes) and attempts < 2800:
        attempts += 1
        country, capital, continent, _cur, _l = pool[attempts % len(pool)]
        peers = [c for c in by_cont.get(continent, []) if c != country]
        if len(peers) < 3:
            continue
        sample = rng.sample(peers, 3)
        q = pick_det(
            [
                f"sebutkan tiga negara lain yang masih satu kawasan {continent} dengan {country} dong",
                f"nara, negara tetangga sekawasan {continent} dari {country} contohnya apa saja?",
                f"selain {country}, negara apa saja yang sama-sama berada di {continent}?",
            ],
            f"neggrp-{country}-{attempts}q",
        )
        a = pick_det(
            [
                f"Di kawasan {continent}, contoh negara selain {country} antara lain {sample[0]}, {sample[1]}, dan {sample[2]}. Ibu kota {country} sendiri adalah {capital}.",
                f"Tiga contoh negara sekawasan {continent} dengan {country} adalah {sample[0]}, {sample[1]}, serta {sample[2]}. Ketiganya sama-sama negara berdaulat di kawasan yang sama.",
                f"Kamu bisa menyebut {sample[0]}, {sample[1]}, dan {sample[2]} sebagai contoh negara di {continent} selain {country} yang beribu kota di {capital}.",
            ],
            f"neggrp-{country}-{attempts}a",
        )
        if col.add(q, a):
            made += 1


def _provinces(col, target_bytes, rng):
    by_island: dict[str, list[str]] = {}
    for prov, _c, island in data_world.PROVINCES:
        by_island.setdefault(island, []).append(prov)
    for prov, cap, island in data_world.PROVINCES:
        if col.total_bytes_est >= target_bytes:
            return
        peers = [p for p in by_island.get(island, []) if p != prov]
        peer_txt = ""
        if len(peers) >= 2:
            sample = rng.sample(peers, min(2, len(peers)))
            peer_txt = f" Provinsi lain di kawasan yang sama misalnya {sample[0]}" + (f" dan {sample[1]}." if len(sample) > 1 else ".")
        q = pick_det(
            [
                f"lengkapi info ini dong: provinsi {prov} ibu kotanya apa dan di kawasan mana?",
                f"nara, {cap} itu pusat pemerintahan provinsi apa saja infonya?",
                f"kasih ringkasan provinsi {prov} dalam satu jawaban dong",
            ],
            f"prov-{prov}q",
        )
        a = f"Provinsi {prov} terletak di kawasan {island} dengan ibu kota di {cap}.{peer_txt}"
        col.add(q, a)


def _world_pairs(col, target_bytes):
    for dish, origin, main_ing in data_world.FOODS:
        if col.total_bytes_est >= target_bytes:
            return
        col.add(
            pick_det(
                [f"kalau aku lagi di {origin}, kuliner berbahan {main_ing} yang terkenal apa ya?", f"nara, hidangan khas {origin} yang memakai {main_ing} namanya apa?"],
                f"food-{dish}q",
            ),
            f"Kuliner yang dimaksud adalah {dish}, hidangan khas {origin} yang bahan utamanya berupa {main_ing}. Rasanya sangat melekat dengan cita rasa daerah asalnya.",
        )
    for item, kind, region, desc in data_world.CULTURE:
        if col.total_bytes_est >= target_bytes:
            return
        col.add(
            pick_det([f"budaya berupa {kind} dari {region} yang cirinya {desc} itu namanya apa?", f"nara, {kind} asal {region} yang terkenal contohnya apa?"], f"cult-{item}q"),
            f"Contohnya adalah {item}, yaitu {kind} tradisional dari {region}. Keunikannya, ia {desc}, sehingga mudah dikenali banyak orang.",
        )
    for animal, diet, habitat, trait in data_world.ANIMALS:
        if col.total_bytes_est >= target_bytes:
            return
        col.add(
            pick_det([f"hewan pemakan {diet} yang hidup di {habitat} dan cirinya {trait} itu hewan apa?", f"nara, rangkum info hewan {animal} dalam satu jawaban dong"], f"anim-{animal}q"),
            f"Hewan itu adalah {animal}. Ia memakan {diet}, hidup di {habitat}, dan ciri khasnya adalah {trait}.",
        )
    for fig, field, role in data_world.FIGURES:
        if col.total_bytes_est >= target_bytes:
            return
        col.add(
            pick_det([f"tokoh di bidang {field} yang dikenang karena {role} itu siapa?", f"nara, kenapa nama {fig} bisa terkenal di bidang {field}?"], f"fig-{fig}q"),
            f"Tokoh yang dimaksud adalah {fig}. Di bidang {field}, namanya dikenang luas karena {role}.",
        )
    for term, desc, ex in data_facts.TECH:
        if col.total_bytes_est >= target_bytes:
            return
        col.add(
            pick_det([f"istilah teknologi untuk {desc} itu disebut apa?", f"nara, di mana aku bisa menemui contoh {term} dalam keseharian?"], f"tech-{term}q"),
            f"Istilahnya adalah {term}, yaitu {desc}. Contoh paling dekat dalam keseharian bisa kamu temui pada {ex}.",
        )
    for name, city, country in data_world.LANDMARKS:
        if col.total_bytes_est >= target_bytes:
            return
        col.add(
            pick_det([f"bangunan atau tempat terkenal {name} itu lokasinya di kota dan negara mana?", f"nara, kalau mau berkunjung ke {name} harus pergi ke mana?"], f"land-{name}q"),
            f"{name} berada di kota {city}, negara {country}. Tempat ini termasuk salah satu penanda terkenal yang sering dikunjungi wisatawan di sana.",
        )


def _comparisons(col, target_bytes, rng):
    # Gunung: siapa lebih tinggi + selisih (dihitung)
    made = 0
    attempts = 0
    while not _done(col, made, 900, target_bytes) and attempts < 3600:
        attempts += 1
        (m1, h1, l1), (m2, h2, l2) = rng.sample(data_world.MOUNTAINS, 2)
        if h1 == h2:
            continue
        high, low = ((m1, h1, l1), (m2, h2, l2)) if h1 > h2 else ((m2, h2, l2), (m1, h1, l1))
        diff = high[1] - low[1]
        q = pick_det(
            [f"lebih tinggi {m1} atau {m2}? selisihnya berapa meter?", f"nara, bandingkan ketinggian {m1} dengan {m2} dong", f"di antara {m1} dan {m2}, puncak mana yang paling tinggi?"],
            f"mt-{m1}-{m2}q",
        )
        a = pick_det(
            [
                f"Yang lebih tinggi adalah {high[0]} di {high[2]} dengan ketinggian sekitar {fmt_id(high[1])} meter. {low[0]} tingginya sekitar {fmt_id(low[1])} meter, jadi selisih keduanya adalah {fmt_id(diff)} meter.",
                f"{high[0]} unggul karena mencapai sekitar {fmt_id(high[1])} meter, sedangkan {low[0]} sekitar {fmt_id(low[1])} meter. Selisih ketinggian mereka adalah {fmt_id(diff)} meter.",
            ],
            f"mt-{m1}-{m2}a",
        )
        if col.add(q, a):
            made += 1
    # Unsur: nomor atom lebih besar + selisih
    made = 0
    attempts = 0
    while not _done(col, made, 700, target_bytes) and attempts < 2800:
        attempts += 1
        (e1, s1, n1), (e2, s2, n2) = rng.sample(data_world.ELEMENTS, 2)
        if n1 == n2:
            continue
        big, small = ((e1, s1, n1), (e2, s2, n2)) if n1 > n2 else ((e2, s2, n2), (e1, s1, n1))
        q = pick_det(
            [f"unsur {e1} (`{s1}`) dan {e2} (`{s2}`), nomor atom siapa yang lebih besar?", f"nara, urutkan unsur {e1} dan {e2} dari nomor atom terkecil dong", f"di tabel periodik, {e1} atau {e2} yang nomor atomnya lebih besar?"],
            f"el-{e1}-{e2}q",
        )
        a = f"Nomor atom {big[0]} (`{big[1]}`) lebih besar, yaitu {big[2]}, dibandingkan {small[0]} (`{small[1]}`) yang bernomor atom {small[2]}. Urutan dari kecil ke besar adalah {small[0]} lalu {big[0]}."
        if col.add(q, a):
            made += 1
    # Peristiwa: siapa lebih dulu + jarak tahun
    made = 0
    attempts = 0
    while not _done(col, made, 700, target_bytes) and attempts < 2800:
        attempts += 1
        (v1, y1, d1), (v2, y2, d2) = rng.sample(data_world.EVENTS, 2)
        if y1 == y2:
            continue
        early, late = ((v1, y1, d1), (v2, y2, d2)) if y1 < y2 else ((v2, y2, d2), (v1, y1, d1))
        gap = late[1] - early[1]
        q = pick_det(
            [f"peristiwa {v1} dan {v2}, mana yang terjadi lebih dulu?", f"nara, jarak tahun antara {v1} dengan {v2} itu berapa lama?", f"urutkan dari yang paling awal: {v1} atau {v2}?"],
            f"ev-{v1}-{v2}q",
        )
        a = f"Yang terjadi lebih dulu adalah {early[0]} pada tahun {early[1]}, sedangkan {late[0]} berlangsung pada tahun {late[1]}. Jarak waktu antara kedua peristiwa itu adalah {fmt_id(gap)} tahun."
        if col.add(q, a):
            made += 1


def _calendar_and_orders(col, target_bytes, rng):
    # Bulan: jumlah hari, urutan, tetangga
    for idx, (name, days) in enumerate(MONTHS):
        if col.total_bytes_est >= target_bytes:
            return
        nxt = MONTH_NAMES[(idx + 1) % 12]
        prv = MONTH_NAMES[(idx - 1) % 12]
        extra_days = " Pada tahun kabisat, bulan ini bertambah menjadi 29 hari." if name == "Februari" else ""
        col.add(
            pick_det([f"bulan {name} itu bulan ke berapa dan punya berapa hari?", f"nara, sesudah bulan {name} bulan apa? sekalian jumlah harinya ya", f"kasih info urutan serta jumlah hari bulan {name} dong"], f"mon-{name}q"),
            f"Bulan {name} adalah bulan ke-{idx + 1} dalam setahun dan memiliki {days} hari.{extra_days} Bulan sebelumnya adalah {prv}, dan bulan sesudahnya adalah {nxt}.",
        )
    long_months = [m for m, d in MONTHS if d == 31]
    short_months = [m for m, d in MONTHS if d == 30]
    col.add(
        "bulan apa saja yang jumlah harinya 31 hari?",
        f"Bulan yang memiliki 31 hari ada {len(long_months)}, yaitu {', '.join(long_months)}. Sisanya umumnya 30 hari, kecuali Februari yang 28 atau 29 hari.",
    )
    col.add(
        "nara, bulan yang harinya 30 itu yang mana saja?",
        f"Bulan yang memiliki tepat 30 hari adalah {', '.join(short_months)}. Cara mudah mengingatnya adalah menghafal bulan-bulan 31 hari dan pengecualian Februari.",
    )
    # Hari: tetangga
    for idx, day in enumerate(WEEKDAYS):
        if col.total_bytes_est >= target_bytes:
            return
        col.add(
            pick_det([f"kalau hari ini hari {day}, besok hari apa dan kemarin hari apa?", f"nara, sebutkan hari sebelum dan sesudah hari {day} dong"], f"day-{day}q"),
            f"Kalau hari ini hari {day}, maka besok adalah hari {WEEKDAYS[(idx + 1) % 7]} dan kemarin adalah hari {WEEKDAYS[(idx - 1) % 7]}. Urutan lengkapnya adalah {', '.join(WEEKDAYS)}.",
        )
    # Hari dalam sepekan dari suatu tanggal (dihitung datetime)
    made = 0
    attempts = 0
    while not _done(col, made, 1400, target_bytes) and attempts < 4200:
        attempts += 1
        year = rng.randint(2024, 2032)
        month = rng.randint(1, 12)
        last = 29 if (month == 2 and (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0))) else MONTHS[month - 1][1]
        day_num = rng.randint(1, last)
        date = dt.date(year, month, day_num)
        wname = WEEKDAYS[date.weekday()]
        label = f"{day_num} {MONTH_NAMES[month - 1]} {year}"
        q = pick_det(
            [f"tanggal {label} jatuh pada hari apa?", f"nara, {label} itu hari apa ya?", f"cek kalender dong, hari dari tanggal {label} apa?"],
            f"cal-{label}q",
        )
        a = pick_det(
            [
                f"Tanggal {label} jatuh pada hari {wname}. Kamu bisa mencocokkannya dengan kalender tahun {year} untuk memastikan jadwalmu.",
                f"Menurut hitungan kalender Masehi, {label} adalah hari {wname}. Hari berikutnya adalah {WEEKDAYS[(date.weekday() + 1) % 7]}.",
                f"{label} merupakan hari {wname}. Satu hari sebelumnya adalah {WEEKDAYS[(date.weekday() - 1) % 7]}, dan satu hari sesudahnya adalah {WEEKDAYS[(date.weekday() + 1) % 7]}.",
            ],
            f"cal-{label}a",
        )
        if col.add(q, a):
            made += 1
    # Tahun kabisat (dihitung)
    made = 0
    attempts = 0
    while not _done(col, made, 700, target_bytes) and attempts < 2400:
        attempts += 1
        year = rng.randint(1900, 2200)
        leap = year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
        feb = 29 if leap else 28
        q = pick_det(
            [f"tahun {year} termasuk tahun kabisat atau bukan?", f"nara, bulan Februari tahun {year} ada berapa hari?", f"apakah tahun {year} punya tanggal 29 Februari?"],
            f"leap-{year}q",
        )
        if leap:
            a = f"Tahun {year} adalah tahun kabisat, jadi Februari di tahun itu memiliki {feb} hari dan tanggal 29 Februari benar-benar ada. Tahun kabisat adalah tahun yang habis dibagi 400, atau habis dibagi 4 tetapi tidak habis dibagi 100."
        else:
            a = f"Tahun {year} bukan tahun kabisat, jadi Februari di tahun itu hanya memiliki {feb} hari dan tidak ada tanggal 29 Februari. Tahun kabisat harus habis dibagi 400, atau habis dibagi 4 tetapi tidak habis dibagi 100."
        if col.add(q, a):
            made += 1
    # Planet: urutan & tetangga
    for idx, (name, trait) in enumerate(PLANETS):
        if col.total_bytes_est >= target_bytes:
            return
        neighbor = ""
        if idx + 1 < len(PLANETS):
            neighbor = f" Planet sesudahnya adalah {PLANETS[idx + 1][0]}."
        if idx > 0:
            neighbor += f" Planet sebelumnya adalah {PLANETS[idx - 1][0]}."
        col.add(
            pick_det([f"planet {name} urutan ke berapa dari Matahari dan apa cirinya?", f"nara, ceritakan posisi serta ciri planet {name} dong"], f"plan-{name}q"),
            f"{name} adalah planet urutan ke-{idx + 1} dari Matahari. Planet ini dikenal sebagai {trait}.{neighbor}",
        )
    col.add(
        "sebutkan urutan delapan planet dari yang terdekat ke Matahari dong",
        "Urutan delapan planet dari yang terdekat dengan Matahari adalah " + ", ".join(p for p, _ in PLANETS) + ". Cara mudah mengingatnya adalah memperhatikan huruf awal tiap nama secara berurutan.",
    )
    # Arah mata angin: kebalikan (dihitung dari indeks)
    for idx, direc in enumerate(DIRECTIONS):
        if col.total_bytes_est >= target_bytes:
            return
        opp = DIRECTIONS[(idx + 4) % 8]
        col.add(
            pick_det([f"arah yang berlawanan dengan {direc} itu arah apa?", f"nara, kalau menghadap {direc}, arah belakangku apa?"], f"dir-{direc}q"),
            f"Arah yang tepat berlawanan dengan {direc} adalah {opp}. Di kompas, urutan delapan arah utamanya adalah {', '.join(DIRECTIONS)}.",
        )
    # Pancasila
    for idx, sila in enumerate(PANCASILA):
        if col.total_bytes_est >= target_bytes:
            return
        col.add(
            pick_det([f"bunyi sila ke-{idx + 1} Pancasila itu apa?", f"nara, sila nomor {idx + 1} dalam Pancasila berbunyi bagaimana?"], f"sila-{idx}q"),
            f"Sila ke-{idx + 1} Pancasila berbunyi: '{sila}'. Pancasila sendiri terdiri dari lima sila yang menjadi dasar negara Indonesia.",
        )
    # Campuran warna cat dasar
    for c1, c2, hasil in COLOR_MIX:
        if col.total_bytes_est >= target_bytes:
            return
        col.add(
            pick_det([f"kalau cat warna {c1} dicampur warna {c2}, hasilnya warna apa?", f"nara, campuran cat {c1} dan {c2} jadi warna apa ya?"], f"mix-{c1}-{c2}q"),
            f"Campuran cat berwarna {c1} dan {c2} akan menghasilkan warna {hasil}. Hasil akhir bisa sedikit berbeda tergantung perbandingan takaran kedua warnanya.",
        )
    # Benua menurut luas
    for idx, benua in enumerate(CONTINENTS_BY_AREA):
        if col.total_bytes_est >= target_bytes:
            return
        col.add(
            pick_det([f"benua {benua} menempati urutan luas ke berapa di dunia?", f"nara, sebutkan posisi {benua} dalam urutan benua terluas dong"], f"ben-{benua}q"),
            f"Benua {benua} menempati urutan ke-{idx + 1} dalam daftar benua terluas. Urutan lengkap dari yang terluas adalah {', '.join(CONTINENTS_BY_AREA)}.",
        )
    # Zona waktu Indonesia
    for zone, utc, wilayah in TIMEZONES_ID:
        if col.total_bytes_est >= target_bytes:
            return
        col.add(
            pick_det([f"zona waktu {zone} itu UTC berapa dan meliputi wilayah apa saja?", f"nara, daerah mana saja yang memakai {zone}?"], f"tz-{zone}q"),
            f"Zona {zone} setara dengan {utc}. Wilayah Indonesia yang memakainya antara lain {wilayah}.",
        )
    col.add(
        "kalau di WIB jam 9 pagi, di WITA dan WIT jam berapa?",
        "Kalau di wilayah WIB menunjukkan pukul 09.00, maka di WITA sudah pukul 10.00 dan di WIT sudah pukul 11.00. Selisihnya tetap satu jam berurutan karena WITA adalah UTC+8 dan WIT adalah UTC+9.",
    )


def build_pengetahuan_v3(
    col: CategoryCollector,
    *,
    target_bytes: int,
    seed: int = 20261024,
) -> dict:
    rng = random.Random(seed)
    _countries(col, target_bytes, rng)
    _provinces(col, target_bytes, rng)
    _world_pairs(col, target_bytes)
    _comparisons(col, target_bytes, rng)
    _calendar_and_orders(col, target_bytes, rng)
    return {"rows": len(col.rows), "est_bytes": col.total_bytes_est}
