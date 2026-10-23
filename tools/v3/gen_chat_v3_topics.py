"""Tabel topik percakapan baru untuk Nara-Allegretto-3 (v3).

Semua baris di berkas ini adalah materi baru yang ditulis untuk v3 (bukan
salinan daftar v2). Format tiap topik tips: (masalah, tip imperatif, alasan).
Format curhat: (situasi, perasaan, langkah menenangkan, penguat hati).
Format resep: (bahan, nama hidangan, langkah ringkas).
Bahasa konsisten santai `aku/kamu`, tanpa kata `saya/anda`.
"""
from __future__ import annotations

# ------------------------- A. Kos & rumah harian ------------------------- #
KOS_TOPICS = [
    ("lupa mematikan kompor setelah masak", "biasakan mengecek knop kompor sambil mengucapkan 'sudah mati' dengan suara pelan sebelum meninggalkan dapur", "kebiasaan yang diucapkan lantang jauh lebih mudah diingat otak daripada sekadar niat dalam hati"),
    ("kehabisan air galon pas malam hari", "tempel catatan kecil di dispenser setiap galon tinggal seperempat supaya kamu memesan pengganti sebelum benar-benar habis", "persediaan air minum itu kebutuhan pokok yang paling repot kalau baru dicari mendadak"),
    ("kunci kamar kos sering ketinggalan di dalam", "gantung kunci cadangan di gantungan khusus persis di samping pintu dan latih tangan menyentuh saku sebelum menarik gagang", "ritual sentuh saku yang konsisten berubah jadi refleks kurang dari sepekan"),
    ("sampah kamar menumpuk sampai berbau", "sediakan kantong kecil khusus sampah basah dan buang ke tempat sampah luar setiap selesai makan", "sisa makanan adalah sumber bau paling cepat, sedangkan sampah kering masih bisa menunggu"),
    ("pakaian bersih menumpuk belum dilipat berminggu-minggu", "lipat pakaian sambil mendengarkan satu lagu favorit dan berhenti begitu lagu selesai, lalu lanjutkan lagi nanti", "target yang dibatasi lagu terasa ringan sehingga tumpukan menyusut tanpa terasa jadi beban besar"),
    ("lantai kamar cepat berdebu padahal baru disapu", "letakkan keset serap di depan pintu dan biasakan melepas alas kaki luar sebelum melangkah masuk", "sebagian besar debu kamar sebenarnya terbawa masuk dari sol sepatu dan sandal"),
    ("tamu teman kos datang mendadak saat kamar berantakan", "siapkan satu keranjang 'sembunyi cepat' untuk memasukkan barang acak, lalu rapikan isinya setelah tamu pulang", "kamar yang terlihat lega di permukaan sudah cukup membuat tamu merasa nyaman"),
    ("lampu kamar kos putus pas lagi butuh belajar malam", "simpan satu lampu cadangan kecil atau lampu meja isi ulang di laci khusus darurat", "barang darurat yang tempatnya tetap tidak akan bikin panik saat dicari dalam gelap"),
    ("jemuran tidak kering-kering selama musim hujan", "peras pakaian dua kali sebelum dijemur dan beri jarak longgar antarhanger agar udara mengalir", "pakaian yang terlalu rapat menjebak uap air di tengah sehingga makin lama keringnya"),
    ("tetangga kos berisik saat jam istirahat malam", "sampaikan keberatanmu siang hari dengan kalimat ramah berisi jam tenang yang kamu usulkan, bukan menegur saat sedang emosi", "usulan jam yang jelas terdengar sebagai ajakan sepakat, bukan serangan pribadi"),
    ("barang pinjam-meminjam antar teman kos sering hilang kabar", "catat nama peminjam dan tanggalnya di catatan HP setiap barang keluar dari kamarmu", "catatan sederhana menghilangkan canggung saat kamu perlu menagih barangmu kembali"),
    ("tagihan listrik kos membengkak tanpa sadar", "cabut pengisi daya dan matikan kipas atau lampu setiap meninggalkan kamar lebih dari lima menit", "alat elektronik yang dibiarkan menyala kosong adalah penyumbang tagihan yang paling tidak terasa"),
    ("dinding kamar lembap dan mulai berjamur", "geser lemari beberapa senti dari dinding dan buka jendela tiap pagi agar udara lembap berganti", "jamur tumbuh subur di sudut gelap yang udaranya diam dan basah berhari-hari"),
    ("kasur terasa keras dan bikin badan pegal", "lapisi kasur dengan selimut tebal yang dilipat rata atau alas tidur tipis sebelum memasang sprei", "sedikit bantalan tambahan membantu tulang belakang tidak menekan permukaan keras semalaman"),
    ("bingung menata barang di kamar kos yang sempit", "manfaatkan ruang vertikal dinding dengan gantungan dan simpan barang musiman di kolong tempat tidur dalam kotak berlabel", "lantai yang lega membuat kamar sempit terasa dua kali lebih luas dan gampang dibersihkan"),
    ("sering kehabisan sabun dan perlengkapan mandi mendadak", "buat daftar isi ulang bulanan dan belanja semua perlengkapan mandi sekaligus pada tanggal yang sama", "belanja terjadwal mencegah pembelian panik eceran yang biasanya lebih mahal"),
]

# -------------------------- B. Uang & belanja ---------------------------- #
UANG_TOPICS = [
    ("uang jajan habis sebelum tengah bulan", "pisahkan uang makan, transport, dan hiburan ke tiga amplop atau dompet digital berbeda sejak awal bulan", "uang yang sudah dipisahkan per tujuan terasa lebih jelas batasnya dibanding uang yang tercampur jadi satu"),
    ("tergoda beli barang cuma karena gratis ongkir", "masukkan barang ke keranjang lalu tunggu sampai besok pagi sebelum memutuskan membayar", "keinginan impulsif biasanya menyusut jauh setelah tidur semalam"),
    ("lupa mencatat pengeluaran kecil sehari-hari", "catat pengeluaran di catatan HP begitu membayar, cukup tulis nominal dan satu kata keterangan", "pengeluaran kecil yang sering justru yang paling besar jumlahnya saat diakumulasikan sebulan"),
    ("saldo dompet digital cepat bocor buat pesan makanan", "tetapkan hari khusus pesan makanan online, misalnya hanya dua hari dalam sepekan", "batasan hari membuat kebiasaan pesan makanan jadi acara istimewa, bukan refleks harian"),
    ("susah menabung karena nominal terasa harus besar", "mulai dari menyisihkan dua ribu rupiah setiap selesai makan siang ke celengan khusus", "kebiasaan menabung dibentuk oleh kerutinan kecil, bukan oleh besarnya nominal awal"),
    ("uang transport membengkak karena sering naik ojek online", "hitung rute yang bisa ditempuh jalan kaki di bawah satu kilometer dan jadikan itu pilihan utama saat cuaca bersahabat", "jarak dekat yang ditempuh jalan kaki ikut menambah gerak harian dan menekan biaya"),
    ("bingung membedakan kebutuhan dan keinginan saat promo", "tanyakan pada diri sendiri apakah barang itu akan dipakai minggu ini juga, kalau tidak berarti bisa ditunda", "barang kebutuhan selalu punya jadwal pakai yang jelas dalam waktu dekat"),
    ("teman sering pinjam uang kecil tapi lama mengembalikan", "tetapkan batas nominal pinjaman yang rela kamu ikhlaskan dan sampaikan batas itu dengan ramah sejak awal", "batas yang jelas menjaga pertemanan tetap enak tanpa rasa mengganjal berbulan-bulan"),
    ("harga kebutuhan naik tapi uang saku tetap", "bandingkan harga per gram atau per mili antar merek, bukan cuma harga kemasan yang terlihat", "kemasan besar kadang lebih murah per satuan walau harga totalnya tampak lebih tinggi"),
    ("terlalu sering jajan minuman manis kekinian", "bawa botol minum berisi air atau teh buatan sendiri setiap keluar rumah", "haus yang sudah teratasi membuat godaan mampir beli minuman turun drastis"),
    ("langganan aplikasi menumpuk tak terpakai", "daftar semua langganan berbayar lalu hentikan yang tidak dibuka sama sekali bulan lalu", "biaya langganan yang kecil terasa sepele padahal rutin memotong saldo tiap bulan"),
    ("keperluan mendadak selalu menguras tabungan", "bangun dana darurat kecil terpisah mulai dari target lima ratus ribu rupiah secara bertahap", "dana darurat membuat keperluan mendadak tidak lagi merusak rencana keuangan utama"),
    ("belanja bulanan selalu melebihi daftar", "foto isi kulkas dan rak sebelum berangkat supaya tidak membeli barang yang sebenarnya masih ada", "pembelian dobel adalah penyebab belanja membengkak yang paling sering tidak disadari"),
    ("penghasilan tambahan langsung habis begitu diterima", "pindahkan sebagian penghasilan tambahan ke tabungan pada hari yang sama sebelum dipakai apa pun", "uang yang sudah berpindah tempat terasa bukan lagi uang belanja bebas"),
    ("susah menolak ajakan nongkrong yang mahal", "usulkan tempat alternatif yang lebih ramah kantong sambil tetap menjaga suasana kumpul tetap seru", "kebanyakan teman sebenarnya lebih peduli kumpulnya daripada harga tempatnya"),
    ("uang kembalian receh selalu tercecer hilang", "sediakan satu wadah khusus koin di dekat pintu dan kosongkan saku ke sana tiap pulang", "koin yang terkumpul rapi lumayan untuk parkir, angkot, atau isi ulang galon"),
]

# ------------------------- C. Belajar & pekerjaan ------------------------ #
BELAJAR_TOPICS = [
    ("salah membaca jadwal sehingga terlambat ikut kelas atau rapat", "tulis ulang jadwal mingguanmu dengan tangan di kertas yang ditempel dekat cermin", "menulis ulang membuat otak memproses jadwal jauh lebih dalam dibanding sekadar melihat layar"),
    ("catatan digital tersebar di banyak aplikasi sampai susah dicari", "tetapkan satu aplikasi sebagai rumah utama semua catatan dan pindahkan sisanya bertahap setiap akhir pekan", "satu tempat penyimpanan menghilangkan waktu berburu catatan saat sedang dibutuhkan cepat"),
    ("tugas kelompok selalu dikerjakan mepet oleh orang yang sama", "usulkan pembagian tugas tertulis dengan batas waktu per bagian sejak pertemuan pertama", "kesepakatan tertulis membuat tanggung jawab tiap orang terlihat jelas oleh seluruh kelompok"),
    ("presentasi berakhir terlalu cepat karena materi habis", "siapkan satu contoh cerita pendek untuk tiap poin utama sebagai bahan cadangan pengembang", "contoh konkret membuat penjelasan lebih hidup dan mengisi waktu secara wajar"),
    ("susah memahami istilah asing di materi kuliah atau kerja", "buat daftar istilah pribadi di halaman terakhir buku catatan beserta arti sederhananya dengan bahasamu sendiri", "istilah yang diterjemahkan dengan kata-kata sendiri jauh lebih mudah menempel di ingatan"),
    ("berkas tugas tertukar versi lama dan versi terbaru", "beri nama berkas dengan pola tanggal dan nomor versi, misalnya laporan-2026-10-23-v2", "nama berkas yang konsisten membuat versi terbaru selalu terlihat tanpa membuka satu per satu"),
    ("rapat atau kelas daring terasa membuang banyak waktu", "siapkan daftar pertanyaan dan keputusan yang kamu butuhkan sebelum pertemuan dimulai", "pertemuan dengan tujuan pribadi yang jelas membuatmu aktif dan cepat menangkap hasilnya"),
    ("ide tulisan selalu muncul saat tidak membawa alat tulis", "biasakan mengirim pesan singkat ke diri sendiri di aplikasi chat setiap ide melintas", "ide yang tidak dicatat dalam semenit pertama biasanya hilang sebelum sempat dikembangkan"),
    ("belajar bahasa asing berhenti di tengah jalan terus", "ikat latihan bahasa dengan rutinitas yang sudah ada, misalnya lima menit setiap selesai sarapan", "kebiasaan baru yang menempel pada kebiasaan lama jauh lebih mudah bertahan"),
    ("lembur atau belajar tambahan membuat waktu istirahat hilang", "tetapkan jam berhenti yang tegas dan umumkan ke rekanmu agar tidak ada tugas baru sesudahnya kecuali darurat", "istirahat yang dijaga membuat kualitas kerja esok hari tidak ikut turun"),
    ("susah mulai mengerjakan laporan karena formatnya membingungkan", "salin contoh laporan lama yang sudah benar lalu ganti isinya bagian demi bagian", "kerangka yang sudah jadi menghilangkan kebingungan format sehingga tenaga fokus ke isi"),
    ("sering salah kirim berkas atau pesan ke orang lain", "biasakan berhenti satu detik untuk membaca nama penerima dan nama berkas sebelum menekan kirim", "jeda satu detik adalah rem termurah untuk mencegah kesalahan yang memalukan"),
    ("target membaca buku tidak pernah tercapai", "turunkan target menjadi sepuluh halaman sehari dan letakkan buku tepat di samping bantal", "target kecil yang selalu tercapai membangun momentum lebih kuat daripada target besar yang gagal"),
    ("diskusi kelompok melebar ke mana-mana tanpa keputusan", "usulkan satu orang pencatat keputusan yang membacakan kesimpulan setiap selesai satu topik", "keputusan yang dibacakan lantang mencegah topik yang sama dibahas berulang-ulang"),
    ("kewalahan mengejar banyak kursus daring sekaligus", "pilih satu kursus utama sampai selesai dan simpan kursus lain sebagai daftar tunggu", "menyelesaikan satu kursus penuh memberi keterampilan nyata dibanding lima kursus setengah jalan"),
    ("hasil pekerjaan rumah sering tertinggal tidak terbawa", "masukkan hasil pekerjaan ke tas pada malam sebelumnya tepat setelah selesai dikerjakan", "barang yang dipacking saat selesai tidak bergantung pada ingatan pagi yang terburu-buru"),
]

# --------------------------- D. Makan & dapur ---------------------------- #
MAKAN_TOPICS = [
    ("masakan selalu kurang bumbu di tengah proses", "letakkan semua bumbu yang dibutuhkan di satu nampan kecil sebelum kompor dinyalakan", "persiapan di awal membuat proses masak tidak terputus untuk berburu bumbu yang kurang"),
    ("sayuran cepat layu sebelum sempat dimasak", "bungkus sayuran daun dengan kain bersih kering sebelum dimasukkan ke wadah tertutup di kulkas", "kain menyerap embun berlebih yang biasanya mempercepat daun menjadi busuk"),
    ("nasi cepat basi padahal baru dimasak kemarin", "aduk nasi sekali setelah matang agar uap menyebar, lalu simpan sisanya di kulkas begitu sudah tidak panas", "uap yang terperangkap membuat permukaan nasi basah dan cepat ditumbuhi bakteri"),
    ("minyak goreng cepat hitam dan berbau", "saring minyak bekas gorengan bertepung setelah dingin dan jangan memanaskannya sampai berasap", "remah gosong yang tertinggal adalah penyebab utama minyak cepat rusak dan pahit"),
    ("bingung menentukan telur masih segar atau tidak", "rendam telur di gelas berisi air; telur segar akan tenggelam rebah, sedangkan yang lama cenderung mengapung", "kantong udara di dalam telur membesar seiring usia sehingga daya apungnya berubah"),
    ("masak terlalu banyak sampai lauk bersisa berhari-hari", "timbang bahan mentah dengan gelas takar sederhana dan catat porsi yang pas untuk jumlah orang di rumah", "catatan porsi pribadi jauh lebih akurat daripada menebak dengan perasaan lapar"),
    ("rasa masakan selalu hambar di tengah", "masukkan garam bertahap di tiga tahap masak sambil mencicipi, bukan sekaligus di akhir", "garam yang masuk bertahap meresap ke bahan, bukan hanya menempel di permukaan kuah"),
    ("dapur berantakan setiap selesai masak besar", "cuci alat yang sudah selesai dipakai sambil menunggu masakan mendidih atau matang", "waktu menunggu masakan adalah waktu gratis yang paling pas untuk mencicil cucian"),
    ("buah potong cepat berubah warna menjadi kecokelatan", "kucuri sedikit air jeruk nipis atau lemon pada permukaan potongan buah sebelum disimpan", "asam dari jeruk memperlambat reaksi oksidasi yang membuat daging buah berubah warna"),
    ("roti tawar berjamur sebelum habis dimakan", "simpan sebagian roti di freezer dalam kantong tertutup dan panggang seperlunya saat mau dimakan", "suhu beku menghentikan pertumbuhan jamur tanpa banyak mengubah rasa roti"),
    ("bumbu dapur bubuk menggumpal karena lembap", "simpan bumbu bubuk di wadah kedap jauh dari kompor dan ambil selalu dengan sendok kering", "uap masakan dan sendok basah adalah dua jalan masuk utama kelembapan ke bumbu"),
    ("selalu bingung mau masak apa setiap hari", "susun daftar menu sepekan sederhana di kertas kulkas setiap akhir pekan", "keputusan menu yang dibuat sekali sepekan menghemat tenaga mikir setiap sore"),
    ("makanan beku lupa dikeluarkan sampai jam masak tiba", "pindahkan bahan beku ke kulkas bawah sejak malam sebelumnya agar mencair perlahan dan aman", "pencairan perlahan di kulkas menjaga tekstur bahan dan menghambat pertumbuhan bakteri"),
    ("air rebusan pasta atau mie selalu meluap", "letakkan sendok kayu melintang di atas panci dan kecilkan api begitu air mulai mendidih", "sendok kayu memecah gelembung busa sehingga luapan rebusan lebih terkendali"),
    ("pisang cepat matang semua dalam waktu bersamaan", "pisahkan pisang dari tandannya dan simpan sebagian di kulkas begitu kulitnya menguning pas", "gas etilen dari pisang matang mempercepat kematangan pisang lain di dekatnya"),
    ("bekal makanan berkuah sering tumpah di tas", "pisahkan kuah ke botol kecil bertutup ulir dan bungkus lagi dengan kantong antiair", "tutup ulir jauh lebih tahan guncangan daripada tutup tekan biasa selama perjalanan"),
]

# ------------------------- E. Sosial & keluarga -------------------------- #
SOSIAL_TOPICS = [
    ("lupa membalas pesan penting dari teman atau keluarga", "tandai pesan yang belum bisa dibalas saat itu juga sebagai belum dibaca agar muncul lagi nanti", "pesan yang sudah terbuka tanpa tanda hampir pasti terkubur obrolan baru"),
    ("canggung memulai obrolan dengan orang yang baru kenal", "mulai dari hal yang sama-sama sedang kalian alami di tempat itu, misalnya acara atau antrean yang sama", "konteks bersama adalah pembuka obrolan paling aman karena tidak terasa menginterogasi"),
    ("janji ketemuan sering batal karena tidak jelas jamnya", "tutup setiap ajakan dengan satu kalimat kepastian berisi hari, jam, dan tempat berkumpul", "ajakan tanpa tiga unsur itu hampir selalu berakhir menjadi wacana grup semata"),
    ("beda pendapat dengan saudara berujung suasana canggung", "pisahkan topik yang sedang diperdebatkan dari hubungan pribadi dengan kalimat penenang sebelum lanjut bicara", "mengingatkan tujuan baik bersama membuat perdebatan tetap soal ide, bukan soal orang"),
    ("susah menolak permintaan tolong padahal sedang sibuk", "tawarkan bantuan pada waktu lain yang sanggup kamu tepati, bukan menolak tanpa alternatif sama sekali", "alternatif waktu menunjukkan niat baik tanpa mengorbankan urusanmu sendiri"),
    ("acara keluarga terasa melelahkan karena ditanya hal yang sama terus", "siapkan satu jawaban ringan dan sopan sebagai andalan untuk pertanyaan berulang itu", "jawaban siap pakai membuatmu tidak perlu menguras emosi menyusun kalimat baru tiap kali"),
    ("teman cerita panjang lebar tapi aku bingung menanggapi", "ulangi inti perasaannya dalam satu kalimat sebelum memberi saran apa pun", "orang yang bercerita biasanya ingin merasa dipahami dulu sebelum diberi jalan keluar"),
    ("grup chat terlalu ramai sampai info penting tenggelam", "usulkan menyematkan pesan penting dan memakai fitur balas agar topik tidak bercampur", "pesan tersemat membuat anggota yang baru membuka grup langsung menemukan inti informasi"),
    ("tetangga baru belum kenal siapa pun di lingkungan rumah", "sapa lebih dulu saat berpapasan dan kenalkan nama serta nomor rumahmu dengan singkat", "sapaan pertama yang ramah membuka pintu bantuan timbal balik di kemudian hari"),
    ("hadiah untuk teman selalu dibeli mendadak dan asal", "catat hal yang disukai teman-teman dekatmu di catatan HP setiap mereka menyebutkannya dalam obrolan", "ide hadiah terbaik biasanya muncul dari ucapan spontan mereka jauh sebelum hari istimewa"),
    ("orang tua jarang dikabari karena merasa tidak ada bahan obrolan", "kirim foto kegiatan harian sederhana, misalnya masakan atau jalan sore, sebagai pembuka kabar", "foto keseharian membuat orang tua merasa ikut hadir dalam hidupmu dari jauh"),
    ("salah paham di grup karena nada chat dibaca berbeda", "tambahkan satu kata penjelas suasana seperti 'santai ya' atau emoji seperlunya pada kalimat yang rawan disalahartikan", "teks tidak membawa nada suara, jadi penanda kecil sangat membantu maksudmu terbaca benar"),
    ("undangan acara menumpuk di hari yang sama", "dahulukan acara yang mengharuskan konfirmasi kehadiran dan balas semua undangan dalam satu waktu duduk", "balasan cepat yang jelas jauh lebih dihargai tuan rumah daripada jawaban menggantung"),
    ("adik atau kakak sering meminjam barang tanpa bilang", "sepakati aturan sederhana bahwa barang pribadi tertentu wajib izin lewat pesan singkat lebih dulu", "aturan yang disepakati bersama terasa adil dan tidak seperti larangan sepihak"),
    ("teman lama hanya muncul saat butuh bantuan", "balas dengan ramah tapi jujur soal batas bantuan yang sanggup kamu berikan kali ini", "kejujuran soal batas membuat hubungan tetap sehat tanpa kamu merasa dimanfaatkan"),
    ("foto bersama keluarga tercecer di banyak HP anggota", "buat satu album bersama di layanan awan dan minta semua anggota mengunggah foto pilihan tiap acara selesai", "album bersama menyelamatkan foto keluarga dari risiko HP rusak atau hilang"),
]

# ------------------------ F. Gadget & internet --------------------------- #
GADGET_TOPICS = [
    ("baterai HP cepat habis sebelum sore hari", "cek daftar aplikasi pemakan baterai terbesar di pengaturan lalu batasi aktivitas latar belakang yang jarang kamu pakai", "penyebab baterai boros biasanya terlihat jelas dari peringkat konsumsi aplikasi"),
    ("memori HP penuh oleh foto tangkapan layar", "luangkan lima menit tiap akhir pekan untuk menghapus tangkapan layar yang sudah tidak dibutuhkan", "tangkapan layar adalah jenis berkas yang paling cepat menumpuk tanpa terasa"),
    ("kata sandi akun memakai pola yang sama semua", "ganti kata sandi akun terpenting lebih dulu dengan frasa panjang yang unik dan aktifkan verifikasi dua langkah", "satu kata sandi bocor tidak boleh bisa membuka semua akunmu yang lain"),
    ("notifikasi aplikasi mengganggu waktu fokus", "matikan notifikasi semua aplikasi kecuali pesan pribadi dan kalender selama jam fokusmu", "setiap bunyi notifikasi memecah konsentrasi yang butuh beberapa menit untuk kembali utuh"),
    ("wifi rumah lambat di jam-jam sibuk malam", "letakkan perute wifi di tempat terbuka agak tinggi dan jauhkan dari dinding tebal serta peralatan logam besar", "sinyal wifi melemah setiap kali harus menembus penghalang padat di sekitarnya"),
    ("berkas unduhan menumpuk berantakan di laptop", "buat tiga folder tetap bernama tugas, pribadi, dan arsip lalu rapikan unduhan tiap selesai mengunduh berkas penting", "kebiasaan merapikan saat itu juga mencegah folder unduhan berubah jadi gudang tak bernama"),
    ("layar laptop cepat membuat leher pegal", "ganjal bagian belakang laptop dengan buku tebal agar layar sejajar pandangan mata", "layar yang terlalu rendah memaksa leher menunduk terus selama berjam-jam"),
    ("kabel pengisi daya cepat rusak di pangkalnya", "pegang kepala konektor saat mencabut, jangan menarik kabelnya, dan gulung longgar saat disimpan", "pangkal kabel adalah titik tekuk paling rapuh yang serabutnya mudah putus di dalam"),
    ("sering lupa mencadangkan foto dan dokumen penting", "aktifkan pencadangan otomatis ke awan dan jadwalkan salin manual ke penyimpanan lain sebulan sekali", "dua salinan di tempat berbeda membuat kehilangan satu perangkat tidak berujung bencana"),
    ("mata cepat lelah membaca teks kecil di layar", "perbesar ukuran huruf sistem satu tingkat dan naikkan jarak baca sejauh rentangan tangan", "huruf kecil memaksa mata bekerja ekstra keras memfokuskan setiap baris"),
    ("grup dan kanal yang diikuti terlalu banyak sampai kewalahan", "keluar atau bisukan grup yang tidak lagi kamu baca selama sebulan terakhir", "linimasa yang ramping membuat informasi yang benar-benar penting kembali terlihat"),
    ("HP cepat panas saat dipakai navigasi perjalanan jauh", "lepas casing tebal selama navigasi dan turunkan kecerahan layar secukupnya", "layar terang dan sinyal yang terus mencari adalah dua sumber panas terbesar di perjalanan"),
    ("aplikasi tiba-tiba tertutup sendiri berulang kali", "perbarui aplikasi ke versi terbaru lalu nyalakan ulang HP sebelum mencoba langkah yang lebih rumit", "sebagian besar gangguan aplikasi selesai oleh pembaruan dan nyala ulang yang bersih"),
    ("kuota internet habis sebelum masa aktif paket berakhir", "aktifkan pengingat batas kuota di pengaturan dan unduh video atau musik hanya saat tersambung wifi", "streaming video adalah pemakan kuota terbesar yang sering tidak terasa jumlahnya"),
    ("akun lama di situs yang sudah tidak dipakai masih aktif", "tutup akun lama yang tidak terpakai satu per satu setiap akhir bulan sambil memperbarui kata sandinya", "akun terlantar adalah pintu masuk kebocoran data yang paling jarang diawasi"),
    ("berkas hasil pindaian dokumen susah ditemukan saat dibutuhkan", "beri nama hasil pindaian dengan pola jenis dokumen dan tahun, misalnya ktp-2026 atau ijazah-2024", "nama berkas yang berbicara membuat pencarian dokumen selesai dalam hitungan detik"),
]

DOMAIN_TOPICS = [KOS_TOPICS, UANG_TOPICS, BELAJAR_TOPICS, MAKAN_TOPICS, SOSIAL_TOPICS, GADGET_TOPICS]

# ------------------------------- Curhat ---------------------------------- #
CURHAT_TOPICS = [
    ("malu karena harus tampil di acara kecil lingkungan rumah", "pipi terasa panas membayangkan semua mata melihat ke arahku", "latih bagian pembuka saja sampai hafal, sebab awal yang mulus biasanya menenangkan sisa penampilan", "penonton tetangga umumnya datang buat mendukung, bukan mencari-cari kesalahan kecilmu"),
    ("kesepian padahal sedang berada di tengah keramaian", "sekeliling ramai tapi rasanya tidak ada yang benar-benar nyambung", "dekati satu orang yang terlihat santai dan mulai obrolan ringan dari hal di sekitar kalian", "rasa sepi di keramaian dialami banyak orang dan bukan tanda kamu sulit bergaul"),
    ("sedih karena hewan peliharaan di rumah sedang sakit", "waswas tiap melihatnya lemas tidak seperti biasanya", "catat perubahan makannya sejak kapan dan konsultasikan ke dokter hewan bila kondisinya tidak membaik", "kepedulianmu memperhatikan perubahan kecil adalah bekal terbaik buat kesembuhannya"),
    ("bangga karena akhirnya berani mencoba hobi baru", "hasilnya masih sederhana tapi hati rasanya puas banget", "foto hasil pertamamu dan simpan sebagai penanda awal perjalanan hobimu", "keberanian memulai selalu lebih berarti daripada menunggu sampai merasa sempurna dulu"),
    ("kesal karena mengantre lama buat urusan yang sebentar", "kaki pegal dan waktu terasa terbuang percuma", "manfaatkan antrean untuk merapikan galeri HP atau menyusun daftar urusan berikutnya", "waktu menunggu terasa jauh lebih pendek saat tangan dan pikiran punya kegiatan"),
    ("merasa bersalah lupa mengucapkan selamat ulang tahun ke teman dekat", "takut dia mengira aku sudah tidak peduli lagi", "kirim ucapan sekarang juga dengan jujur dan hangat, ucapan terlambat tetap jauh lebih baik daripada diam", "teman dekat umumnya lebih menghargai ketulusan daripada ketepatan tanggal"),
    ("bingung menentukan pilihan kursus atau jurusan lanjutan", "semua pilihan terlihat menarik tapi takut salah jalan", "tulis tiga hal yang paling kamu nikmati saat belajar lalu cocokkan dengan isi tiap pilihan", "pilihan yang selaras dengan minat harian biasanya lebih bertahan daripada yang sekadar terlihat keren"),
    ("lelah bergantian menjaga anggota keluarga yang sedang pemulihan", "badan kurang istirahat dan pikiran tidak pernah benar-benar lepas", "buat jadwal jaga tertulis bergiliran agar setiap orang punya waktu tidur yang utuh", "merawat orang tersayang juga menuntut perawatnya tetap sehat dan cukup istirahat"),
    ("senang karena dapat teman baru yang nyambung banget", "obrolannya mengalir ringan seperti sudah kenal lama", "tindaklanjuti dengan ajakan kegiatan sederhana supaya pertemanannya tumbuh alami", "kecocokan awal adalah modal bagus, sisanya tumbuh dari kebersamaan yang konsisten"),
    ("gugup pertama kali naik kendaraan umum sendirian ke kota sebelah", "takut salah turun dan bingung harus bertanya ke siapa", "simpan titik tujuan di peta HP dan duduk dekat jendela agar mudah mengenali penanda jalan", "petugas dan penumpang lain umumnya senang hati membantu penumpang yang bertanya sopan"),
    ("kecewa karena rencana liburan bareng keluarga batal mendadak", "sudah membayangkan serunya sejak jauh-jauh hari", "ganti dengan acara kecil di rumah pada tanggal yang sama agar momen berkumpulnya tidak hilang", "yang paling dirindukan dari liburan biasanya kebersamaannya, dan itu bisa diciptakan di rumah"),
    ("rindu masakan rumah karena lama tidak pulang", "makanan di perantauan terasa ada yang kurang terus", "minta resep sederhana satu masakan rumah ke keluarga dan coba masak versi kosnya", "aroma masakan rumah punya kekuatan menghadirkan rasa pulang dari dapur sendiri"),
    ("cemas menjelang pindah kos ke lingkungan yang benar-benar baru", "membayangkan harus beradaptasi dari nol lagi rasanya berat", "kunjungi lingkungan barunya sekali di siang hari dan tandai warung, masjid atau tempat ibadah, serta minimarket terdekat", "tempat yang sudah pernah dilihat dengan mata sendiri jauh tidak menakutkan dibanding bayangan"),
    ("puas karena tabungan kecil-kecilan akhirnya mencapai target pertama", "rasanya usaha menyisihkan receh selama ini terbayar lunas", "rayakan secukupnya lalu naikkan target berikutnya sedikit saja dari target yang tercapai ini", "target pertama yang tercapai adalah bukti bahwa kebiasaan barumu benar-benar bekerja"),
    ("sebal karena barang kesayangan rusak tanpa sengaja", "barang itu punya banyak kenangan dan susah dicari gantinya", "cek dulu kemungkinan diperbaiki sebelum memutuskan membuang atau membeli baru", "kenangan pada barang itu tetap milikmu meski wujudnya tidak lagi sempurna"),
    ("semangat karena diajak ikut proyek kecil yang sesuai minat", "kepala langsung penuh ide dan tidak sabar ingin mulai", "catat semua idemu malam ini lalu pilih tiga yang paling realistis besok pagi", "semangat awal yang diarahkan ke langkah kecil akan berubah jadi hasil nyata"),
    ("iri melihat adik atau kakak lebih diperhatikan akhir-akhir ini", "rasanya perhatian di rumah sedang tidak terbagi rata", "sampaikan perasaanmu dengan kalimat tentang dirimu sendiri tanpa membandingkan siapa pun", "orang rumah sering tidak sadar pembagian perhatiannya terasa timpang sampai ada yang bicara"),
    ("bosan setengah mati selama perjalanan jauh di kendaraan", "jam terasa berjalan lambat dan badan mulai pegal semua", "bagi perjalanan jadi babak kecil: musik, camilan, melihat pemandangan, lalu tidur sejenak", "perjalanan panjang terasa lebih ringan saat dipecah menjadi kegiatan-kegiatan pendek"),
]

# ------------------------------- Resep ----------------------------------- #
RESEP_TOPICS = [
    ("tiga butir telur dan dua batang daun bawang", "telur dadar daun bawang tebal", "kocok telur bersama irisan daun bawang dan sedikit garam sampai berbusa, lalu dadar di api kecil dengan wajan bertutup agar matang merata dan tebal"),
    ("bakso sapi dan sayuran beku campuran", "capcay kuah bakso cepat", "tumis bawang putih sampai harum, tuang air secukupnya, masukkan irisan bakso dan sayuran beku, lalu bumbui garam, merica, dan sedikit saus tiram"),
    ("paha ayam dan satu ruas jahe", "ayam kecap jahe hangat", "tumis irisan jahe dan bawang putih, masukkan potongan ayam sampai berubah warna, lalu siram kecap manis dan sedikit air dan masak sampai meresap"),
    ("mie telur kering dan satu ikat caisim", "mie nyemek caisim telur", "tumis bawang merah-putih dan cabai, tuang air sedikit, masukkan mie dan caisim, lalu pecahkan telur dan aduk sampai kuahnya menyusut nyemek"),
    ("beras dan sisa ayam goreng semalam", "bubur ayam penanak nasi", "masak beras dengan air empat kali lipat di penanak nasi sambil sesekali diaduk, lalu sajikan bersama suwiran ayam goreng dan irisan daun bawang"),
    ("oyong muda dan satu butir telur", "sup oyong telur bening", "didihkan air bersama geprekan bawang putih, masukkan potongan oyong dua menit, lalu tuang kocokan telur perlahan sambil kuah diaduk memutar"),
    ("buncis muda dan satu butir telur", "tumis buncis telur orak-arik", "buat orak-arik telur lalu sisihkan, tumis bawang putih dan buncis potong serong di api besar, kemudian campurkan kembali telur dengan sedikit kecap asin"),
    ("kentang kecil dan cabai merah", "kentang balado mini", "goreng kentang utuh kecil sampai berkulit, tumis halusan cabai merah, bawang merah, dan tomat sampai matang berminyak, lalu aduk kentang ke dalamnya"),
    ("tempe dan gula merah sepotong", "tempe bacem teflon kilat", "rebus tempe bersama air, gula merah sisir, ketumbar bubuk, dan garam sampai menyusut, lalu panggang sebentar di teflon sampai permukaannya karamel"),
    ("tahu putih dan dua butir telur", "tahu telur siram kecap bawang", "goreng tahu dan telur dadar menjadi satu lapisan, lalu siram campuran kecap manis, irisan bawang merah, dan cabai rawit di atasnya"),
    ("labu siam dan santan instan satu bungkus", "sayur lodeh labu sederhana", "rebus irisan labu siam bersama bawang merah, bawang putih, dan lengkuas geprek, lalu masukkan santan instan encer dan masak sebentar tanpa sampai pecah santan"),
    ("nasi hangat dan ikan teri segenggam", "nasi liwet penanak nasi sederhana", "masak beras seperti biasa dengan tambahan santan encer, daun salam, serai geprek, dan teri yang sudah digoreng sebentar, lalu aduk rata saat matang"),
    ("pisang kepok matang dan tepung terigu", "pisang goreng tepung renyah", "buat adonan tepung, sedikit gula, dan air hingga kental, celupkan belahan pisang, lalu goreng di minyak panas sampai kuning keemasan"),
    ("wortel dan kentang satu buah", "sop wortel kentang bawang putih", "rebus potongan wortel dan kentang bersama bawang putih geprek sampai empuk, bumbui garam dan merica, lalu taburi irisan seledri menjelang diangkat"),
    ("kacang panjang dan tempe sepotong", "oseng kacang panjang tempe", "goreng tempe potong korek setengah kering, tumis bawang dan cabai, masukkan kacang panjang dan sedikit kecap manis, lalu aduk bersama tempe"),
    ("jagung manis pipil dan susu cair", "jasuke jagung susu keju sederhana", "kukus atau rebus jagung pipil sampai empuk, selagi hangat campur dengan susu cair, sedikit margarin, dan taburan keju parut bila ada"),
    ("sawi putih dan tahu kuning", "tumis sawi putih tahu", "tumis bawang putih dan cabai, masukkan potongan tahu kuning yang sudah digoreng sebentar, lalu tambahkan sawi putih dan sedikit air sampai layu"),
    ("dada ayam dan nanas matang sepotong", "ayam asam manis nanas rumahan", "tumis potongan ayam sampai matang, masukkan potongan nanas, saus tomat, sedikit gula dan garam, lalu masak sampai sausnya mengental ringan"),
    ("telur puyuh rebus dan kentang", "semur telur puyuh kentang", "tumis bawang merah dan bawang putih, tuang air dan kecap manis, masukkan kentang potong dan telur puyuh kupas, lalu masak sampai kuah meresap"),
    ("bayam dan bawang merah saja", "sayur bening bayam kunci", "didihkan air bersama irisan bawang merah dan sepotong temu kunci geprek bila ada, masukkan bayam satu menit terakhir, lalu beri garam secukupnya"),
    ("roti tawar dan telur satu butir", "roti celup telur panggang teflon", "kocok telur dengan sejumput garam, celupkan roti tawar sebentar di kedua sisi, lalu panggang di teflon bermargarin sampai kecokelatan"),
    ("ubi ungu dan santan instan", "kolak ubi ungu sederhana", "rebus potongan ubi ungu sampai hampir empuk, masukkan santan encer, gula, dan selembar daun pandan bila ada, lalu masak sebentar sambil diaduk"),
]

MEAL_CTX_V3 = [
    ("buat lauk tanggal tua yang tetap nikmat", "Bahannya murah meriah tapi rasanya sama sekali tidak terasa seperti makanan penghematan."),
    ("buat menu buka puasa sederhana di rumah", "Rasanya yang hangat dan tidak neko-neko pas untuk mengawali buka sebelum makanan utama."),
    ("buat bekal anak atau bekal kerja besok pagi", "Masakan ini tahan disimpan semalam di kulkas dan tinggal dipanaskan sebentar sebelum berangkat."),
    ("buat makan malam ringan setelah hari yang melelahkan", "Porsinya yang tidak berlebihan bikin perut nyaman tanpa mengganggu waktu istirahat."),
    ("buat lauk patungan bareng teman satu kos", "Biaya bahannya enak dibagi rata dan memasaknya bisa gantian tugas biar adil."),
    ("buat sarapan akhir pekan yang agak santai", "Akhir pekan adalah waktu yang pas buat sarapan hangat buatan sendiri tanpa buru-buru."),
    ("buat camilan sore sambil minum teh di teras", "Disantap pelan-pelan bersama teh hangat bikin sore terasa jauh lebih nikmat."),
    ("buat menu saat badan kurang fit dan ingin yang hangat", "Makanan rumahan hangat seperti ini biasanya lebih bersahabat untuk perut yang sedang sensitif."),
    ("buat variasi menu supaya tidak bosan lauk yang itu-itu saja", "Satu menu baru dalam sepekan sudah cukup membuat urusan makan terasa segar lagi."),
    ("buat dimasak bareng adik atau keponakan yang lagi belajar dapur", "Langkahnya aman dan sederhana, cocok dikenalkan ke pemula dengan pendampingan orang dewasa."),
]
