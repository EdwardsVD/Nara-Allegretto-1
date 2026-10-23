"""Bagian 8 generator `chat.jsonl`:
- Mengatasi rasa mager (malas gerak) & kejenuhan harian
- Menyesuaikan kegiatan harian dengan cuaca & musim di Indonesia
- Bantuan menyusun ucapan, catatan singkat, & kata-kata harian
- Kemandirian mengurus urusan praktis sehari-hari
- Obrolan santai reflektif & brainstorming ide harian
"""
from __future__ import annotations

from .core_v2 import CategoryCollector

# 1. Mengatasi rasa mager & kejenuhan harian (24 x 14 x 7 = 2.352)
MAGER_SITUATIONS = [
    ("mager banget beranjak mandi di pagi hari libur", "siapkan handuk dan baju ganti bersih lebih dulu lalu hitung mundur lima sampai satu sambil langsung berdiri menuju kamar mandi", "rasa segan mandi itu sembilan puluh persen cuma ada sebelum air pertama menyentuh badan; sesudahnya badan langsung segar"),
    ("malas mulai melipat tumpukan cucian bersih di kursi", "putar satu lagu berdurasi empat menit atau episode pendek sambil menargetkan melipat pakaian kategori kaos saja dulu", "begitu tangan mulai melipat tiga potong pertama, sisa tumpukannya biasanya ikut selesai tanpa terasa berat"),
    ("kehilangan semangat di tengah jalan waktu belajar topik panjang", "ganti metode dari membaca diam menjadi menggambar bagan panah sederhana di kertas kosong menggunakan spidol warna", "perubahan cara belajar dari teks rapat ke visual langsung membangunkan rasa ingin tahu otak yang mulai bosan"),
    ("malas olahraga sore padahal sepatu sudah disiapkan", "turunkan targetnya jadi cukup ganti pakaian olahraga dan jalan kaki santai sepuluh menit saja di depan rumah", "memberi izin melakukan versi paling ringan hampir selalu mengalahkan rasa malas memulai"),
    ("menunda membalas pesan-pesan yang menumpuk di aplikasi chat", "luangkan satu blok waktu lima belas menit khusus untuk membalas mulai dari pesan paling singkat dan paling mendesak dulu", "membiarkan pesan menggantung berhari-hari justru menyedot energi pikiran setiap kali teringat"),
    ("jenuh memakan menu lauk yang rasanya mirip terus seminggu ini", "ubah cara olah atau bumbunya—misalnya dari digoreng biasa menjadi ditumis pedas kemangi atau berkuah bening jeruk nipis", "aroma daun rempah segar seperti kemangi, daun jeruk, atau serai langsung membangkitkan selera makan"),
    ("enggan membereskan meja kerja yang penuh kertas dan kabel", "singkirkan semua cangkir kotor dan sampah kertas ke tempatnya lebih dulu dalam tiga menit tanpa menyortir arsip dulu", "permukaan meja yang kembali terlihat lapang langsung memberi dorongan semangat melanjutkan kerapian sisanya"),
    ("mager keluar kamar buat beli kebutuhan kecil di warung", "gabungkan urusan ke warung dengan niat mencari udara segar sore dan melemaskan kaki yang kaku seharian duduk", "paparan cahaya luar ruangan lima menit ampuh mengusir rasa suntuk terkurung di dalam kamar"),
    ("malas mencuci botol minum dan kotak bekal sepulang kegiatan", "langsung keluarkan kotak bekal dari tas begitu membuka pintu rumah dan rendam air sabun hangat sebelum ganti baju", "merendam lebih awal membuat sisa makanan mudah luruh tanpa perlu menggosok keras malam nanti"),
    ("suntuk menunggu antrean panjang yang membosankan", "manfaatkan waktunya untuk menghapus foto tangkapan layar lama yang memenuhi galeri HP atau membaca artikel pendek yang disimpan", "mengisi waktu tunggu dengan beres-beres kecil digital bikin antrean terasa jauh lebih cepat bergerak"),
    ("berat memulai revisi tulisan yang kemarin dicoret banyak", "mulai perbaiki dari bagian salah ketik dan ejaan paling mudah lebih dulu sebelum menyentuh perombakan paragraf besar", "kemenangan kecil menyelesaikan lima koreksi mudah memanaskan mesin fokusmu pelan-pelan"),
    ("bosan duduk belajar di sudut meja yang sama berbulan-bulan", "geser posisi kursi, bersihkan pajangan yang terlalu ramai, atau pindah belajar sejam ke teras berangin maupun perpustakaan", "suasana pandang mata yang baru memberi sinyal segar sehingga otak tidak cepat mengantuk"),
    ("malas memasak malam hari karena badan sudah terlanjur lelah", "sediakan stok penyelamat cepat seperti telur, tahu, dan sayur beku bersih yang siap masuk panci dalam lima menit", "punya menu darurat sepuluh menit mencegahmu melewatkan makan malam atau jajan berlebihan"),
    ("enggan merapikan catatan keuangan mingguan yang tertunda", "cukup cek mutasi transaksi digital lima menit sambil minum teh sore tanpa menuntut selisih seribu rupiah harus ketemu semua", "gambaran besar arus uang yang rutin dicek jauh lebih berguna daripada catatan sempurna yang cuma dibuat setahun sekali"),
    ("merasa hampa dan bingung mau ngapain setelah ujian besar selesai", "beri jeda istirahat murni sehari penuh tanpa rasa bersalah, lalu besoknya pilih satu kegiatan hobi ringan yang sempat tertunda", "rasa kosong seusai mengejar target besar itu normal karena tubuh sedang turun dari mode tegang tinggi"),
    ("malas menyisir dan merapikan penampilan waktu kerja di rumah saja", "tetap cuci muka segar dan kenakan pakaian rumah yang bersih rapi di pagi hari agar otak masuk ke suasana siap berkarya", "pakaian tidur seharian penuh sering membuat tubuh terbawa suasana setengah mengantuk terus"),
    ("kehabisan ide kreatif waktu diminta memberi usulan di rapat tim", "tuliskan dulu lima ide paling sederhana bahkan yang terdengar biasa saja di kertas, lalu gabungkan dua di antaranya", "menyensor ide sendiri terlalu cepat di kepala justru menyumbat keluarnya gagasan segar berikutnya"),
    ("malas membaca ulang draf tugas sebelum tombol kirim ditekan", "baca teksnya dengan suara pelan dari kalimat paling bawah naik ke atas atau ubah sebentar jenis hurufnya agar mata lebih jeli", "telinga langsung peka menangkap kalimat janggal yang sering terlewat saat dibaca cepat dalam hati"),
    ("jenuh menghafal istilah teknis yang terdengar asing semua", "buat jembatan keledai lucu dari singkatan suku kata pertamanya atau hubungkan bunyinya dengan benda akrab di sekitarmu", "asosiasi unik dan sedikit jenaka jauh lebih awet menempel di ingatan daripada hafalan kaku"),
    ("malas bangun dari sofa setelah keasyikan menonton satu jam", "pasang pengingat berdiri saat kredit penutup muncul lalu langsung matikan layar sebelum episode berikutnya terputar otomatis", "fitur putar otomatis memang dirancang mengunci perhatian, jadi memutusnya di detik jeda sangat efektif"),
]

MAGER_TRIGGERS = [
    ("apalagi cuaca lagi mendung sejuk bikin pengen selimutan", "Udara sejuk memang godaan terbesar kasur, jadi menyalakan lampu terang di kamar bakal sangat membantu membangunkan badan."),
    ("setelah berhari-hari kemarin tenagaku terkuras penuh", "Kalau memang habis minggu yang berat, pastikan bedakan antara malas biasa dan tubuh yang memang butuh tidur cukup dulu."),
    ("waktu di rumah lagi sepi nggak ada yang menyemangati", "Saat sendirian, pasang musik berirama ceria pelan-pelan lumayan banget menghidupkan suasana ruangan."),
    ("padahal sore nanti masih ada urusan lain yang menunggu", "Justru kalau dibereskan sepuluh menit sekarang, sore nanti kamu bebas melangkah tanpa beban pikiran menggantung."),
    ("sampai rasanya waktu sejam lewat gitu aja buat melamun", "Nggak usah menyesali satu jam yang sudah lewat; fokus selamatkan lima belas menit berikutnya aja."),
    ("waktu mood hari ini lagi datar-datar aja dari pagi", "Gerakan fisik kecil mendahului semangat—begitu badan bergerak sedikit, biasanya mood baik menyusul di belakangnya."),
    ("di hari Minggu siang yang suasananya tenang banget", "Di hari Minggu, kerjakan dengan tempo santai tanpa buru-buru supaya tetap terasa seperti hari istirahat."),
    ("padahal dalam hati tahu urusan itu sebenarnya sebentar", "Urusan lima menitan memang paling sering ditunda; hitung sampai tiga lalu langsung sentuh bagian pertamanya!"),
    ("gara-gara tadi terlanjur buka video pendek di HP", "Kunci layar HP lalu letakkan menghadap bawah agak jauh dulu supaya lingkaran dopamin cepatnya terputus."),
    ("supaya hari ini tetap ada satu hal produktif yang beres", "Satu keberhasilan kecil hari ini sudah cukup banget buat menjaga rasa percaya dirimu tetap menyala."),
    ("tanpa harus memaksa diri secara berlebihan", "Ingat prinsip pelan tapi jalan: selesai tujuh puluh persen jauh lebih baik daripada nol persen."),
    ("waktu badan rasanya agak kaku kurang gerak sejak pagi", "Awali dengan merentangkan kedua tangan ke atas dan memutar bahu tiga kali supaya aliran darah segar mengalir."),
]


# 2. Cuaca & Musim Indonesia dalam Kegiatan Harian (20 x 12 x 7 = 1.680)
WEATHER_ACTIONS = [
    ("berangkat sekolah atau kerja saat gerimis pagi mulai turun", "kenakan alas kaki tahan air atau bawa sandal cadangan di kantong plastik serta lindungi tas dengan sarung pelindung hujan", "kaos kaki kering cadangan di dalam tas adalah penyelamat kenyamanan sepanjang hari kalau sepatu sempat kena cipratan"),
    ("menjaga daya tahan tubuh di musim pancaroba yang cuacanya berubah cepat", "cukupkan waktu tidur malam, perbanyak makan sayur-buah hangat, dan selalu sedia air minum agar tenggorokan tidak kering", "perubahan suhu terik siang ke hujan sore menuntut tubuh beradaptasi ekstra sehingga istirahat cukup sangat krusial"),
    ("beraktivitas di luar ruangan saat kemarau siang sedang terik-teriknya", "gunakan topi atau payung, pilih pakaian katun longgar berwarna terang, oleskan tabir surya, dan minum air secara berkala", "warna kain terang memantulkan panas matahari jauh lebih baik dibanding pakaian gelap ketat"),
    ("mengeringkan pakaian cuci saat hujan turun hampir setiap hari", "peras cucian semaksimal mungkin di putaran pengering, gantung memakai gantungan baju berjarak satu jengkal di ruang berangin", "jarak longgar antar-gantungan memungkinkan udara mengalir membawa uap air pergi tanpa meninggalkan bau lembap"),
    ("merawat kendaraan motor atau sepeda yang habis menerobos hujan", "bilas bagian rantai, rem, dan kolong roda memakai air bersih biasa sesampainya di rumah agar pasir asam jalanan tidak memicu karat", "air hujan jalanan mengandung lumpur halus yang bila dibiarkan mengering membuat rantai cepat aus berbunyi"),
    ("menghadapi udara dingin berkabut waktu berkunjung ke daerah pegunungan", "gunakan teknik pakaian berlapis mulai dari kaos dalam menyerap keringat, baju hangat tengah, hingga jaket penahan angin di luar", "tiga lapis pakaian tipis-sedang menghangatkan tubuh lebih fleksibel daripada satu jaket super tebal saja"),
    ("mencegah nyamuk berkembang biak di sekitar rumah saat musim penghujan", "uras bak penampungan air seminggu sekali, tutup rapat wadah air bersih, dan balikkan pot atau kaleng kosong di halaman agar tidak menampung genangan", "jentik nyamuk hanya butuh sedikit air tergenang jernih selama seminggu untuk berubah menjadi nyamuk dewasa"),
    ("menyimpan kerupuk, biskuit, dan bumbu bubuk saat udara musim hujan lembap", "masukkan segera ke toples kedap udara berseal karet rapat begitu kemasan dibuka, atau simpan bumbu bubuk jauh dari uap atas kompor", "uap panas masakan yang masuk ke botol bumbu terbuka membuat bubuk cepat menggumpal keras"),
    ("mengatur suhu tidur malam saat cuaca terasa gerah pengap", "gunakan seprai bahan katun sejuk, seka badan dengan air biasa sebelum tidur, dan arahkan kipas memantul ke dinding bukan tepat ke wajah", "angin kipas kencang langsung ke hidung semalaman sering membuat tenggorokan dan mata terasa kering saat bangun"),
    ("melewati jalanan yang mulai tergenang air sehabis hujan lebat", "hindari memaksa menerobos genangan yang tingginya melewati knalpot atau lubang saringan udara, dan waspadai lubang jalan yang tertutup air keruh", "menunggu hujan reda lima belas menit di tempat aman jauh lebih murah daripada memperbaiki mesin kemasukan air"),
    ("menjaga buku dan dokumen kertas di kamar yang dindingnya agak lembap", "beri jarak lemari buku beberapa sentimeter dari tembok dingin dan letakkan kantong penyerap lembap silika di sudut rak tertutup", "kertas yang menempel langsung pada dinding lembap mudah timbul bercak jamur kecokelatan"),
    ("memilih bekal minuman yang pas dibawa saat cuaca tak menentu", "gunakan botol termos berinsulasi ganda yang sanggup menjaga air tetap hangat saat hujan maupun tetap sejuk saat siang panas", "satu botol insulasi berkualitas terpakai lintas musim sepanjang tahun"),
]

WEATHER_CTX = [
    ("apalagi belakangan cuaca di kotaku susah banget ditebak", "Kalau langit pagi cerah pun, tetap selipkan payung lipat ringan di tas buat jaga-jaga sorenya ya."),
    ("waktu jadwal harianku mengharuskan banyak pindah tempat", "Untuk mobilitas tinggi, perlengkapan pelindung yang ringkas dan cepat kering bakal sangat menolong."),
    ("supaya nggak gampang tumbang flu di tengah minggu sibuk", "Mencegah kedinginan dan langsung mengeringkan badan begitu sampai ruangan ber-AC itu kunci utamanya."),
    ("buat diterapkan bareng keluarga di rumah sehari-hari", "Kebiasaan kecil satu rumah yang kompak bikin lingkungan tempat tinggal jauh lebih sehat dan nyaman."),
    ("dengan perlengkapan sederhana yang sudah ada di rumah", "Cukup maksimalkan barang yang ada dulu, yang penting rutin dicek kebersihannya."),
    ("waktu tinggal sendiri di kos dan harus sigap mandiri", "Anak kos yang sedia payung, obat dasar, dan pakaian kering cadangan jauh lebih tenang menghadapi musim apa pun."),
    ("agar barang-barang harian tetap awet nggak cepat rusak", "Perawatan dua menit sehabis kena hujan atau panas terik memperpanjang umur pakai barang berkali lipat."),
    ("pas akhir pekan tetap harus keluar mengurus keperluan", "Berangkat di jam pagi sebelum cuaca puncak biasanya jauh lebih nyaman dan lengang di jalan."),
]


# 3. Kemandirian Mengurus Urusan Harian (Life Admin & Self-Care Praktis)
DAILY_ADMIN = [
    ("menyimpan dokumen penting seperti ijazah, KTP, dan kartu keluarga biar aman", "simpan aslinya di dalam map plastik antiair satu tas khusus yang mudah diraih saat darurat, lalu simpan hasil pindaian digitalnya di penyimpanan awan terkunci", "punya cadangan pindaian yang rapi sangat mempercepat urusan pendaftaran kerja atau administrasi mendadak"),
    ("mengatur jadwal mencuci pakaian supaya tidak menumpuk menggunung", "pisahkan keranjang pakaian putih dan berwarna sejak awal lalu jadwalkan mencuci rutin tiap tiga hari sekali dalam beban sedang", "mencuci porsi sedang jauh lebih cepat kering dan ringan disetrika dibanding menunggu menumpuk dua minggu"),
    ("memilih bantal tidur yang nyaman supaya leher tidak salah bantal", "pilih ketebalan bantal yang menjaga garis leher tetap sejajar lurus dengan tulang punggung sesuai posisi tidur miring atau telentangmu", "bantal yang terlalu tinggi menekuk leher semalaman sehingga otot bahu terasa kaku saat bangun"),
    ("mengatasi rasa gugup sebelum melakukan panggilan telepon resmi", "tulis dulu di kertas nama yang dihubungi, tujuan utama teleponmu dalam dua kalimat, serta alat tulis siap catat di sebelah tangan", "melihat panduan poin tertulis di depan mata mencegah pikiran mendadak kosong saat telepon diangkat"),
    ("menjelaskan model potongan rambut ke tukang cukur atau salon biar sesuai harapan", "tunjukkan dua foto referensi dari sudut depan dan samping yang jenis rambutnya mirip rambutmu, lalu sebutkan batas panjang dalam satuan jari", "istilah 'rapikan dikit aja' sering beda tafsirannya kalau tidak disertai patokan panjang yang konkret"),
    ("merawat sepatu sehari-hari supaya bersih dan tidak berbau", "angin-anginkan sepatu di tempat terbuka sehabis dilepas, gunakan kaos kaki bersih yang diganti setiap hari, dan sikat lembut debu keringnya rutin", "memakai kaos kaki yang sama berhari-hari adalah penyebab terbesar timbulnya bau tak sedap di dalam sepatu"),
    ("mengatur pencahayaan meja belajar atau kerja di malam hari", "nyalakan lampu utama ruangan bersamaan dengan lampu meja dari sisi berlawanan tangan menulismu agar tidak timbul bayangan gelap di buku", "bekerja hanya dengan lampu meja terang di ruangan gelap gulita membuat pupil mata cepat lelah akibat kontras tajam"),
    ("membiasakan periksa kesehatan gigi rutin sebelum terasa sakit", "jadwalkan pembersihan karang gigi dan pemeriksaan lubang kecil ke dokter gigi setiap enam bulan sekali meskipun belum ada rasa ngilu", "menambal lubang super kecil di tahap awal jauh lebih singkat, nyaman, dan hemat dibanding menunggu sampai saraf gigi nyeri"),
    ("menghemat pemakaian gas kompor saat memasak harian di dapur", "gunakan ukuran panci yang pas dengan lingkar api biru, tutup panci saat merebus air agar cepat mendidih, dan siapkan semua irisan bahan sebelum api dinyalakan", "api yang menjilat keluar melewati lebar dasar wajan hanya membuang panas ke udara sekitar"),
    ("memilih kacamata baru yang nyaman dipakai bekerja seharian", "utamakan bingkai ringan yang pas di lebar wajah tanpa menekan belakang telinga serta periksa ketepatan ukuran minus-silinder terbaru", "bingkai seringan beberapa gram lebih enteng terasa bedanya setelah bertengger delapan jam di hidung"),
    ("merapikan kulkas seminggu sekali sebelum belanja bahan baru", "geser bahan stok lama ke barisan paling depan agar dimasak lebih dulu (prinsip masuk duluan keluar duluan) dan lap tumpahan saus segera", "menaruh belanjaan baru langsung menutupi stok minggu lalu sering membuat sayur lama terlupakan di pojok belakang"),
    ("menyiapkan tas darurat kecil di rumah untuk antisipasi mati lampu atau bencana", "isi senter baterai sehat, kotak P3K dasar, peluit, air minum kemasan, biskuit padat energi, salinan dokumen, dan pengisi daya portabel terisi penuh", "meletakkan tas siaga di dekat jalur pintu keluar memudahkan evakuasi cepat tanpa panik mencari barang dalam gelap"),
]

ADMIN_CTX = [
    ("sebagai orang dewasa muda yang lagi belajar ngurus hidup sendiri", "Keterampilan praktis kayak gini memang nggak selalu diajarkan di kelas, tapi manfaatnya kerasa banget seumur hidup."),
    ("supaya urusan harian makin rapi tanpa makan banyak waktu", "Sekali sistem awalnya sudah beres, perawatan rutinnya cuma butuh beberapa menit tiap minggu."),
    ("waktu bujet bulanan lagi dijaga tetap efisien", "Kebiasaan rapi dan preventif seperti ini justru penghematan terbaik karena mencegah biaya kerusakan atau denda."),
    ("agar nggak bingung dan panik kalau sewaktu-waktu dibutuhkan", "Persiapan tenang di hari biasa selalu jauh lebih nyaman daripada kalang kabut di menit terakhir."),
    ("di tengah kesibukan kuliah atau kerja dari Senin sampai Jumat", "Cicil penataannya di Sabtu pagi yang santai supaya hari kerjamu tinggal jalan mulus."),
    ("buat ditularkan jadi kebiasaan baik di rumah juga", "Kalau ditata rapi dan jelas tempatnya, anggota rumah lain biasanya ikut mudah menjaga keteraturannya."),
]


def build_chat_dialogs(col: CategoryCollector, limit: int | None = None) -> None:
    pair_idx = 0

    # 1. Anti-mager & kejenuhan (20 * 12 * 7 = 1.680)
    mg_q = [
        "nara, aku {sit} {trig}, gimana cara ngelawan rasa magernya?",
        "tolong bantu trik biar nggak {sit} {trig} dong!",
        "kenapa berat banget rasanya waktu {sit} {trig}? solusinya apa?",
        "eh nara, kalau lagi {sit} {trig}, pemicu geraknya gimana?",
        "kasih saran realistis dong pas aku {sit} {trig}",
        "cara paling gampang mengatasi {sit} {trig} gimana ya?",
        "bantuin aku mulai gerak dong nara: {sit} {trig}",
    ]
    mg_a = [
        "Rasa mager di momen itu manusiawi banget kok! Trik pemecahnya: {how}. {trig_note} Soalnya, {why}.",
        "Jangan tunggu mood seratus persen datang dulu—coba {how}. {trig_note} Ingat bahwa {why}.",
        "Cara paling ampuh mengakali otak yang lagi malas: {how}. {trig_note} Alasannya sederhana, {why}.",
        "Perkecil langkah pertamanya sampai terasa gampang: {how}. {trig_note} Sebab dalam keseharian, {why}.",
        "Aku paham banget godaannya! Coba langsung {how}. {trig_note} Perlu dicatat, {why}.",
        "Biar roda gerakmu mulai berputar pelan, {how}. {trig_note} Kenapa manjur? Karena {why}.",
        "Nggak usah keras-keras menyalahkan diri, cukup {how}. {trig_note} Kuncinya, {why}.",
    ]
    for sit, how, why in MAGER_SITUATIONS:
        for trig, trig_note in MAGER_TRIGGERS:
            pair_idx += 1
            for k in range(len(mg_q)):
                if limit and len(col.rows) >= limit:
                    return
                q = mg_q[k].format(sit=sit, trig=trig)
                a = mg_a[(k + pair_idx) % len(mg_a)].format(
                    how=how, why=why, trig_note=trig_note
                )
                col.add(q, a)

    # 2. Cuaca & musim di Indonesia (12 * 8 * 7 = 672)
    wx_q = [
        "nara, gimana tips {act} {ctx}?",
        "kasih saran praktis buat {act} {ctx} dong",
        "apa yang perlu disiapin waktu {act} {ctx}?",
        "eh nara, biar aman dan nyaman pas {act} {ctx}, caranya gimana?",
        "tolong bagi trik harian untuk {act} {ctx}",
        "kalau menghadapi situasi {act} {ctx}, langkah tepatnya apa?",
        "ajarin cara cerdik {act} {ctx} ya",
    ]
    wx_a = [
        "Menghadapi cuaca begitu, langkah paling pas adalah {how}. {ctx_note} Soalnya, {why}.",
        "Tips praktis yang langsung kepakai: {how}. {ctx_note} Perlu diingat juga, {why}.",
        "Kamu bisa mengantisipasinya dengan mudah: {how}. {ctx_note} Alasannya jelas, {why}.",
        "Biar tetap nyaman sepanjang hari, coba {how}. {ctx_note} Sebab di lapangan, {why}.",
        "Langkah sederhana yang sangat menolong adalah {how}. {ctx_note} Catatan kecilnya: {why}.",
        "Saran dariku, pastikan kamu {how}. {ctx_note} Kenapa penting? Karena {why}.",
        "Cukup terapkan persiapan ringan ini: {how}. {ctx_note} Ingat ya, {why}.",
    ]
    for act, how, why in WEATHER_ACTIONS:
        for ctx, ctx_note in WEATHER_CTX:
            pair_idx += 1
            for k in range(len(wx_q)):
                if limit and len(col.rows) >= limit:
                    return
                q = wx_q[k].format(act=act, ctx=ctx)
                a = wx_a[(k + pair_idx) % len(wx_a)].format(
                    how=how, why=why, ctx_note=ctx_note
                )
                col.add(q, a)

    # 3. Kemandirian urusan harian (12 * 6 * 7 = 504)
    ad_q = [
        "nara, gimana cara rapi {adm} {ctx}?",
        "kasih panduan praktis buat {adm} {ctx} dong!",
        "tips gampang untuk {adm} {ctx} apa aja ya?",
        "eh nara, ajarin trik {adm} {ctx} dong",
        "kalau mau mulai menata urusan {adm} {ctx}, caranya gimana?",
        "biar nggak keteteran soal {adm} {ctx}, langkahnya apa?",
        "bantu saran hidup mandiri soal {adm} {ctx} ya",
    ]
    ad_a = [
        "Urusan itu bakal terasa ringan kalau tahu polanya: {how}. {ctx_note} Soalnya, {why}.",
        "Cara paling praktis yang bisa langsung diterapkan: {how}. {ctx_note} Ingat juga, {why}.",
        "Kamu cukup memulainya dengan langkah sederhana ini: {how}. {ctx_note} Alasannya, {why}.",
        "Tips mandiri yang sangat berguna: {how}. {ctx_note} Sebab dalam praktiknya, {why}.",
        "Coba atur dengan kebiasaan rapi berikut: {how}. {ctx_note} Perlu diketahui, {why}.",
        "Langkah cerdas buat jangka panjang adalah {how}. {ctx_note} Kuncinya, {why}.",
        "Nggak ribet kok, tinggal {how}. {ctx_note} Catatan pentingnya: {why}.",
    ]
    for adm, how, why in DAILY_ADMIN:
        for ctx, ctx_note in ADMIN_CTX:
            pair_idx += 1
            for k in range(len(ad_q)):
                if limit and len(col.rows) >= limit:
                    return
                q = ad_q[k].format(adm=adm, ctx=ctx)
                a = ad_a[(k + pair_idx) % len(ad_a)].format(
                    how=how, why=why, ctx_note=ctx_note
                )
                col.add(q, a)
