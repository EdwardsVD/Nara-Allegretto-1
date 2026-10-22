"""Materi bahasa Indonesia yang disusun manual: sinonim, antonim, arti kata,
terjemahan, kata baku, peribahasa, dan aturan penulisan.
"""
from __future__ import annotations

import random

from nara_core import Builder

# --------------------------------------------------------------------------- #
# Sinonim: (kata, sinonim, penjelasan)
# --------------------------------------------------------------------------- #
SYNONYMS = [
    ("pintar", "cerdas", "sama-sama menggambarkan orang yang cepat menangkap pelajaran"),
    ("pandai", "cendekia", "sama-sama berarti punya banyak pengetahuan"),
    ("senang", "gembira", "sama-sama menunjukkan perasaan bahagia"),
    ("sedih", "murung", "sama-sama menggambarkan suasana hati yang tidak cerah"),
    ("takut", "cemas", "sama-sama berkaitan dengan rasa khawatir"),
    ("marah", "kesal", "sama-sama menunjukkan perasaan tidak suka"),
    ("lelah", "capek", "sama-sama berarti kehabisan tenaga"),
    ("sehat", "bugar", "sama-sama berarti badan dalam kondisi baik"),
    ("kuat", "kokoh", "sama-sama berarti tidak mudah rusak atau roboh"),
    ("lemah", "rapuh", "sama-sama berarti mudah rusak atau tidak bertenaga"),
    ("cantik", "elok", "sama-sama menggambarkan wajah yang menarik"),
    ("tampan", "ganteng", "sama-sama menggambarkan pria yang menarik"),
    ("rajin", "tekun", "sama-sama berarti bekerja dengan sungguh-sungguh"),
    ("malas", "enggan", "sama-sama berarti tidak bersemangat untuk melakukan sesuatu"),
    ("bohong", "dusta", "sama-sama berarti mengatakan hal yang tidak benar"),
    ("baik", "bagus", "sama-sama berarti berkualitas atau menyenangkan"),
    ("buruk", "jelek", "sama-sama berarti tidak bagus"),
    ("indah", "permai", "sama-sama menggambarkan pemandangan yang elok"),
    ("lucu", "jenaka", "sama-sama berarti membuat orang tertawa"),
    ("mudah", "gampang", "sama-sama berarti tidak sulit dikerjakan"),
    ("sulit", "susah", "sama-sama berarti butuh usaha lebih untuk diselesaikan"),
    ("penting", "krusial", "sama-sama berarti sangat menentukan"),
    ("langka", "jarang", "sama-sama berarti tidak sering ditemukan"),
    ("sering", "kerap", "sama-sama berarti berulang kali terjadi"),
    ("awal", "permulaan", "sama-sama menunjuk bagian pertama"),
    ("akhir", "ujung", "sama-sama menunjuk bagian terakhir"),
    ("sekarang", "kini", "sama-sama menunjuk waktu saat ini"),
    ("besok", "esok", "sama-sama menunjuk hari setelah hari ini"),
    ("teman", "kawan", "sama-sama berarti orang yang dekat dan akrab"),
    ("musuh", "lawan", "sama-sama berarti pihak yang berseberangan"),
    ("rumah", "kediaman", "sama-sama berarti tempat tinggal"),
    ("tugas", "kewajiban", "sama-sama berarti hal yang harus dikerjakan"),
    ("makanan", "pangan", "sama-sama berarti bahan yang dimakan"),
    ("pakaian", "busana", "sama-sama berarti sesuatu yang dipakai di badan"),
    ("uang", "duit", "sama-sama berarti alat pembayaran"),
    ("hutan", "rimba", "sama-sama berarti kawasan yang penuh pohon"),
    ("laut", "samudra", "sama-sama menunjuk perairan yang sangat luas"),
    ("sungai", "kali", "sama-sama menunjuk aliran air di daratan"),
    ("angin", "bayu", "sama-sama berarti udara yang bergerak"),
    ("matahari", "surya", "sama-sama menunjuk bintang pusat tata surya"),
    ("bumi", "dunia", "sama-sama menunjuk tempat kita tinggal"),
    ("cerita", "kisah", "sama-sama berarti rangkaian peristiwa yang diceritakan"),
    ("berita", "kabar", "sama-sama berarti informasi tentang peristiwa"),
    ("kabar", "warta", "sama-sama berarti informasi atau berita"),
    ("nama", "sebutan", "sama-sama berarti kata untuk menyebut sesuatu"),
    ("suara", "bunyi", "sama-sama berarti sesuatu yang bisa didengar"),
    ("bentuk", "rupa", "sama-sama berarti wujud sesuatu"),
    ("jumlah", "total", "sama-sama berarti hasil menjumlahkan"),
    ("masalah", "persoalan", "sama-sama berarti hal yang perlu diselesaikan"),
    ("jawaban", "balasan", "sama-sama berarti respons terhadap pertanyaan"),
    ("pertanyaan", "soal", "sama-sama berarti hal yang ditanyakan"),
    ("alasan", "sebab", "sama-sama berarti dasar terjadinya sesuatu"),
    ("tujuan", "maksud", "sama-sama berarti hal yang ingin dicapai"),
    ("cara", "metode", "sama-sama berarti langkah untuk melakukan sesuatu"),
    ("aturan", "ketentuan", "sama-sama berarti hal yang harus dipatuhi"),
    ("kebebasan", "kemerdekaan", "sama-sama berarti keadaan bebas dari belenggu"),
    ("persatuan", "kesatuan", "sama-sama berarti keadaan bersatu"),
    ("perbedaan", "selisih", "sama-sama berarti jarak atau ketidaksamaan"),
    ("persamaan", "kesamaan", "sama-sama berarti hal yang sama"),
    ("keuntungan", "laba", "sama-sama berarti hasil lebih dari modal"),
    ("kerugian", "rugi", "sama-sama berarti keadaan kehilangan nilai"),
    ("harga", "nilai", "sama-sama menunjuk ukuran berharga suatu barang"),
    ("diskon", "potongan harga", "sama-sama berarti pengurangan dari harga awal"),
    ("pajak", "pungutan", "sama-sama berarti biaya yang ditarik negara"),
    ("gaji", "upah", "sama-sama berarti bayaran atas pekerjaan"),
    ("pekerja", "buruh", "sama-sama berarti orang yang bekerja"),
    ("atasan", "bos", "sama-sama berarti orang yang memimpin pekerja"),
    ("pelanggan", "konsumen", "sama-sama berarti orang yang memakai barang atau jasa"),
    ("penjual", "pedagang", "sama-sama berarti orang yang menjual barang"),
    ("barang", "produk", "sama-sama berarti sesuatu yang dibuat atau dijual"),
    ("murid", "siswa", "sama-sama berarti orang yang belajar di sekolah"),
    ("guru", "pengajar", "sama-sama berarti orang yang mengajar"),
    ("buku", "kitab", "sama-sama berarti kumpulan tulisan yang dijilid"),
    ("ilmu", "pengetahuan", "sama-sama berarti hal yang diketahui"),
    ("akal", "pikiran", "sama-sama berarti kemampuan berpikir"),
    ("perasaan", "emosi", "sama-sama berarti keadaan batin yang dirasakan"),
    ("cinta", "kasih", "sama-sama berarti rasa sayang yang kuat"),
    ("rindu", "kangen", "sama-sama berarti ingin bertemu"),
    ("bahagia", "riang", "sama-sama menggambarkan suasana hati yang cerah"),
    ("sedih", "pilu", "sama-sama menggambarkan perasaan yang perih"),
    ("makan", "santap", "sama-sama berarti memasukkan makanan"),
    ("melihat", "memandang", "sama-sama berarti mengarahkan mata"),
    ("berbicara", "berkata", "sama-sama berarti mengeluarkan kata-kata"),
    ("mengatakan", "menyampaikan", "sama-sama berarti memberitahukan sesuatu"),
    ("menjawab", "membalas", "sama-sama berarti memberikan respons"),
    ("membuat", "membikin", "sama-sama berarti menghasilkan sesuatu"),
    ("memperbaiki", "membetulkan", "sama-sama berarti membuat sesuatu menjadi baik"),
    ("datang", "tiba", "sama-sama berarti sampai di suatu tempat"),
    ("pergi", "berangkat", "sama-sama berarti meninggalkan tempat"),
    ("tinggal", "menetap", "sama-sama berarti bermukim di suatu tempat"),
    ("mati", "wafat", "sama-sama berarti berakhirnya kehidupan"),
    ("tumbuh", "berkembang", "sama-sama berarti bertambah besar"),
    ("membantu", "menolong", "sama-sama berarti memberi bantuan"),
    ("meminta", "mohon", "sama-sama berarti mengajukan permintaan"),
    ("memaafkan", "mengampuni", "sama-sama berarti tidak menghukum kesalahan"),
    ("memulai", "mengawali", "sama-sama berarti melakukan sesuatu pertama kali"),
    ("menjaga", "merawat", "sama-sama berarti membuat sesuatu tetap baik"),
]

# --------------------------------------------------------------------------- #
# Antonim: (kata, antonim, penjelasan)
# --------------------------------------------------------------------------- #
ANTONYMS = [
    ("besar", "kecil", "ukuran keduanya bertolak belakang"),
    ("tinggi", "rendah", "menunjuk ukuran vertikal yang berlawanan"),
    ("panjang", "pendek", "menunjuk ukuran memanjang yang berlawanan"),
    ("lebar", "sempit", "menunjuk ukuran melintang yang berlawanan"),
    ("tebal", "tipis", "menunjuk ukuran ketebalan yang berlawanan"),
    ("berat", "ringan", "menunjuk massa yang berlawanan"),
    ("cepat", "lambat", "menunjuk kecepatan yang berlawanan"),
    ("panas", "dingin", "menunjuk suhu yang berlawanan"),
    ("terang", "gelap", "menunjuk cahaya yang berlawanan"),
    ("siang", "malam", "menunjuk waktu yang berlawanan"),
    ("awal", "akhir", "menunjuk urutan yang berlawanan"),
    ("depan", "belakang", "menunjuk posisi yang berlawanan"),
    ("atas", "bawah", "menunjuk arah yang berlawanan"),
    ("kiri", "kanan", "menunjuk sisi yang berlawanan"),
    ("dalam", "luar", "menunjuk ruang yang berlawanan"),
    ("jauh", "dekat", "menunjuk jarak yang berlawanan"),
    ("banyak", "sedikit", "menunjuk jumlah yang berlawanan"),
    ("ramai", "sepi", "menunjuk suasana yang berlawanan"),
    ("bersih", "kotor", "menunjuk kondisi yang berlawanan"),
    ("rajin", "malas", "menunjuk semangat kerja yang berlawanan"),
    ("pintar", "bodoh", "menunjuk kecerdasan yang berlawanan"),
    ("kaya", "miskin", "menunjuk harta yang berlawanan"),
    ("kuat", "lemah", "menunjuk tenaga yang berlawanan"),
    ("sehat", "sakit", "menunjuk kondisi badan yang berlawanan"),
    ("senang", "sedih", "menunjuk perasaan yang berlawanan"),
    ("berani", "takut", "menunjuk keberanian yang berlawanan"),
    ("benar", "salah", "menunjuk kebenaran yang berlawanan"),
    ("baik", "buruk", "menunjuk kualitas yang berlawanan"),
    ("mudah", "sulit", "menunjuk tingkat kesulitan yang berlawanan"),
    ("murah", "mahal", "menunjuk harga yang berlawanan"),
    ("basah", "kering", "menunjuk kadar air yang berlawanan"),
    ("keras", "lembut", "menunjuk tekstur yang berlawanan"),
    ("tajam", "tumpul", "menunjuk ketajaman yang berlawanan"),
    ("penuh", "kosong", "menunjuk isi yang berlawanan"),
    ("buka", "tutup", "menunjuk keadaan akses yang berlawanan"),
    ("masuk", "keluar", "menunjuk arah gerak yang berlawanan"),
    ("naik", "turun", "menunjuk arah gerak yang berlawanan"),
    ("datang", "pergi", "menunjuk arah kedatangan yang berlawanan"),
    ("maju", "mundur", "menunjuk arah langkah yang berlawanan"),
    ("menang", "kalah", "menunjuk hasil pertandingan yang berlawanan"),
    ("hidup", "mati", "menunjuk keadaan makhluk yang berlawanan"),
    ("tua", "muda", "menunjuk usia yang berlawanan"),
    ("baru", "lama", "menunjuk waktu pemakaian yang berlawanan"),
    ("umum", "khusus", "menunjuk cakupan yang berlawanan"),
    ("asli", "palsu", "menunjuk keaslian yang berlawanan"),
    ("aman", "bahaya", "menunjuk kondisi yang berlawanan"),
    ("untung", "rugi", "menunjuk hasil usaha yang berlawanan"),
    ("pemasukan", "pengeluaran", "menunjuk arus uang yang berlawanan"),
    ("utara", "selatan", "menunjuk arah mata angin yang berlawanan"),
    ("timur", "barat", "menunjuk arah mata angin yang berlawanan"),
    ("hulu", "hilir", "menunjuk bagian aliran sungai yang berlawanan"),
    ("segar", "layu", "menunjuk kondisi tumbuhan yang berlawanan"),
    ("gemuk", "kurus", "menunjuk bentuk badan yang berlawanan"),
    ("ramah", "kasar", "menunjuk sikap yang berlawanan"),
    ("hemat", "boros", "menunjuk cara memakai uang yang berlawanan"),
    ("tetap", "berubah", "menunjuk keadaan yang berlawanan"),
    ("suka", "benci", "menunjuk perasaan yang berlawanan"),
    ("terbuka", "tertutup", "menunjuk keadaan yang berlawanan"),
    ("sederhana", "mewah", "menunjuk gaya hidup yang berlawanan"),
    ("dekat", "jauh", "menunjuk jarak yang berlawanan"),
]

# --------------------------------------------------------------------------- #
# Arti kata: (kata, arti)
# --------------------------------------------------------------------------- #
MEANINGS = [
    ("abadi", "kekal, tidak pernah berakhir, dan tidak bisa hilang"),
    ("adaptasi", "proses menyesuaikan diri dengan keadaan baru"),
    ("aktif", "selalu bergerak atau ikut serta dalam kegiatan"),
    ("akurat", "tepat dan sesuai dengan kenyataan"),
    ("algoritma", "urutan langkah yang jelas untuk menyelesaikan suatu masalah"),
    ("alternatif", "pilihan lain di luar pilihan utama"),
    ("analisis", "kegiatan memeriksa sesuatu secara rinci untuk memahami bagian-bagiannya"),
    ("antusias", "sangat bersemangat dalam melakukan sesuatu"),
    ("apresiasi", "penghargaan atau pengakuan terhadap sesuatu yang baik"),
    ("arsip", "dokumen atau catatan yang disimpan secara teratur"),
    ("asumsi", "anggapan yang diterima sementara sebelum dibuktikan"),
    ("atmosfer", "lapisan gas yang menyelimuti bumi"),
    ("audiens", "orang-orang yang mendengarkan atau menonton suatu acara"),
    ("autentik", "asli dan bisa dipercaya kebenarannya"),
    ("bakteri", "makhluk hidup bersel satu yang sangat kecil"),
    ("beban", "sesuatu yang harus ditanggung atau dikerjakan"),
    ("bencana", "peristiwa yang menimbulkan kerusakan atau kerugian besar"),
    ("berkembang", "bertambah besar, banyak, atau maju"),
    ("biaya", "uang yang perlu dikeluarkan untuk suatu keperluan"),
    ("budaya", "kebiasaan, nilai, dan hasil karya suatu masyarakat"),
    ("cahaya", "energi yang membuat mata bisa melihat"),
    ("canggih", "maju dan memiliki teknologi tinggi"),
    ("contoh", "sesuatu yang dipakai untuk menjelaskan hal lain"),
    ("dampak", "akibat yang ditimbulkan oleh suatu tindakan"),
    ("data", "keterangan atau fakta yang bisa diolah"),
    ("dedikasi", "kesetiaan dan kesungguhan dalam mengerjakan sesuatu"),
    ("definisi", "penjelasan tentang arti suatu kata atau istilah"),
    ("demokrasi", "sistem pemerintahan yang melibatkan rakyat dalam pengambilan keputusan"),
    ("desain", "rancangan bentuk atau susunan sesuatu"),
    ("diagnosis", "penentuan jenis penyakit berdasarkan pemeriksaan"),
    ("digital", "berkaitan dengan teknologi komputer dan sinyal angka"),
    ("dinamis", "terus berubah dan bergerak mengikuti keadaan"),
    ("diskusi", "percakapan untuk membahas suatu masalah bersama"),
    ("donasi", "pemberian sukarela untuk membantu orang lain"),
    ("efektif", "berhasil mencapai tujuan yang diinginkan"),
    ("efisien", "mencapai hasil terbaik dengan usaha atau biaya seminimal mungkin"),
    ("ekosistem", "hubungan antara makhluk hidup dan lingkungannya"),
    ("ekspresi", "perubahan wajah atau sikap untuk menunjukkan perasaan"),
    ("evaluasi", "penilaian terhadap sesuatu setelah diperiksa"),
    ("fakta", "hal yang benar-benar terjadi dan bisa dibuktikan"),
    ("fenomena", "peristiwa yang bisa diamati dan dijelaskan"),
    ("fleksibel", "mudah menyesuaikan diri dengan keadaan"),
    ("fungsi", "kegunaan atau peran sesuatu"),
    ("generasi", "kelompok orang yang hidup pada masa yang sama"),
    ("global", "mencakup seluruh dunia"),
    ("harmoni", "keadaan selaras dan tidak bertentangan"),
    ("hipotesis", "dugaan awal yang masih perlu diuji"),
    ("ide", "gagasan yang muncul dalam pikiran"),
    ("identitas", "ciri yang menunjukkan siapa atau apa sesuatu"),
    ("iklim", "keadaan rata-rata cuaca dalam waktu panjang"),
    ("ilustrasi", "gambar atau penjelasan untuk memperjelas sesuatu"),
    ("informasi", "keterangan tentang suatu hal"),
    ("inovasi", "gagasan atau cara baru yang memberi manfaat"),
    ("inspirasi", "dorongan yang membuat orang punya ide atau semangat baru"),
    ("interaksi", "hubungan saling memengaruhi antara dua pihak atau lebih"),
    ("interpretasi", "cara memahami atau menafsirkan sesuatu"),
    ("investasi", "penanaman modal untuk mendapatkan keuntungan di masa depan"),
    ("karakter", "sifat atau watak yang melekat pada seseorang"),
    ("karier", "perjalanan pekerjaan yang dijalani seseorang"),
    ("kategori", "kelompok yang disusun berdasarkan ciri tertentu"),
    ("kebijakan", "aturan atau arahan yang dibuat untuk mencapai tujuan"),
    ("koleksi", "kumpulan barang yang dikumpulkan dengan sengaja"),
    ("kompleks", "terdiri dari banyak bagian yang saling berkaitan"),
    ("komunikasi", "proses menyampaikan pesan antara dua pihak atau lebih"),
    ("konsep", "gambaran atau ide dasar tentang sesuatu"),
    ("konsisten", "tetap dan tidak berubah-ubah"),
    ("kreatif", "mampu menghasilkan ide atau karya baru"),
    ("kualitas", "tingkat baik buruknya sesuatu"),
    ("krisis", "keadaan sulit yang butuh penanganan segera"),
    ("literasi", "kemampuan membaca, menulis, dan memahami informasi"),
    ("logika", "cara berpikir yang masuk akal dan runtut"),
    ("manfaat", "kegunaan atau hal baik yang didapat"),
    ("media", "alat atau saluran untuk menyampaikan informasi"),
    ("metode", "cara yang teratur untuk melakukan sesuatu"),
    ("motivasi", "dorongan yang membuat seseorang mau bertindak"),
    ("negosiasi", "proses tawar-menawar untuk mencapai kesepakatan"),
    ("objektif", "melihat sesuatu berdasarkan fakta, bukan perasaan pribadi"),
    ("observasi", "kegiatan mengamati sesuatu secara langsung"),
    ("opini", "pendapat seseorang yang belum tentu berupa fakta"),
    ("peluang", "kesempatan yang bisa dimanfaatkan"),
    ("pemrograman", "kegiatan menulis instruksi agar komputer bisa bekerja"),
    ("pendidikan", "proses belajar untuk mengembangkan pengetahuan dan sikap"),
    ("populasi", "seluruh jumlah makhluk atau objek yang diteliti"),
    ("potensi", "kemampuan yang masih bisa dikembangkan"),
    ("prediksi", "perkiraan tentang hal yang akan terjadi"),
    ("prestasi", "hasil yang dicapai setelah berusaha"),
    ("prioritas", "hal yang didahulukan karena lebih penting"),
    ("prosedur", "langkah-langkah yang harus diikuti secara berurutan"),
    ("produktif", "mampu menghasilkan sesuatu dalam jumlah berarti"),
    ("profesional", "bekerja dengan standar dan tanggung jawab yang tinggi"),
    ("proses", "rangkaian langkah dari awal sampai akhir"),
    ("reaksi", "tanggapan terhadap suatu kejadian atau perlakuan"),
    ("referensi", "sumber yang dipakai sebagai rujukan"),
    ("relevan", "masih berkaitan dengan hal yang sedang dibahas"),
    ("reputasi", "penilaian orang lain terhadap nama baik seseorang atau lembaga"),
    ("risiko", "kemungkinan terjadinya hal buruk"),
    ("respons", "jawaban atau tanggapan terhadap sesuatu"),
    ("riset", "kegiatan mencari data dan fakta secara sistematis"),
    ("rutin", "dilakukan secara teratur dan berulang"),
    ("sains", "ilmu yang mempelajari alam melalui pengamatan dan percobaan"),
    ("sistem", "susunan bagian yang saling bekerja sama"),
    ("solusi", "cara untuk menyelesaikan masalah"),
    ("spesifik", "jelas dan terbatas pada hal tertentu"),
    ("strategi", "rencana yang disusun untuk mencapai tujuan"),
    ("struktur", "susunan bagian-bagian dalam suatu kesatuan"),
    ("subjektif", "dipengaruhi pendapat atau perasaan pribadi"),
    ("sukses", "berhasil mencapai tujuan yang diinginkan"),
    ("teknologi", "penerapan ilmu untuk membuat alat atau cara yang membantu manusia"),
    ("toleransi", "sikap menghargai perbedaan"),
    ("tradisi", "kebiasaan yang diwariskan dari generasi ke generasi"),
    ("transformasi", "perubahan bentuk atau keadaan secara menyeluruh"),
    ("transparan", "terbuka dan mudah diketahui oleh semua pihak"),
    ("valid", "sah dan bisa diterima kebenarannya"),
    ("variasi", "perbedaan bentuk atau jenis dalam satu kelompok"),
    ("virtual", "ada dalam dunia komputer, bukan dalam bentuk fisik"),
    ("wawasan", "pengetahuan dan pemahaman yang luas"),
    ("wilayah", "daerah yang menjadi bagian suatu negara atau pemerintahan"),
    ("zona", "daerah dengan batas dan ciri tertentu"),
]

# --------------------------------------------------------------------------- #
# Terjemahan: (Indonesia, Inggris)
# --------------------------------------------------------------------------- #
TRANSLATIONS = [
    ("rumah", "house"), ("makan", "eat"), ("minum", "drink"), ("tidur", "sleep"),
    ("bangun", "wake up"), ("pergi", "go"), ("datang", "come"), ("lihat", "see"),
    ("dengar", "hear"), ("bicara", "speak"), ("tulis", "write"), ("baca", "read"),
    ("belajar", "study"), ("kerja", "work"), ("main", "play"), ("beli", "buy"),
    ("jual", "sell"), ("beri", "give"), ("ambil", "take"), ("buat", "make"),
    ("makanan", "food"), ("minuman", "beverage"), ("air", "water"), ("nasi", "rice"),
    ("roti", "bread"), ("susu", "milk"), ("telur", "egg"), ("ayam", "chicken"),
    ("ikan", "fish"), ("daging", "meat"), ("buah", "fruit"), ("sayur", "vegetable"),
    ("manis", "sweet"), ("asin", "salty"), ("pedas", "spicy"), ("pahit", "bitter"),
    ("asam", "sour"), ("panas", "hot"), ("dingin", "cold"), ("besar", "big"),
    ("kecil", "small"), ("tinggi", "tall"), ("pendek", "short"), ("panjang", "long"),
    ("cepat", "fast"), ("lambat", "slow"), ("baru", "new"), ("lama", "long time"),
    ("muda", "young"), ("tua", "old"), ("baik", "good"), ("buruk", "bad"),
    ("senang", "happy"), ("sedih", "sad"), ("marah", "angry"), ("takut", "afraid"),
    ("lelah", "tired"), ("lapar", "hungry"), ("haus", "thirsty"), ("sekolah", "school"),
    ("kantor", "office"), ("pasar", "market"), ("toko", "shop"), ("jalan", "road"),
    ("kota", "city"), ("desa", "village"), ("negara", "country"), ("kamar", "room"),
    ("dapur", "kitchen"), ("pintu", "door"), ("jendela", "window"), ("meja", "table"),
    ("kursi", "chair"), ("buku", "book"), ("pensil", "pencil"), ("kertas", "paper"),
    ("tas", "bag"), ("baju", "shirt"), ("celana", "pants"), ("sepatu", "shoes"),
    ("topi", "hat"), ("jam", "clock"), ("uang", "money"), ("harga", "price"),
    ("murah", "cheap"), ("mahal", "expensive"), ("mobil", "car"), ("motor", "motorcycle"),
    ("sepeda", "bicycle"), ("bus", "bus"), ("kereta", "train"), ("pesawat", "airplane"),
    ("kapal", "ship"), ("ayah", "father"), ("ibu", "mother"), ("kakak", "older sibling"),
    ("adik", "younger sibling"), ("teman", "friend"), ("guru", "teacher"), ("murid", "student"),
    ("dokter", "doctor"), ("polisi", "police"), ("petani", "farmer"), ("hari", "day"),
    ("minggu", "week"), ("bulan", "month"), ("tahun", "year"), ("pagi", "morning"),
    ("siang", "afternoon"), ("sore", "late afternoon"), ("malam", "night"),
    ("sekarang", "now"), ("besok", "tomorrow"), ("kemarin", "yesterday"),
    ("merah", "red"), ("biru", "blue"), ("hijau", "green"), ("kuning", "yellow"),
    ("hitam", "black"), ("putih", "white"), ("satu", "one"), ("dua", "two"),
    ("tiga", "three"), ("empat", "four"), ("lima", "five"), ("sepuluh", "ten"),
    ("seratus", "one hundred"), ("kucing", "cat"), ("anjing", "dog"), ("burung", "bird"),
    ("sapi", "cow"), ("kambing", "goat"), ("bunga", "flower"), ("pohon", "tree"),
    ("hujan", "rain"), ("angin", "wind"), ("matahari", "sun"), ("bintang", "star"),
    ("langit", "sky"), ("laut", "sea"), ("gunung", "mountain"), ("sungai", "river"),
    ("danau", "lake"), ("tanah", "land"), ("api", "fire"), ("batu", "stone"),
    ("pasir", "sand"), ("awan", "cloud"),
]

# --------------------------------------------------------------------------- #
# Kata baku: (salah, benar, catatan)
# --------------------------------------------------------------------------- #
TYPO_PAIRS = [
    ("ijin", "izin", "bentuk baku menurut KBBI adalah 'izin'"),
    ("jaman", "zaman", "kata baku memakai 'z', bukan 'j'"),
    ("aktifitas", "aktivitas", "bentuk bakunya 'aktivitas'"),
    ("apotik", "apotek", "bentuk bakunya 'apotek'"),
    ("antri", "antre", "bentuk bakunya 'antre'"),
    ("atlit", "atlet", "bentuk bakunya 'atlet'"),
    ("analisa", "analisis", "bentuk bakunya 'analisis'"),
    ("cendikiawan", "cendekiawan", "bentuk bakunya 'cendekiawan'"),
    ("diagnosa", "diagnosis", "bentuk bakunya 'diagnosis'"),
    ("disain", "desain", "bentuk bakunya 'desain'"),
    ("ekstrim", "ekstrem", "bentuk bakunya 'ekstrem'"),
    ("hapal", "hafal", "bentuk bakunya 'hafal'"),
    ("hakekat", "hakikat", "bentuk bakunya 'hakikat'"),
    ("himbau", "imbau", "bentuk bakunya 'imbau'"),
    ("ijasah", "ijazah", "bentuk bakunya 'ijazah'"),
    ("karir", "karier", "bentuk bakunya 'karier'"),
    ("komplit", "komplet", "bentuk bakunya 'komplet'"),
    ("kongkrit", "konkret", "bentuk bakunya 'konkret'"),
    ("kwalitas", "kualitas", "bentuk bakunya 'kualitas'"),
    ("kwantitas", "kuantitas", "bentuk bakunya 'kuantitas'"),
    ("kwitansi", "kuitansi", "bentuk bakunya 'kuitansi'"),
    ("lapal", "lafal", "bentuk bakunya 'lafal'"),
    ("lembab", "lembap", "bentuk bakunya 'lembap'"),
    ("mahkluk", "makhluk", "bentuk bakunya 'makhluk'"),
    ("merubah", "mengubah", "bentuk bakunya 'mengubah'"),
    ("metoda", "metode", "bentuk bakunya 'metode'"),
    ("nafas", "napas", "bentuk bakunya 'napas'"),
    ("nasehat", "nasihat", "bentuk bakunya 'nasihat'"),
    ("negri", "negeri", "bentuk bakunya 'negeri'"),
    ("obyek", "objek", "bentuk bakunya 'objek'"),
    ("praktek", "praktik", "bentuk bakunya 'praktik'"),
    ("propinsi", "provinsi", "bentuk bakunya 'provinsi'"),
    ("resiko", "risiko", "bentuk bakunya 'risiko'"),
    ("silahkan", "silakan", "bentuk bakunya 'silakan'"),
    ("sekedar", "sekadar", "bentuk bakunya 'sekadar'"),
    ("subyek", "subjek", "bentuk bakunya 'subjek'"),
    ("tekhnik", "teknik", "bentuk bakunya 'teknik'"),
    ("telpon", "telepon", "bentuk bakunya 'telepon'"),
    ("type", "tipe", "bentuk bakunya 'tipe'"),
    ("frustasi", "frustrasi", "bentuk bakunya 'frustrasi'"),
    ("frekwensi", "frekuensi", "bentuk bakunya 'frekuensi'"),
    ("goncang", "guncang", "bentuk bakunya 'guncang'"),
    ("karna", "karena", "bentuk bakunya 'karena'"),
    ("bilyard", "biliar", "bentuk bakunya 'biliar'"),
    ("jumat", "Jumat", "nama hari ditulis dengan huruf kapital di awal"),
    ("seksama", "saksama", "bentuk bakunya 'saksama'"),
    ("standard", "standar", "bentuk bakunya 'standar'"),
    ("sistim", "sistem", "bentuk bakunya 'sistem'"),
    ("teoritis", "teoretis", "bentuk bakunya 'teoretis'"),
    ("mempengaruhi", "memengaruhi", "bentuk bakunya 'memengaruhi'"),
]

# --------------------------------------------------------------------------- #
# Peribahasa: (peribahasa, arti)
# --------------------------------------------------------------------------- #
PROVERBS = [
    ("air beriak tanda tak dalam", "orang yang banyak bicara biasanya ilmunya belum dalam"),
    ("ada udang di balik batu", "ada maksud tersembunyi di balik suatu tindakan"),
    ("bagai air di daun talas", "orang yang tidak punya pendirian tetap"),
    ("bagai pinang dibelah dua", "dua orang yang sangat mirip satu sama lain"),
    ("besar pasak daripada tiang", "pengeluaran lebih besar daripada pemasukan"),
    ("berat sama dipikul, ringan sama dijinjing", "susah dan senang dijalani bersama"),
    ("buah jatuh tidak jauh dari pohonnya", "sifat anak biasanya mirip orang tuanya"),
    ("cepat kaki ringan tangan", "suka menolong orang lain"),
    ("habis manis sepah dibuang", "setelah tidak berguna lalu ditinggalkan"),
    ("ibarat menegakkan benang basah", "mengerjakan sesuatu yang mustahil berhasil"),
    ("jauh di mata, dekat di hati", "meski berjauhan, tetap dekat di hati"),
    ("kacang lupa kulitnya", "lupa asal-usul atau lupa diri setelah berhasil"),
    ("kalah jadi abu, menang jadi arang", "pertengkaran selalu merugikan kedua pihak"),
    ("karena nila setitik rusak susu sebelanga", "satu kesalahan kecil bisa merusak semuanya"),
    ("malu bertanya sesat di jalan", "jangan malu bertanya supaya tidak salah langkah"),
    ("nasi sudah menjadi bubur", "sesuatu sudah terlanjur terjadi dan tidak bisa diubah"),
    ("pucuk dicinta ulam pun tiba", "mendapat sesuatu yang memang diinginkan"),
    ("rajin pangkal pandai", "orang yang rajin akan menjadi pandai"),
    ("sambil menyelam minum air", "mengerjakan dua hal sekaligus dalam satu kesempatan"),
    ("sekali mendayung, dua tiga pulau terlampaui", "satu tindakan bisa memberi banyak manfaat"),
    ("tong kosong nyaring bunyinya", "orang yang tidak banyak tahu justru banyak bicara"),
    ("tak kenal maka tak sayang", "perlu saling mengenal sebelum menyayangi"),
    ("tidak ada asap tanpa api", "setiap kejadian pasti ada sebabnya"),
    ("air susu dibalas air tuba", "kebaikan dibalas dengan kejahatan"),
    ("alah bisa karena biasa", "sesuatu menjadi mudah karena sering dilakukan"),
    ("bermain api akan terbakar", "melakukan hal berbahaya akan terkena akibatnya"),
    ("dalam laut bisa diduga, dalam hati siapa tahu", "isi hati manusia sulit ditebak"),
    ("gajah mati meninggalkan gading", "orang besar meninggalkan jasa yang dikenang"),
    ("harimau mati meninggalkan belang", "orang meninggalkan nama baik atau buruk setelah pergi"),
    ("ilmu padi semakin berisi semakin merunduk", "semakin berilmu seseorang, semakin rendah hati"),
    ("lain ladang lain belalang", "adat dan kebiasaan berbeda di setiap tempat"),
    ("membuang garam ke laut", "melakukan sesuatu yang sia-sia"),
    ("menepuk air di dulang, terpercik ke muka sendiri", "membuka aib sendiri di depan orang"),
    ("seperti katak dalam tempurung", "orang yang wawasannya sempit"),
    ("sudah jatuh tertimpa tangga", "kesialan yang datang bertumpuk"),
    ("tangan mencencang bahu memikul", "harus siap menanggung akibat perbuatan sendiri"),
    ("sedap jangan ditelan, pahit jangan dimuntahkan", "pertimbangkan baik-baik sebelum memutuskan"),
]

# --------------------------------------------------------------------------- #
# Aturan bahasa: (pertanyaan, jawaban)
# --------------------------------------------------------------------------- #
GRAMMAR = [
    ("kapan 'di' ditulis terpisah dan kapan digabung?",
     "'Di' ditulis terpisah kalau menunjukkan tempat, contohnya 'di rumah' dan 'di sekolah'. 'Di' ditulis gabung kalau berfungsi sebagai awalan pembentuk kata kerja pasif, contohnya 'ditulis', 'dibaca', dan 'dibawa'."),
    ("kapan 'pun' ditulis terpisah?",
     "'Pun' ditulis terpisah kalau bermakna 'juga', contohnya 'aku pun ikut'. Kalau sudah menjadi bagian kata, penulisannya digabung, seperti 'meskipun', 'walaupun', dan 'kendatipun'."),
    ("bagaimana penulisan kata 'dimana' yang benar?",
     "Bentuk baku yang benar adalah 'di mana', ditulis terpisah. Contoh: 'di mana kamu tinggal?'. Kata 'dimana' tanpa spasi termasuk bentuk tidak baku."),
    ("bagaimana penulisan 'Rp' yang benar?",
     "Rp ditulis tanpa spasi dengan angkanya, misalnya Rp10.000 dan Rp2.500.000. Untuk nilai di bawah seribu tetap ditulis lengkap, contohnya Rp500."),
    ("apakah angka boleh ditulis di awal kalimat?",
     "Angka sebaiknya tidak ditulis di awal kalimat. Kalau terpaksa, tulis dengan huruf, contohnya 'Dua puluh siswa ikut lomba' bukan '20 siswa ikut lomba'."),
    ("bagaimana penulisan tanggal yang benar?",
     "Tanggal ditulis dengan urutan hari, bulan, tahun, contohnya 17 Agustus 1945. Nama bulan memakai huruf kapital di awal."),
    ("kapan huruf kapital dipakai?",
     "Huruf kapital dipakai di awal kalimat, pada nama orang, nama tempat, nama hari, nama bulan, dan gelar yang mengikuti nama. Contohnya 'Budi tinggal di Magelang sejak Senin'."),
    ("bagaimana penulisan kata ulang yang benar?",
     "Kata ulang ditulis dengan tanda hubung, contohnya 'anak-anak', 'buku-buku', dan 'sayur-sayuran'. Jangan menulisnya dengan angka seperti 'anak2' dalam tulisan resmi."),
    ("kapan tanda koma dipakai sebelum 'tetapi'?",
     "Tanda koma dipakai sebelum kata penghubung pertentangan seperti 'tetapi', 'melainkan', dan 'sedangkan' pada kalimat majemuk. Contoh: 'Aku ingin pergi, tetapi hujan turun'."),
    ("bagaimana penulisan singkatan 'dan lain-lain'?",
     "Bentuk lengkapnya 'dan lain-lain', sedangkan singkatannya 'dll.' yang ditulis dengan titik. Jangan mencampur keduanya menjadi 'dan dll'."),
    ("bagaimana penulisan 'terima kasih'?",
     "'Terima kasih' ditulis terpisah karena terdiri dari dua kata. Bentuk 'terimakasih' yang digabung tidak baku."),
    ("bagaimana penulisan 'barang siapa'?",
     "Bentuk baku menurut KBBI adalah 'barangsiapa', ditulis serangkai. Contoh: 'barangsiapa terlambat tidak boleh masuk'."),
    ("bagaimana penulisan 'antar kota'?",
     "Bentuk baku adalah 'antarkota', ditulis serangkai tanpa spasi. Awalan 'antar-' dirangkai dengan kata berikutnya, seperti 'antarprovinsi' dan 'antarsekolah'."),
    ("bagaimana penulisan 'pasca'?",
     "Awalan 'pasca-' ditulis serangkai, contohnya 'pascasarjana', 'pascapanen', dan 'pascabencana'."),
    ("bagaimana penulisan 'non'?",
     "Awalan 'non-' ditulis serangkai dengan kata berikutnya, contohnya 'nonfiksi', 'nonformal', dan 'nonaktif'."),
    ("bagaimana penulisan 'anti'?",
     "Awalan 'anti-' ditulis serangkai, contohnya 'antikorupsi', 'antibiotik', dan 'antipanas'."),
    ("bagaimana penulisan 'maha'?",
     "Awalan 'maha-' ditulis serangkai, contohnya 'mahasiswa', 'mahakuasa', dan 'mahabesar'."),
    ("bagaimana cara menulis persen yang benar?",
     "Persen bisa ditulis dengan lambang '%' tanpa spasi, contohnya 50%, atau dengan kata 'persen' setelah angka, contohnya 50 persen. Pilih salah satu dan jangan dicampur dalam satu kalimat."),
    ("bagaimana penulisan 'silahkan' yang benar?",
     "Bentuk baku adalah 'silakan', bukan 'silahkan'. Contoh: 'silakan duduk'."),
    ("bagaimana penulisan 'praktek' yang benar?",
     "Bentuk baku menurut KBBI adalah 'praktik'. Contoh: 'praktik kerja lapangan'."),
    ("bagaimana penulisan 'ijin' yang benar?",
     "Bentuk baku adalah 'izin'. Kata 'ijin' termasuk bentuk tidak baku dan sebaiknya dihindari dalam tulisan resmi."),
    ("bagaimana penulisan 'jaman' yang benar?",
     "Bentuk baku adalah 'zaman', memakai huruf z. Contoh: 'zaman dahulu'."),
    ("bagaimana penulisan 'merubah' yang benar?",
     "Bentuk baku adalah 'mengubah'. Imbuhan me- bertemu kata 'ubah' berubah menjadi 'meng-', bukan 'me-'."),
    ("bagaimana penulisan 'mempengaruhi' yang benar?",
     "Bentuk baku adalah 'memengaruhi', tanpa huruf p setelah me-. Kata dasarnya 'pengaruh', lalu mendapat imbuhan me- menjadi 'memengaruhi'."),
    ("bagaimana penulisan 'nafas' yang benar?",
     "Bentuk baku adalah 'napas', memakai huruf p. Contoh: 'menarik napas dalam-dalam'."),
    ("bagaimana penulisan 'resiko' yang benar?",
     "Bentuk baku adalah 'risiko'. Contoh: 'risiko kecelakaan'."),
    ("bagaimana penulisan 'obyek' yang benar?",
     "Bentuk baku adalah 'objek'. Kata 'subjek' juga memakai j, bukan y."),
    ("bagaimana penulisan 'propinsi' yang benar?",
     "Bentuk baku adalah 'provinsi', memakai v. Contoh: 'Provinsi Jawa Tengah'."),
    ("bagaimana penulisan 'apotik' yang benar?",
     "Bentuk baku adalah 'apotek'. Contoh: 'membeli obat di apotek'."),
    ("bagaimana penulisan 'analisa' yang benar?",
     "Bentuk baku adalah 'analisis'. Contoh: 'analisis data'."),
    ("bagaimana penulisan 'aktifitas' yang benar?",
     "Bentuk baku adalah 'aktivitas', memakai v. Contoh: 'aktivitas sehari-hari'."),
    ("bagaimana penulisan 'himbau' yang benar?",
     "Bentuk baku adalah 'imbau', tanpa huruf h di depan. Contoh: 'imbauan pemerintah'."),
    ("bagaimana penulisan 'kwitansi' yang benar?",
     "Bentuk baku adalah 'kuitansi'. Contoh: 'simpan kuitansi pembayaran'."),
    ("bagaimana penulisan 'tehnik' yang benar?",
     "Bentuk baku adalah 'teknik', tanpa huruf h. Contoh: 'teknik memasak'."),
    ("bagaimana penulisan 'jumat' yang benar?",
     "Nama hari ditulis dengan huruf kapital di awal, yaitu 'Jumat'. Contoh: 'hari Jumat'."),
    ("bagaimana penulisan 'senin' yang benar?",
     "Nama hari ditulis dengan huruf kapital di awal, yaitu 'Senin'. Contoh: 'hari Senin'."),
    ("bagaimana penulisan 'agustus' yang benar?",
     "Nama bulan ditulis dengan huruf kapital di awal, yaitu 'Agustus'. Contoh: '17 Agustus 1945'."),
    ("bagaimana penulisan kalimat tanya yang benar?",
     "Kalimat tanya diakhiri tanda tanya, bukan titik. Contoh: 'kamu sudah makan?' dan 'di mana rumahmu?'."),
    ("bagaimana penulisan kutipan langsung?",
     "Kutipan langsung ditulis di antara tanda petik, contohnya dia berkata, \"aku akan datang besok\". Tanda petik pembuka dan penutup harus lengkap."),
    ("apa itu kalimat efektif?",
     "Kalimat efektif adalah kalimat yang jelas, singkat, dan tidak berlebihan. Contoh yang kurang efektif: 'para siswa-siswa'. Bentuk efektifnya 'para siswa' atau 'siswa-siswa'."),
    ("bagaimana penulisan 'para siswa-siswa'?",
     "Bentuk itu berlebihan karena 'para' sudah menunjukkan jamak. Pilih 'para siswa' atau 'siswa-siswa', jangan dipakai bersamaan."),
    ("kapan memakai 'ke' dan 'kepada'?",
     "'Ke' dipakai untuk arah atau tempat, contohnya 'pergi ke pasar'. 'Kepada' dipakai untuk orang, contohnya 'memberi hadiah kepada teman'."),
    ("kapan memakai 'dari' dan 'daripada'?",
     "'Dari' dipakai untuk asal tempat atau waktu, contohnya 'dari rumah'. 'Daripada' dipakai untuk perbandingan, contohnya 'lebih tinggi daripada'."),
    ("bagaimana penulisan 'di rumah' dan 'dirumah'?",
     "Yang benar adalah 'di rumah', ditulis terpisah karena 'di' menunjukkan tempat. Bentuk 'dirumah' tidak baku."),
    ("bagaimana penulisan 'ke pasar' dan 'kepasar'?",
     "Yang benar adalah 'ke pasar', ditulis terpisah karena 'ke' menunjukkan arah. Bentuk 'kepasar' tidak baku."),
    ("bagaimana penulisan angka ribuan?",
     "Angka ribuan memakai titik sebagai pemisah, contohnya 1.000, 25.000, dan 1.250.000. Jangan memakai koma untuk pemisah ribuan dalam format Indonesia."),
    ("bagaimana penulisan desimal yang benar?",
     "Desimal memakai koma, contohnya 2,5 dan 0,75. Titik dipakai untuk ribuan, jadi jangan dibalik."),
]


def _add_synonyms(b: Builder) -> None:
    for word, syn, note in SYNONYMS:
        key = f"sinonim-{word}"
        question = b.pick(
            [
                "sinonim dari '{w}' apa?",
                "'{w}' kira-kira sama artinya dengan kata apa?",
                "persamaan kata '{w}' apa ya?",
                "kasih tahu sinonim '{w}' dong",
            ],
            key,
        ).format(w=word)
        answer = b.pick(
            [
                f"Sinonim '{word}' adalah '{syn}'. Dua kata ini {note}, jadi sering bisa dipakai bergantian.",
                f"'{word}' bersinonim dengan '{syn}'. Keduanya {note}, meskipun nuansanya bisa sedikit berbeda tergantung kalimat.",
                f"Persamaan kata '{word}' adalah '{syn}'. Dalam banyak kalimat, keduanya {note}.",
            ],
            key,
        )
        b.add(question, answer, "bahasa", fact=key)


def _add_antonyms(b: Builder) -> None:
    for word, ant, note in ANTONYMS:
        key = f"antonim-{word}-{ant}"
        question = b.pick(
            [
                "lawan kata '{w}' apa?",
                "antonim dari '{w}' apa ya?",
                "'{w}' berlawanan dengan kata apa?",
                "kasih tahu lawan kata '{w}' dong",
            ],
            key,
        ).format(w=word)
        answer = b.pick(
            [
                f"Lawan kata '{word}' adalah '{ant}', karena {note}. Jadi keduanya dipakai untuk hal yang bertolak belakang.",
                f"Antonim '{word}' adalah '{ant}'. Keduanya {note}, makanya sering muncul sebagai pasangan lawan kata.",
                f"'{word}' berlawanan dengan '{ant}'. Dua kata ini {note} dan tidak bisa dipakai untuk hal yang sama.",
            ],
            key,
        )
        b.add(question, answer, "bahasa", fact=key)


def _add_meanings(b: Builder) -> None:
    for word, meaning in MEANINGS:
        key = f"arti-{word}"
        question = b.pick(
            [
                "arti kata '{w}' apa?",
                "'{w}' itu apa sih maksudnya?",
                "apa arti '{w}'?",
                "jelaskan arti kata '{w}' dong",
            ],
            key,
        ).format(w=word)
        answer = b.pick(
            [
                f"Kata '{word}' berarti {meaning}. Itu arti yang paling umum dipakai sehari-hari.",
                f"'{word}' artinya {meaning}. Kalau dipakai dalam kalimat, maknanya mengikuti konteks pembicaraan.",
                f"Arti '{word}' adalah {meaning}. Jadi kata ini menggambarkan hal tersebut.",
            ],
            key,
        )
        b.add(question, answer, "bahasa", fact=key)


def _add_translations(b: Builder) -> None:
    for indo, eng in TRANSLATIONS:
        key = f"terjemah-id-en-{indo}"
        question = b.pick(
            [
                "bahasa Inggris dari '{w}' apa?",
                "'{w}' kalau dalam bahasa Inggris disebut apa?",
                "gimana bilang '{w}' dalam bahasa Inggris?",
            ],
            key,
        ).format(w=indo)
        answer = b.pick(
            [
                f"'{indo}' dalam bahasa Inggris adalah '{eng}'. Kosakata ini termasuk yang sering dipakai sehari-hari.",
                f"Bahasa Inggris dari '{indo}' adalah '{eng}'. Kalau dipakai dalam kalimat, bentuknya bisa berubah mengikuti tata bahasa.",
                f"'{indo}' biasa diterjemahkan menjadi '{eng}'. Artinya tetap sama, cuma bahasanya yang berbeda.",
            ],
            key,
        )
        b.add(question, answer, "bahasa", fact=key, allow_english=True)

        key2 = f"terjemah-en-id-{eng}"
        question2 = b.pick(
            [
                "bahasa Indonesia dari '{w}' apa?",
                "'{w}' dalam bahasa Indonesia artinya apa?",
                "kalau '{w}' diterjemahkan ke bahasa Indonesia jadi apa?",
            ],
            key2,
        ).format(w=eng)
        answer2 = b.pick(
            [
                f"'{eng}' dalam bahasa Indonesia berarti '{indo}'. Itu bentuk yang paling umum dipakai.",
                f"Bahasa Indonesia dari '{eng}' adalah '{indo}'. Bisa dipakai untuk percakapan sehari-hari.",
                f"'{eng}' kalau diterjemahkan menjadi '{indo}'. Maknanya sama, hanya bahasanya yang berganti.",
            ],
            key2,
        )
        b.add(question2, answer2, "bahasa", fact=key2, allow_english=True)


def _add_typos(b: Builder) -> None:
    for wrong, right, note in TYPO_PAIRS:
        key = f"baku-{wrong}"
        question = b.pick(
            [
                "mana yang benar, '{w}' atau '{r}'?",
                "penulisan yang baku itu '{w}' atau '{r}'?",
                "'{w}' bener nggak sih, atau harusnya '{r}'?",
            ],
            key,
        ).format(w=wrong, r=right)
        answer = b.pick(
            [
                f"Yang benar '{right}', karena {note}. Jadi kalau menulis kalimat resmi, pakai bentuk '{right}'.",
                f"Bentuk baku yang tepat adalah '{right}', sebab {note}. Kata '{wrong}' sebaiknya dihindari dalam tulisan formal.",
                f"'{right}' yang baku. {note.capitalize()}, sedangkan '{wrong}' tidak termasuk bentuk baku.",
            ],
            key,
        )
        b.add(question, answer, "bahasa", fact=key)


def _add_proverbs(b: Builder) -> None:
    for proverb, meaning in PROVERBS:
        key = f"peribahasa-{proverb}"
        question = b.pick(
            [
                "arti peribahasa '{p}' apa?",
                "'{p}' maksudnya apa ya?",
                "jelaskan makna peribahasa '{p}'",
            ],
            key,
        ).format(p=proverb)
        answer = b.pick(
            [
                f"Peribahasa '{proverb}' berarti {meaning}. Biasanya dipakai untuk memberi nasihat atau sindiran halus.",
                f"Maknanya, {meaning}. Orang memakai peribahasa '{proverb}' supaya pesannya terdengar lebih halus.",
                f"'{proverb}' menggambarkan keadaan ketika {meaning}. Itu pesan yang ingin disampaikan.",
            ],
            key,
        )
        b.add(question, answer, "bahasa", fact=key)


def _add_grammar(b: Builder) -> None:
    for i, (question, answer) in enumerate(GRAMMAR):
        b.add(question, answer, "bahasa", fact=f"tata-bahasa-{i}")


def build_language_content(b: Builder) -> None:
    _add_synonyms(b)
    _add_antonyms(b)
    _add_meanings(b)
    _add_translations(b)
    _add_typos(b)
    _add_proverbs(b)
    _add_grammar(b)
