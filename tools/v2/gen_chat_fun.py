"""Bagian 5 generator `chat.jsonl`:
- Hobi baru & aktivitas kreatif ramah pemula
- Ide kado, bingkisan, & apresiasi sederhana
- Rekomendasi kegiatan akhir pekan & libur singkat
- Perjalanan harian, transportasi umum, mudik, & packing ringkas
- Hiburan sesuai suasana hati, teka-teki santai, & humor receh sopan
"""
from __future__ import annotations

from .core_v2 import CategoryCollector

# --------------------------------------------------------------------------- #
# 1. Hobi Baru & Aktivitas Kreatif (26 hobi x 18 situasi x 6 gaya = 2.808)
# --------------------------------------------------------------------------- #
HOBBIES = [
    ("menulis jurnal harian lima menit", "siapkan satu buku tulis biasa lalu catat tiga hal yang disyukuri dan satu pelajaran kecil sebelum tidur", "menuangkan isi kepala ke kertas terbukti bikin pikiran lebih rapi tanpa butuh bakat sastra"),
    ("fotografi jalanan dan benda sekitar pakai kamera HP", "aktifkan garis bantu grid 3x3 di kamera ponsel dan manfaatkan cahaya miring pagi atau sore dekat jendela", "komposisi dan arah cahaya alami jauh lebih menentukan hasil foto daripada mahalnya perangkat"),
    ("menggambar sketsa pensil sederhana", "mulai dengan menggambar bentuk dasar benda di mejamu seperti cangkir atau daun selama sepuluh menit tanpa takut garisnya miring", "tangan yang terbiasa mengamati proporsi pelan-pelan akan luwes dengan sendirinya"),
    ("belajar kunci dasar gitar akustik", "kuasai perpindahan empat kunci ramah pemula seperti C, G, Am, dan F mudah dengan tempo pelan tapi bersih bunyinya", "latihan lima belas menit tiap sore jauh lebih cepat melenturkan ujung jari dibanding dua jam seminggu sekali"),
    ("merawat tanaman hias daun di sudut kamar", "pilih tanaman tangguh seperti lidah mertua atau sirih gading yang tahan teduh dan cukup disiram saat media tanam mulai kering", "menyiram terlalu sering setiap hari justru kesalahan pemula paling umum yang membuat akar busuk"),
    ("memasak kudapan manis memakai wajan teflon", "coba resep dasar dadar gulung, panekuk pisang, atau roti panggang susu yang takarannya cukup memakai sendok makan", "berhasil membuat camilan hangat sendiri memberi rasa puas instan tanpa perlu punya oven besar"),
    ("bermain catur santai untuk melatih strategi", "pelajari prinsip pembukaan dasar yaitu menguasai petak tengah, mengeluarkan kuda-gajah lebih awal, dan mengamankan raja lewat rokade", "membahas ulang satu langkah ceroboh sehabis bermain jauh lebih cepat menaikkan kemampuan daripada main cepat puluhan kali"),
    ("merajut benang katun menggunakan hakpen tunggal", "mulai dari tusuk rantai dan tusuk tunggal memakai benang warna terang berukuran sedang agar mata rantai mudah terlihat", "gerakan berulang merajut punya efek menenangkan pikiran mirip meditasi ringan"),
    ("membaca buku cerita pendek atau esai ringan", "targetkan cukup lima sampai sepuluh halaman sehari sambil menyeduh teh supaya kebiasaan membacanya terasa menyenangkan", "memilih topik tipis yang benar-benar bikin penasaran jauh lebih ampuh membangun kebiasaan baca dibanding buku tebal yang berat"),
    ("belajar kaligrafi kuas atau tulisan tangan rapi (lettering)", "latih tarikan garis tipis saat naik dan garis agak tegas saat turun memakai spidol kuas murah di kertas bergaris titik", "konsistensi jarak antarhuruf lebih menentukan kerapian tulisan daripada hiasan yang terlalu ramai"),
    ("lari pelan (slow jogging) keliling lingkungan rumah", "jaga kecepatan lari tetap santai sampai kamu masih sanggup mengobrol tanpa terengah-engah berat selama lima belas menit", "mulai dengan irama pelan mencegah nyeri tulang kering dan bikin kamu tidak kapok di minggu pertama"),
    ("melipat kertas origami bentuk hewan dan kotak kecil", "gunakan kertas lipat persegi biasa lalu tekan setiap lipatan dengan ujung jari secara presisi dari sudut ke sudut", "ketelitian mengikuti lipatan awal membuat bentuk akhirnya simetris dan rapi"),
    ("belajar kosakata bahasa asing lewat lagu dan film pendek", "catat tiga ungkapan sehari-hari yang sering muncul lalu coba ucapkan ulang dalam kalimat buatanmu sendiri", "mengingat kata di dalam konteks kalimat utuh jauh lebih awet daripada menghafal daftar kata lepas"),
    ("menanam cabai atau daun bawang di pot kecil teras", "manfaatkan pangkal batang daun bawang sisa dapur di pot tanah gembur yang terkena sinar matahari pagi minimal tiga jam", "melihat tunas hijau baru tumbuh setiap pagi memberi semangat segar dan hasilnya bisa dipanen buat masak"),
    ("menyusun puzzle gambar atau teka-teki silang", "pisahkan kepingan bagian tepi lurus dan kelompokkan warnanya lebih dulu di atas alas karton agar mudah disimpan", "aktivitas merangkai pola melatih kesabaran sekaligus mengistirahatkan mata dari layar gawai"),
    ("membuat kerajinan pembatas buku dari karton bekas kemasan", "gunting karton bersih ukuran memanjang, hias dengan potongan majalah lama atau gambar spidol, lalu beri pita di ujungnya", "mendaur ulang bahan yang sudah ada di rumah melatih kreativitas tanpa keluar biaya sama sekali"),
    ("latihan peregangan kelenturan tubuh di atas matras", "lakukan gerakan peregangan punggung, bahu, dan paha belakang sambil mengatur napas panjang tanpa memantulkan badan paksa", "tubuh yang rutin diregangkan sepuluh menit sehari terasa jauh lebih ringan saat bangun tidur"),
    ("mendengarkan siniar (podcast) cerita sejarah atau sains populer", "putar satu episode berdurasi dua puluh menit sambil membereskan kamar, mencuci piring, atau jalan sore", "menggabungkan tontonan suara dengan pekerjaan tangan ringan bikin kegiatan rutin terasa cepat selesai"),
    ("mencoba seduh kopi manual sederhana di rumah", "perhatikan perbandingan bubuk kopi dan air panas yang baru turun sedikit dari mendidih agar rasanya tidak gosong pahit", "mencicipi perbedaan rasa dari suhu air dan gilingan kopi jadi eksperimen pagi yang seru"),
    ("belajar sulap kartu atau koin sederhana buat hiburan teman", "latihan gerakan dasarnya di depan cermin sampai perpindahan tangannya terlihat wajar dan tidak kaku", "trik sederhana yang dibawakan dengan cerita santai jauh lebih menghibur daripada teknik rumit yang terburu-buru"),
    ("menulis cerita pendek fiksi dari kejadian sehari-hari", "mulai dari satu tokoh yang menginginkan sesuatu sederhana namun terhalang satu masalah kecil di perjalanannya", "membatasi cerita hanya seribu kata membantu pemula menuntaskan naskah sampai kalimat terakhir"),
    ("mengamati burung atau serangga taman di pagi hari", "perhatikan warna bulu dan kicauannya di pohon sekitar pukul enam pagi lalu catat ciri uniknya di buku kecil", "kebiasaan memperhatikan alam sekitar melatih kepekaan dan membuat jalan pagi terasa penuh kejutan"),
    ("belajar mengetik sepuluh jari tanpa melihat papan ketik", "letakkan telunjuk di tombol bertonjol F dan J lalu latih ketepatan huruf lebih dulu sebelum mengejar kecepatan", "begitu jari hafal letak tombol secara otomatis, menulis tugas panjang jadi jauh lebih hemat tenaga"),
    ("membuat kolase catatan tempel (scrapbook) kenangan", "kumpulkan tiket perjalanan, bungkus teh unik, atau catatan kecil lalu tempel rapi dengan keterangan satu kalimat singkat", "menyimpan kenangan fisik punya kesan hangat tersendiri saat dibuka kembali beberapa tahun kemudian"),
    ("belajar harmonika atau rekorder nada dasar", "latih tiupan napas yang stabil pada satu lubang nada dulu sebelum mencoba memainkan lagu anak-anak pendek", "alat musik tiup kecil mudah disimpan di tas dan tidak memakan ruang di kamar sempit"),
    ("merapikan dan mendesain ulang tata letak meja belajar", "kosongkan seluruh permukaan meja lebih dulu, bersihkan debunya, lalu kembalikan hanya barang yang benar-benar dipakai harian", "mengubah arah meja menghadap cahaya alami sering langsung menyegarkan suasana belajar"),
]

HOBBY_CONTEXTS = [
    ("buat ngisi waktu luang pulang sekolah atau kerja", "Karena dilakukan sehabis beraktivitas, anggap hobi ini sebagai ruang bermain santai tanpa target sempurna."),
    ("dengan modal super hemat anak kos", "Kabar baiknya, kamu bisa mulai dari alat paling dasar di rumah dulu sebelum memutuskan beli perlengkapan tambahan."),
    ("supaya nggak rebahan main medsos terus pas libur", "Mengganti satu jam layar dengan kegiatan tangan nyata bikin akhir pekanmu terasa jauh lebih berisi."),
    ("waktu cuma punya ruang sempit di kamar", "Kegiatan ini praktis banget karena nggak butuh pojok khusus yang lebar dan cepat dibereskan kembali."),
    ("padahal aku ngerasa nggak punya bakat seni dari kecil", "Hobi itu tujuannya bikin hati senang, bukan lomba juara—jadi nikmati saja proses coba-cobanya."),
    ("biar punya kegiatan tenang buat melepas stres", "Ritme pelan dari aktivitas ini pas banget membantu menurunkan ketegangan kepala setelah minggu yang sibuk."),
    ("waktu pengen nyoba hal baru sendirian di rumah", "Menikmati hobi mandiri di rumah melatih kita nyaman dan betah menemani diri sendiri."),
    ("kalau cuma bisa meluangkan 15 menit sehari", "Lima belas menit yang konsisten jauh lebih terasa kemajuannya daripada menunggu waktu luang berjam-jam."),
    ("buat dikerjakan bareng adik atau teman di akhir pekan", "Kalau dikerjakan berdua sambil ngobrol ringan, suasananya bakal jauh lebih seru dan akrab."),
    ("supaya pikiran nggak gampang jenuh sama rutinitas", "Punya satu kegiatan kreatif di luar urusan wajib memberi warna segar yang ditunggu-tunggu setiap hari."),
    ("tanpa harus ikut kursus berbayar dulu", "Latihan mandiri dari langkah dasar sudah sangat cukup buat membangun pondasi awalnya."),
    ("waktu cuaca musim hujan sering ketahan di dalam rumah", "Pas di luar hujan terus, punya aktivitas seru di dalam ruangan bikin kamu anti mati gaya."),
    ("buat melatih kesabaran dan ketelitian pelan-pelan", "Proses bertahapnya secara alami mengasah fokus tanpa terasa seperti sedang mengerjakan tugas berat."),
    ("setelah lama banget nggak punya hobi tetap", "Jangan langsung pasang target tinggi di minggu pertama; cukup rasakan serunya mencoba hal baru dulu."),
    ("sambil ditemani teh hangat sore hari", "Memadukan waktu santai sore dengan hobi ringan seperti ini cepat banget mengembalikan mood baik."),
    ("biar akhir bulan tetap ada hiburan seru tanpa jajan luar", "Hiburan produktif di rumah kayak gini penyelamat banget waktu lagi mengerem pengeluaran jalan-jalan."),
    ("waktu pengen ngurangin kebiasaan begadang sia-sia", "Kegiatan tenang di sore atau awal malam justru membantu pikiran rileks sehingga tidur lebih nyenyak."),
    ("sebagai hadiah waktu berkualitas buat diri sendiri", "Menyisihkan sedikit waktu khusus buat hal yang kamu sukai adalah bentuk merawat kesehatan pikiran yang sehat."),
]


# --------------------------------------------------------------------------- #
# 2. Ide Kado & Kejutan Sederhana (22 penerima x 16 momen/bujet x 6 gaya = 2.112)
# --------------------------------------------------------------------------- #
GIFT_IDEAS = [
    ("ibu di rumah", "selendang katun lembut, peralatan masak antilengket ringan, atau paket teh herbal hangat lengkap dengan kartu ucapan tulisan tangan", "perhatian tulus lewat surat singkat buatan sendiri sering kali jadi bagian yang paling disimpan ibu"),
    ("ayah yang suka hal praktis", "termos kopi tahan panas, senter kecil serbaguna, kaos kerah bahan adem, atau bantal penyangga punggung kursi", "barang fungsional yang langsung terpakai dalam kegiatan hariannya hampir selalu jadi favorit ayah"),
    ("sahabat kuliah yang sedang kejar tugas akhir", "botol minum takaran jam, camilan kacang-cokelat sehat, lampu baca jepit meja, atau buku catatan ringkas", "hadiah yang menemani jam begadang dan menjaga staminanya terasa sangat pengertian"),
    ("teman dekat yang baru wisuda", "tempat kartu identitas kerja yang rapi, pena logam bertinta halus, atau bingkai foto kecil kenangan perjuangan kalian", "kado yang berguna untuk langkah barunya setelah lulus lebih awet dipakai daripada karangan bunga sesaat"),
    ("adik yang masih sekolah", "kotak alat tulis rapi, jam beker meja unik, botol minum olahraga, atau buku cerita bergambar sesuai minatnya", "pilih warna kesukaannya supaya dia makin semangat membawanya ke sekolah"),
    ("kakak yang baru mulai kerja kantoran", "tas bekal makan siang tahan hangat, payung lipat kokoh untuk di tas, atau penyangga laptop lipat portabel", "perlengkapan komuter harian seperti itu sangat menolong rutinitas barunya"),
    ("rekan kerja yang pindah divisi atau resign", "cangkir keramik bertutup kayu untuk meja barunya, kopi bubuk nusantara kemasan kecil, disertai catatan apresiasi kerja sama", "ukuran kado yang ringkas memudahkan dia membawanya pulang di hari terakhir kerja"),
    ("guru atau dosen pembimbing sebagai tanda terima kasih", "buku bacaan umum berkualitas, kotak teh seduh pilihan, atau plakat kayu kecil sederhana berisi ucapan terima kasih sopan", "hindari barang terlalu mewah agar beliau nyaman menerimanya sebagai kenang-kenangan tulus"),
    ("teman yang hobi masak di rumah", "celemek kain kanvas tebal, satu set sendok takar baja tahan karat, atau toples kaca bumbu seragam", "peralatan dapur yang rapi dan awet bikin sesi memasaknya makin menyenangkan"),
    ("teman yang baru pindah ke kamar kos baru", "keset kaki lembut yang menyerap air, lampu tidur kuning redup colok dinding, atau keranjang lipat pakaian", "penghuni kos baru sering lupa membeli perlengkapan kecil yang justru dibutuhkan tiap hari"),
    ("sahabat yang suka olahraga lari atau jalan pagi", "kaos kaki olahraga bantalan empuk, tas sabuk pinggang tipis penyimpan kunci-HP, atau handuk mikrofiber cepat kering", "perlengkapan kecil olahraga yang nyaman selalu terpakai berulang kali tiap minggu"),
    ("teman pasangan yang baru menikah", "satu set seprai katun sejuk warna netral, sepasang handuk mandi serasi, atau wadah kaca kedap udara penyimpan makanan", "warna netral seperti krem, abu muda, atau biru teduh mudah masuk ke dekorasi rumah apa pun"),
    ("teman yang sedang pemulihan sehabis sakit", "keranjang buah segar mudah kupas seperti jeruk-pir, madu murni botol kecil, atau kaus kaki hangat yang nyaman", "pastikan makanannya ringan dan sesuai pantangan kesehatannya bila ada"),
    ("sepupu yang gemar menggambar dan seni", "buku sketsa kertas tebal (sketchbook), satu set pensil gradasi ketebalan, atau penghapus uleni khusus gambar", "kertas gambar tebal tidak mudah tembus sehingga nyaman dipakai berbagai media"),
    ("teman yang suka berkebun tanaman kecil", "pot terakota bernapas dengan tatakan bawah, gunting pangkas daun mungil, atau semprotan kabut air", "perkakas kebun ukuran mini sangat pas untuk merawat tanaman di beranda sempit"),
    ("teman yang hobi baca buku", "lampu baca jepit bertenaga baterai isi ulang, pembatas buku magnetik tipis, atau sampul buku kain pelindung tas", "sampul kain melindungi sudut buku kesayangannya agar tidak tertekuk saat dibawa di ransel"),
    ("keponakan kecil yang aktif bermain", "balok susun kayu warna-warni, buku aktivitas mewarnai, atau bola karet lembut yang aman dimainkan di dalam rumah", "mainan tanpa komponen super kecil jauh lebih aman dan melatih motorik tangannya"),
    ("nenek atau kakek tercinta", "selimut rajut hangat yang ringan, sandal rumah beralas karet antiselip, atau radio pemutar suara tombol besar", "utamakan faktor keamanan antilicin serta kemudahan pemakaian tanpa tombol rumit"),
    ("teman satu tim kepanitiaan setelah acara sukses", "gantungan kunci akrilik tema acara, cokelat batang pembangkit energi, dan catatan kecil menyebutkan kontribusi kerennya", "apresiasi spesifik terhadap kerja kerasnya bikin lelah kepanitiaan langsung terbayar"),
    ("diri sendiri setelah berhasil melewati bulan berat", "makanan hangat favorit, buku yang sudah lama masuk daftar incaran, atau bantal tidur baru yang empuk", "memberi penghargaan terukur pada diri sendiri menjaga semangat tetap sehat untuk target berikutnya"),
]

GIFT_CONTEXTS = [
    ("dengan bujet hemat di bawah Rp50.000", "Dengan anggaran hemat, bungkus rapi memakai kertas cokelat polos dan pita sederhana sudah bikin tampilannya manis banget."),
    ("dengan bujet menengah sekitar Rp75.000 sampai Rp150.000", "Di rentang bujet ini kamu sudah leluasa memilih bahan yang cukup awet dipakai bertahun-tahun."),
    ("waktu waktunya mepet buat besok sore", "Semua pilihan ini mudah dicari langsung di toko buku, swalayan, atau toko perlengkapan rumah terdekat tanpa tunggu pengiriman lama."),
    ("supaya kadonya beneran kepakai nggak cuma jadi pajangan", "Barang yang menyentuh rutinitas harian hampir tidak pernah berakhir berdebu di pojok lemari."),
    ("buat momen ulang tahun yang hangat", "Tambahkan tiga kalimat doa tulus di kartu kecil agar nuansa ulang tahunnya terasa personal."),
    ("sebagai kejutan kecil tanpa nunggu hari spesial", "Hadiah spontan di hari biasa justru sering terasa dua kali lebih menyentuh karena tidak diduga."),
    ("waktu kadonya harus dikirim paket ke luar kota", "Pilih varian yang tidak mudah pecah dan ringan timbangannya supaya aman di perjalanan ekspedisi."),
    ("kalau kita patungan bareng dua-tiga teman lain", "Karena patungan bertiga, kamu bisa memilih satu barang berkualitas bagus sekaligus pelengkap kecilnya."),
    ("padahal orangnya sering bilang 'nggak usah repot-repot'", "Orang yang bilang begitu biasanya paling luluh sama hadiah sederhana yang menunjukkan kamu memperhatikan kebiasaannya."),
    ("biar berkesan rapi walau sederhana", "Kerapian bungkusan dan kebersihan barang melepas label harga memberi kesan niat yang tulus."),
    ("waktu belum tahu persis ukuran baju atau sepatunya", "Memilih perlengkapan bebas ukuran seperti ini jauh lebih aman daripada menebak nomor sepatu lalu kekecilan."),
    ("buat merayakan pencapaian barunya bulan ini", "Selipkan ucapan selamat atas pencapaiannya supaya barang itu selalu mengingatkan pada momen bangganya."),
    ("menjelang kumpul hari raya atau liburan keluarga", "Kado bernuansa hangat dan berguna bersama-sama selalu mencairkan suasana kumpul keluarga."),
    ("dengan tema warna netral yang aman buat siapa aja", "Pilihan warna kalem seperti krem, biru tua, atau hijau daun jarang sekali meleset dari selera kebanyakan orang."),
]


# --------------------------------------------------------------------------- #
# 3. Kegiatan Akhir Pekan, Perjalanan Harian, & Hiburan Ringan (3 blok besar)
# --------------------------------------------------------------------------- #
WEEKEND_PLANS = [
    ("jalan pagi keliling taman kota lalu sarapan bubur hangat", "berangkat sekitar pukul enam pagi saat udara masih bersih dan matahari belum terik", "bergerak ringan di ruang hijau pagi hari menyegarkan mata yang seminggu penuh menatap tembok dan layar"),
    ("merapikan isi lemari baju dan menyisihkan pakaian layak pakai", "keluarkan per rak lalu pisahkan pakaian yang setahun terakhir tidak pernah tersentuh untuk disumbangkan", "lemari yang longgar membuat pagi hari kerja jauh lebih cepat saat memilih pakaian"),
    ("mengunjungi perpustakaan daerah atau taman baca komunitas", "bawa kartu identitas untuk mendaftar anggota gratis dan pilih pojok duduk tenang dekat cahaya jendela", "suasana hening perpustakaan memberi liburan tenang tanpa mengeluarkan uang sepeser pun"),
    ("masak menu makan siang spesial bareng keluarga atau teman kos", "bagi tugas memotong bahan dan mencuci alat sejak awal sambil memutar lagu santai", "makan masakan hasil olahan bersama terasa lebih akrab daripada sekadar beli jadi"),
    ("bersepeda santai menyusuri jalur pinggir kota yang teduh", "cek tekanan angin ban dan fungsi rem malam sebelumnya serta bawa air minum sendiri", "angin sepoi-sepoi di atas sepeda cepat mengusir penat duduk seminggu penuh"),
    ("menonton ulang film favorit lama sambil membuat berondong jagung sendiri", "redupkan lampu ruangan dan simpan HP agak jauh agar benar-benar menikmati alur ceritanya utuh", "menonton fokus satu film penuh lebih memulihkan pikiran daripada melompat-lompat video pendek berjam-jam"),
    ("mencoba resep minuman segar rumahan seperti es jeruk selasih atau teh serai", "seduh bahan rempah segar yang ada di dapur lalu nikmati di teras sore hari", "bereksperimen meracik minuman sendiri jauh lebih sehat takaran gulanya dibanding minuman kaleng"),
    ("mencuci bersih sepatu, tas harian, dan helm yang dipakai seminggu", "sikat lembut bagian kotor pagi hari supaya kering sempurna terkena angin siang", "memulai hari Senin dengan perlengkapan bersih dan wangi menaikkan semangat berangkat"),
    ("menulis rencana santai minggu depan dan mengevaluasi minggu lalu", "cukup luangkan dua puluh menit di Minggu sore mencatat tiga prioritas utama pekan depan", "kepala yang sudah punya peta kasar untuk besok Senin tidak mudah terkena cemas Minggu malam"),
    ("piknik sederhana membawa bekal roti dan buah di halaman atau kebun raya", "bawa alas duduk lipat serta kantong kecil khusus untuk membawa pulang kembali semua bungkus sampahmu", "duduk santai memandang pepohonan sambil mengobrol tanpa terburu-buru sangat menenangkan saraf"),
    ("belajar satu keterampilan praktis baru seperti menjahit kancing lepas", "siapkan jarum, benang warna netral, dan coba pada kain perca atau kemeja lama yang kancingnya longgar", "kemampuan kecil merawat pakaian sendiri bakal terpakai seumur hidup di saat darurat"),
    ("berkunjung ke museum lokal atau kawasan kota tua bersejarah", "datang di pagi hari saat pengunjung masih lengang dan baca papan kisah di balik koleksinya pelan-pelan", "melihat jejak sejarah kota sendiri sering membuka wawasan baru yang jarang kita sadari"),
    ("tidur siang berkualitas 20-30 menit lalu mandi air hangat sorenya", "pasang alarm setengah jam di awal siang agar tidak kebablasan tidur terlalu sore yang mengganggu tidur malam", "tidur singkat yang terukur membayar sedikit utang lelah tanpa membuat kepala pusing saat bangun"),
    ("mengobrol santai via telepon panjang sama sahabat jauh atau orang tua", "cari waktu sore yang longgar sambil duduk nyaman supaya obrolannya mengalir tanpa melirik jam kerja", "mendengar suara orang terdekat secara utuh jauh lebih menghangatkan hati daripada sekadar bertukar stiker chat"),
]

WEEKEND_MOODS = [
    ("waktu dompet lagi tipis banget di akhir bulan", "Semua langkahnya nyaris tanpa biaya besar, jadi dompetmu tetap aman sampai awal bulan."),
    ("pas badan lumayan terkuras habis minggu yang berat", "Temponya bisa kamu atur sesantai mungkin supaya energi tubuhmu benar-benar terisi kembali."),
    ("waktu teman-teman lagi sibuk sama urusan masing-masing", "Dijalani sendirian pun kegiatan ini tetap asyik dan nggak terasa canggung sama sekali."),
    ("kalau cuma punya waktu luang setengah hari aja", "Durasinya ringkas kok, dua-tiga jam saja sudah tuntas dan sisanya tetap bisa istirahat."),
    ("pas cuaca pagi kelihatan cerah dan bersahabat", "Manfaatkan cahaya cerahnya mumpung mendukung, tapi tetap pakai pelindung matahari kalau di luar ya."),
    ("supaya hari libur nggak lewat begitu aja sambil rebahan", "Ada hasil nyata atau pengalaman segar yang kamu rasakan waktu malam tiba nanti."),
    ("bareng satu teman dekat yang sama-sama pengen suasana tenang", "Cocok banget buat ngobrol dari hati ke hati tanpa kebisingan pusat perbelanjaan."),
    ("waktu pengen istirahat dari hiruk-pikuk media sosial", "Menjauh sebentar dari layar seharian bakal bikin pikiranmu terasa jauh lebih ringan."),
    ("di hari Minggu sebelum kembali ke rutinitas besok", "Penutup akhir pekan yang tenang seperti ini bikin transisi ke hari Senin terasa mulus."),
    ("tanpa harus menempuh macet perjalanan jauh", "Lokasinya dekat saja di sekitar tempat tinggal, jadi tenagamu nggak habis di jalan."),
]


# --------------------------------------------------------------------------- #
# 4. Perjalanan Harian, Komuter, & Persiapan Pergi (14 topik x 10 situasi x 6 gaya)
# --------------------------------------------------------------------------- #
TRAVEL_TIPS = [
    ("menyiapkan isi tas harian supaya nggak berat tapi siap cuaca berubah", "bawa payung lipat ringan atau jas hujan tipis, tisu kering, kantong plastik lipat buat barang basah, dan kabel pengisi daya pendek", "mengeluarkan struk lama dan barang duplikat dari tas tiap akhir pekan mengurangi beban pundak secara nyata"),
    ("berangkat naik kereta komuter atau bus kota di jam sibuk", "siapkan kartu pembayaran elektronik di saku luar yang mudah dijangkau dan kenakan ransel di dada saat gerbong padat", "menyimpan dompet utama dan HP di bagian beritsleting dalam menjaga keamanan sekaligus memudahkan gerak turun"),
    ("mengemas pakaian ke ransel untuk perjalanan dua-tiga hari", "gulung pakaian bahan kaos secara padat di bagian bawah tas dan taruh barang berat menempel dekat punggung", "menggulung baju menghemat ruang jauh lebih banyak sekaligus mengurangi bekas lipatan kusut"),
    ("mencegah mabuk darat waktu naik bus atau mobil jarak jauh", "pilih kursi bagian depan atau tengah dekat roda, tatap garis cakrawala jauh di depan, dan hindari membaca teks kecil di HP", "mabuk perjalanan muncul saat mata melihat layar diam sementara telinga dalam merasakan guncangan gerak"),
    ("berkendara motor saat langit mulai mendung gelap", "gunakan jas hujan model baju-celana (bukan ponco lebar yang rawan tersangkut roda), nyalakan lampu utama, dan jaga jarak pengereman dua kali lebih jauh", "aspal pada lima belas menit pertama hujan paling licin karena debu bercampur minyak naik ke permukaan"),
    ("menjaga keamanan rumah atau kamar kos sebelum ditinggal mudik beberapa hari", "cabut steker listrik yang tidak esensial, kosongkan tempat sampah dapur agar tidak mengundang serangga, dan pastikan keran air serta jendela terkunci rapat", "memotret kondisi kompor dan colokan yang sudah dicabut sebelum mengunci pintu bikin hati tenang sepanjang jalan"),
    ("mengatasi kaki kaku dan bosan selama perjalanan kereta atau bus berjam-jam", "gerakkan pergelangan kaki memutar tiap jam, minum air secukupnya, dan unduh bacaan atau musik offline sebelum berangkat", "mengandalkan sinyal internet di jalur antarkota sering putus-nyambung dan cepat menguras baterai"),
    ("datang ke stasiun atau terminal supaya nggak panik ketinggalan jadwal", "targetkan tiba minimal 30-45 menit sebelum jam keberangkatan dan cek nomor peron atau pintu masuk begitu sampai", "waktu cadangan setengah jam menyelamatkanmu kalau tiba-tiba ada antrean cetak tiket atau pengalihan jalan"),
    ("membawa bekal makanan untuk perjalanan jauh agar tidak mudah basi", "pilih lauk kering seperti kering tempe, abon, roti, atau buah kulit utuh seperti jeruk dan pisang, serta pisahkan sambal dari nasi", "makanan bersantan basah yang tertutup panas di dalam tas cepat berubah asam dalam hitungan jam"),
    ("menghadapi helm yang bagian dalamnya mulai lembap setelah dipakai harian", "lepas busa dalam untuk dicuci sabun lembut saat akhir pekan cerah, dan angin-anginkan helm menghadap terbalik setiap habis dipakai", "menyimpan helm langsung di tempat tertutup saat masih lembap keringat memicu bau dan gatal di kulit kepala"),
]

TRAVEL_CONTEXTS = [
    ("apalagi sekarang cuaca sering berubah mendadak siang ke sore", "Di musim pancaroba, sedia pelindung hujan tipis di tas menyelamatkan baju dan elektronikmu."),
    ("waktu harus berangkat pagi-pagi banget", "Menyiapkan semuanya sejak malam sebelumnya bikin pagi harimu bebas lari-larian panik."),
    ("pas pergi sendirian tanpa teman seperjalanan", "Kalau jalan sendiri, kerapian menyimpan dokumen dan baterai cadangan jadi kunci rasa aman utama."),
    ("sambil membawa laptop kerja di dalam ransel", "Pastikan laptop terbungkus pelindung tahan cipratan air di kompartemen tengah tas ya."),
    ("supaya sampai tujuan badan nggak langsung tumbang kecapekan", "Mengatur kenyamanan kecil sepanjang jalan menjaga energimu tetap utuh waktu tiba di lokasi."),
    ("dengan barang bawaan seringkas mungkin satu tas saja", "Bepergian satu ransel ringkas bikin langkahmu jauh lebih gesit saat naik-turun kendaraan."),
]


# --------------------------------------------------------------------------- #
# 5. Teka-teki Santai, Humor Receh, & Obrolan Ringan Khas Indonesia
# --------------------------------------------------------------------------- #
JOKES_AND_LIGHT = [
    ("kasih aku satu jokes receh bapak-bapak dong nara", "Kenapa pohon kelapa di depan rumah harus ditebang? Soalnya kalau dicabut berat banget, mending ditebang aja! Receh ya, tapi lumayan bikin senyum tipis kan?"),
    ("lempar lelucon santai soal anak sekolah dong", "Guru tanya: 'Kenapa kamu telat?' Murid jawab: 'Soalnya di jalan ada plang tulisannya Awas Sekolah Pelan-Pelan, jadi aku jalannya pelan banget sampai sini!'"),
    ("punya humor receh tentang makanan nggak?", "Tahu nggak kenapa tempe kalau digoreng suka bareng tahu? Soalnya kalau sendirian namanya kesepian di wajan panas. Garing kayak gorengan baru angkat nih!"),
    ("kasih teka-teki logika ringan buat hiburan sore dong", "Coba tebak: benda apa yang punya leher tapi nggak punya kepala, dan tiap hari dipakai orang? Jawabannya **baju** atau **botol**! Dua-duanya punya bagian leher kan."),
    ("tebak-tebakan santai dong nara, biar nggak ngantuk", "Apa yang makin dipotong justru makin tinggi? Jawabannya **celana panjang**! Makin dipotong bawahnya, posisinya makin naik ke atas lutut."),
    ("nara, kamu tim bubur diaduk atau nggak diaduk?", "Sebagai AI yang nggak punya sendok, aku pengamat damai dua kubu! Tim diaduk menang di rasa bumbu yang merata di tiap suap, sedangkan tim nggak diaduk menang di tampilan rapi dan kerupuk yang tetap renyah lebih lama. Kamu sendiri kubu mana?"),
    ("menurutmu lebih nikmat minum teh manis hangat atau es teh tawar?", "Tergantung cuaca di luar jendela! Kalau sore hujan rintik-rintik jelas teh hangat juaranya, tapi kalau habis jalan siang terik rasanya es teh tawar dingin langsung menyegarkan tenggorokan."),
    ("kasih ide nama lucu buat kucing peliharaan baru dong", "Kalau bulunya oranye aktif bisa dinamai **Oyen**, **Kunyit**, atau **Marmalade**; kalau putih bersih cocok **Mochi** atau **Kapas**; kalau hitam gagah keren dipanggil **Kopi** atau **Arang**!"),
    ("bantu ide nama grup belajar bareng teman biar seru dong", "Bisa pakai nama santai tapi memotivasi kayak **Pejuang SKS**, **Kopi & Catatan**, **Lulus Bareng**, **Anti Sistem Kebut**, atau **Ruang Diskusi Sore**."),
    ("kasih teka-teki lagi: apa yang selalu datang tapi nggak pernah sampai?", "Jawabannya **hari esok**! Soalnya begitu kita sampai di harinya, namanya langsung berubah jadi 'hari ini'."),
    ("punya jokes pendek soal programmer nggak nara?", "Kenapa programmer kurang suka jalan-jalan ke hutan belantara? Soalnya di sana terlalu banyak *bugs* alias serangga!"),
    ("tebak-tebakan dong: pintu apa yang didorong sepuluh orang tetap nggak mau terbuka?", "Pintu yang ada tulisannya **GESER** atau **TARIK**! Mau didorong sekuat apa pun ya jelas mentok di kusennya."),
    ("nara, enaknya makan gorengan pakai cabai rawit atau saus sambal?", "Wah, dua-duanya punya penggemar garis keras! Cabai rawit hijau ngasih sensasi pedas segar yang meletup pas digigit bareng tahu isi, sementara saus sambal kacang atau botol enak buat cocolan bakwan hangat."),
    ("kasih kalimat penyemangat singkat yang nggak klise dong", "Kamu nggak harus menyelesaikan seluruh tangga minggu ini dalam satu lompatan; cukup pastikan kakimu menapak mantap di satu anak tangga hari ini."),
]


def build_chat_fun(col: CategoryCollector, limit: int | None = None) -> None:
    pair_idx = 0

    for q, a in JOKES_AND_LIGHT:
        if limit and len(col.rows) >= limit:
            return
        col.add(q, a)

    # 1. Hobi baru (26 * 18 * 6 = 2.808)
    h_q = [
        "nara, aku pengen mulai hobi {hobby} {ctx}, mulainya gimana ya?",
        "kasih tips pemula buat mencoba {hobby} {ctx} dong!",
        "cocok nggak sih hobi {hobby} {ctx}? caranya gimana?",
        "gimana langkah awal biar betah {hobby} {ctx}?",
        "eh nara, ajarin cara mulai {hobby} {ctx} dong",
        "pengen nyoba kegiatan {hobby} {ctx}, ada saran praktis?",
    ]
    h_a = [
        "Ide seru tuh! Untuk memulai {hobby}, cukup {start}. {ctx_note} Kuncinya, {why}.",
        "Cocok banget dicoba! Langkah pertamanya gampang: {start}. {ctx_note} Perlu diingat, {why}.",
        "Bisa langsung kamu mulai hari ini kok: {start}. {ctx_note} Soalnya, {why}.",
        "Buat pemula di {hobby}, cara paling asyik adalah {start}. {ctx_note} Ingat ya, {why}.",
        "Nggak usah nunggu alat lengkap dulu—mulai saja dengan {start}. {ctx_note} Alasannya, {why}.",
        "Hobi {hobby} itu menyenangkan kalau dimulai ringan: {start}. {ctx_note} Sebab, {why}.",
    ]
    for hobby, start, why in HOBBIES:
        for ctx, ctx_note in HOBBY_CONTEXTS:
            pair_idx += 1
            for k in range(len(h_q)):
                if limit and len(col.rows) >= limit:
                    return
                q = h_q[k].format(hobby=hobby, ctx=ctx)
                a = h_a[(k + pair_idx) % len(h_a)].format(
                    hobby=hobby, start=start, why=why, ctx_note=ctx_note
                )
                col.add(q, a)

    # 2. Ide kado (20 * 14 * 6 = 1.680)
    g_q = [
        "nara, kasih ide kado buat {who} {ctx} dong",
        "bingung mau beliin hadiah apa untuk {who} {ctx}, bantu saran ya",
        "rekomendasi kado yang pas buat {who} {ctx} apa aja?",
        "kalau mau ngasih sesuatu ke {who} {ctx}, enaknya pilih apa?",
        "eh nara, hadiah berkesan untuk {who} {ctx} kira-kira apa ya?",
        "bantuin cari ide bingkisan buat {who} {ctx} dong!",
    ]
    g_a = [
        "Buat {who}, pilihan yang manis dan bermanfaat itu {items}. {ctx_note} Catatan kecil: {why}.",
        "Kamu bisa mempertimbangkan {items} untuk {who}. {ctx_note} Soalnya, {why}.",
        "Ide kado yang jarang gagal buat {who} antara lain {items}. {ctx_note} Ingat juga, {why}.",
        "Coba lirik pilihan seperti {items} buat {who}. {ctx_note} Kenapa pas? Karena {why}.",
        "Kalau untuk {who}, aku sarankan {items}. {ctx_note} Selain itu, {why}.",
        "Pilihan aman sekaligus berkesan buat {who} adalah {items}. {ctx_note} Sebab, {why}.",
    ]
    for who, items, why in GIFT_IDEAS:
        for ctx, ctx_note in GIFT_CONTEXTS:
            pair_idx += 1
            for k in range(len(g_q)):
                if limit and len(col.rows) >= limit:
                    return
                q = g_q[k].format(who=who, ctx=ctx)
                a = g_a[(k + pair_idx) % len(g_a)].format(
                    who=who, items=items, why=why, ctx_note=ctx_note
                )
                col.add(q, a)

    # 3. Rencana akhir pekan (14 * 10 * 6 = 840)
    w_q = [
        "nara, enaknya akhir pekan coba {plan} nggak ya {mood}?",
        "kasih tips biar kegiatan {plan} terasa seru {mood} dong",
        "kalau libur ini aku mau {plan} {mood}, gimana ngaturnya?",
        "cocok nggak rencana {plan} {mood}?",
        "eh nara, ide {plan} {mood} kira-kira asyik nggak?",
        "bantu saran singkat buat {plan} {mood} ya",
    ]
    w_a = [
        "Pas banget idenya! Biar maksimal, coba {how}. {mood_note} Manfaatnya kerasa karena {why}.",
        "Rencana yang menyegarkan tuh! Kamu cukup {how}. {mood_note} Soalnya, {why}.",
        "Cocok banget dicoba akhir pekan ini: {how}. {mood_note} Apalagi {why}.",
        "Gas aja, itu kegiatan libur yang sehat! Tipsnya, {how}. {mood_note} Ingat, {why}.",
        "Asyik banget lho! Langkah simpelnya tinggal {how}. {mood_note} Sebab {why}.",
        "Setuju banget sama rencanamu—coba {how}. {mood_note} Alasannya jelas: {why}.",
    ]
    for plan, how, why in WEEKEND_PLANS:
        for mood, mood_note in WEEKEND_MOODS:
            pair_idx += 1
            for k in range(len(w_q)):
                if limit and len(col.rows) >= limit:
                    return
                q = w_q[k].format(plan=plan, mood=mood)
                a = w_a[(k + pair_idx) % len(w_a)].format(
                    how=how, why=why, mood_note=mood_note
                )
                col.add(q, a)

    # 4. Perjalanan & transportasi harian (10 * 6 * 6 = 360)
    t_q = [
        "nara, gimana tips {topic} {ctx}?",
        "kasih saran praktis buat {topic} {ctx} dong",
        "biar aman dan nyaman pas {topic} {ctx}, harus perhatiin apa?",
        "eh nara, ajarin trik {topic} {ctx} ya",
        "kalau mau {topic} {ctx}, persiapannya gimana?",
        "ada tips ringkas soal {topic} {ctx}?",
    ]
    t_a = [
        "Biar perjalananmu lancar, coba {how}. {ctx_note} Penting juga diingat: {why}.",
        "Trik praktisnya begini: {how}. {ctx_note} Soalnya di lapangan, {why}.",
        "Kamu bisa menyiapkan ini dulu: {how}. {ctx_note} Alasannya sederhana, {why}.",
        "Langkah paling aman adalah {how}. {ctx_note} Sekadar info tambahan, {why}.",
        "Coba terapkan kebiasaan ini: {how}. {ctx_note} Sebab, {why}.",
        "Supaya nggak repot di jalan, {how}. {ctx_note} Ingat ya, {why}.",
    ]
    for topic, how, why in TRAVEL_TIPS:
        for ctx, ctx_note in TRAVEL_CONTEXTS:
            pair_idx += 1
            for k in range(len(t_q)):
                if limit and len(col.rows) >= limit:
                    return
                q = t_q[k].format(topic=topic, ctx=ctx)
                a = t_a[(k + pair_idx) % len(t_a)].format(
                    how=how, why=why, ctx_note=ctx_note
                )
                col.add(q, a)
