"""Bagian 4 generator `chat.jsonl`:
- Mengatur uang harian, tabungan kecil, & belanja bijak
- Karier pemula, magang, & adaptasi dunia kerja
- Dilema pilihan sehari-hari ("mending A atau B?")
- Kesehatan ringan, tidur, & kebugaran harian
- Masalah praktis HP, laptop, & kebiasaan digital sehari-hari
"""
from __future__ import annotations

from .core_v2 import CategoryCollector

# --------------------------------------------------------------------------- #
# 1. Keuangan Harian & Mengatur Uang (24 topik x 16 kondisi x 6 gaya)
# --------------------------------------------------------------------------- #
MONEY_TOPICS = [
    ("uang saku atau gaji bulanan cepat habis sebelum tanggal dua puluh", "pisahkan jatah makan wajib dan tabungan tepat di hari pertama uang masuk ke rekening terpisah", "mengandalkan sisa uang di akhir bulan hampir selalu berujung nol karena terpakai belanja kecil"),
    ("sering tergoda beli barang lucu waktu promo tanggal kembar", "masukkan barangnya ke keranjang lalu wajibkan diri menunggu 48 jam sebelum menekan tombol bayar", "dorongan belanja impulsif biasanya menguap sendiri setelah lewat dua malam"),
    ("bingung mulai mengumpulkan dana darurat dari nominal kecil", "mulai saja sisihkan Rp10.000 sampai Rp20.000 rutin ke wadah terpisah yang tidak terhubung kartu belanja harian", "konsistensi menyisihkan nominal kecil jauh lebih penting daripada menunggu punya uang besar"),
    ("uang receh jajan kopi dan camilan sore ternyata bocor besar sebulan", "tetapkan kuota jajan minuman manis maksimal dua kali seminggu dan bawa botol minum serta seduhan sendiri di hari lainnya", "pengeluaran kecil yang berulang tiap hari sering tidak terasa sampai dijumlahkan sebulan"),
    ("malas mencatat pengeluaran karena terasa ribet banget", "cukup buat tiga batas amplop besar saja: kebutuhan pokok, transportasi, dan hiburan bebas tanpa mencatat tiap permen", "sistem pencatatan yang terlalu rumit biasanya cuma bertahan tiga hari lalu ditinggalkan"),
    ("bingung membagi penghasilan pertama waktu baru mulai kerja", "coba patokan awal 50 persen kebutuhan hidup, 30 persen keinginan wajar, dan 20 persen tabungan sambil disesuaikan biaya kotamu", "punya kerangka kasar sejak gaji pertama mencegah gaya hidup langsung melonjak liar"),
    ("sering boncos gara-gara ongkos kirim pesan makanan online", "masak nasi putih sendiri di rumah lalu beli lauk matang di warung dekat tempat tinggal sambil jalan kaki sebentar", "ongkos kirim dan biaya layanan aplikasi kalau dikumpulkan sebulan bisa setara makan seminggu"),
    ("ragu mau beli barang murah tapi cepat rusak atau agak mahal tapi awet", "untuk barang yang dipakai setiap hari seperti sepatu jalan atau tas kerja, pilih kualitas menengah yang kuat jahitannya", "membeli barang murah tiga kali dalam setahun jatuhnya lebih mahal daripada satu barang awet"),
    ("sungkan menolak ajakan makan di tempat mahal bareng teman", "usulkan tempat makan alternatif yang ramah kantong atau jujur bilang sedang menjaga pos pengeluaran minggu ini", "teman yang sehat pergaulannya tidak akan mengukur pertemanan dari mahalnya tempat nongkrong"),
    ("tagihan langganan aplikasi bulanan diam-diam memotong saldo", "daftar semua langganan aktif hari ini lalu matikan perpanjangan otomatis pada layanan yang sebulan terakhir jarang dibuka", "biaya langganan kecil yang terlupakan adalah kebocoran saldo paling klasik"),
    ("ingin menabung buat beli laptop belajar tanpa berutang", "hitung harga targetnya lalu bagi ke jumlah bulan realistis dan simpan di tabungan khusus yang terpisah dari uang jajan", "melihat grafik progres tabungan bertambah tiap minggu bikin semangat menabung terjaga"),
    ("bingung membedakan kebutuhan beneran sama lapar mata sesaat", "tanyakan ke diri sendiri: kalau barang ini tidak dibeli minggu ini, apakah sekolah atau kerjaku bakal terganggu?", "jika jawabannya tidak terganggu sama sekali, berarti barang itu masuk kategori keinginan yang aman ditunda"),
    ("pengeluaran membengkak waktu musim banyak undangan acara teman", "siapkan pos sosial kecil tiap bulan sejak jauh hari supaya saat ada undangan tidak mengganggu jatah makan harian", "merencanakan pos kondangan atau kado sejak awal menyelamatkan arus kas bulanan"),
    ("uang tunai di dompet sering habis tanpa ingat dipakai apa saja", "tarik uang tunai secukupnya untuk jatah tiga hari saja dan simpan bukti struk sampai malam sebelum direkap singkat", "membatasi uang tunai harian di dompet otomatis mengerem jajan spontan di pinggir jalan"),
    ("tergiur fitur bayar nanti (paylater) buat beli barang non-darurat", "hindari cicilan konsumtif untuk barang hiburan karena bunga dan denda keterlambatannya bisa menumpuk cepat", "membiasakan beli tunai sesuai kemampuan membuat tidur malam jauh lebih tenang tanpa bayang-bayang tagihan"),
    ("harga bahan makanan naik sehingga uang belanja mingguan terasa sempit", "susun daftar menu seminggu dulu sebelum ke pasar dan utamakan sumber protein lokal bergizi seperti telur, tahu, dan tempe", "pergi belanja dengan daftar tertulis mencegah tangan mengambil barang di luar rencana"),
]

MONEY_CONTEXTS = [
    ("sebagai mahasiswa rantau yang ngatur uang bulanan sendiri", "Hidup merantau memang kuncinya mengamankan biaya kos dan makan pokok lebih dulu di minggu pertama."),
    ("waktu baru dapat penghasilan magang pertama kali", "Uang hasil keringat sendiri memang menggoda buat dihabiskan, tapi menyisihkan sedikit sejak awal bakal bikin kamu bangga."),
    ("pas lagi tinggal bareng orang tua tapi pengen mandiri", "Mumpung biaya tempat tinggal masih terbantu di rumah, porsi menabungmu sebenarnya bisa dibuat lebih longgar."),
    ("waktu pemasukan bulanan belum tetap alias naik-turun", "Kalau pendapatan fluktuatif, patok gaya hidupmu memakai angka bulan paling sepi supaya tetap aman."),
    ("menjelang libur panjang yang biasanya banyak pengeluaran", "Menyiapkan batas anggaran khusus sebelum musim liburan menjaga tabungan utamamu tetap utuh."),
    ("setelah bulan lalu sempat kebablasan belanja banyak", "Nggak usah menyesal berlarut-larut soal bulan lalu; jadikan bahan evaluasi buat mengerem pos hiburan bulan ini."),
    ("padahal target tabunganku tahun ini lumayan penting", "Tempel catatan tujuan tabunganmu di tempat yang sering terlihat biar kamu ingat prioritas utamanya."),
    ("tanpa harus hidup terlalu pelit sampai menyiksa diri", "Berhemat yang sehat itu memotong yang mubazir, bukan memangkas makan bergizi atau istirahatmu."),
    ("waktu harga kebutuhan harian lagi berasa naik", "Di situasi harga naik, membandingkan harga satuan per gram atau liter di rak toko lumayan banget menghemat."),
    ("supaya nggak perlu pinjam uang ke teman di akhir bulan", "Kemandirian menjaga cukupnya uang sampai tanggal gajian bikin pikiran tenang dan harga diri terjaga."),
    ("sambil tetap menyisihkan sedikit buat hiburan akhir pekan", "Memberi jatah hiburan kecil yang terukur justru mencegah efek balas dendam belanja besar di kemudian hari."),
    ("buat membangun kebiasaan finansial sehat dari muda", "Kebiasaan mengatur uang Rp100.000 dengan rapi adalah fondasi sebelum nanti mengelola nominal jutaan."),
]


# --------------------------------------------------------------------------- #
# 2. Karier Pemula, Magang, & Dunia Kerja Sehari-hari (16 topik x 12 kondisi x 6 gaya)
# --------------------------------------------------------------------------- #
CAREER_TOPICS = [
    ("grogi menjawab pertanyaan 'ceritakan tentang dirimu' saat wawancara", "rangkum dalam tiga bagian singkat: latar belakang belajarmu, satu pengalaman relevan yang pernah dikerjakan, dan alasan melamar posisi tersebut", "pewawancara mencari benang merah kemampuanmu dalam dua menit, bukan biodata panjang sejak SD"),
    ("bingung menjawab pertanyaan kelemahan diri waktu interview kerja", "sebutkan satu kekurangan nyata yang tidak fatal bagi posisi itu lalu jelaskan langkah konkret yang sedang kamu lakukan untuk memperbaikinya", "jawaban jujur yang disertai usaha perbaikan terdengar jauh lebih matang daripada mengaku sempurna"),
    ("takut salah bertanya di minggu pertama magang atau kerja baru", "kumpulkan beberapa pertanyaan kecil sekaligus di buku catatan lalu tanyakan di waktu rekan senior tidak sedang dikejar tenggat", "mencatat jawaban mereka supaya tidak menanyakan hal yang sama dua kali akan meninggalkan kesan sangat baik"),
    ("merasa kemampuan belum selevel rekan kerja lain di kantor", "fokus menyerap alur kerja dasar timmu satu per satu dan minta umpan balik spesifik pada tugas pertamamu", "setiap orang ahli di ruangan itu juga pernah melewati fase bingung di bulan pertamanya"),
    ("tugas dari atasan instruksinya kurang jelas batasannya", "ulangi pemahamanmu dalam dua-tiga poin singkat lewat pesan atau lisan lalu tanyakan apakah arah tersebut sudah sesuai ekspektasi", "konfirmasi lima menit di awal menyelamatkan berjam-jam kerja ulang karena salah arah"),
    ("CV terasa kosong karena belum punya pengalaman kerja resmi", "tonjolkan proyek kuliah, kepanitiaan, kerja sukarela, atau portofolio latihan mandiri lengkap dengan hasil terukurnya", "perekrut pemula menilai inisiatif dan kemampuan menyelesaikan masalah, bukan semata-mata nama perusahaan besar"),
    ("pekerjaan menumpuk di jam empat sore menjelang jam pulang", "urutkan mana yang benar-benar jatuh tempo hari ini dan mana yang aman dikerjakan segar besok pagi jam pertama", "memaksakan kerja rumit saat otak sudah kelelahan sore hari justru rawan melahirkan kesalahan ketik"),
    ("bekerja dari rumah (remote) bikin batas jam kerja dan istirahat kabur", "tentukan jam mulai dan jam tutup laptop yang tegas, serta gunakan meja khusus di luar kasur", "ritual menutup laptop dan berganti pakaian santai membantu otak sadar bahwa jam kerja sudah selesai"),
    ("menerima revisi banyak pada draf pekerjaan pertama", "pisahkan perasaan pribadi dari dokumen kerjamu, lalu tandai tiap poin masukan sebagai daftar periksa perbaikan", "revisi di awal kerja adalah cara tercepat memahami standar kualitas tim barumu"),
    ("bingung menulis email atau pesan pengantar saat mengirim lamaran", "tulis subjek yang jelas memuat posisi dan namamu, lalu isi badan pesan maksimal dua paragraf ringkas yang sopan", "perekrut memeriksa puluhan berkas sehari, jadi pesan yang ringkas dan rapi paling disukai"),
    ("leher dan punggung sering pegal karena duduk di depan komputer seharian", "sejajarkan tinggi layar dengan pandangan mata dan berdiri berjalan mengambil air minum setiap satu jam sekali", "postur menunduk berjam-jam memberi beban berlipat pada otot leher belakang"),
    ("ragu memilih antara tawaran magang dekat rumah atau di kota besar", "hitung selisih biaya hidup bersihnya lalu bandingkan mana yang memberi mentor serta ruang belajar paling nyata buat tujuanmu", "tempat yang membimbingmu tumbuh langsung di proyek nyata sering lebih berharga bagi karier awal"),
]

CAREER_CONTEXTS = [
    ("sebagai lulusan baru yang pertama kali terjun kerja", "Sebagai pendatang baru, kemauan belajar cepat dan sikap ramah adalah modal terkuatmu."),
    ("waktu melamar posisi magang semester akhir", "Di tahap magang, perusahaan memang menyiapkan ruang belajar asalkan kamu proaktif bertanya."),
    ("pas pindah ke bidang yang agak beda dari jurusan kuliah", "Latar belakang berbeda justru sering memberi sudut pandang segar selama dasar teknisnya kamu kejar."),
    ("di tim yang ritme kerjanya lumayan cepat", "Di lingkungan serba cepat, komunikasi singkat yang langsung ke poin utama bakal sangat dihargai."),
    ("waktu komunikasinya banyak lewat chat online tanpa tatap muka", "Karena tidak bertemu langsung, kejelasan tulisan dan ketepatan waktu merespons jadi cerminan utamamu."),
    ("padahal aku tipe orang yang pemalu dan pendiam", "Orang yang tenang tetap bisa bersinar lewat hasil kerja yang rapi dan catatan yang terstruktur."),
    ("menjelang jadwal wawancara besok pagi", "Malam ini cukup latihan bicara pelan dua kali lalu tidur tepat waktu supaya besok suaramu segar."),
    ("setelah sempat gagal di wawancara sebelumnya", "Pengalaman wawancara kemarin sebenarnya latihan berharga yang bikin kamu lebih siap menghadapi pertanyaan kali ini."),
    ("supaya terlihat profesional tapi nggak kaku", "Profesional itu intinya tepat janji, jelas komunikasinya, dan menghargai waktu rekan kerja."),
    ("waktu harus membagi fokus sama sisa tugas kampus", "Jujurlah soal jadwal kuliahmu sejak awal supaya ekspektasi tim tidak berbenturan di tengah jalan."),
]


# --------------------------------------------------------------------------- #
# 3. Dilema Pilihan Sehari-hari "Mending A atau B?" (18 dilema x 12 kondisi x 6 gaya)
# --------------------------------------------------------------------------- #
AB_DILEMMAS = [
    ("ngekos dekat banget sama kampus tapi agak mahal atau agak jauh tapi murah", "kos dekat menghemat tenaga dan ongkos harian, sedangkan kos agak jauh menghemat uang sewa bulanan asalkan akses jalannya mudah", "hitung total sewa ditambah ongkos transportasi sebulan penuh supaya perbandingannya adil"),
    ("belajar pagi subuh habis bangun tidur atau malam hari sebelum tidur", "pagi hari unggul karena otak baru istirahat dan suasana tenang, sementara malam cocok untuk mengulang ringkasan materi ringan", "pilih waktu di mana kamu paling jarang terdistraksi HP dan tetap dapat tidur minimal tujuh jam"),
    ("beli buku cetak fisik atau baca buku digital di layar", "buku fisik lebih nyaman di mata dan enak dicoret catatan pinggir, sedangkan buku digital praktis dibawa ke mana-mana dan sering lebih hemat", "untuk buku referensi belajar mendalam biasanya cetak lebih fokus, sementara bacaan ringan praktis di digital"),
    ("olahraga pagi sebelum beraktivitas atau sore hari sepulang kegiatan", "olahraga pagi bikin badan segar sejak awal hari, sedangkan sore hari otot tubuh sudah lentur dan bisa sekalian melepas penat harian", "waktu olahraga terbaik adalah jadwal yang paling sanggup kamu jalani rutin tiga kali seminggu"),
    ("masak sendiri tiap hari atau langganan warung makan rumahan", "masak sendiri menang di kebersihan dan hemat biaya, sedangkan warung rumahan menang di penghematan waktu saat jadwalmu padat", "jalan tengah paling enak adalah masak nasi sendiri lalu selingi masak lauk gampang dan beli sayur matang"),
    ("belajar sendiri di kamar tenang atau belajar bareng teman di perpustakaan", "belajar sendiri lebih cepat untuk memahami konsep dasar, sedangkan belajar bareng efektif buat saling menguji pemahaman", "pahami materinya sendiri dulu satu jam, baru diskusi bareng teman supaya nggak berubah jadi ngobrol doang"),
    ("servis barang elektronik lama yang rusak ringan atau sekalian beli baru", "jika biaya servis di bawah sepertiga harga baru dan umurnya belum terlalu tua, servis masih sangat layak dipilih", "kalau kerusakannya sudah berulang tiap bulan sampai menghambat tugas, menabung unit baru lebih menenangkan"),
    ("naik transportasi umum atau bawa kendaraan sendiri buat harian", "transportasi umum membebaskanmu dari lelah menyetir di kemacetan, sedangkan kendaraan pribadi lebih fleksibel kalau harus mampir banyak tempat", "coba bandingkan waktu tempuh pintu-ke-pintu dan tingkat lelah badanmu saat sampai tujuan"),
    ("minum kopi atau teh hangat buat teman fokus kerja pagi", "kopi memberi dorongan kafein lebih kuat dengan cepat, sedangkan teh memberikan fokus lebih halus tanpa bikin jantung mudah berdebar", "kalau perutmu sensitif asam di pagi hari, pastikan isi perut dengan sarapan dulu sebelum ngopi"),
    ("langsung kerja mencari pengalaman setelah lulus atau lanjut studi dulu", "bekerja dulu memberi gambaran nyata kebutuhan lapangan dan kemandirian finansial, sedangkan lanjut studi cocok bila bidangmu memang mensyaratkan spesialisasi akademik", "melihat dunia kerja setahun-dua tahun sering kali membuat pilihan jurusan studi lanjutan jauh lebih terarah"),
    ("mencatat pakai buku tulis dan pulpen atau aplikasi catatan di laptop/HP", "menulis tangan membantu daya ingat konsep lebih kuat, sedangkan catatan digital unggul saat perlu dicari ulang dengan kata kunci", "banyak orang memadukan kertas untuk coretan ide awal lalu merapikan poin pentingnya ke aplikasi digital"),
    ("liburan singkat dekat kota tiap bulan atau nabung buat satu perjalanan jauh setahun", "istirahat singkat dekat kota menjaga kewarasan rutin tanpa menguras tabungan, sementara perjalanan jauh memberi pengalaman suasana yang benar-benar baru", "sesuaikan dengan tingkat kejenuhanmu sekarang—kadang tidur nyenyak dan jalan ke taman kota sudah cukup menyegarkan"),
]

AB_PRIORITIES = [
    ("kalau bujet bulananku lagi lumayan ketat", "Karena faktor hemat lagi jadi prioritas utama, opsi yang paling menekan biaya rutin bulanan layak dimenangkan dulu."),
    ("kalau waktuku sehari-hari padat banget dari pagi sampai sore", "Berhubung waktumu sangat terbatas, pilih opsi yang paling memangkas kerepotan dan menghemat menit perjalanan."),
    ("kalau badanku gampang capek dan butuh jaga stamina", "Mengingat kesehatan fisikmu nomor satu, utamakan pilihan yang paling ramah buat waktu istirahat tubuhmu."),
    ("kalau aku tipe orang yang gampang bosan sama suasana monoton", "Buat kamu yang butuh variasi suasana, pilih opsi yang paling fleksibel diubah-ubah sesuai mood mingguan."),
    ("kalau target utamaku semester ini adalah naikin fokus belajar", "Demi mengejar fokus akademik, menangkan pilihan yang paling minim gangguan dan paling mendukung konsentrasi."),
    ("kalau aku baru pertama kali nyoba ngatur semuanya mandiri", "Untuk tahap awal mandiri, ambil pilihan yang paling sederhana risikonya supaya kamu mudah beradaptasi."),
    ("kalau jarak tempuh di kotaku lumayan rawan macet dan hujan", "Di kota yang cuacanya sulit ditebak dan macet, faktor dekat serta praktis bakal terasa berkahnya setiap hari."),
    ("kalau aku pengen solusi yang tahan lama buat setahun ke depan", "Untuk horizon setahun penuh, hitung kenyamanan jangka panjangnya, bukan cuma murahnya di minggu pertama."),
]


# --------------------------------------------------------------------------- #
# 4. Kesehatan Ringan & Masalah Digital Harian (20 topik x 10 konteks x 6 gaya)
# --------------------------------------------------------------------------- #
WELLNESS_AND_TECH = [
    ("memori penyimpanan HP hampir penuh terus sampai lemot", "hapus file video besar di folder unduhan dan grup chat, bersihkan cache aplikasi berat, lalu cadangkan foto lama ke penyimpanan awan atau laptop", "sisakan ruang kosong minimal 10-15 persen agar sistem ponsel tidak tersendat saat membuka aplikasi"),
    ("baterai HP terasa makin boros padahal jarang dipakai main game", "cek menu penggunaan baterai untuk melihat aplikasi latar belakang yang aktif terus, kurangi kecerahan layar otomatis, dan matikan pencari lokasi yang tidak perlu", "sinyal seluler yang lemah di dalam gedung juga memaksa ponsel bekerja ekstra hingga menguras daya"),
    ("laptop mulai terasa berat dan kipasnya bunyi kencang waktu buka banyak tab", "tutup tab browser yang sudah tidak dibaca, cek program yang ikut menyala otomatis saat laptop baru hidup, dan pastikan lubang ventilasi bawah tidak tertutup kasur", "menaruh laptop langsung di atas bantal atau kasur menyumbat aliran udara dingin sehingga mesin cepat panas"),
    ("takut kena tautan penipuan (phishing) yang masuk lewat pesan singkat", "jangan pernah mengeklik tautan mencurigakan atau menginstal file `.apk` kiriman nomor asing, dan cek alamat domain resmi secara manual di browser", "instansi resmi maupun bank tidak pernah meminta kode rahasia OTP atau PIN lewat pesan chat"),
    ("file tugas di folder laptop berantakan sampai susah dicari waktu butuh cepat", "buat struktur folder sederhana per semester atau proyek dan beri nama file berformat tanggal-topik seperti `2026-10-laporan-biologi.pdf`", "nama file yang jelas jauh lebih menyelamatkan waktu daripada puluhan dokumen bernama ` revisi-final-banget`"),
    ("sering lupa minum air putih karena keasyikan duduk depan meja", "taruh botol minum ukuran terukur tepat di sebelah layar kerja dan biasakan minum beberapa teguk setiap selesai satu sub-tugas", "menunggu sampai tenggorokan kering sekali sebenarnya tanda tubuh sudah mulai kekurangan cairan ringan"),
    ("punggung bawah dan bahu terasa kaku habis duduk lama", "berdiri setiap 45-60 menit untuk memutar bahu perlahan, merentangkan tangan ke atas, dan berjalan kecil satu menit", "otot manusia dirancang untuk bergerak bergantian, bukan terkunci di satu sudut kursi berjam-jam"),
    ("tenggorokan mulai terasa agak gatal habis kehujanan atau kurang tidur", "perbanyak minum air hangat, kurangi gorengan berminyak untuk sementara, berkumur air garam hangat tipis, dan tidur lebih awal malam ini", "kalau disertai demam tinggi atau nyeri menelan hebat beberapa hari, sebaiknya periksa ke dokter"),
    ("susah mengurangi kebiasaan minum minuman kemasan manis tiap hari", "kurangi bertahap dengan mencampur air putih dingin dan irisan jeruk nipis segar atau pilih teh tawar dingin saat cuaca terik", "lidah kita biasanya hanya butuh satu-dua minggu untuk terbiasa lagi menikmati rasa segar tanpa gula tinggi"),
    ("kaki terasa pegal linu setelah seharian banyak berdiri atau jalan jauh", "rendam telapak kaki di air hangat selama sepuluh menit lalu ganjal pergelangan kaki sedikit lebih tinggi menggunakan bantal saat berbaring", "posisi kaki sedikit terangkat membantu aliran balik darah sehingga rasa berat di betis lebih cepat reda"),
]

WT_CONTEXTS = [
    ("apalagi barang/kondisi ini kupakai kerja dan belajar tiap hari", "Karena dipakai harian, merawat hal kecil dari sekarang mencegah gangguan besar pas lagi sibuk-sibuknya."),
    ("waktu lagi banyak tenggat minggu ini", "Di minggu padat begini, langkah beres-beres 10 menit malam ini bakal menyelamatkan waktumu besok pagi."),
    ("tanpa harus keluar biaya tambahan", "Enaknya lagi, langkah ini gratis dan bisa langsung kamu praktikkan sekarang juga."),
    ("padahal sebelumnya aku jarang merhatiin hal sepele gini", "Nggak ada kata terlambat buat mulai kebiasaan rapi; perubahan kecil hari ini langsung kerasa bedanya."),
    ("biar ke depannya lebih nyaman dan awet", "Perawatan rutin ringan kayak gini jauh lebih mudah daripada memperbaiki saat sudah terlanjur parah."),
    ("waktu lagi di rumah atau kamar kos akhir pekan ini", "Mumpung agak senggang di rumah, pas banget meluangkan lima belas menit buat membereskannya."),
]


def build_chat_life(col: CategoryCollector, limit: int | None = None) -> None:
    pair_idx = 0

    # 1. Keuangan harian (16 * 12 * 6 = 1.152)
    m_q = [
        "nara, aku punya masalah {prob} {ctx}, gimana cara ngaturnya?",
        "kasih tips keuangan praktis dong: {prob} {ctx}",
        "gimana ya biar nggak {prob} {ctx}?",
        "bantuin saran hemat nara, soalnya {prob} {ctx}",
        "eh nara, kalau {prob} {ctx}, langkah pertamanya apa?",
        "cara bijak mengatasi {prob} {ctx} gimana?",
    ]
    m_a = [
        "Soal uang harian memang butuh trik sederhana: coba {fix}. {ctx_note} Soalnya, {why}.",
        "Langkah paling realistis buat kondisimu adalah {fix}. {ctx_note} Perlu diingat, {why}.",
        "Nggak perlu pakai rumus rumit, mulai aja dengan {fix}. {ctx_note} Alasannya jelas: {why}.",
        "Kalau boleh kasih saran praktis, langsung {fix}. {ctx_note} Kenapa begitu? Karena {why}.",
        "Coba rapikan pelan-pelan lewat kebiasaan ini: {fix}. {ctx_note} Ingat ya, {why}.",
        "Trik yang paling terasa dampaknya adalah {fix}. {ctx_note} Sebab dalam keseharian, {why}.",
    ]
    for prob, fix, why in MONEY_TOPICS:
        for ctx, ctx_note in MONEY_CONTEXTS:
            pair_idx += 1
            for k in range(len(m_q)):
                if limit and len(col.rows) >= limit:
                    return
                q = m_q[k].format(prob=prob, ctx=ctx)
                a = m_a[(k + pair_idx) % len(m_a)].format(
                    fix=fix, why=why, ctx_note=ctx_note
                )
                col.add(q, a)

    # 2. Karier pemula & kerja (12 * 10 * 6 = 720)
    c_q = [
        "nara, aku lagi menghadapi masalah {prob} {ctx}, sarannya gimana?",
        "gimana tips menghadapi situasi {prob} {ctx}?",
        "tolong bantu saran dunia kerja dong: {prob} {ctx}",
        "kalau {prob} {ctx}, sebaiknya aku ngapain ya?",
        "eh nara, wajar nggak kalau {prob} {ctx}? terus solusinya apa?",
        "kasih masukan santai buat {prob} {ctx} dong",
    ]
    c_a = [
        "Wajar banget mengalami hal itu! Coba {fix}. {ctx_note} Kuncinya, {why}.",
        "Pendekatan paling rapi untuk situasi tersebut adalah {fix}. {ctx_note} Ingat bahwa {why}.",
        "Kamu bisa menyikapinya dengan langkah tenang: {fix}. {ctx_note} Soalnya, {why}.",
        "Saran praktis dariku, langsung coba {fix}. {ctx_note} Alasannya sederhana: {why}.",
        "Jangan panik dulu, atur dengan cara {fix}. {ctx_note} Sebab di dunia kerja, {why}.",
        "Langkah kecil yang sangat membantu adalah {fix}. {ctx_note} Pegang satu hal ini: {why}.",
    ]
    for prob, fix, why in CAREER_TOPICS:
        for ctx, ctx_note in CAREER_CONTEXTS:
            pair_idx += 1
            for k in range(len(c_q)):
                if limit and len(col.rows) >= limit:
                    return
                q = c_q[k].format(prob=prob, ctx=ctx)
                a = c_a[(k + pair_idx) % len(c_a)].format(
                    fix=fix, why=why, ctx_note=ctx_note
                )
                col.add(q, a)

    # 3. Dilema pilihan A atau B (12 * 8 * 6 = 576)
    ab_q = [
        "nara, menurutmu mending {dilemma} {prio}?",
        "aku bingung milih nih: {dilemma} {prio}?",
        "bantu timbang plus minus {dilemma} {prio} dong!",
        "kalau posisiku {prio}, lebih pas {dilemma}?",
        "eh nara, enaknya pilih mana ya antara {dilemma} {prio}?",
        "minta pertimbangan santai dong soal {dilemma} {prio}",
    ]
    ab_a = [
        "Dua-duanya punya nilai plus sendiri: {comp}. {prio_note} Tips praktisnya, {rule}.",
        "Kalau ditimbang adil, {comp}. {prio_note} Biar makin mantap memutuskan, {rule}.",
        "Yuk kita bandingkan singkat: {comp}. {prio_note} Saran dariku, {rule}.",
        "Sebenarnya nggak ada yang mutlak salah, karena {comp}. {prio_note} Jadi coba {rule}.",
        "Menarik nih pilihannya! Secara umum, {comp}. {prio_note} Langkah penentunya: {rule}.",
        "Biar nggak bingung berkepanjangan, lihat sisi praktisnya: {comp}. {prio_note} Terakhir, {rule}.",
    ]
    for dilemma, comp, rule in AB_DILEMMAS:
        for prio, prio_note in AB_PRIORITIES:
            pair_idx += 1
            for k in range(len(ab_q)):
                if limit and len(col.rows) >= limit:
                    return
                q = ab_q[k].format(dilemma=dilemma, prio=prio)
                a = ab_a[(k + pair_idx) % len(ab_a)].format(
                    comp=comp, rule=rule, prio_note=prio_note
                )
                col.add(q, a)

    # 4. Kesehatan ringan & teknologi harian (10 * 6 * 6 = 360)
    wt_q = [
        "nara, gimana cara beresin masalah {prob} {ctx}?",
        "kasih solusi praktis dong kalau {prob} {ctx}",
        "aduh {prob} nih {ctx}, enaknya diapain ya?",
        "ada tips gampang buat mengatasi {prob} {ctx}?",
        "eh nara, bantu trik harian dong: {prob} {ctx}",
        "kalau mengalami {prob} {ctx}, langkah amannya apa?",
    ]
    wt_a = [
        "Bisa diatasi pelan-pelan kok! Coba {fix}. {ctx_note} Perlu diingat juga, {why}.",
        "Langkah paling praktis yang bisa langsung dicoba: {fix}. {ctx_note} Soalnya, {why}.",
        "Coba tangani mulai dari hal dasar dulu: {fix}. {ctx_note} Alasannya, {why}.",
        "Solusi sederhananya begini: {fix}. {ctx_note} Sekadar pengingat tambahan, {why}.",
        "Kamu cukup melakukan langkah ringan ini: {fix}. {ctx_note} Kenapa penting? Karena {why}.",
        "Biar cepat beres, langsung {fix}. {ctx_note} Catatan kecilnya: {why}.",
    ]
    for prob, fix, why in WELLNESS_AND_TECH:
        for ctx, ctx_note in WT_CONTEXTS:
            pair_idx += 1
            for k in range(len(wt_q)):
                if limit and len(col.rows) >= limit:
                    return
                q = wt_q[k].format(prob=prob, ctx=ctx)
                a = wt_a[(k + pair_idx) % len(wt_a)].format(
                    fix=fix, why=why, ctx_note=ctx_note
                )
                col.add(q, a)
