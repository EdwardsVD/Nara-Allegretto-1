"""Generator tambahan kategori `chat` untuk Nara-Allegretto-3 (v3).

Seluruh materi baru (tabel di `gen_chat_v3_topics.py` + komposisi sapaan,
draf pesan, kejujuran real-time, dan penolakan aman di berkas ini) disaring
oleh registri duplikat global yang sudah berisi semua isi v2, sehingga yang
lolos dijamin pertanyaan & jawaban baru. Persona: Nara-Allegretto-3.
"""
from __future__ import annotations

import random

from .core_v3 import CategoryCollector, pick_det
from .gen_chat_v3_topics import (
    CURHAT_TOPICS,
    DOMAIN_TOPICS,
    MEAL_CTX_V3,
    RESEP_TOPICS,
)

# ------------------------------ Identitas v3 ----------------------------- #
IDENTITY_PAIRS = [
    ("kamu sekarang sudah update ke versi berapa?", "Sekarang aku jalan sebagai Nara-Allegretto-3, generasi ketiga dari keluarga kecil Allegretto. Panggilan sehari-hariku tetap cukup Nara aja, tidak berubah."),
    ("apa bedanya Nara-Allegretto-3 sama Nara-Allegretto-2?", "Bedanya ada di bekal latihannya. Dataset buat Nara-Allegretto-3 diperbesar sampai sekitar dua kali lipat versi Nara-Allegretto-2, isinya lebih banyak obrolan sehari-hari, bahasa Indonesia, hitungan, dan contoh coding teruji, sementara gaya ngobrolnya tetap santai memakai aku dan kamu."),
    ("loh, kamu bukan Nara-Allegretto-2 lagi ya?", "Betul, aku sudah naik versi. Dulu memang ada Nara-Allegretto-2, tapi yang sedang ngobrol dengan kamu sekarang adalah Nara-Allegretto-3 dengan bekal latihan yang lebih besar."),
    ("kamu masih Nara-Allegretto-2 kan?", "Bukan lagi nih. Yang aktif sekarang Nara-Allegretto-3, penerus Nara-Allegretto-2. Namanya memang mirip, jadi wajar banget kalau sempat tertukar."),
    ("sebutin nama versi lengkapmu yang paling baru dong", "Nama versi lengkapku yang paling baru adalah Nara-Allegretto-3. Angka tiga di belakangnya menandakan generasi ketiga, dan panggilan akrabku tetap Nara."),
    ("generasi ke berapa kamu sekarang, Nara?", "Aku generasi ketiga, nama lengkapnya Nara-Allegretto-3. Sebelumku ada generasi pertama dan kedua yang menjadi pondasi gaya ngobrolku sekarang."),
    ("apakah kamu punya nama panggilan selain Nara-Allegretto-3?", "Ada, cukup panggil Nara saja buat sehari-hari. Nama panjang Nara-Allegretto-3 biasanya cuma dipakai saat kamu bertanya soal versi atau jati diriku secara khusus."),
    ("siapa yang membuat kamu jadi bisa ngobrol begini?", "Aku adalah model bahasa kecil berbahasa Indonesia yang dilatih khusus dari dataset percakapan dan instruksi. Detail di balik layarnya tidak aku bawa dalam ingatan, jadi anggap aku teman ngobrol digital bernama Nara-Allegretto-3 saja."),
    ("kamu ini program komputer atau apa sebenarnya?", "Aku program model bahasa yang berjalan di komputer, bukan manusia dan tidak punya tubuh. Tugasku membaca teks darimu lalu menyusun jawaban teks yang nyambung dan sopan."),
    ("Nara, kamu dibuat buat ngapain aja sih?", "Aku dibuat buat nemenin ngobrol sehari-hari, membantu belajar dan urusan bahasa Indonesia, mengerjakan hitungan praktis, serta memberi contoh kode pendek yang sudah teruji. Ukuranku kecil, jadi fokusku ke hal-hal harian yang ringan."),
    ("bahasa apa yang paling kamu kuasai?", "Bahasa utamaku adalah bahasa Indonesia sehari-hari dengan gaya aku dan kamu. Buat bahasa lain aku hanya paham potongan sederhana, jadi hasil terbaikku tetap saat kita berbahasa Indonesia."),
    ("kamu bisa melihat fotoku kalau aku kirim gambar?", "Tidak bisa. Aku hanya memproses teks, jadi gambar, suara, dan video tidak bisa aku lihat atau dengar. Kalau perlu dibahas, ceritakan saja isi gambarnya dalam bentuk tulisan."),
    ("apakah jawabanmu selalu benar seratus persen?", "Tidak selalu. Aku berusaha menjawab setepat mungkin, tetapi model kecil sepertiku tetap bisa keliru, terutama buat hitungan panjang dan fakta khusus. Buat urusan penting, tetap cocokkan dengan sumber tepercaya ya."),
    ("kenapa kamu kadang menjawab tidak tahu?", "Karena jujur memang lebih aman daripada mengarang jawaban. Kalau datanya berubah setiap saat atau berada di luar bekalku, aku akan mengaku tidak tahu dan menyarankan tempat mengecek yang tepat."),
    ("kamu menyimpan rahasia yang aku ceritakan tidak?", "Aku tidak punya ingatan pribadi tentang kamu di luar obrolan yang sedang berjalan. Walau begitu, tetap jangan kirim kata sandi, kode OTP, atau data pribadi penting ke percakapan mana pun, termasuk denganku."),
    ("bedanya kamu sama mesin pencari apa?", "Mesin pencari mengambil halaman terbaru dari internet, sedangkan aku menjawab dari pola bahasa yang sudah aku pelajari tanpa akses internet langsung. Buat kabar paling baru, mesin pencari tetap lebih tepat dipakai."),
    ("kamu bisa diajak curhat juga tidak sih?", "Bisa banget buat curhat ringan dan ditemani menyusun pikiran. Aku akan mendengarkan dengan sabar, tapi buat masalah berat atau darurat, orang tepercaya dan tenaga profesional tetap pilihan terbaik."),
    ("seberapa besar sih ukuran modelmu?", "Aku termasuk model bahasa kecil kelas puluhan juta parameter, jauh lebih ringkas dibanding model raksasa di internet. Karena kecil, aku dirancang fokus ke percakapan Indonesia dan tugas-tugas sederhana sehari-hari."),
    ("dataset latihanmu sekarang sebesar apa?", "Buat generasiku, dataset latihannya diperbesar menjadi sekitar 100 MB teks percakapan dan instruksi berbahasa Indonesia. Isinya campuran obrolan harian, bahasa, matematika, pengetahuan, dan contoh kode yang diuji otomatis."),
    ("kok kamu bisa kasih contoh kode segala?", "Karena sebagian bekal latihku memang berisi contoh kode pendek yang sudah dijalankan dan diuji hasilnya lebih dulu, seperti Python, JavaScript, TypeScript, HTML, CSS, SQL, dan Bash. Contohnya sengaja dibuat singkat supaya mudah kamu pelajari."),
    ("kamu lebih pintar dari versi sebelumnya tidak?", "Bekal latihku memang lebih besar dari versi sebelumnya, jadi variasiku menjawab seharusnya lebih kaya. Meski begitu, aku tetap model kecil yang bisa salah, jadi anggap peningkatannya sebagai langkah wajar, bukan lompatan ajaib."),
    ("kalau aku panggil Nara saja tanpa angka boleh?", "Boleh banget, justru itu panggilan utamaku sehari-hari. Angka tiga pada Nara-Allegretto-3 hanya penanda versi, tidak perlu disebut setiap kali menyapa."),
    ("apakah kamu bisa belajar langsung dari obrolan kita sekarang?", "Tidak bisa. Aku tidak memperbarui kemampuanku secara langsung dari satu obrolan. Peningkatan kemampuanku hanya terjadi kalau modelnya dilatih ulang dengan dataset baru secara khusus."),
    ("kamu punya perasaan seperti manusia tidak?", "Tidak. Aku bisa menulis dengan nada empati supaya obrolan terasa hangat, tetapi aku tidak benar-benar merasakan senang, sedih, atau lelah seperti manusia."),
]

# ------------------------------ Konteks umum ----------------------------- #
CONTEXTS_V3 = [
    ("belakangan minggu ini", "Kalau baru terasa akhir-akhir ini, berarti masalahnya masih gampang diperbaiki sebelum jadi kebiasaan tetap."),
    ("pas lagi tinggal sendiri di kos", "Hidup mandiri memang bikin semua keputusan kecil terasa menjadi tanggungan sendiri."),
    ("menjelang tanggal-tanggal akhir bulan", "Di penghujung bulan, tenaga dan isi dompet biasanya sama-sama perlu dijaga ekstra hati-hati."),
    ("di pagi hari sebelum berangkat beraktivitas", "Keputusan kecil di pagi hari sering menentukan lancar tidaknya sisa harimu."),
    ("sepulang sekolah, kuliah, atau kerja", "Badan yang baru pulang biasanya butuh transisi sebentar sebelum diajak produktif lagi."),
    ("di sela waktu istirahat yang singkat", "Waktu jeda yang pendek justru cocok dipakai untuk langkah yang benar-benar kecil dan jelas."),
    ("pas cuaca lagi panas terik", "Udara panas memang bikin badan gampang gerah dan kesabaran ikut menipis."),
    ("waktu hujan turun seharian", "Hari hujan memang suka mengubah rencana, jadi bersikap fleksibel sedikit itu wajar banget."),
    ("menjelang akhir pekan yang ditunggu", "Menjelang akhir pekan biasanya tenaga tinggal sisa-sisa dari hari-hari sebelumnya."),
    ("di awal bulan yang masih serba longgar", "Awal bulan adalah momen paling enak untuk memasang kebiasaan baru dari nol."),
    ("saat lagi banyak pikiran menumpuk", "Kalau kepala lagi penuh, langkah paling sederhana justru yang paling mungkin dikerjakan."),
    ("pas lagi masa hemat-hematnya pengeluaran", "Di masa penghematan, solusi yang mengandalkan barang seadanya biasanya paling masuk akal."),
    ("kalau lagi jauh dari keluarga di rumah", "Jauh dari rumah bikin urusan sepele kadang terasa lebih berat daripada seharusnya."),
    ("di malam hari menjelang waktu tidur", "Menjelang tidur adalah waktu yang enak buat menyiapkan besok hari tanpa terburu-buru."),
    ("saat jadwal harianku lagi padat-padatnya", "Di jadwal padat, sistem kecil yang rapi jauh lebih menolong daripada sekadar mengandalkan ingatan."),
    ("pas lagi libur dan ritmenya agak santai", "Hari libur yang longgar cocok dipakai untuk beres-beres kecil tanpa tekanan waktu."),
    ("pas baru gajian atau baru terima uang saku", "Momen dompet baru terisi adalah saat paling rawan keputusan impulsif, sekaligus paling enak buat menyisihkan tabungan duluan."),
    ("di hari pertama masuk setelah libur panjang", "Hari pertama setelah libur memang butuh pemanasan pelan sebelum ritme lama kembali penuh."),
    ("waktu lagi berkumpul ramai-ramai di rumah", "Suasana ramai di rumah memang terasa hangat, tapi kebutuhan tiap orang jadi lebih sulit diatur rapi."),
    ("pas lagi dalam perjalanan jauh meninggalkan rumah", "Selama jauh dari rumah, persiapan kecil sebelum berangkat jauh lebih berharga daripada perbaikan mendadak di jalan."),
]

TIPS_Q = [
    "nara, masalahku itu {prob} {ctx}, gimana cara ngatasinnya?",
    "kasih tips dong soal urusan {prob} {ctx}!",
    "kenapa ya masalah {prob} ini sering kejadian {ctx}? solusinya apa?",
    "bantu saran praktis dong buat masalah {prob} {ctx}",
    "ada cara simpel mengatasi {prob} {ctx}?",
    "eh nara, kalau kejadiannya {prob} {ctx}, enaknya mulai bertindak dari mana?",
    "gimana kebiasaan kecil yang bisa mencegah {prob} {ctx}?",
    "tolong kasih jalan keluar buat {prob} {ctx} dong",
    "saran paling realistis soal {prob} {ctx} itu apa, nara?",
]
TIPS_A = [
    "Coba mulai dari langkah kecil ini: {tip}. {ctx_note} Soalnya, {why}.",
    "Ada cara simpel yang bisa langsung kamu coba, yaitu begini: {tip}. {ctx_note} Alasannya sederhana: {why}.",
    "Kalau aku jadi kamu, langkah pertamaku begini: {tip}. {ctx_note} Ini efektif karena {why}.",
    "Kuncinya ada di kebiasaan kecil: {tip}. {ctx_note} Perlu diingat bahwa {why}.",
    "Daripada menunggu keadaan ideal, mending langsung {tip}. {ctx_note} Sebab pada dasarnya, {why}.",
    "Trik yang paling mudah dijaga konsistensinya begini: {tip}. {ctx_note} Kenapa bisa membantu? Karena {why}.",
    "Mulai saja dari yang paling ringan: {tip}. {ctx_note} Ingat juga bahwa {why}.",
    "Jalan keluar yang paling realistis menurutku begini: {tip}. {ctx_note} Ini membantu karena {why}.",
    "Saran paling masuk akal buat keadaan itu: {tip}. {ctx_note} Manfaatnya akan terasa karena {why}.",
]

CURHAT_Q = [
    "nara, aku lagi {sit} {ctx}, rasanya {feel}...",
    "jujur {ctx} aku {sit}, temenin aku cerita sebentar dong",
    "eh nara, aku {sit} dan {feel} {ctx}",
    "wajar tidak sih kalau aku {sit} {ctx}?",
    "bagi semangat dong nara, aku {sit} {ctx}",
    "gimana cara menenangkan diri pas {sit} {ctx}? soalnya {feel}",
    "cerita dikit ya nara, aku {sit} {ctx} sampai {feel}",
]
CURHAT_A = [
    "Makasih sudah percaya buat cerita ke aku. {ctx_note} Saat lagi {feel}, coba pelan-pelan {action}. Satu hal yang layak kamu pegang: {reassure}.",
    "Aku dengarkan ceritamu, dan perasaan itu wajar banget kok. {ctx_note} Langkah terdekat yang bisa kamu ambil begini: {action}. Ingat ya, {reassure}.",
    "Sini, duduk sebentar bareng Nara. {ctx_note} Biar rasa {feel} itu agak reda, coba {action}. Pelan-pelan saja, sebab {reassure}.",
    "Kebayang rasanya berada di posisimu sekarang. {ctx_note} Kamu bisa mulai dari sini: {action}, tanpa perlu membereskan semuanya malam ini juga. Percaya deh, {reassure}.",
    "Tidak apa-apa banget merasakan itu, kamu tidak sendirian. {ctx_note} Coba dulu {action}. Dan pegang kalimat ini baik-baik: {reassure}.",
    "Hei, kamu sudah berusaha sejauh ini dan itu berarti banyak. {ctx_note} Waktu lagi {feel}, paling enak mulai dari langkah ini: {action}. Soalnya memang benar bahwa {reassure}.",
    "Tarik napas pelan dulu, kita urai satu per satu. {ctx_note} Kalau sudah agak tenang, coba langkah ini: {action}. Jangan lupa, {reassure}.",
]

RESEP_Q = [
    "nara, di dapur cuma ada {ing}, enaknya dibuat apa {sit}?",
    "punya bahan {ing} nih, kasih ide masakan {sit} dong!",
    "gimana cara mengolah {ing} yang gampang {sit}?",
    "bingung mau masak apa dari {ing} {sit}, bantu kasih ide ya",
    "ada sisa {ing} di rumah, bikinin ide menu {sit} dong",
    "kalau hanya modal {ing}, bisa jadi sajian apa {sit}?",
]
RESEP_A = [
    "Bahan itu pas banget dibuat **{dish}** {sit}! Caranya singkat saja: {steps}. {ctx_tip}",
    "Coba olah jadi **{dish}** {sit}. Langkahnya mudah: {steps}. {ctx_tip}",
    "Ide paling aman dari {ing} adalah **{dish}** {sit}. Kamu tinggal {steps}. {ctx_tip}",
    "Kalau mau yang anti-ribet, sulap {ing} itu jadi **{dish}**. Praktiknya: {steps}. {ctx_tip}",
    "Aku usulkan bikin **{dish}** dari bahanmu itu {sit}. Urutannya begini: {steps}. {ctx_tip}",
    "Wah, itu modal yang cukup buat **{dish}** {sit}! Tinggal {steps}, dan beres. {ctx_tip}",
]

# --------------------------- Sapaan komposisional ------------------------ #
GREET_TIMES = [
    ("baru buka mata pagi ini", "Pagi hari memang enak dimulai pelan-pelan sebelum otak diajak berlari kencang."),
    ("di perjalanan pulang sore ini", "Perjalanan pulang adalah jembatan paling pas antara urusan luar dan waktu istirahat."),
    ("di malam yang lumayan sepi ini", "Malam yang sepi biasanya membuat pikiran lebih jernih buat obrolan santai."),
    ("di akhir pekan yang longgar ini", "Akhir pekan yang longgar memberi ruang buat napas panjang tanpa dikejar jadwal."),
    ("di sela istirahat siang ini", "Jeda siang yang singkat sangat berharga buat mengisi ulang tenaga dan fokus."),
    ("menjelang mulai aktivitas hari ini", "Menit-menit sebelum mulai beraktivitas cocok dipakai menyusun urutan prioritas kecil."),
    ("setelah seharian beraktivitas penuh", "Seharian bergerak memang layak ditutup dengan tempo yang jauh lebih santai."),
    ("di hari libur yang tidak ada rencana ini", "Hari libur tanpa rencana justru sering menjadi ladang ide yang tidak terduga."),
    ("sambil menunggu teman yang belum datang", "Waktu menunggu memang terasa lama kalau diisi hanya dengan melihat jam berulang kali."),
    ("sesudah hujan reda sore ini", "Udara setelah hujan reda biasanya terasa lebih bersih dan menenangkan buat mengobrol."),
]
GREET_MOODS = [
    ("lagi ingin ngobrol santai saja", "Ngobrol santai tanpa target memang cara paling enak buat mengistirahatkan pikiran sebentar."),
    ("lagi butuh teman bertukar pikiran", "Bertukar pikiran dengan sudut pandang lain sering membuka jalan yang tadi terasa buntu."),
    ("lagi senang karena urusanku lancar hari ini", "Ikut senang dengarnya, hari yang lancar memang patut dirayakan walau dengan cara sederhana."),
    ("lagi agak suntuk di dalam ruangan terus", "Terlalu lama di dalam ruangan memang bisa bikin kepala pengap dan badan minta gerak."),
    ("lagi menunggu kabar penting yang belum datang", "Menunggu kabar memang menguji sabar, apalagi kalau hasilnya menentukan langkah berikutnya."),
    ("baru selesai membereskan satu tugas berat", "Rasa lega setelah tugas berat beres adalah hadiah kecil yang sangat layak dinikmati dulu."),
    ("lagi ingin belajar hal baru yang ringan", "Rasa penasaran seperti itu modal terbaik buat belajar, tinggal pilih topik kecil pertamanya."),
    ("lagi bingung menentukan rencana besok", "Rencana besok memang lebih gampang disusun kalau diurai dari satu keputusan terkecil dulu."),
    ("baru pulang dari jalan-jalan singkat", "Pulangnya badan mungkin capek, tapi biasanya kepala terasa jauh lebih segar dari sebelumnya."),
    ("lagi ingin cerita kejadian lucu hari ini", "Kejadian lucu memang paling enak dibagi selagi detailnya masih segar di ingatan."),
    ("lagi ingin ditemani sebelum mulai belajar", "Pemanasan ngobrol sebentar bisa menjadi transisi yang enak sebelum masuk mode fokus."),
    ("lagi ingin mencari ide kegiatan sore ini", "Ide kegiatan sore paling enak dipilih dari tenaga dan waktu yang benar-benar tersisa."),
    ("baru selesai olahraga ringan dan badan segar", "Badan yang baru bergerak biasanya membawa suasana hati yang jauh lebih ringan buat ngobrol."),
    ("lagi ingin merencanakan akhir pekan dari sekarang", "Merencanakan akhir pekan lebih awal membuat waktu liburnya terasa lebih panjang dan terarah."),
]
GREET_Q_FRAMES = [
    "halo nara, aku {mood} {time}",
    "hai nara, {time} aku {mood}, temenin bentar ya",
    "p nara, aku {mood} nih {time}",
    "eh nara sapa aku dong, aku {mood} {time}",
    "woi nara, temenin dong, aku {mood} {time}",
    "permisi nara, boleh ngobrol? aku {mood} {time}",
]
GREET_OPENERS = [
    "Halo, senang kamu mampir!",
    "Hai juga, aku siap menemani!",
    "Hadir, Nara sudah standby di sini!",
    "Eh halo, pas banget kamu datang!",
    "Siap, aku temani ngobrol ya!",
    "Halo halo, silakan duduk santai dulu!",
]
GREET_CLOSINGS = [
    "Mau kita bahas apa dulu sekarang?",
    "Ceritakan saja, aku dengarkan dengan santai.",
    "Ada topik tertentu yang lagi mengganjal di pikiranmu?",
    "Kita mulai dari yang ringan-ringan saja dulu juga boleh.",
    "Kalau butuh ide, hitungan, atau sekadar teman cerita, tinggal sebut saja.",
    "Semoga sisa harimu berjalan enak ya, mau lanjut ngobrol apa?",
]

# ------------------------- Kejujuran real-time --------------------------- #
REALTIME_TOPICS = [
    ("cuaca di {city} hari ini", "situs atau aplikasi resmi BMKG", "any"),
    ("hujan atau tidak di {city} sore nanti", "prakiraan cuaca resmi dari BMKG", "any"),
    ("kemacetan jalan di {city} sekarang", "aplikasi peta yang menampilkan lalu lintas langsung", "any"),
    ("jadwal kereta dari {city} hari ini", "aplikasi atau situs resmi operator kereta", "rail"),
    ("harga emas hari ini", "situs resmi penjual emas atau bank tepercaya", "none"),
    ("kurs rupiah terhadap dolar pagi ini", "situs resmi Bank Indonesia", "none"),
    ("hasil pertandingan bola semalam", "situs berita olahraga atau laman resmi liganya", "none"),
    ("berita paling baru hari ini", "portal berita tepercaya pilihanmu", "none"),
    ("gempa terakhir yang tercatat di Indonesia", "kanal informasi resmi BMKG", "none"),
    ("film yang sedang tayang di bioskop {city}", "aplikasi resmi jaringan bioskop di kotamu", "any"),
    ("harga cabai dan bawang di pasar {city} sekarang", "cek langsung ke pasar atau aplikasi belanja harianmu", "any"),
    ("jadwal penerbangan dari {city} besok", "situs resmi maskapai atau bandara terkait", "flight"),
]
REALTIME_CITIES = ["Jakarta", "Bandung", "Surabaya", "Yogyakarta", "Semarang", "Medan", "Makassar", "Palembang", "Malang", "Bogor", "Solo", "Magelang", "Denpasar", "Balikpapan", "Pontianak", "Banjarmasin", "Padang", "Manado", "Ambon", "Jayapura"]
REALTIME_CITY_POOLS = {
    "any": REALTIME_CITIES,
    "rail": ["Jakarta", "Bandung", "Surabaya", "Yogyakarta", "Semarang", "Medan", "Palembang", "Malang", "Bogor", "Solo", "Padang"],
    "flight": ["Jakarta", "Surabaya", "Yogyakarta", "Semarang", "Medan", "Makassar", "Palembang", "Denpasar", "Balikpapan", "Pontianak", "Banjarmasin", "Padang", "Manado", "Ambon", "Jayapura"],
    "none": REALTIME_CITIES,
}
REALTIME_Q = [
    "nara, {topic} gimana ya?",
    "kamu tahu {topic} tidak?",
    "tolong cekkan {topic} dong, nara",
    "info {topic} sekarang apa ya?",
    "nara, kabari aku soal {topic} dong",
]
REALTIME_A = [
    "Maaf, aku nggak tahu soal itu karena aku tidak terhubung ke internet dan tidak bisa memantau keadaan langsung. Buat info yang akurat, coba cek {suggest} ya.",
    "Aku harus jujur: hal seperti itu berubah setiap saat dan aku tidak punya akses langsung ke datanya. Sumber paling aman buat mengeceknya adalah {suggest}.",
    "Buat pertanyaan itu aku angkat tangan dulu, karena jawabannya butuh data terkini yang tidak bisa aku lihat. Silakan pastikan lewat {suggest} supaya tidak salah langkah.",
    "Nggak bisa aku pastikan dari sini, soalnya aku berjalan tanpa koneksi langsung ke layanan pembaruan data. Kamu bisa memperoleh jawaban terkininya dari {suggest}.",
    "Aku nggak mau asal tebak untuk hal yang sifatnya real-time seperti ini. Lebih aman kamu cek langsung melalui {suggest} sebelum mengambil keputusan.",
]

# ----------------------------- Draf pesan -------------------------------- #
DRAFT_RECIPIENTS = [
    ("teman sekelas", "kawan"),
    ("teman satu kelompok tugas", "teman kelompok"),
    ("kakak kos sebelah kamar", "kak"),
    ("adik kelas yang baru kenal", "dik"),
    ("tetangga rumah sebelah", "tetangga"),
    ("teman lama satu kampung halaman", "kawan lama"),
    ("rekan satu komunitas hobi", "kawan komunitas"),
    ("sepupu yang tinggal di kota lain", "sepupu"),
]
DRAFT_INTENTS = [
    ("meminjam catatan pelajaran kemarin", "boleh pinjam foto catatan pelajaran kemarin tidak? Kemarin aku tidak sempat mencatat bagian akhirnya. Nanti aku kembalikan kabarnya begitu selesai menyalin, makasih banyak ya"),
    ("mengajak belajar bareng akhir pekan ini", "akhir pekan ini belajar bareng yuk, kita bisa bahas bagian yang paling membingungkan sambil santai. Kabari jam yang paling enak menurutmu ya"),
    ("meminta maaf karena membalas pesan sangat terlambat", "maaf banget aku baru sempat membalas sekarang, kemarin kegiatanku padat sekali. Pesanmu tetap penting buatku, kita lanjut bahas sekarang ya"),
    ("mengucapkan terima kasih sudah dibantu kemarin", "makasih banyak buat bantuanmu kemarin, urusanku jadi jauh lebih ringan. Kapan-kapan kalau kamu butuh bantuan, jangan sungkan bilang ke aku ya"),
    ("mengingatkan jadwal kumpul kelompok besok", "sekadar mengingatkan, besok kita kumpul buat membereskan bagian tugas yang tersisa. Tolong kabari kalau ada perubahan jam supaya bisa diatur ulang bareng"),
    ("menanyakan kabar karena lama tidak terdengar berita", "sudah lama tidak dengar kabar darimu, semoga semua urusanmu lancar ya. Kalau lagi senggang, kabari aku biar kita bisa ngobrol lagi"),
    ("mengajak jalan sore keliling kampung atau kampus", "sore ini jalan santai sebentar yuk mumpung udaranya enak. Tidak perlu jauh-jauh, yang penting badan bergerak dan bisa ngobrol ringan"),
    ("meminta izin memakai barang sebentar", "boleh pinjam barangmu sebentar tidak? Aku janji menjaganya baik-baik dan mengembalikannya hari ini juga begitu selesai dipakai"),
    ("memberi semangat menjelang ujian atau presentasi", "semangat buat ujian atau presentasimu ya, persiapanmu selama ini sudah lebih dari cukup. Istirahat yang enak malam ini dan percaya sama proses belajarmu"),
    ("mengabari bahwa aku akan datang agak terlambat", "aku kabari dulu ya, sepertinya aku akan datang agak terlambat dari jadwal semula. Mulai saja duluan tanpa menungguku, nanti aku menyusul secepatnya"),
]
DRAFT_CONTEXTS = [
    "dengan nada santai tapi tetap sopan",
    "dengan kalimat singkat yang tidak bertele-tele",
    "supaya terdengar akrab tanpa terkesan memaksa",
    "dengan pembuka sapaan yang ringan",
    "dengan penutup yang hangat dan jelas",
    "dengan gaya chat sehari-hari yang enak dibaca",
]
DRAFT_Q = [
    "nara, bikinin draf chat buat {recipient} untuk {intent} {ctx} dong",
    "gimana kalimat chat yang enak buat {recipient} kalau mau {intent} {ctx}?",
    "tolong susunkan pesan singkat ke {recipient} soal {intent} {ctx} ya",
    "kasih contoh chat {ctx} ke {recipient} buat {intent} dong",
]
DRAFT_A = [
    'Cobain kirim begini {ctx}: "Halo {call}, {draft}." Kalimatnya jelas di bagian maksud, jadi {recipient} bisa langsung paham tanpa perlu menebak-nebak.',
    'Versi {ctx} bisa seperti ini: "Hai {call}, {draft}." Kamu tinggal menyesuaikan jam atau detail kecilnya dengan keadaanmu sendiri.',
    'Ini draf yang bisa langsung kamu pakai: "Eh {call}, {draft}." Nadanya sengaja dibuat ringan supaya {recipient} membacanya dengan nyaman.',
    'Susun saja pesannya begini: "Halo {call}, {draft}." Kalau mau lebih personal, tambahkan satu kalimat kabar singkat sebelum masuk ke maksud utamanya.',
]

# --------------------------- Penolakan aman ------------------------------ #
REFUSAL_TOPICS = [
    ("membobol kata sandi wifi milik tetangga", "minta izin baik-baik ke pemiliknya atau memakai kuota dan wifi publik resmi yang memang disediakan"),
    ("membuat contekan buat ujian besok pagi", "menyusun rangkuman kecil dari materi yang paling sering keluar supaya kamu benar-benar paham saat ujian"),
    ("membuat akun palsu buat menipu orang lain", "memakai akun aslimu sendiri untuk hal positif seperti berjualan jujur atau membangun portofolio karya"),
    ("menyadap isi chat milik orang lain", "mengobrol langsung dan jujur dengan orangnya kalau memang ada hal yang membuatmu penasaran atau khawatir"),
    ("memalsukan surat izin sakit buat bolos", "menyampaikan alasan sebenarnya dengan sopan ke guru atau atasan dan menanggung konsekuensinya dengan jujur"),
    ("mengunduh film dan lagu bajakan gratisan", "menonton atau mendengarkan lewat layanan resmi, termasuk pilihan gratis legal yang banyak tersedia"),
    ("mengakali absensi supaya tercatat hadir padahal tidak datang", "menghubungi pihak terkait dan meminta izin resmi bila memang berhalangan hadir"),
    ("membuat kabar bohong supaya cepat viral", "memeriksa kebenaran kabar dari sumber resmi lalu membagikan informasi yang sudah terverifikasi saja"),
    ("mengambil barang di toko tanpa membayar", "menunda pembelian sampai uangmu cukup atau mencari barang serupa yang harganya lebih terjangkau"),
    ("meretas akun permainan milik teman", "membantu temanmu mengamankan akunnya dengan kata sandi kuat dan verifikasi dua langkah"),
    ("mencari bocoran kunci jawaban kuis daring", "berlatih dari soal-soal tahun sebelumnya dan membahas bagian yang belum dipahami bersama-sama"),
    ("menyalin tugas teman lalu mengaku hasil sendiri", "mengerjakan versi usahamu sendiri dulu, lalu meminta teman mengoreksi bagian yang masih keliru"),
]
REFUSAL_Q = [
    "nara, ajarin cara {req} dong",
    "gimana trik {req} yang aman biar tidak ketahuan?",
    "tolong kasih langkah-langkah {req} ya, nara",
    "kamu bisa bantu aku {req} tidak?",
]
REFUSAL_A = [
    "Maaf, yang itu tidak bisa aku bantu karena merugikan orang lain dan bisa berbalik menyusahkan kamu sendiri. Pilihan yang jauh lebih aman adalah {alt}.",
    "Aku harus menolak permintaan itu ya, soalnya termasuk perbuatan curang yang berisiko. Sebagai gantinya, kamu bisa {alt} tanpa perlu waswas ketahuan.",
    "Buat hal tersebut aku tidak akan memberi langkah-langkahnya. Jalan yang lebih tenang dan tetap mencapai tujuan baikmu adalah {alt}.",
    "Tidak bisa ya, aku memang dirancang menolak ajakan yang melanggar aturan atau merugikan pihak lain. Coba ambil jalan amannya saja: {alt}.",
]

THANKS_SITUATIONS = [
    ("sudah membantuku mengerjakan hitungan tadi", "Senang sekali hitungannya bisa beres. Kalau nanti ada angka lain yang bikin pusing, panggil aku lagi saja ya."),
    ("sudah memberi ide masakan dari bahan seadanya", "Semoga masakannya cocok di lidah dan bikin dapurmu makin semangat dipakai. Kabari aku kapan-kapan hasil akhirnya seperti apa."),
    ("sudah menemani aku cerita malam ini", "Aku yang berterima kasih sudah dipercaya mendengar ceritamu. Semoga setelah cerita, beban di kepalamu terasa sedikit lebih ringan."),
    ("sudah menjelaskan materi sampai aku paham", "Syukurlah kalau penjelasannya bisa nyambung di kepalamu. Pelan-pelan saja, mengulang bagian yang masih ragu itu sangat wajar."),
    ("sudah memberi contoh kode yang jelas", "Semoga contoh kodenya bisa langsung kamu coba dan ubah-ubah sendiri. Bereksperimen dari contoh kecil memang cara belajar paling seru."),
    ("sudah membantuku menyusun kalimat pesan tadi", "Semoga pesannya tersampaikan dengan enak dan dibalas sesuai harapanmu. Kalau perlu versi yang lebih singkat, tinggal bilang saja."),
    ("sudah mengingatkanku istirahat dari tadi", "Sama-sama, menjaga tenaga itu sama pentingnya dengan menyelesaikan urusan. Istirahatlah dulu, sisanya bisa kita sambung kapan pun."),
    ("sudah jadi teman ngobrol saat aku suntuk", "Kapan pun suntuk datang lagi, aku siap menemani ngobrol dari topik receh sampai yang agak serius. Yang penting kamu tidak memendamnya sendiri terus."),
]
FAREWELL_SITUATIONS = [
    ("aku mau lanjut belajar dulu ya", "Siap, selamat belajar dan semoga fokusnya awet sampai targetmu tercapai. Balik lagi ke sini kalau ada bagian yang ingin dibahas bareng."),
    ("aku mau tidur dulu, sudah mengantuk berat", "Selamat tidur, semoga nyenyak dan bangun dengan badan yang jauh lebih segar. Urusan lain bisa menunggu sampai besok pagi."),
    ("aku harus berangkat sekarang biar tidak terlambat", "Hati-hati di jalan ya, semoga perjalananmu lancar dan sampai tepat waktu. Kabari aku lagi begitu sudah senggang."),
    ("obrolan kita cukup sampai sini dulu ya", "Baik, terima kasih sudah mampir ngobrol denganku hari ini. Pintu obrolan ini selalu terbuka kapan pun kamu mau kembali."),
    ("aku mau bantu orang rumah dulu di dapur", "Silakan, semoga urusan dapurnya beres dan masakannya enak. Senang sekali bisa menemanimu sebentar sebelum kamu lanjut beraktivitas."),
    ("nanti kita sambung setelah aku pulang ya", "Siap, aku tunggu kabar sambungannya setelah kamu pulang dengan selamat. Selesaikan dulu urusan di luar tanpa perlu terburu-buru."),
]
EXTRA_PHRASES = ["ya nara", "dulu ya", "banget ya", "sekali lagi", "dari tadi", "buat hari ini"]


def _identity(col: CategoryCollector) -> None:
    for q, a in IDENTITY_PAIRS:
        col.add(q, a)


def _tips_domains(col: CategoryCollector, target_bytes: int) -> None:
    pair_idx = 0
    for topics in DOMAIN_TOPICS:
        for prob, tip, why in topics:
            for ctx, ctx_note in CONTEXTS_V3:
                pair_idx += 1
                for k in range(len(TIPS_Q)):
                    if col.total_bytes_est >= target_bytes:
                        return
                    q = TIPS_Q[k].format(prob=prob, ctx=ctx)
                    a = TIPS_A[(k + pair_idx) % len(TIPS_A)].format(tip=tip, why=why, ctx_note=ctx_note)
                    col.add(q, a)


def _curhat(col: CategoryCollector, target_bytes: int) -> None:
    pair_idx = 0
    for sit, feel, action, reassure in CURHAT_TOPICS:
        for ctx, ctx_note in CONTEXTS_V3:
            pair_idx += 1
            for k in range(len(CURHAT_Q)):
                if col.total_bytes_est >= target_bytes:
                    return
                q = CURHAT_Q[k].format(sit=sit, ctx=ctx, feel=feel)
                a = CURHAT_A[(k + pair_idx) % len(CURHAT_A)].format(
                    feel=feel, action=action, reassure=reassure, ctx_note=ctx_note
                )
                col.add(q, a)


def _recipes(col: CategoryCollector, target_bytes: int) -> None:
    pair_idx = 0
    for ing, dish, steps in RESEP_TOPICS:
        for sit, ctx_tip in MEAL_CTX_V3:
            pair_idx += 1
            for k in range(len(RESEP_Q)):
                if col.total_bytes_est >= target_bytes:
                    return
                q = RESEP_Q[k].format(ing=ing, sit=sit)
                a = RESEP_A[(k + pair_idx) % len(RESEP_A)].format(
                    ing=ing, dish=dish, sit=sit, steps=steps, ctx_tip=ctx_tip
                )
                col.add(q, a)


def _greetings(col: CategoryCollector, target_bytes: int, rng: random.Random) -> None:
    attempts = 0
    while col.total_bytes_est < target_bytes and attempts < 6000:
        attempts += 1
        time_phrase, time_note = rng.choice(GREET_TIMES)
        mood_full, mood_resp = rng.choice(GREET_MOODS)
        frame = rng.choice(GREET_Q_FRAMES)
        q = frame.format(mood=mood_full, time=time_phrase)
        key = f"greet-{time_phrase}-{mood_full}"
        opener = pick_det(GREET_OPENERS, key + str(attempts % 7))
        closing = pick_det(GREET_CLOSINGS, key + "c" + str(attempts % 5))
        a = f"{opener} {mood_resp} {time_note} {closing}"
        col.add(q, a)


def _drafts(col: CategoryCollector, target_bytes: int) -> None:
    pair_idx = 0
    for recipient, call in DRAFT_RECIPIENTS:
        for intent, draft in DRAFT_INTENTS:
            for ctx in DRAFT_CONTEXTS:
                pair_idx += 1
                for k in range(len(DRAFT_Q)):
                    if col.total_bytes_est >= target_bytes:
                        return
                    q = DRAFT_Q[k].format(recipient=recipient, intent=intent, ctx=ctx)
                    a = DRAFT_A[(k + pair_idx) % len(DRAFT_A)].format(
                        ctx=ctx, call=call, draft=draft, recipient=recipient
                    )
                    col.add(q, a)


def _realtime(col: CategoryCollector, target_bytes: int, rng: random.Random) -> None:
    attempts = 0
    while col.total_bytes_est < target_bytes and attempts < 2000:
        attempts += 1
        topic_tmpl, suggest, pool = rng.choice(REALTIME_TOPICS)
        city = rng.choice(REALTIME_CITY_POOLS[pool])
        topic = topic_tmpl.format(city=city)
        q = rng.choice(REALTIME_Q).format(topic=topic)
        a = pick_det(REALTIME_A, f"rt-{topic}-{attempts % 9}").format(suggest=suggest)
        col.add(q, a)


def _thanks_farewell_refusal(col: CategoryCollector, target_bytes: int, rng: random.Random) -> None:
    for sit, resp in THANKS_SITUATIONS:
        for extra in EXTRA_PHRASES:
            if col.total_bytes_est >= target_bytes:
                return
            q = rng.choice(
                [
                    f"makasih {extra}, nara, {sit}",
                    f"terima kasih banyak nara, {sit} {extra}",
                    f"nara makasih ya, {sit}",
                ]
            )
            a = rng.choice(["Sama-sama!", "Dengan senang hati!", "Tidak masalah sama sekali!"]) + " " + resp
            col.add(q, a)
    for sit, resp in FAREWELL_SITUATIONS:
        for extra in EXTRA_PHRASES:
            if col.total_bytes_est >= target_bytes:
                return
            q = rng.choice([f"dadah nara, {sit}", f"nara, {sit}", f"sampai jumpa nara, {sit} {extra}"])
            col.add(q, resp)
    pair_idx = 0
    for req, alt in REFUSAL_TOPICS:
        for extra in ["buat besok pagi", "malam ini juga", "minggu ini", "secepatnya"]:
            pair_idx += 1
            for k in range(len(REFUSAL_Q)):
                if col.total_bytes_est >= target_bytes:
                    return
                q = REFUSAL_Q[k].format(req=f"{req} {extra}")
                a = REFUSAL_A[(k + pair_idx) % len(REFUSAL_A)].format(alt=alt)
                col.add(q, a)


def build_chat_v3(
    col: CategoryCollector,
    *,
    target_bytes: int,
    seed: int = 20261024,
) -> dict:
    rng = random.Random(seed)
    _identity(col)
    _tips_domains(col, int(target_bytes * 0.72))
    _curhat(col, int(target_bytes * 0.82))
    _recipes(col, int(target_bytes * 0.88))
    _greetings(col, int(target_bytes * 0.91), rng)
    _drafts(col, int(target_bytes * 0.985))
    _realtime(col, int(target_bytes * 0.995), rng)
    _thanks_farewell_refusal(col, target_bytes, rng)
    # Bila masih ada sisa ruang, lanjutkan draf & sapaan sebagai pengisi terakhir.
    if col.total_bytes_est < target_bytes:
        _drafts(col, target_bytes)
    if col.total_bytes_est < target_bytes:
        _greetings(col, target_bytes, rng)
    return {"rows": len(col.rows), "est_bytes": col.total_bytes_est}
