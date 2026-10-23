"""Bagian 7 generator `chat.jsonl`:
- Merencanakan acara kecil, kumpul teman, & kegiatan bersama
- Rekomendasi tema buku, film, musik, & permainan santai sesuai suasana hati
- Aktivitas harian menghadapi perubahan cuaca & musim di Indonesia
- Keterampilan ngobrol tatap muka, bercerita, & percaya diri sehari-hari
- Kebiasaan mikro pagi & malam agar hidup lebih rapi
- Mengatasi rasa mager (malas gerak) & kejenuhan harian
- Obrolan santai imajinatif & refleksi ringan sehari-hari
"""
from __future__ import annotations

from .core_v2 import CategoryCollector

# --------------------------------------------------------------------------- #
# Block A: Merencanakan Acara Kecil & Kumpul Bersama (24 x 16 x 7 = 2.688)
# --------------------------------------------------------------------------- #
EVENT_PLANS = [
    ("makan malam bareng teman lama yang susah cocok jadwalnya", "buat pemungutan suara tiga pilihan tanggal saja dua minggu sebelumnya lalu kunci tanggal dengan suara terbanyak", "menunggu seratus persen orang kosong di hari yang sama biasanya bikin rencana batal berbulan-bulan"),
    ("acara syukuran kecil pindah ke kamar kos atau rumah baru", "pesan atau masak satu menu utama praktis seperti nasi kuning kotak ditambah buah potong dan air mineral gelas", "fokus utamanya silaturahmi kenal tetangga dekat, jadi hidangan ringkas jauh mengurangi repot bersih-bersih"),
    ("belajar kelompok lima orang menjelang ujian semester", "bagi subbab materi ke tiap anggota sehari sebelumnya supaya saat kumpul masing-masing bergantian menjelaskan rangkumannya", "tanpa pembagian materi di awal, kumpul belajar lima orang rawan habis buat mengobrol di luar pelajaran"),
    ("kejutan ulang tahun sederhana buat sahabat di sela jam istirahat", "patungan kue ukuran kecil atau donat isi enam disertai kartu ucapan yang ditandatangani semua teman satu lingkaran", "kejutan singkat yang tulus tanpa mengganggu jam kelas atau kerja justru terasa manis dan berkesan"),
    ("olahraga bulu tangkis atau futsal santai akhir pekan bareng teman", "pesan lapangan lebih dulu lalu kumpulkan uang patungan sewa di awal agar semua peserta merasa berkomitmen hadir", "patungan di muka efektif mencegah pembatalan mendadak satu jam sebelum jadwal main"),
    ("kerja bakti membersihkan selokan dan halaman lingkungan RT", "mulai pukul setengah tujuh pagi saat matahari belum terik, bagi area sapuan jelas, dan sediakan teh hangat serta rebusan", "pembagian titik kerja yang jelas membuat kerja bakti beres dalam sembilan puluh menit saja"),
    ("nonton bareng pertandingan olahraga atau film di ruang tengah", "siapkan colokan kabel tambahan, atur jarak layar agar nyaman dilihat dari karpet, dan sediakan kantong sampah di sudut", "menyiapkan kantong sampah sejak awal membuat beres-beres seusai acara selesai dalam lima menit"),
    ("arisan keluarga bulanan di rumah yang ruang tamunya tidak terlalu luas", "gulung karpet bersih lesehan dengan menyingkirkan meja tengah ke tepi dinding dan sajikan makanan prasmanan satu arah di meja samping", "duduk lesehan justru memuat lebih banyak anggota keluarga dengan suasana yang lebih akrab"),
    ("piknik hemat bawa bekal sendiri bareng teman satu kelas", "gunakan sistem potluck di mana satu orang membawa satu jenis makanan berbeda seperti nasi, lauk ayam, sayur, buah, dan minuman", "membagi jenis bawaan mencegah semua orang datang membawa keripik ringan yang sama"),
    ("rapat perdana kepanitiaan acara sekolah atau kampus", "kirim daftar agenda tiga poin sebelum rapat dimulai dan batasi durasi diskusi maksimal enam puluh menit dengan notula jelas", "rapat singkat yang menghasilkan pembagian tugas konkret bikin anggota semangat datang lagi"),
    ("menjenguk teman yang baru pulang dirawat dari rumah sakit", "tanyakan dulu jam istirahatnya kepada keluarganya, datang dalam rombongan kecil maksimal tiga orang, dan batasi kunjungan dua puluh menit", "pasien masa pemulihan cepat lelah kalau harus menjamu obrolan ramai terlalu lama"),
    ("masak bakar-bakaran jagung dan sosis malam liburan di teras", "oles bumbu setelah bahan setengah matang supaya tidak cepat gosong pahit dan siapkan kipas serta air dekat panggangan", "memanggang bumbu manis terlalu awal di atas bara panas membuat luarnya hangus padahal dalamnya dingin"),
    ("jalan kaki pagi Minggu lanjut sarapan bareng keluarga", "sepakati rute putaran sekitar tiga kilometer yang teduh dan pilih tempat sarapan yang buka sejak pukul enam pagi", "berangkat lebih pagi menghindarkan rombongan dari antrean penuh dan terik matahari"),
    ("tukar kado silang (tukar hadiah acak) harga terjangkau di grup teman", "tentukan batas harga ketat misalnya Rp30.000 dengan tema barang berguna sehari-hari tanpa makanan cepat basi", "aturan harga yang seragam memastikan semua orang senang tanpa ada yang merasa timpang"),
    ("sesi foto kenangan bareng teman seangkatan sebelum lulus", "tentukan dua warna pakaian senada yang semua orang sudah punya di lemari seperti putih-hitam atau biru dongker-krem", "memakai warna dasar yang sudah dimiliki semua orang menghemat pengeluaran beli seragam baru"),
    ("penggalangan donasi buku layak baca untuk taman baca anak", "tetapkan kriteria buku cerita atau pengetahuan yang halamannya masih lengkap lalu kelompokkan berdasarkan usia pembaca", "menyortir kelayakan buku sejak titik kumpul memudahkan relawan langsung memajangnya di rak"),
    ("diskusi bedah buku santai empat sampai enam orang", "pilih buku tipis di bawah dua ratus halaman dan siapkan tiga pertanyaan pemantik ringan agar semua peserta kebagian cerita", "suasana santai tanpa istilah rumit membuat peserta pemula berani menyampaikan kesannya"),
    ("perjalanan pulang bareng satu mobil sewa saat libur semester", "sepakati pembagian biaya sewa dan bensin secara transparan di grup serta batasi ukuran koper maksimal per penumpang", "membahas batas bagasi di awal mencegah barang bawaan tidak muat masuk bagasi saat hari keberangkatan"),
    ("buka puasa atau makan sore bersama di tempat makan ramai", "lakukan reservasi meja beserta daftar pesanan menu maksimal H-2 agar makanan keluar serentak saat waktunya tiba", "memesan menu di tempat saat jam puncak sering membuat rombongan menunggu lebih dari satu jam"),
    ("latihan musik atau paduan suara kecil tanpa mengganggu tetangga", "pilih jadwal latihan sore hari kerja atau Sabtu siang, tutup pintu-jendela rapat, dan hindari berlatih lewat pukul delapan malam", "memberi tahu tetangga sebelah sebelumnya menunjukkan sikap sopan yang menghindarkan teguran"),
    ("bazar makanan kecil untuk dana kegiatan organisasi", "pilih dua-tiga menu cepat saji yang tahan suhu ruang dengan modal terukur dan siapkan uang kembalian pecahan kecil sejak pagi", "kehabisan uang kembalian receh di jam ramai sering membuat pembeli batal bertransaksi"),
    ("mengantar sahabat ke stasiun atau bandara sebelum merantau jauh", "datang lebih awal supaya masih sempat duduk mengobrol tenang dan berikan catatan kecil yang baru boleh dibuka di perjalanan", "momen perpisahan yang hangat tanpa terburu-buru meninggalkan kenangan manis buat perantau"),
    ("kumpul main permainan papan (board game) sore hari di rumah", "pilih permainan yang aturannya bisa dijelaskan dalam tiga menit untuk pemanasan sebelum masuk ke permainan strategi panjang", "aturan pembuka yang sederhana membuat teman yang baru pertama ikut langsung menikmati suasananya"),
    ("reuni kecil lima sahabat lama setelah bertahun-tahun lulus", "pilih tempat duduk yang musik latarnya pelan supaya suara obrolan terdengar jelas tanpa harus berteriak", "tujuan utama reuni adalah melepas kangen lewat cerita, jadi kenyamanan ngobrol mengalahkan tempat yang sekadar viral"),
]

EVENT_CTX = [
    ("waktu pesertanya punya sifat yang beda-beda", "Menyatukan banyak kepala memang kuncinya komunikasi singkat yang adil dan nggak memihak."),
    ("dengan anggaran patungan yang ramah kantong pelajar", "Kumpul seru nggak harus mahal kok; kebersamaan dan rencana rapi jauh lebih menentukan."),
    ("padahal waktu persiapannya tinggal tiga hari lagi", "Karena waktunya mepet, pangkas detail tambahan dan amankan lokasi serta konsumsinya saja dulu."),
    ("supaya nggak cuma jadi wacana grup chat doang", "Begitu ada tanggal, tempat, dan satu koordinator tegas, wacana biasanya langsung berubah jadi nyata."),
    ("waktu aku kebagian tugas jadi pengatur utamanya", "Jangan pikul semua sendirian—delegasikan urusan konsumsi dan dokumentasi ke dua teman lain ya."),
    ("pas musim hujan yang cuacanya susah ditebak", "Selalu siapkan rencana cadangan ruang beratap supaya acara tetap jalan walau tiba-tiba turun hujan."),
    ("agar semua yang datang merasa dilibatkan dan nggak canggung", "Menyapa teman yang pendiam dan menariknya ke obrolan ringan bikin suasana grup terasa hangat merata."),
    ("tanpa menyisakan kelelahan beres-beres berlebih sesudahnya", "Menerapkan kebiasaan membereskan bekas makan masing-masing sebelum bubar sangat meringankan tuan rumah."),
    ("waktu sebagian teman suka datang ngaret dari jadwal", "Pasang jam kumpul tiga puluh menit lebih awal dari jam inti acara sebagai penyangga keterlambatan."),
    ("di sela minggu yang jadwal kuliah atau kerjanya lumayan padat", "Batasi durasi kumpul secukupnya dua jam berkualitas supaya besok semua tetap segar beraktivitas."),
    ("buat mempererat keakraban tim yang baru terbentuk", "Suasana santai di luar urusan tugas sering mencairkan kekakuan jauh lebih cepat daripada rapat formal."),
    ("dengan lokasi yang adil di tengah-tengah tempat tinggal semua orang", "Memilih titik temu dekat jalur angkutan umum memudahkan teman yang tidak membawa kendaraan pribadi."),
    ("supaya orang rumah juga nyaman kalau acaranya di rumahku", "Kabari orang rumah soal jam mulai-selesai dan jumlah teman yang datang sejak sehari sebelumnya."),
    ("waktu jumlah pesertanya sekitar enam sampai sepuluh orang", "Ukuran grup segini paling ideal karena masih cukup ramai tapi tetap bisa ngobrol satu meja utuh."),
]


# --------------------------------------------------------------------------- #
# Block B: Rekomendasi Tema Buku, Film, Musik, & Hiburan Tanpa Spoiler (24 x 14 x 7 = 2.352)
# --------------------------------------------------------------------------- #
MEDIA_THEMES = [
    ("cerita detektif misteri teka-teki ruang tertutup", "mengajak otak ikut menebak petunjuk kecil di sepanjang bab atau adegan tanpa adegan seram berlebihan", "perhatikan dialog awal tokoh-tokohnya karena petunjuk terpenting biasanya diselipkan secara halus di sana"),
    ("komedi keluarga hangat sehari-hari", "menyajikan tawa ringan dari salah paham akrab di meja makan yang ujungnya tetap bikin hati hangat", "tontonan atau bacaan seperti ini ampuh banget menurunkan ketegangan tanpa bikin kening berkerut"),
    ("dokumenter keindahan bawah laut dan hutan tropis", "memanjakan mata lewat warna alam yang menakjubkan sekaligus narasi tenang yang menambah wawasan", "sangat pas diputar sore hari sambil bersantai karena alurnya damai dan meneduhkan"),
    ("kisah petualangan persahabatan melintasi daerah baru", "menghadirkan semangat perjalanan, kerja sama saat menghadapi rintangan, dan pemandangan tempat yang menyegarkan", "cerita perjalanan sering membangkitkan rasa optimis waktu kita sendiri sedang jenuh di satu tempat"),
    ("musik akustik gitar dan piano tempo pelan", "memberi latar suara hangat yang menenangkan detak jantung tanpa mengganggu alur pikiran", "atur volumenya rendah sekitar tiga puluh persen supaya tetap menjadi latar yang nyaman di telinga"),
    ("novel irisan kehidupan (slice of life) berlatar toko kecil atau kedai kopi", "berfokus pada percakapan sederhana antarmanusia yang pelan-pelan menyembuhkan luka batin keseharian", "bab-babnya biasanya pendek dan mandiri sehingga nyaman dibaca satu bab setiap menjelang tidur"),
    ("kisah nyata perjuangan atlet atau penemu pantang menyerah", "memperlihatkan proses latihan panjang di balik layar sehingga memotivasi kita lebih sabar mengejar target sendiri", "melihat kegagalan awal tokoh besar menyadarkan kita bahwa ahli pun dulunya pernah tertatih-tatih"),
    ("fiksi ilmiah ringan tentang penjelajahan luar angkasa", "memancing rasa ingin tahu lewat gagasan masa depan dan keajaiban sains tanpa kehilangan sisi kemanusiaannya", "seru banget kalau habis menonton atau membaca lalu lanjut mencari tahu fakta astronomi aslinya"),
    ("kumpulan esai pendek reflektif tentang kebiasaan hidup", "menyuguhkan sudut pandang jernih soal hal remeh sehari-hari dalam tulisan tiga-empat halaman per topik", "kamu bebas membuka halaman mana saja secara acak sesuai judul bab yang sedang menarik perhatianmu"),
    ("musik instrumental suara alam hujan dan aliran sungai", "menutup suara bising kendaraan dari luar jendela sehingga menciptakan kubah fokus yang stabil di meja belajar", "sangat membantu saat harus membaca teks panjang karena tidak ada lirik kata yang memecah perhatian"),
    ("film animasi petualangan penuh warna yang sarat makna", "visualnya memanjakan imajinasi sementara pesan ceritanya tetap dalam saat direnungkan orang dewasa", "pilihan paling aman kalau menonton bersama anggota keluarga lintas usia di ruang tengah"),
    ("buku sejarah populer tentang jalur rempah dan pelayaran Nusantara", "membuka cerita asal-usul kota pelabuhan, kuliner, dan pertemuan budaya yang membentuk keseharian kita sekarang", "membaca sejarah lewat kisah keseharian masyarakatnya terasa hidup dan jauh dari kesan hafalan tahun"),
    ("siniar (podcast) obrolan ringan dua sahabat membahas keseharian", "terasa seperti ikut duduk satu meja mendengarkan teman mengobrol santai sambil mengerjakan pekerjaan rumah", "cocok diputar waktu menyetrika baju, mencuci piring, atau berjalan kaki sore keliling kompleks"),
    ("permainan tebak kata dan asosiasi petunjuk singkat", "mengaktifkan kelincahan kosakata dan memancing tawa spontan tanpa membutuhkan papan permainan rumit", "bisa dimainkan kapan saja bermodal kertas kecil waktu menunggu pesanan makanan datang"),
    ("cerita kuliner yang mengulik kisah di balik masakan tradisional", "menggabungkan hangatnya cerita keluarga dengan deskripsi aroma bumbu dapur yang menggugah selera", "hati-hati kalau menikmatinya tengah malam karena hampir pasti bikin perut ikut keroncongan!"),
    ("musik tempo ceria era lawas yang akrab di telinga", "membangkitkan energi gerak sehingga pekerjaan beres-beres kamar atau olahraga ringan terasa jauh lebih bersemangat", "irama yang ketukannya jelas membantu menjaga langkah kaki atau gerakan tangan tetap kompak"),
    ("buku panduan ilustrasi visual tentang cara kerja benda sehari-hari", "menjelaskan mekanisme mesin, alam, atau tubuh manusia lewat gambar potongan melintang yang langsung mudah dipahami", "cocok buat kamu yang lebih cepat menangkap penjelasan lewat gambar dibandingkan teks rapat"),
    ("kisah drama ruang sidang atau pemecahan kasus logis", "menyuguhkan adu argumen yang rapi, bukti bertahap, serta cara berpikir runtut dari berbagai sudut pandang", "melatih kita melihat sebuah persoalan dari dua sisi sebelum terburu-buru menarik kesimpulan"),
    ("antologi puisi pendek bahasa sehari-hari yang lugas", "merangkum perasaan rumit seperti rindu, lelah, atau harap ke dalam larik singkat yang mengena di hati", "dibaca lima menit di sela istirahat siang sudah cukup memberi jeda bernapas bagi pikiran"),
    ("permainan strategi menyusun rute atau kota di atas meja", "melatih perencanaan beberapa langkah ke depan sambil berinteraksi langsung tatap muka dengan teman semeja", "serunya permainan meja terletak pada negosiasi dan ekspresi langsung yang tidak tergantikan layar"),
]

MEDIA_MOODS = [
    ("waktu otak lagi lelah banget nggak kuat mikir berat", "Pilih durasi pendek atau bab tipis saja supaya tetap terasa menyegarkan tanpa menambah beban pikiran."),
    ("pas malam Minggu santai sendirian di kamar", "Siapkan minuman favorit dan pencahayaan lampu kuning teduh biar suasana istirahatmu makin maksimal."),
    ("buat nemenin perjalanan jauh di kereta atau bus", "Pastikan sudah diunduh ke memori perangkat sebelumnya supaya nggak terputus saat sinyal hilang di terowongan."),
    ("waktu pengen cari bahan obrolan seru bareng teman", "Habis menikmatinya, kamu punya banyak sudut menarik buat didiskusikan santai besoknya."),
    ("pas suasana hati lagi agak mendung butuh penghangat", "Cerita atau nada yang hangat pelan-pelan membantu mengangkat mood tanpa terasa memaksa ceria."),
    ("di sela istirahat tiga puluh menit siang hari", "Potongan singkatnya pas dinikmati sebentar lalu mudah dijeda saat harus kembali beraktivitas."),
    ("waktu lagi bosan sama tontonan algoritma yang itu-itu aja", "Mencoba genre yang jarang disentuh sering mempertemukan kita dengan favorit baru yang menyegarkan."),
    ("pas kumpul santai bareng adik atau keponakan di rumah", "Temanya ramah untuk semua umur, jadi aman dinikmati bareng tanpa rasa khawatir."),
    ("waktu lagi pengen memantik ide kreatif yang mampet", "Melihat karya dari medium berbeda sering membuka sambungan ide segar yang tak terpikirkan sebelumnya."),
    ("sebelum tidur malam supaya nggak scroll video pendek terus", "Ritme alurnya yang lebih tenang membantu mata dan pikiran melambat alami menuju jam tidur."),
    ("waktu cuaca hujan deras di luar sepanjang sore", "Perpaduan suara hujan dan pilihan hiburan yang pas bikin betah berlama-lama di rumah."),
    ("pas baru selesai melewati minggu ujian yang menguras tenaga", "Anggap ini hadiah istirahat yang layak setelah kepalamu bekerja keras berhari-hari."),
]


# --------------------------------------------------------------------------- #
# Block C: Keterampilan Ngobrol, Kebiasaan Pagi/Malam, & Anti-Mager (3 blok besar)
# --------------------------------------------------------------------------- #
SPEAKING_SKILLS = [
    ("memulai obrolan ringan sama orang di sebelah waktu antre atau di ruang tunggu", "lontarkan komentar netral seputar situasi bersama saat itu—misalnya panjangnya antrean atau sejuknya ruangan—sambil tersenyum tipis", "jika lawan bicara merespons singkat lalu kembali melihat HP, hormati isyaratnya bahwa ia sedang ingin tenang"),
    ("memperkenalkan diri di pertemuan komunitas baru tanpa terdengar kaku", "sebutkan nama panggilan, kesibukan singkat saat ini, serta satu hal spesifik yang membuatmu tertarik hadir di acara tersebut", "menyebutkan minat yang relevan memberi kail mudah bagi orang lain untuk menyambung obrolan"),
    ("menyampaikan ketidaksetujuan dalam diskusi tanpa membuat lawan bicara tersinggung", "akui dulu sisi masuk akal dari pendapatnya sebelum menyambung dengan kalimat 'di sisi lain, gimana kalau kita juga mempertimbangkan...'", "mengganti kata 'tapi kamu salah' menjadi 'bagaimana kalau dilihat dari sisi ini' menjaga suasana tetap sejuk"),
    ("menjadi pendengar yang bikin teman merasa nyaman bercerita", "jaga kontak mata yang wajar, beri anggukan kecil, dan tahan keinginan langsung memotong dengan cerita pengalaman dirimu sendiri", "sering kali orang bercerita hanya butuh didengarkan utuh dulu sebelum ditawari solusi"),
    ("menutup obrolan yang sudah terlalu panjang karena harus lanjut kerja", "rangkum hangat dalam satu kalimat seperti 'senang banget ngobrolin ini, berhubung jam dua ada tenggat aku izin lanjut kerja dulu ya'", "menyebutkan agenda berikutnya secara jelas membuat pamitmu terdengar wajar dan sopan"),
    ("menceritakan kejadian lucu supaya nggak terdengar garing atau bertele-tele", "pangkas detail sampingan yang tidak penting, bangun gambaran singkat situasinya, dan simpan kalimat kuncinya tepat di bagian akhir", "cerita pendek dua menit yang padat jauh lebih memancing tawa daripada cerita sepuluh menit yang berputar-putar"),
    ("meminta penjelasan ulang saat belum paham maksud pembicara", "katakan dengan jujur bagian mana yang sudah ditangkap lalu tanyakan 'boleh bantu beri contoh singkat untuk bagian terakhir tadi?'", "bertanya spesifik menunjukkan kamu menyimak serius, bukan melamun"),
    ("menghadapi keheningan canggung (awkward silence) saat jalan berdua", "terima jeda hening beberapa detik dengan santai sambil mengamati sekitar, lalu tanyakan pendapatnya tentang tempat yang baru dilewati", "tidak setiap detik kebersamaan harus dijejali suara; jeda tenang justru tanda obrolan yang rileks"),
    ("mengucapkan terima kasih yang terasa tulus dan berkesan", "sebutkan secara spesifik bantuan apa yang ia lakukan beserta dampak nyatanya yang meringankan urusanmu hari itu", "ucapan terima kasih yang menyebut detail usaha seseorang terasa sepuluh kali lebih hangat daripada sekadar satu kata singkat"),
    ("meminta maaf secara langsung ketika melakukan kekeliruan nyata", "akui letak kesalahanmu secara lugas tanpa menyalahkan keadaan, sampaikan penyesalan tulus, dan tanyakan apa yang bisa diperbaiki sekarang", "permintaan maaf tanpa kata 'tapi kan gara-gara...' menunjukkan tanggung jawab yang dewasa"),
    ("menenangkan teman yang sedang bicara dengan nada panik terburu-buru", "turunkan tempo dan volume suaramu sendiri lebih dulu, ajak ia duduk menarik napas, lalu bantu urutkan masalahnya satu per satu", "ketenangan suara lawan bicara secara alami menular menurunkan kepanikan di ruangan"),
    ("menolak ajakan debat kusir di kolom komentar atau tongkrongan", "tersenyum tenang dan katakan 'menarik sudut pandangmu, kayaknya kita memang melihat dari kacamata berbeda aja soal ini' lalu alihkan topik", "menghemat energi dari perdebatan yang tidak mencari kebenaran membuat hatimu jauh lebih damai"),
]

SPEAK_CTX = [
    ("buat aku yang aslinya introvert dan gampang kehabisan kata-kata", "Sebagai introvert, keunggulannya justru kamu pengamat yang tulus—cukup satu kalimat hangat, nggak perlu jadi paling ramai."),
    ("waktu ketemu orang yang usianya jauh lebih senior", "Menghadapi yang lebih senior, sikap sopan mendengarkan dan nada bicara tenang sudah memberi nilai plus besar."),
    ("pas suasananya baru kenal lima menit pertama", "Di menit-menit awal perkenalan, ekspresi wajah ramah berbicara lebih nyaring daripada kalimat panjang."),
    ("supaya nggak kepikiran terus sehabis pulang ke rumah", "Kalau niatmu baik dan bahasamu sopan, nggak perlu memutar ulang tiap detik percakapannya malam nanti."),
    ("di acara kumpul sekolah, kampus, atau kantor", "Di acara bersama, cukup fokus ngobrol berkualitas dengan dua-tiga orang daripada memaksa menyapa puluhan orang sekaligus."),
    ("waktu tenggorokan rasanya agak kaku karena gugup", "Minum seteguk air putih dulu dan perlambat sedikit kecepatan bicaramu supaya napas tetap teratur."),
    ("agar komunikasi sehari-hari makin luwes pelan-pelan", "Anggap tiap obrolan singkat harian sebagai latihan ringan—makin sering dicoba, makin hilang rasa canggungnya."),
    ("tanpa harus berpura-pura jadi pribadi orang lain", "Tetap jadi dirimu yang apa adanya; ketulusan jauh lebih nyaman dirasakan lawan bicara daripada gaya yang dibuat-buat."),
]

HABIT_ROUTINES = [
    ("merapikan seprai dan selimut langsung begitu bangun tidur", "butuh waktu kurang dari dua menit untuk menarik ujung seprai dan melipat selimut sebelum keluar kamar", "menyelesaikan satu kerapian visual pertama di pagi hari memberi rasa teratur yang menular ke kegiatan berikutnya"),
    ("menyiapkan pakaian dan isi tas sejak malam sebelumnya", "gantung baju yang sudah rapi dan masukkan dompet serta buku catatan ke tas sebelum mematikan lampu tidur", "pagi harimu bebas dari kepanikan membongkar lemari sehingga kamu bisa sarapan dengan tenang"),
    ("mencuci piring dan gelas kotor sebelum pergi tidur malam", "biasakan langsung membilas alat makan sesudah makan malam agar sisa saus tidak mengering keras semalaman", "bangun pagi melihat wastafel dapur bersih memberi suasana hati yang jauh lebih segar"),
    ("menaruh kunci, kartu akses, dan kacamata di satu mangkuk tetap dekat pintu", "sediakan satu wadah kecil khusus di meja dekat pintu dan disiplinkan tangan langsung menaruhnya begitu masuk rumah", "kebiasaan satu titik tetap ini menghemat puluhan jam waktu panik mencari barang terselip setiap tahunnya"),
    ("mematikan layar gawai tiga puluh menit sebelum jam tidur", "aktifkan pengingat mode malam otomatis lalu ganti sisa waktunya dengan meredupkan lampu dan peregangan ringan", "tanpa paparan cahaya biru layar jarak dekat, hormon kantuk alami bekerja jauh lebih mulus"),
    ("menulis tiga kalimat rasa syukur atau hal baik kecil malam hari", "catat hal sederhana seperti makanan enak siang tadi, cuaca cerah, atau sapaan ramah teman di buku saku", "melatih otak mengenali hal baik kecil menyeimbangkan kecenderungan alami manusia yang suka terpaku pada masalah"),
    ("minum satu gelas penuh air putih suhu ruang saat bangun pagi", "letakkan gelas tertutup atau botol bersih di meja samping tempat tidur sejak malam agar langsung terlihat saat buka mata", "tubuh kehilangan cairan lewat pernapasan sepanjang tujuh jam tidur sehingga air pagi cepat menyegarkan badan"),
    ("melakukan aturan dua menit untuk urusan remeh di depan mata", "jika suatu pekerjaan kecil seperti membuang bungkus paket atau mengelap tumpahan air selesai di bawah dua menit, kerjakan detik itu juga", "tumpukan berantakan besar hampir selalu berawal dari sepuluh urusan dua menitan yang ditunda"),
    ("mengecek ramalan cuaca dan jadwal agenda sambil sarapan", "intip sebentar agenda hari itu agar tahu perlu membawa payung, bekal tambahan, atau berangkat sedikit lebih awal", "antisipasi satu menit di meja sarapan menyelamatkanmu dari kejutan jadwal mendadak di siang hari"),
    ("menyisihkan sepuluh menit Minggu malam merapikan dompet dan tas", "buang kertas struk lama yang tak terpakai, susun uang kertas rapi, dan isi ulang tisu saku untuk pekan baru", "tas yang ringan dan rapi bikin langkah berangkat hari Senin terasa jauh lebih siap"),
    ("berjemur kena sinar matahari pagi sepuluh menit sambil jalan kecil", "keluar ke teras atau halaman sekitar pukul tujuh sampai delapan pagi sambil menggerakkan bahu dan lengan", "cahaya alami pagi membantu menyetel jam biologis tubuh sehingga malamnya kamu lebih mudah mengantuk tepat waktu"),
    ("memberi jeda hening lima menit sepulang beraktivitas sebelum pegang urusan rumah", "duduk tenang setelah ganti pakaian rumah untuk mengatur napas agar kepenatan luar tidak terbawa ke obrolan rumah", "transisi singkat ini menjaga suasana hati tetap ramah kepada orang rumah maupun diri sendiri"),
]

HABIT_CTX = [
    ("padahal selama ini aku orangnya agak pelupa dan berantakan", "Justru karena sering lupa, tempelkan kebiasaan baru ini persis sesudah kebiasaan lama yang sudah otomatis kamu lakukan."),
    ("waktu lagi sibuk banget sampai merasa nggak punya waktu luang", "Semua langkah ini cuma memakan satu sampai lima menit, malahan menghemat jauh lebih banyak waktu di belakang."),
    ("supaya nggak cuma semangat tiga hari pertama terus berhenti", "Kalau suatu hari terlewat sekali, jangan menyerah total—cukup sambung lagi besoknya tanpa menyalahkan diri sendiri."),
    ("di kamar kos sendiri yang nggak ada orang mengingatkan", "Pasang pengingat visual sederhana di meja atau pintu sampai gerakan tangannya jadi refleks alami dalam tiga minggu."),
    ("bareng teman sekamar atau anggota rumah biar kompak", "Kalau disepakati bareng penghuni rumah secara santai, menjaga kerapian bersama jadi terasa jauh lebih ringan."),
    ("buat memperbaiki pola hidup pelan-pelan di bulan ini", "Pilih satu kebiasaan saja dulu minggu ini; setelah menempel kuat, baru tambahkan kebiasaan berikutnya."),
    ("waktu badan rasanya sering mager kalau sudah rebahan", "Lakukan tepat sebelum kamu menjatuhkan badan ke kasur, karena bangkit dari kasur butuh tenaga mental dua kali lipat."),
    ("agar kepala terasa lebih tenang dan nggak dikejar-kejar terus", "Hidup yang tertata di hal-hal kecil memberi rasa kendali yang menenangkan pikiran sepanjang hari."),
]


def build_chat_everyday_plus(col: CategoryCollector, limit: int | None = None) -> None:
    pair_idx = 0

    # Block A: Merencanakan acara kecil (24 * 14 * 7 = 2.352)
    ev_q = [
        "nara, gimana tips ngatur {ev} {ctx}?",
        "kasih saran praktis buat {ev} {ctx} dong!",
        "biar acara {ev} berjalan lancar {ctx}, kuncinya apa?",
        "aku mau nyiapin {ev} {ctx}, enaknya mulai dari mana?",
        "eh nara, bantu trik beresin {ev} {ctx} ya",
        "kalau mau ngadain {ev} {ctx}, apa yang perlu diperhatiin?",
        "ada tips simpel merencanakan {ev} {ctx}?",
    ]
    ev_a = [
        "Biar acaranya beres tanpa pusing, coba {how}. {ctx_note} Soalnya dari pengalaman sehari-hari, {why}.",
        "Langkah paling efektif untuk itu adalah {how}. {ctx_note} Perlu diingat juga bahwa {why}.",
        "Kuncinya sederhana kok: langsung {how}. {ctx_note} Alasannya jelas, {why}.",
        "Saran praktis dariku, mulai dengan {how}. {ctx_note} Kenapa penting? Karena {why}.",
        "Kamu bisa mengaturnya dengan cara santai tapi rapi: {how}. {ctx_note} Sebab, {why}.",
        "Supaya semua nyaman dan lancar, {how}. {ctx_note} Catatan kecilnya: {why}.",
        "Trik yang paling sering menyelamatkan acara begitu adalah {how}. {ctx_note} Ingat ya, {why}.",
    ]
    for ev, how, why in EVENT_PLANS:
        for ctx, ctx_note in EVENT_CTX:
            pair_idx += 1
            for k in range(len(ev_q)):
                if limit and len(col.rows) >= limit:
                    return
                q = ev_q[k].format(ev=ev, ctx=ctx)
                a = ev_a[(k + pair_idx) % len(ev_a)].format(
                    how=how, why=why, ctx_note=ctx_note
                )
                col.add(q, a)

    # Block B: Rekomendasi tema buku/film/musik/hiburan (20 * 12 * 7 = 1.680)
    md_q = [
        "nara, cocok nggak menikmati hiburan bertema {theme} {mood}?",
        "kasih gambaran serunya {theme} {mood} dong!",
        "kalau {mood}, kenapa tema {theme} enak dipilih?",
        "eh nara, menurutmu {theme} pas nggak buat {mood}?",
        "rekomendasiin alasan kenapa {theme} asyik dinikmati {mood}",
        "lagi pengen suasana {theme} nih {mood}, tips menikmatinya gimana?",
        "bantu saran hiburan santai: gimana kalau {theme} {mood}?",
    ]
    md_a = [
        "Pilihan yang pas banget! Tema {theme} itu asyik karena {desc}. {mood_note} Tips kecilnya, {tip}.",
        "Cocok sekali buat kondisimu! Lewat {theme}, karya seperti itu {desc}. {mood_note} Biar makin seru, {tip}.",
        "Wah, selera yang hangat nih! Biasanya {theme} {desc}. {mood_note} Selain itu, {tip}.",
        "Aku setuju banget sama ide itu, sebab {theme} {desc}. {mood_note} Coba juga {tip}.",
        "Pas banget! Daya tarik utama {theme} memang {desc}. {mood_note} Sekadar saran ringan, {tip}.",
        "Boleh banget dicoba! Soalnya {theme} {desc}. {mood_note} Jangan lupa, {tip}.",
        "Ide bagus buat melepas penat, karena {theme} {desc}. {mood_note} Catatan asyiknya: {tip}.",
    ]
    for theme, desc, tip in MEDIA_THEMES:
        for mood, mood_note in MEDIA_MOODS:
            pair_idx += 1
            for k in range(len(md_q)):
                if limit and len(col.rows) >= limit:
                    return
                q = md_q[k].format(theme=theme, mood=mood)
                a = md_a[(k + pair_idx) % len(md_a)].format(
                    theme=theme, desc=desc, tip=tip, mood_note=mood_note
                )
                col.add(q, a)

    # Block C: Keterampilan ngobrol & percaya diri (12 * 8 * 7 = 672)
    sp_q = [
        "nara, gimana cara {skill} {ctx}?",
        "ajarin tips praktis buat {skill} {ctx} dong",
        "biar luwes waktu {skill} {ctx}, triknya apa ya?",
        "aku suka bingung kalau harus {skill} {ctx}, sarannya gimana?",
        "eh nara, kasih panduan santai soal {skill} {ctx}",
        "langkah gampang supaya bisa {skill} {ctx} apa aja?",
        "bantu masukan dong buat latihan {skill} {ctx}",
    ]
    sp_a = [
        "Nggak sesulit bayangan kok! Kamu cukup {how}. {ctx_note} Ingat juga bahwa {why}.",
        "Trik komunikasi sederhananya begini: {how}. {ctx_note} Soalnya, {why}.",
        "Coba mulai dengan langkah ringan ini: {how}. {ctx_note} Alasannya jelas, {why}.",
        "Pendekatan paling nyaman adalah {how}. {ctx_note} Pegang prinsip kecil ini: {why}.",
        "Kamu bisa mempraktikkannya pelan-pelan: {how}. {ctx_note} Sebab dalam obrolan, {why}.",
        "Kuncinya ada di ketenangan: {how}. {ctx_note} Perlu dicatat juga, {why}.",
        "Saran dariku, langsung coba {how}. {ctx_note} Kenapa manjur? Karena {why}.",
    ]
    for skill, how, why in SPEAKING_SKILLS:
        for ctx, ctx_note in SPEAK_CTX:
            pair_idx += 1
            for k in range(len(sp_q)):
                if limit and len(col.rows) >= limit:
                    return
                q = sp_q[k].format(skill=skill, ctx=ctx)
                a = sp_a[(k + pair_idx) % len(sp_a)].format(
                    how=how, why=why, ctx_note=ctx_note
                )
                col.add(q, a)

    # Block D: Kebiasaan mikro pagi & malam (12 * 8 * 7 = 672)
    hb_q = [
        "nara, seberapa ngaruh kebiasaan {hab} {ctx}?",
        "gimana cara mulai membiasakan {hab} {ctx}?",
        "kasih tips biar konsisten {hab} {ctx} dong!",
        "eh nara, praktis nggak sih rutinitas {hab} {ctx}?",
        "bantu cara gampang menerapkan {hab} {ctx} ya",
        "kenapa kebiasaan kecil kayak {hab} bagus dicoba {ctx}?",
        "ajarin trik anti gagal buat {hab} {ctx} dong",
    ]
    hb_a = [
        "Kebiasaan kecil itu dampaknya terasa banget! Caranya ringan: {how}. {ctx_note} Manfaat utamanya, {why}.",
        "Sangat layak dicoba karena praktis: {how}. {ctx_note} Soalnya, {why}.",
        "Mulainya gampang banget kok, {how}. {ctx_note} Alasannya sederhana: {why}.",
        "Rutinitas ini ringan tapi efektif—{how}. {ctx_note} Perlu diingat, {why}.",
        "Bisa langsung dipraktikkan hari ini: {how}. {ctx_note} Sebab dalam keseharian, {why}.",
        "Kuncinya karena langkahnya singkat: {how}. {ctx_note} Selain itu, {why}.",
        "Aku sangat menyarankan ini karena {how}. {ctx_note} Efek baiknya, {why}.",
    ]
    for hab, how, why in HABIT_ROUTINES:
        for ctx, ctx_note in HABIT_CTX:
            pair_idx += 1
            for k in range(len(hb_q)):
                if limit and len(col.rows) >= limit:
                    return
                q = hb_q[k].format(hab=hab, ctx=ctx)
                a = hb_a[(k + pair_idx) % len(hb_a)].format(
                    how=how, why=why, ctx_note=ctx_note
                )
                col.add(q, a)
