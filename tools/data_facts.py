"""Pengetahuan teknologi, kesehatan, sains, kewarganegaraan, olahraga,
lingkungan, panduan praktis, dan tanya-jawab umum.
"""
from __future__ import annotations

from nara_core import Builder

TECH = [
    ("internet", "jaringan komputer global yang menghubungkan miliaran perangkat", "membuka situs web dan mengirim pesan"),
    ("CPU", "unit pemrosesan utama yang menjalankan instruksi program", "prosesor di komputer atau ponsel"),
    ("RAM", "memori sementara yang menyimpan data saat program berjalan", "memori 8 GB di laptop"),
    ("ROM", "memori permanen yang menyimpan instruksi dasar perangkat", "chip firmware di ponsel"),
    ("hard disk", "media penyimpanan magnetik untuk data berukuran besar", "disk 1 TB di komputer"),
    ("SSD", "penyimpanan digital tanpa bagian bergerak yang lebih cepat dari hard disk", "SSD 512 GB di laptop"),
    ("sistem operasi", "perangkat lunak yang mengatur perangkat keras dan program lain", "Windows, Linux, dan Android"),
    ("aplikasi", "program yang dibuat untuk membantu pekerjaan pengguna", "aplikasi pesan dan pengolah kata"),
    ("browser", "program untuk membuka dan menampilkan halaman web", "Chrome dan Firefox"),
    ("server", "komputer yang melayani permintaan dari komputer lain", "server situs web"),
    ("klien", "perangkat atau program yang meminta layanan dari server", "ponsel saat membuka situs"),
    ("database", "kumpulan data yang disimpan dan diatur agar mudah dicari", "basis data pelanggan toko"),
    ("algoritma", "urutan langkah yang jelas untuk menyelesaikan masalah", "langkah mencari angka terbesar"),
    ("bahasa pemrograman", "bahasa yang dipakai untuk menulis instruksi bagi komputer", "Python dan JavaScript"),
    ("variabel", "wadah untuk menyimpan nilai dalam program", "nama = 'Nara'"),
    ("fungsi", "blok kode yang bisa dipanggil untuk menjalankan tugas tertentu", "fungsi menghitung luas"),
    ("loop", "perulangan untuk menjalankan kode berkali-kali", "for dan while"),
    ("debugging", "proses mencari dan memperbaiki kesalahan pada program", "memeriksa pesan error"),
    ("API", "antarmuka yang memungkinkan dua program saling berkomunikasi", "API cuaca dan API pembayaran"),
    ("cloud computing", "penggunaan sumber daya komputer lewat internet", "menyimpan file di layanan awan"),
    ("kecerdasan buatan", "sistem komputer yang bisa meniru kemampuan berpikir manusia", "chatbot dan pengenal gambar"),
    ("machine learning", "cabang kecerdasan buatan yang membuat komputer belajar dari data", "rekomendasi film"),
    ("jaringan saraf tiruan", "model komputasi yang terinspirasi dari cara kerja neuron", "pengenal wajah"),
    ("chatbot", "program yang bisa bercakap-cakap dengan pengguna", "asisten virtual"),
    ("token", "potongan teks yang diproses model bahasa", "kata atau bagian kata"),
    ("enkripsi", "proses mengubah data agar tidak bisa dibaca tanpa kunci", "pesan terenkripsi"),
    ("password", "kata sandi untuk membuktikan hak akses", "kombinasi huruf dan angka"),
    ("phishing", "penipuan yang menyamar sebagai pihak resmi untuk mencuri data", "email palsu minta password"),
    ("malware", "program berbahaya yang merusak atau mencuri data", "virus dan trojan"),
    ("firewall", "sistem yang menyaring lalu lintas jaringan", "memblokir koneksi mencurigakan"),
    ("VPN", "jaringan pribadi virtual yang mengenkripsi koneksi", "VPN saat memakai Wi-Fi umum"),
    ("domain", "nama alamat situs web", "contoh.com"),
    ("URL", "alamat lengkap sebuah halaman web", "https://contoh.com/halaman"),
    ("HTML", "bahasa markup untuk menyusun isi halaman web", "tag judul dan paragraf"),
    ("CSS", "bahasa untuk mengatur tampilan halaman web", "warna dan ukuran huruf"),
    ("JavaScript", "bahasa pemrograman yang membuat halaman web interaktif", "tombol yang merespons klik"),
    ("Python", "bahasa pemrograman yang mudah dibaca dan sering dipakai pemula", "skrip pengolah data"),
    ("Git", "sistem pengontrol versi untuk melacak perubahan kode", "commit dan branch"),
    ("repository", "tempat menyimpan kode dan riwayat perubahannya", "repositori di GitHub"),
    ("open source", "perangkat lunak yang kode sumbernya bisa dilihat dan diubah", "Linux dan Firefox"),
    ("backup", "salinan data untuk berjaga-jaga kalau data asli hilang", "cadangan di hard disk eksternal"),
    ("cache", "penyimpanan sementara agar data bisa diakses lebih cepat", "cache browser"),
    ("cookie", "data kecil yang disimpan situs di browser", "menyimpan status login"),
    ("bandwidth", "kapasitas maksimum data yang bisa lewat dalam jaringan", "bandwidth 100 Mbps"),
    ("IP address", "alamat numerik yang menandai perangkat di jaringan", "192.168.1.1"),
]

HEALTH = [
    ("minum air cukup", "Minum sekitar 8 gelas air sehari, atau lebih kalau banyak beraktivitas. Air membantu menjaga suhu tubuh dan melancarkan pencernaan."),
    ("tidur cukup", "Usahakan tidur 7 sampai 9 jam setiap malam. Tidur cukup membantu daya ingat, suasana hati, dan daya tahan tubuh."),
    ("cuci tangan", "Cuci tangan dengan sabun dan air mengalir minimal 20 detik. Lakukan sebelum makan dan setelah dari toilet."),
    ("sikat gigi", "Sikat gigi dua kali sehari, pagi setelah sarapan dan malam sebelum tidur. Jangan lupa membersihkan sela gigi."),
    ("olahraga rutin", "Lakukan aktivitas fisik minimal 30 menit sehari, lima kali seminggu. Mulailah dari jalan cepat atau bersepeda."),
    ("sarapan", "Sarapan memberi energi untuk memulai hari. Pilih makanan yang mengandung karbohidrat, protein, dan serat."),
    ("makan buah dan sayur", "Usahakan makan buah dan sayur setiap hari. Keduanya mengandung vitamin, mineral, dan serat yang dibutuhkan tubuh."),
    ("batasi gula", "Kurangi minuman manis dan makanan tinggi gula. Konsumsi gula berlebih berkaitan dengan risiko diabetes dan obesitas."),
    ("batasi garam", "Batasi garam agar tekanan darah tetap terkendali. Perhatikan juga garam tersembunyi di makanan kemasan."),
    ("hindari rokok", "Rokok berbahaya bagi perokok dan orang di sekitarnya. Berhenti merokok memberi manfaat kesehatan sejak hari pertama."),
    ("kelola stres", "Atur waktu istirahat dan lakukan hal yang menyenangkan. Cerita ke orang yang dipercaya juga bisa membantu mengurangi stres."),
    ("cek kesehatan rutin", "Periksa kesehatan secara berkala, terutama tekanan darah dan gula darah. Deteksi dini membuat penanganan lebih mudah."),
    ("imunisasi", "Ikuti jadwal imunisasi yang dianjurkan. Vaksin membantu tubuh mengenali dan melawan penyakit tertentu."),
    ("demam", "Istirahat yang cukup dan minum air lebih banyak. Kalau demam tinggi atau berlangsung lama, segera periksa ke dokter."),
    ("batuk", "Minum air hangat dan istirahat. Batuk yang disertai sesak napas atau darah perlu segera diperiksa."),
    ("flu", "Flu biasanya membaik dengan istirahat dan cairan. Tutup mulut saat bersin agar tidak menular ke orang lain."),
    ("diare", "Ganti cairan yang hilang dengan oralit. Kalau diare parah atau berdarah, segera cari bantuan medis."),
    ("luka ringan", "Bersihkan luka dengan air mengalir, lalu tutup dengan plester. Ganti plester secara teratur."),
    ("luka bakar", "Alirkan air dingin pada luka bakar selama beberapa menit. Jangan beri pasta gigi atau mentega."),
    ("mimisan", "Duduk tegak dan condongkan kepala sedikit ke depan. Tekan bagian lunak hidung selama beberapa menit."),
    ("keram otot", "Hentikan aktivitas dan regangkan otot yang keram. Minum air dan pastikan asupan mineral cukup."),
    ("dehidrasi", "Tanda dehidrasi antara lain lemas dan urine berwarna gelap. Minum air sedikit-sedikit tapi sering."),
    ("anemia", "Anemia sering disebabkan kekurangan zat besi. Makan makanan seperti sayur hijau dan daging tanpa lemak."),
    ("tekanan darah tinggi", "Kurangi garam dan makanan berlemak. Olahraga teratur dan kelola stres untuk menjaga tekanan darah."),
    ("gula darah", "Batasi makanan manis dan rutin bergerak. Penderita diabetes perlu mengikuti anjuran dokter."),
    ("kolesterol", "Kurangi gorengan dan lemak jenuh. Perbanyak sayur, buah, dan ikan."),
    ("obesitas", "Atur porsi makan dan tingkatkan aktivitas fisik. Perubahan kecil yang konsisten lebih baik daripada diet ekstrem."),
    ("osteoporosis", "Cukupi kalsium dan vitamin D. Latihan beban ringan membantu menjaga kepadatan tulang."),
    ("kesehatan mata", "Istirahatkan mata setiap 20 menit saat menatap layar. Jangan membaca dalam cahaya terlalu redup."),
    ("kesehatan mental", "Perasaan sedih atau cemas itu wajar. Kalau mengganggu aktivitas, jangan ragu mencari bantuan profesional."),
]

SCIENCE = [
    ("mengapa langit terlihat biru?", "Cahaya matahari dihamburkan oleh molekul di udara. Warna biru punya panjang gelombang pendek sehingga lebih banyak dihamburkan, makanya langit terlihat biru."),
    ("mengapa air laut terasa asin?", "Air laut mengandung garam mineral yang terbawa dari batuan di darat selama jutaan tahun. Garam itu tertinggal saat air menguap."),
    ("bagaimana pelangi terbentuk?", "Cahaya matahari dibiaskan dan dipantulkan oleh tetesan air hujan. Cahaya lalu terurai menjadi warna merah sampai ungu."),
    ("berapa kecepatan cahaya?", "Kecepatan cahaya di ruang hampa sekitar 299.792.458 meter per detik, sering dibulatkan menjadi 300.000 kilometer per detik."),
    ("berapa titik didih air?", "Air mendidih pada 100 derajat Celsius jika tekanan udaranya 1 atmosfer. Di tempat tinggi, titik didihnya lebih rendah."),
    ("apa rumus kimia air?", "Rumus kimia air adalah H2O, yaitu dua atom hidrogen dan satu atom oksigen."),
    ("gas apa yang dihirup manusia?", "Manusia menghirup oksigen dan menghembuskan karbon dioksida. Oksigen dipakai tubuh untuk menghasilkan energi."),
    ("berapa jumlah tulang manusia dewasa?", "Tubuh manusia dewasa memiliki 206 tulang. Bayi punya lebih banyak tulang, lalu sebagian menyatu saat tumbuh."),
    ("apa organ terbesar manusia?", "Kulit adalah organ terbesar manusia. Kulit melindungi tubuh dari kuman, panas, dan benturan."),
    ("organ apa yang memompa darah?", "Jantung memompa darah ke seluruh tubuh. Jantung berdetak sekitar 60 sampai 100 kali per menit saat istirahat."),
    ("berapa jumlah gigi orang dewasa?", "Orang dewasa biasanya punya 32 gigi, termasuk empat gigi bungsu. Anak-anak punya sekitar 20 gigi susu."),
    ("apa penyebab gempa bumi?", "Gempa bumi paling sering terjadi karena pergeseran lempeng bumi. Getarannya menjalar ke permukaan dan terasa sebagai gempa."),
    ("apa itu fotosintesis?", "Fotosintesis adalah proses tumbuhan membuat makanan dari cahaya matahari, air, dan karbon dioksida. Proses ini menghasilkan oksigen."),
    ("apa itu gravitasi?", "Gravitasi adalah gaya tarik antara benda yang punya massa. Gaya inilah yang membuat benda jatuh ke bumi."),
    ("planet apa yang paling dekat dengan matahari?", "Merkurius adalah planet terdekat dengan matahari. Planet ini juga yang paling kecil di tata surya."),
    ("planet apa yang paling besar?", "Jupiter adalah planet terbesar di tata surya. Ukurannya jauh lebih besar dari bumi."),
    ("planet apa yang punya cincin paling jelas?", "Saturnus punya cincin paling jelas dan lebar. Cincinnya tersusun dari bongkahan es dan debu."),
    ("berapa lama cahaya matahari sampai ke bumi?", "Cahaya matahari butuh sekitar 8 menit 20 detik untuk sampai ke bumi."),
    ("berapa jumlah planet di tata surya?", "Tata surya punya delapan planet. Pluto sekarang dikelompokkan sebagai planet kerdil."),
    ("apa satelit alami bumi?", "Bulan adalah satelit alami bumi. Bulan mengelilingi bumi sekitar 27,3 hari sekali."),
    ("bintang apa yang paling dekat dengan bumi?", "Matahari adalah bintang terdekat dengan bumi. Setelah matahari, bintang terdekat adalah Proxima Centauri."),
    ("apa itu gerhana matahari?", "Gerhana matahari terjadi saat bulan berada di antara bumi dan matahari. Cahaya matahari jadi terhalang sebagian atau seluruhnya."),
    ("apa itu gerhana bulan?", "Gerhana bulan terjadi saat bumi berada di antara matahari dan bulan. Bayangan bumi menutupi bulan."),
    ("mengapa terjadi siang dan malam?", "Bumi berputar pada porosnya sehingga bagian yang menghadap matahari bergantian. Bagian yang terkena cahaya mengalami siang."),
    ("mengapa ada musim?", "Bumi mengelilingi matahari dengan posisi miring. Kemiringan ini membuat penyinaran matahari berbeda sepanjang tahun."),
    ("berapa lama bumi mengelilingi matahari?", "Bumi butuh sekitar 365,25 hari untuk satu kali mengelilingi matahari. Sisa seperempat hari dikumpulkan menjadi tahun kabisat."),
    ("berapa lama bumi berotasi?", "Bumi berotasi sekitar 24 jam sekali. Rotasi inilah yang menyebabkan pergantian siang dan malam."),
    ("apa saja lapisan atmosfer?", "Atmosfer bumi terdiri dari troposfer, stratosfer, mesosfer, termosfer, dan eksosfer. Cuaca terjadi di troposfer."),
    ("gas apa yang paling banyak di atmosfer?", "Nitrogen adalah gas terbanyak di atmosfer, sekitar 78 persen. Oksigen sekitar 21 persen."),
    ("apa itu efek rumah kaca?", "Efek rumah kaca adalah kemampuan gas tertentu menahan panas di atmosfer. Tanpa efek ini, bumi akan terlalu dingin."),
    ("apa itu pemanasan global?", "Pemanasan global adalah kenaikan suhu rata-rata bumi. Salah satu penyebabnya adalah bertambahnya gas rumah kaca."),
    ("apa itu daur air?", "Daur air adalah siklus perpindahan air dari laut ke udara lalu kembali ke darat. Prosesnya meliputi penguapan, kondensasi, dan hujan."),
    ("apa itu simbiosis mutualisme?", "Simbiosis mutualisme adalah hubungan dua makhluk hidup yang saling menguntungkan. Contohnya lebah dengan bunga."),
    ("apa itu rantai makanan?", "Rantai makanan adalah urutan makhluk hidup yang saling makan. Energi berpindah dari produsen ke konsumen."),
    ("apa beda vertebrata dan invertebrata?", "Vertebrata punya tulang belakang, sedangkan invertebrata tidak. Contoh vertebrata adalah kucing, ikan, dan burung."),
    ("apa itu sel?", "Sel adalah unit terkecil kehidupan. Semua makhluk hidup tersusun dari satu atau banyak sel."),
    ("apa itu DNA?", "DNA adalah materi genetik yang membawa informasi sifat makhluk hidup. DNA tersimpan di dalam inti sel."),
    ("apa itu virus?", "Virus adalah partikel yang bisa menginfeksi sel hidup. Virus tidak bisa berkembang biak tanpa sel inang."),
    ("apa itu bakteri?", "Bakteri adalah makhluk hidup bersel satu yang sangat kecil. Sebagian bakteri bermanfaat, sebagian bisa menyebabkan penyakit."),
    ("apa beda virus dan bakteri?", "Bakteri adalah sel hidup yang bisa membelah diri, sedangkan virus bukan sel dan butuh inang. Karena itu obat untuk keduanya berbeda."),
    ("apa itu enzim?", "Enzim adalah protein yang mempercepat reaksi kimia dalam tubuh. Tanpa enzim, banyak reaksi berjalan terlalu lambat."),
    ("apa itu klorofil?", "Klorofil adalah pigmen hijau pada tumbuhan. Zat ini menangkap cahaya untuk proses fotosintesis."),
    ("apa itu energi terbarukan?", "Energi terbarukan berasal dari sumber yang tidak habis, seperti matahari, angin, dan air. Energi ini lebih ramah lingkungan."),
    ("apa sumber energi utama bumi?", "Matahari adalah sumber energi utama bumi. Energi matahari menggerakkan cuaca, arus laut, dan proses fotosintesis."),
    ("apa itu listrik statis?", "Listrik statis adalah muatan listrik yang diam di suatu benda. Gesekan bisa membuat muatan berpindah dan menimbulkan percikan."),
    ("apa itu magnet?", "Magnet adalah benda yang bisa menarik logam tertentu. Magnet punya dua kutub, yaitu utara dan selatan."),
    ("apa itu bunyi?", "Bunyi adalah gelombang getaran yang bisa didengar telinga. Bunyi butuh medium seperti udara atau air untuk merambat."),
    ("mengapa terjadi petir?", "Petir terjadi karena perbedaan muatan listrik di awan atau antara awan dan bumi. Pelepasan muatan itu menghasilkan cahaya dan suara."),
    ("mengapa gunung berapi meletus?", "Gunung berapi meletus karena tekanan magma di dalam bumi mendorong ke permukaan. Tekanan ini bisa dipicu oleh gerakan lempeng."),
    ("apa itu air tanah?", "Air tanah adalah air yang tersimpan di celah-celah batuan dan tanah. Air ini biasanya diambil lewat sumur."),
    ("apa itu erosi?", "Erosi adalah pengikisan tanah oleh air, angin, atau es. Erosi bisa diperlambat dengan menanam pohon dan membuat terasering."),
]

MATHC = [
    ("luas persegi", "Luas persegi dihitung dengan sisi x sisi atau s kuadrat."),
    ("keliling persegi", "Keliling persegi adalah jumlah keempat sisinya, yaitu 4 x sisi."),
    ("luas persegi panjang", "Luas persegi panjang dihitung dengan panjang x lebar."),
    ("keliling persegi panjang", "Keliling persegi panjang adalah 2 x (panjang + lebar)."),
    ("luas segitiga", "Luas segitiga adalah 1/2 x alas x tinggi."),
    ("luas lingkaran", "Luas lingkaran adalah phi x r x r, dengan r sebagai jari-jari."),
    ("keliling lingkaran", "Keliling lingkaran adalah 2 x phi x r atau phi x diameter."),
    ("volume kubus", "Volume kubus adalah sisi x sisi x sisi atau s pangkat 3."),
    ("volume balok", "Volume balok adalah panjang x lebar x tinggi."),
    ("volume tabung", "Volume tabung adalah phi x r x r x tinggi."),
    ("rata-rata", "Rata-rata didapat dari jumlah semua data dibagi banyaknya data."),
    ("median", "Median adalah nilai tengah setelah data diurutkan."),
    ("modus", "Modus adalah nilai yang paling sering muncul dalam data."),
    ("persen", "Persen berarti per seratus. Lima puluh persen sama dengan 50/100 atau 0,5."),
    ("pecahan", "Pecahan ditulis a/b, dengan a sebagai pembilang dan b sebagai penyebut."),
    ("bilangan prima", "Bilangan prima hanya bisa dibagi 1 dan dirinya sendiri. Contohnya 2, 3, 5, 7, dan 11."),
    ("KPK", "KPK adalah kelipatan persekutuan terkecil dari dua bilangan atau lebih."),
    ("FPB", "FPB adalah faktor persekutuan terbesar dari dua bilangan atau lebih."),
    ("bilangan bulat", "Bilangan bulat terdiri dari bilangan negatif, nol, dan bilangan positif."),
    ("bilangan cacah", "Bilangan cacah adalah bilangan bulat yang tidak negatif, mulai dari 0, 1, 2, dan seterusnya."),
    ("bilangan asli", "Bilangan asli adalah bilangan positif yang dimulai dari 1, 2, 3, dan seterusnya."),
    ("bilangan negatif", "Bilangan negatif adalah bilangan yang nilainya kurang dari nol, ditulis dengan tanda minus."),
    ("pangkat", "Pangkat menunjukkan perkalian berulang. Contohnya 2 pangkat 3 berarti 2 x 2 x 2 = 8."),
    ("akar kuadrat", "Akar kuadrat adalah kebalikan dari kuadrat. Akar dari 49 adalah 7 karena 7 x 7 = 49."),
    ("perbandingan", "Perbandingan membandingkan dua nilai atau lebih, misalnya 2:3."),
    ("skala", "Skala membandingkan ukuran pada gambar dengan ukuran sebenarnya."),
    ("debit", "Debit adalah volume zat cair yang mengalir per satuan waktu."),
    ("kecepatan", "Kecepatan adalah jarak yang ditempuh dibagi waktu tempuh."),
    ("jarak", "Jarak dihitung dengan kecepatan x waktu."),
    ("waktu tempuh", "Waktu tempuh dihitung dengan jarak dibagi kecepatan."),
]

CIVICS = [
    ("apa sila pertama Pancasila?", "Sila pertama Pancasila adalah Ketuhanan Yang Maha Esa. Sila ini menegaskan bahwa Indonesia mengakui keberadaan Tuhan."),
    ("apa sila kedua Pancasila?", "Sila kedua Pancasila adalah Kemanusiaan yang adil dan beradab. Sila ini menekankan sikap menghargai sesama manusia."),
    ("apa sila ketiga Pancasila?", "Sila ketiga Pancasila adalah Persatuan Indonesia. Sila ini mengajak seluruh rakyat menjaga persatuan."),
    ("apa sila keempat Pancasila?", "Sila keempat Pancasila adalah Kerakyatan yang dipimpin oleh hikmat kebijaksanaan dalam permusyawaratan/perwakilan."),
    ("apa sila kelima Pancasila?", "Sila kelima Pancasila adalah Keadilan sosial bagi seluruh rakyat Indonesia. Sila ini menekankan keadilan untuk semua."),
    ("apa itu UUD 1945?", "UUD 1945 adalah hukum dasar negara Indonesia. Isinya mengatur penyelenggaraan negara dan hak warga."),
    ("apa arti Bhinneka Tunggal Ika?", "Bhinneka Tunggal Ika berarti berbeda-beda tetapi tetap satu. Semboyan ini mengajak menghargai keberagaman."),
    ("apa tugas MPR?", "MPR terdiri dari DPR dan DPD. Tugasnya antara lain mengubah UUD dan melantik presiden serta wakil presiden."),
    ("apa tugas DPR?", "DPR bertugas membuat undang-undang, mengawasi pemerintah, dan menampung aspirasi rakyat."),
    ("apa tugas DPD?", "DPD mewakili kepentingan daerah di tingkat nasional. Anggotanya dipilih dari setiap provinsi."),
    ("apa tugas presiden?", "Presiden adalah kepala negara dan kepala pemerintahan. Presiden memimpin kabinet dan menjalankan undang-undang."),
    ("apa tugas Mahkamah Agung?", "Mahkamah Agung adalah lembaga peradilan tertinggi. Tugasnya mengadili perkara di tingkat kasasi."),
    ("apa tugas Mahkamah Konstitusi?", "Mahkamah Konstitusi menguji undang-undang terhadap UUD 1945. MK juga memutus sengketa hasil pemilu."),
    ("apa tugas BPK?", "BPK atau Badan Pemeriksa Keuangan memeriksa pengelolaan keuangan negara. Hasil pemeriksaannya disampaikan ke lembaga negara."),
    ("apa tugas Komisi Yudisial?", "Komisi Yudisial mengawasi perilaku hakim. KY juga mengusulkan calon hakim agung."),
    ("apa itu pemilu?", "Pemilu adalah cara rakyat memilih wakil dan pemimpin. Di Indonesia, pemilu memilih presiden, DPR, DPD, dan DPRD."),
    ("apa hak warga negara?", "Hak warga negara antara lain mendapat pendidikan, pekerjaan, dan perlindungan hukum. Hak ini dijamin oleh undang-undang."),
    ("apa kewajiban warga negara?", "Kewajiban warga negara antara lain menaati hukum, membayar pajak, dan menjaga persatuan. Kewajiban ini dilakukan demi kepentingan bersama."),
    ("apa itu gotong royong?", "Gotong royong adalah bekerja sama untuk kepentingan bersama. Budaya ini menjadi ciri khas masyarakat Indonesia."),
    ("apa itu musyawarah?", "Musyawarah adalah cara mengambil keputusan bersama melalui perundingan. Tujuannya mencapai kesepakatan yang menguntungkan semua."),
    ("apa itu NKRI?", "NKRI adalah Negara Kesatuan Republik Indonesia. Bentuk negara ini menjaga wilayah dan pemerintahan tetap satu."),
    ("mengapa harus membayar pajak?", "Pajak dipakai untuk membiayai pembangunan dan layanan publik. Contohnya jalan, sekolah, dan fasilitas kesehatan."),
]

SPORTS = [
    ("berapa jumlah pemain sepak bola satu tim?", "Satu tim sepak bola punya 11 pemain di lapangan, termasuk penjaga gawang. Untuk pertandingan resmi, jumlah pemain minimal 7."),
    ("berapa jumlah pemain basket satu tim?", "Satu tim basket punya 5 pemain di lapangan. Pertandingan dimainkan dalam empat kuarter."),
    ("berapa jumlah pemain voli satu tim?", "Satu tim voli punya 6 pemain di lapangan. Setiap tim boleh melakukan tiga sentuhan sebelum bola melewati net."),
    ("bagaimana cara bermain bulu tangkis?", "Bulu tangkis dimainkan dengan raket dan shuttlecock. Pemain berusaha menjatuhkan shuttlecock di area lawan."),
    ("berapa poin untuk memenangkan set bulu tangkis?", "Satu set bulu tangkis dimenangkan dengan 21 poin, dengan selisih minimal 2 poin. Kalau imbang 20-20, permainan dilanjutkan sampai selisih 2."),
    ("berapa jarak lari maraton?", "Jarak lari maraton adalah 42,195 kilometer. Jarak ini ditetapkan pada Olimpiade 1908."),
    ("berapa tahun sekali Olimpiade diadakan?", "Olimpiade musim panas dan musim dingin diadakan setiap empat tahun. Edisi 2020 ditunda ke 2021 karena pandemi."),
    ("berapa tahun sekali Piala Dunia?", "Piala Dunia sepak bola diadakan setiap empat tahun. Turnamen ini diikuti tim nasional dari berbagai negara."),
    ("apa itu PSSI?", "PSSI adalah induk organisasi sepak bola Indonesia. PSSI mengelola tim nasional dan kompetisi sepak bola di Indonesia."),
    ("berapa tahun sekali SEA Games?", "SEA Games diadakan setiap dua tahun. Pesertanya negara-negara di Asia Tenggara."),
    ("berapa tahun sekali Asian Games?", "Asian Games diadakan setiap empat tahun. Pesertanya negara-negara di Asia."),
    ("apa itu pencak silat?", "Pencak silat adalah seni bela diri tradisional Indonesia. Gerakannya menggabungkan teknik bela diri dan seni."),
    ("dari mana asal karate?", "Karate berasal dari Jepang, tepatnya Okinawa. Olahraga ini menekankan pukulan, tendangan, dan disiplin."),
    ("dari mana asal judo?", "Judo berasal dari Jepang. Olahraga ini menekankan lemparan dan kuncian."),
    ("apa saja cabang atletik?", "Atletik mencakup lari, lompat, dan lempar. Contohnya lari sprint, lompat jauh, dan lempar lembing."),
]

ENV = [
    ("mengapa sampah plastik berbahaya?", "Sampah plastik butuh ratusan tahun untuk terurai. Sampah ini bisa mencemari tanah, sungai, dan laut."),
    ("apa itu 3R?", "3R adalah reduce, reuse, dan recycle. Artinya kurangi, pakai ulang, dan daur ulang sampah."),
    ("bagaimana menghemat air?", "Matikan keran saat tidak dipakai dan perbaiki kebocoran. Menghemat air membantu menjaga persediaan air bersih."),
    ("bagaimana menghemat listrik?", "Matikan lampu dan alat elektronik yang tidak dipakai. Gunakan lampu hemat energi untuk mengurangi konsumsi listrik."),
    ("mengapa harus menanam pohon?", "Pohon menyerap karbon dioksida dan menghasilkan oksigen. Akarnya juga membantu mencegah erosi."),
    ("mengapa memakai transportasi umum?", "Transportasi umum mengurangi jumlah kendaraan pribadi. Ini membantu menurunkan polusi dan kemacetan."),
    ("apa itu energi terbarukan?", "Energi terbarukan berasal dari sumber yang tidak habis, seperti matahari, angin, dan air. Energi ini lebih ramah lingkungan."),
    ("apa penyebab polusi udara?", "Polusi udara berasal dari asap kendaraan, pabrik, dan pembakaran sampah. Gas buangnya bisa mengganggu pernapasan."),
    ("apa itu pemanasan global?", "Pemanasan global adalah kenaikan suhu rata-rata bumi. Penyebab utamanya bertambahnya gas rumah kaca."),
    ("mengapa terumbu karang penting?", "Terumbu karang menjadi tempat hidup banyak ikan. Kerusakan terumbu karang bisa mengganggu ekosistem laut."),
    ("apa fungsi hutan mangrove?", "Mangrove menahan abrasi pantai dan menjadi tempat hidup biota laut. Akarnya juga membantu menahan lumpur."),
    ("bagaimana membuat kompos?", "Kumpulkan sisa sayur dan daun kering, lalu aduk berkala. Setelah beberapa minggu, bahan itu menjadi kompos."),
    ("bagaimana cara mendaur ulang?", "Pisahkan sampah menurut jenisnya, lalu kirim ke tempat daur ulang. Barang bekas juga bisa dipakai untuk keperluan lain."),
    ("apa itu bahan bakar fosil?", "Bahan bakar fosil berasal dari sisa makhluk hidup yang terkubur jutaan tahun. Contohnya batu bara, minyak bumi, dan gas alam."),
    ("apa itu jejak karbon?", "Jejak karbon adalah jumlah gas rumah kaca yang dihasilkan dari aktivitas kita. Mengurangi jejak karbon membantu lingkungan."),
]

HOWTO = [
    ("membuat nasi goreng", "1) Siapkan nasi, bawang, telur, dan kecap. 2) Tumis bawang sampai harum, lalu masukkan telur. 3) Masukkan nasi dan aduk rata, tambahkan kecap dan garam. 4) Masak sampai bumbu merata, lalu sajikan selagi hangat."),
    ("membuat mie instan", "1) Didihkan air sekitar 400 ml. 2) Masukkan mie dan masak 3 menit. 3) Tuang bumbu ke mangkuk, lalu masukkan mie beserta kuahnya. 4) Aduk rata dan tambahkan telur atau sayur kalau mau lebih lengkap."),
    ("membuat teh manis", "1) Didihkan air. 2) Masukkan teh ke gelas dan tuang air panas. 3) Tambahkan gula sesuai selera, lalu aduk sampai larut. 4) Diamkan beberapa menit sebelum diminum."),
    ("membuat kopi", "1) Siapkan kopi bubuk dan air panas sekitar 90 derajat. 2) Tuang air sedikit demi sedikit ke kopi. 3) Diamkan 3 sampai 4 menit agar rasanya keluar. 4) Saring atau angkat ampasnya, lalu sajikan."),
    ("merebus telur", "1) Masukkan telur ke panci dan isi air sampai terendam. 2) Didihkan air, lalu kecilkan api. 3) Rebus 8 sampai 10 menit untuk telur matang penuh. 4) Angkat dan rendam sebentar di air dingin agar mudah dikupas."),
    ("membuat telur dadar", "1) Kocok 2 butir telur dengan sedikit garam. 2) Panaskan minyak di wajan. 3) Tuang telur dan ratakan. 4) Masak sampai kedua sisi matang, lalu angkat."),
    ("membuat pisang goreng", "1) Kupas pisang dan potong sesuai selera. 2) Campur tepung, air, dan sedikit gula menjadi adonan. 3) Celupkan pisang ke adonan. 4) Goreng dalam minyak panas sampai keemasan, lalu tiriskan."),
    ("membuat sambal sederhana", "1) Rebus atau goreng cabai dan bawang. 2) Ulek cabai, bawang, garam, dan sedikit gula. 3) Koreksi rasa, lalu tambahkan perasan jeruk kalau suka. 4) Sambal siap disajikan."),
    ("menggoreng tempe", "1) Potong tempe tipis-tipis. 2) Campur sedikit garam dan air, lalu celupkan tempe. 3) Panaskan minyak dan goreng tempe sampai keemasan. 4) Tiriskan sebelum disajikan."),
    ("membuat sayur sop", "1) Rebus air dan masukkan potongan ayam atau tulang untuk kaldu. 2) Masukkan wortel dan kentang, masak sampai setengah empuk. 3) Tambahkan kol, buncis, dan bumbu. 4) Masak sampai semua sayur matang, lalu sajikan."),
    ("mencuci tangan", "1) Basahi tangan dengan air mengalir. 2) Gosok sabun ke seluruh permukaan tangan, termasuk sela jari. 3) Gosok minimal 20 detik. 4) Bilas sampai bersih, lalu keringkan dengan handuk bersih."),
    ("menyikat gigi", "1) Ambil pasta gigi secukupnya di sikat gigi. 2) Sikat seluruh permukaan gigi dengan gerakan lembut. 3) Sikat juga bagian belakang gigi dan lidah. 4) Berkumur, lalu buang airnya."),
    ("mencuci piring", "1) Buang sisa makanan ke tempat sampah. 2) Bilas piring dengan air. 3) Sabun dan gosok piring sampai bersih. 4) Bilas dengan air bersih, lalu keringkan."),
    ("mencuci baju", "1) Pisahkan baju putih dan berwarna. 2) Masukkan baju ke mesin cuci atau ember. 3) Tambahkan deterjen sesuai petunjuk. 4) Cuci, bilas, lalu jemur di tempat yang terkena sinar matahari."),
    ("menyapu lantai", "1) Ambil sampah besar terlebih dahulu. 2) Sapu dari sudut ruangan ke arah pintu. 3) Kumpulkan sampah di pengki. 4) Buang sampah ke tempatnya."),
    ("mengepel lantai", "1) Bersihkan debu dan sampah dengan sapu. 2) Campur pembersih lantai dengan air. 3) Pel lantai dari bagian dalam ke arah pintu. 4) Biarkan kering sebelum dipakai."),
    ("merapikan kamar", "1) Buang sampah dan barang yang tidak perlu. 2) Rapikan tempat tidur. 3) Susun barang sesuai tempatnya. 4) Lap meja dan sapu lantai."),
    ("membuang sampah", "1) Pisahkan sampah organik dan anorganik. 2) Masukkan sampah ke kantong yang sesuai. 3) Ikat kantong agar tidak terbuka. 4) Buang ke tempat sampah atau bank sampah terdekat."),
    ("menghemat uang", "1) Catat pemasukan dan pengeluaran. 2) Bedakan kebutuhan dan keinginan. 3) Sisihkan sebagian uang begitu menerima pemasukan. 4) Hindari belanja impulsif."),
    ("membuat anggaran bulanan", "1) Jumlahkan semua pemasukan. 2) Catat pengeluaran tetap seperti sewa dan transportasi. 3) Tentukan batas belanja dan tabungan. 4) Evaluasi di akhir bulan."),
    ("menabung", "1) Tentukan tujuan menabung. 2) Pilih rekening atau celengan terpisah. 3) Sisihkan uang secara rutin. 4) Jangan pakai tabungan untuk belanja yang tidak penting."),
    ("belajar efektif", "1) Tentukan target yang jelas. 2) Belajar dalam sesi pendek dengan istirahat. 3) Uji pemahaman dengan latihan soal. 4) Ulangi materi keesokan harinya."),
    ("menghafal", "1) Baca materi sampai paham. 2) Pecah menjadi bagian kecil. 3) Ucapkan atau tulis ulang tanpa melihat. 4) Ulangi di hari berikutnya."),
    ("membuat catatan", "1) Tulis poin utama, bukan semua kalimat. 2) Gunakan singkatan dan tanda panah. 3) Beri contoh supaya mudah diingat. 4) Rapikan catatan setelah selesai belajar."),
    ("tetap fokus belajar", "1) Jauhkan ponsel selama belajar. 2) Tentukan waktu belajar dan istirahat. 3) Kerjakan satu tugas dalam satu waktu. 4) Beri hadiah kecil setelah target tercapai."),
    ("membuat CV", "1) Tulis data diri dan kontak. 2) Cantumkan pendidikan dan pengalaman. 3) Tambahkan keterampilan yang relevan. 4) Periksa ejaan sebelum mengirim."),
    ("membuat surat lamaran", "1) Tulis tujuan dan posisi yang dilamar. 2) Jelaskan singkat pengalaman yang relevan. 3) Lampirkan CV dan dokumen pendukung. 4) Tutup dengan ucapan terima kasih."),
    ("menghadapi wawancara kerja", "1) Pelajari perusahaan dan posisinya. 2) Siapkan cerita singkat tentang pengalaman. 3) Datang lebih awal dan berpakaian rapi. 4) Jawab dengan jujur dan ajukan pertanyaan di akhir."),
    ("membuat presentasi", "1) Tentukan satu pesan utama. 2) Susun alur pembuka, isi, dan penutup. 3) Gunakan sedikit teks dan gambar pendukung. 4) Latih penyampaian dan cek waktu."),
    ("berbicara di depan umum", "1) Kuasai materi yang dibawakan. 2) Tarik napas dan atur tempo bicara. 3) Tatap audiens, jangan terus melihat catatan. 4) Akhiri dengan kesimpulan yang jelas."),
    ("mengirim email", "1) Tulis subjek yang jelas. 2) Awali dengan sapaan. 3) Tulis isi secara singkat dan sopan. 4) Periksa lampiran sebelum menekan kirim."),
    ("melampirkan file", "1) Cari tombol lampiran di aplikasi. 2) Pilih file yang ingin dikirim. 3) Tunggu sampai unggahan selesai. 4) Periksa kembali nama dan ukuran file."),
    ("membuat cadangan data", "1) Pilih data yang penting. 2) Salin ke hard disk eksternal atau penyimpanan awan. 3) Periksa apakah salinan bisa dibuka. 4) Lakukan pencadangan secara rutin."),
    ("membuat password kuat", "1) Gunakan minimal 12 karakter. 2) Campur huruf besar, huruf kecil, angka, dan simbol. 3) Jangan pakai data pribadi yang mudah ditebak. 4) Pakai password berbeda untuk akun penting."),
    ("menjaga privasi online", "1) Batasi data pribadi yang dibagikan. 2) Periksa pengaturan privasi akun. 3) Jangan sembarangan memberi izin aplikasi. 4) Hati-hati menerima tautan dari orang tak dikenal."),
    ("mengenali phishing", "1) Periksa alamat pengirim. 2) Waspadai pesan yang meminta password atau kode OTP. 3) Jangan klik tautan mencurigakan. 4) Hubungi layanan resmi kalau ragu."),
    ("menanam cabai", "1) Siapkan biji cabai dan media tanam. 2) Semai biji di tempat terkena cahaya. 3) Pindahkan bibit setelah punya beberapa daun. 4) Siram rutin dan beri pupuk secukupnya."),
    ("merawat tanaman", "1) Beri air sesuai kebutuhan tanaman. 2) Letakkan di tempat yang cukup cahaya. 3) Bersihkan daun dari debu. 4) Pindahkan ke pot lebih besar kalau akar sudah padat."),
    ("menyiram tanaman", "1) Periksa dulu kelembapan tanah. 2) Siram sampai air meresap, jangan menggenang. 3) Siram pagi atau sore. 4) Kurangi penyiraman saat musim hujan."),
    ("bersepeda dengan aman", "1) Pakai helm dan pastikan rem berfungsi. 2) Gunakan lampu saat malam. 3) Ikuti arah lalu lintas. 4) Beri isyarat tangan sebelum berbelok."),
    ("berkendara dengan aman", "1) Pakai helm atau sabuk pengaman. 2) Patuhi batas kecepatan. 3) Jaga jarak dengan kendaraan lain. 4) Jangan memakai ponsel saat mengemudi."),
    ("menangani luka bakar ringan", "1) Alirkan air dingin pada luka selama 10 sampai 20 menit. 2) Lepaskan perhiasan di sekitar luka. 3) Tutup dengan kain bersih. 4) Jangan beri pasta gigi atau mentega."),
    ("mengatasi mimisan", "1) Duduk tegak dan condongkan kepala sedikit ke depan. 2) Tekan bagian lunak hidung 10 menit. 3) Bernapas lewat mulut. 4) Kalau tidak berhenti, cari bantuan medis."),
    ("menangani demam", "1) Ukur suhu tubuh. 2) Beri minum lebih banyak. 3) Istirahatkan penderita. 4) Kalau demam tinggi atau lama, periksa ke dokter."),
    ("mengatasi keram otot", "1) Hentikan aktivitas. 2) Regangkan otot yang keram dengan lembut. 3) Pijat dan hangatkan bagian tersebut. 4) Minum air untuk mengganti cairan."),
    ("memadamkan api kecil", "1) Jangan panik dan jauhi api dari arah angin. 2) Padamkan dengan alat pemadam atau kain tebal. 3) Jangan memakai air untuk api dari minyak. 4) Kalau api membesar, segera keluar dan hubungi petugas."),
    ("menyelamatkan diri saat gempa", "1) Lindungi kepala dan cari tempat aman. 2) Berlindung di bawah meja yang kuat. 3) Jauhi kaca dan benda yang mudah jatuh. 4) Setelah guncangan berhenti, keluar dengan tertib."),
    ("merawat sepatu", "1) Bersihkan debu setelah dipakai. 2) Simpan di tempat kering dan berventilasi. 3) Jangan menjemur langsung di bawah matahari. 4) Gunakan pelindung saat musim hujan."),
    ("membuat kopi susu", "1) Seduh kopi pekat. 2) Panaskan susu, jangan sampai mendidih. 3) Campur kopi dan susu sesuai selera. 4) Tambahkan gula atau es kalau mau."),
]

GENERAL = [
    ("apa ibu kota Indonesia?", "Jakarta masih menjadi pusat pemerintahan dan ekonomi Indonesia. Nusantara di Kalimantan Timur disiapkan sebagai ibu kota baru, tetapi perpindahannya dilakukan bertahap."),
    ("siapa presiden Indonesia sekarang?", "Presiden Indonesia periode 2024 sampai 2029 adalah Prabowo Subianto. Ia dilantik pada 20 Oktober 2024."),
    ("siapa wakil presiden Indonesia sekarang?", "Wakil Presiden Indonesia periode 2024 sampai 2029 adalah Gibran Rakabuming Raka. Ia dilantik bersama presiden pada 20 Oktober 2024."),
    ("berapa jumlah provinsi di Indonesia?", "Indonesia punya 38 provinsi. Jumlah ini bertambah setelah pemekaran beberapa wilayah di Papua."),
    ("apa lagu kebangsaan Indonesia?", "Lagu kebangsaan Indonesia adalah Indonesia Raya. Lagu ini diciptakan oleh W.R. Supratman."),
    ("apa semboyan negara Indonesia?", "Semboyan Indonesia adalah Bhinneka Tunggal Ika. Artinya berbeda-beda tetapi tetap satu."),
    ("apa mata uang Indonesia?", "Mata uang Indonesia adalah Rupiah. Kode internasionalnya IDR."),
    ("kapan Indonesia merdeka?", "Indonesia memproklamasikan kemerdekaan pada 17 Agustus 1945. Teks proklamasi dibacakan oleh Soekarno dan Mohammad Hatta."),
    ("siapa presiden pertama Indonesia?", "Presiden pertama Indonesia adalah Soekarno. Ia menjabat dari 1945 sampai 1967."),
    ("apa dasar negara Indonesia?", "Dasar negara Indonesia adalah Pancasila. Lima silanya menjadi pedoman dalam kehidupan berbangsa."),
    ("berapa jumlah pulau di Indonesia?", "Indonesia punya lebih dari 17.000 pulau. Sekitar 6.000 di antaranya berpenghuni."),
    ("berapa agama yang diakui di Indonesia?", "Indonesia mengakui enam agama, yaitu Islam, Kristen Protestan, Katolik, Hindu, Buddha, dan Khonghucu."),
    ("apa bahasa resmi Indonesia?", "Bahasa resmi Indonesia adalah Bahasa Indonesia. Bahasa daerah tetap dipakai dan dilestarikan."),
    ("Indonesia ada di benua apa?", "Indonesia terletak di Asia Tenggara. Wilayahnya juga berbatasan dengan benua Australia di bagian timur."),
    ("apa saja samudra yang mengapit Indonesia?", "Indonesia diapit Samudra Hindia di barat dan selatan serta Samudra Pasifik di utara dan timur."),
    ("berapa jumlah penduduk Indonesia?", "Penduduk Indonesia sekitar 280 juta jiwa berdasarkan perkiraan 2024. Angka pastinya berubah setiap tahun."),
    ("apa gunung tertinggi di Indonesia?", "Gunung tertinggi di Indonesia adalah Puncak Jaya di Papua. Ketinggiannya sekitar 4.884 meter."),
    ("apa danau terbesar di Indonesia?", "Danau terbesar di Indonesia adalah Danau Toba di Sumatera Utara. Danau ini terbentuk dari letusan gunung purba."),
    ("apa sungai terpanjang di Indonesia?", "Sungai terpanjang di Indonesia adalah Sungai Kapuas di Kalimantan Barat. Panjangnya sekitar 1.143 kilometer."),
    ("apa pulau terbesar di Indonesia?", "Pulau terbesar di Indonesia adalah Kalimantan. Sebagian wilayah Kalimantan dimiliki Malaysia dan Brunei."),
    ("apa pulau terpadat di Indonesia?", "Pulau terpadat di Indonesia adalah Jawa. Sebagian besar penduduk Indonesia tinggal di pulau ini."),
    ("ada berapa zona waktu di Indonesia?", "Indonesia punya tiga zona waktu, yaitu WIB, WITA, dan WIT. Masing-masing berselisih satu jam."),
    ("apa lambang negara Indonesia?", "Lambang negara Indonesia adalah Garuda Pancasila. Di dadanya ada perisai dengan lima simbol sila."),
    ("apa warna bendera Indonesia?", "Bendera Indonesia berwarna merah dan putih. Merah berarti berani, putih berarti suci."),
    ("berapa jumlah sila dalam Pancasila?", "Pancasila terdiri dari lima sila. Kelimanya menjadi dasar dan pedoman hidup berbangsa."),
    ("apa itu Nusantara?", "Nusantara adalah nama ibu kota baru Indonesia di Kalimantan Timur. Pembangunannya dilakukan bertahap."),
    ("apa itu WIB?", "WIB adalah Waktu Indonesia Barat, yaitu UTC+7. Zona ini mencakup Sumatra, Jawa, serta Kalimantan Barat dan Kalimantan Tengah."),
    ("apa itu WITA?", "WITA adalah Waktu Indonesia Tengah, yaitu UTC+8. Zona ini mencakup Bali, Nusa Tenggara, Sulawesi, serta Kalimantan Selatan, Kalimantan Timur, dan Kalimantan Utara."),
    ("apa itu WIT?", "WIT adalah Waktu Indonesia Timur, yaitu UTC+9. Zona ini mencakup Maluku dan Papua."),
    ("mengapa Jakarta masih disebut ibu kota?", "Jakarta masih menjadi pusat pemerintahan dan ekonomi. Pemindahan ke Nusantara dilakukan bertahap, jadi statusnya masih dalam masa transisi."),
    ("apa hari kemerdekaan Indonesia?", "Hari kemerdekaan Indonesia diperingati setiap 17 Agustus. Upacara biasanya digelar di Istana Merdeka."),
    ("apa ibukota Provinsi Jawa Tengah?", "Ibu kota Provinsi Jawa Tengah adalah Semarang. Kota ini menjadi pusat pemerintahan dan pelabuhan penting."),
    ("apa makanan khas Indonesia yang mendunia?", "Rendang dari Sumatera Barat sering disebut sebagai salah satu makanan khas Indonesia yang mendunia. Makanan ini dimasak lama dengan santan dan rempah."),
    ("apa tarian yang terkenal dari Bali?", "Tari Kecak adalah salah satu tarian terkenal dari Bali. Tarian ini dimainkan banyak orang sambil bersuara cak."),
    ("apa alat musik tradisional dari Jawa Barat?", "Angklung adalah alat musik tradisional dari Jawa Barat. Alat ini terbuat dari bambu dan dimainkan dengan digoyang."),
    ("apa rumah adat dari Sumatera Barat?", "Rumah adat dari Sumatera Barat adalah Rumah Gadang. Atapnya melengkung seperti tanduk kerbau."),
    ("apa itu gotong royong?", "Gotong royong adalah bekerja bersama untuk kepentingan bersama. Budaya ini masih kuat di banyak desa Indonesia."),
    ("apa itu musyawarah?", "Musyawarah adalah perundingan untuk mencapai keputusan bersama. Nilai ini penting dalam kehidupan bermasyarakat."),
    ("apa itu Bhinneka Tunggal Ika?", "Bhinneka Tunggal Ika berarti berbeda-beda tetapi tetap satu. Semboyan ini mengajak kita menghargai perbedaan."),
    ("mengapa kita harus menghargai perbedaan?", "Perbedaan itu wajar dan Indonesia memang beragam. Menghargai perbedaan membuat masyarakat hidup rukun."),
]


def _cap(term: str) -> str:
    if any(ch.isupper() for ch in term):
        return term
    return term[0].upper() + term[1:]


def _tech(b: Builder) -> None:
    for istilah, definisi, contoh in TECH:
        key = f"tek-{istilah}"
        q = b.pick(
            ["apa itu {i}?", "{i} itu apa sih?", "jelaskan {i} dong"],
            key + "def",
        ).format(i=istilah)
        a = b.pick(
            [
                f"{_cap(istilah)} adalah {definisi}. Contohnya {contoh}.",
                f"{_cap(istilah)} itu {definisi}. Salah satu contoh pemakaiannya, {contoh}.",
                f"Secara sederhana, {istilah} adalah {definisi}. Kita bisa melihatnya pada {contoh}.",
            ],
            key + "def",
        )
        b.add(q, a, "pengetahuan", fact=key + ":def")

        q = b.pick(
            ["contoh {i} apa?", "kasih contoh penggunaan {i} dong", "{i} dipakai untuk apa?"],
            key + "contoh",
        ).format(i=istilah)
        a = b.pick(
            [
                f"Contoh {istilah} adalah {contoh}. Intinya, {istilah} adalah {definisi}.",
                f"Salah satu contohnya {contoh}. {_cap(istilah)} berfungsi sebagai {definisi}.",
                f"Kita bisa menemukannya pada {contoh}. Itu termasuk penerapan {istilah}, yaitu {definisi}.",
            ],
            key + "contoh",
        )
        b.add(q, a, "pengetahuan", fact=key + ":contoh")


def _health(b: Builder) -> None:
    for topik, isi in HEALTH:
        key = f"sehat-{topik}"
        q = b.pick(
            ["gimana cara {t}?", "apa tips {t}?", "bagaimana supaya bisa {t}?"],
            key,
        ).format(t=topik)
        a = b.pick(
            [
                f"{isi} Kalau ada keluhan yang menetap, sebaiknya konsultasi ke tenaga kesehatan.",
                f"{isi} Lakukan secara bertahap supaya mudah dijalani dan tidak memberatkan.",
                f"{isi} Yang penting konsisten, karena manfaatnya terasa kalau dilakukan rutin.",
            ],
            key,
        )
        b.add(q, a, "pengetahuan", fact=key)


def _science(b: Builder) -> None:
    for pertanyaan, jawaban in SCIENCE:
        key = f"sains-{pertanyaan}"
        a = b.pick(
            [
                jawaban,
                jawaban + " Itu penjelasan singkatnya.",
                jawaban,
            ],
            key,
        )
        b.add(pertanyaan, a, "pengetahuan", fact=key)


def _mathc(b: Builder) -> None:
    for istilah, penjelasan in MATHC:
        key = f"konsep-{istilah}"
        q = b.pick(
            ["apa itu {i}?", "{i} itu apa?", "jelaskan {i} dalam matematika"],
            key,
        ).format(i=istilah)
        a = b.pick(
            [
                f"{istilah.capitalize()} adalah {penjelasan}",
                f"Dalam matematika, {istilah} adalah {penjelasan}",
                f"{penjelasan} Itulah inti dari {istilah}.",
            ],
            key,
        )
        b.add(q, a, "pengetahuan", fact=key)


def _civics(b: Builder) -> None:
    for pertanyaan, jawaban in CIVICS:
        b.add(pertanyaan, jawaban, "pengetahuan", fact=f"warga-{pertanyaan}")


def _sports(b: Builder) -> None:
    for pertanyaan, jawaban in SPORTS:
        b.add(pertanyaan, jawaban, "pengetahuan", fact=f"olahraga-{pertanyaan}")


def _env(b: Builder) -> None:
    for pertanyaan, jawaban in ENV:
        b.add(pertanyaan, jawaban, "pengetahuan", fact=f"lingkungan-{pertanyaan}")


def _howto(b: Builder) -> None:
    for topik, langkah in HOWTO:
        key = f"cara-{topik}"
        q = b.pick(
            ["gimana cara {t}?", "tolong jelaskan cara {t}", "langkah-langkah {t} apa saja?"],
            key,
        ).format(t=topik)
        a = b.pick(
            [
                f"Caranya begini: {langkah}",
                f"Bisa dilakukan dengan langkah ini: {langkah}",
                f"Berikut urutannya: {langkah}",
            ],
            key,
        )
        b.add(q, a, "pengetahuan", fact=key)


def _general(b: Builder) -> None:
    for pertanyaan, jawaban in GENERAL:
        b.add(pertanyaan, jawaban, "pengetahuan", fact=f"umum-{pertanyaan}")


def build_facts(b: Builder) -> None:
    _tech(b)
    _health(b)
    _science(b)
    _mathc(b)
    _civics(b)
    _sports(b)
    _env(b)
    _howto(b)
    _general(b)
