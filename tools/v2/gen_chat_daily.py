"""Bagian 2 generator `chat.jsonl`:
- Curhat & emosi sehari-hari (sekolah, kuliah, kerja, rantau, pertemanan, hati)
- Makanan harian, ide masak praktis anak kos, & masalah dapur
- Urusan rumah tangga, kebersihan kamar, & rutinitas sehat
- Fokus belajar, anti-ngantuk, anti-menunda, & manajemen energi

Setiap sumbu konteks menyumbangkan kalimat insight utuh yang relevan sehingga
jawaban selalu spesifik terhadap cerita pengguna (bukan sekadar ganti satu kata).
"""
from __future__ import annotations

from .core_v2 import CategoryCollector

# --------------------------------------------------------------------------- #
# 1. Curhat & Emosi Sehari-hari (20 skenario x 14 konteks bermakna x 7 gaya)
# --------------------------------------------------------------------------- #
EMOTION_SCENARIOS = [
    (
        "capek banget habis seharian beraktivitas",
        "badan rasanya remuk dan kepala penuh",
        "rebahkan badan sebentar tanpa lihat layar HP lalu minum segelas air biasa",
        "istirahat malam ini bukan berarti kamu malas, memang tenagamu habis dipakai berjuang",
    ),
    (
        "sedih karena hasil ujian nggak sesuai harapan",
        "udah belajar lama tapi angkanya tetap meleset dari target",
        "kasih jeda sehari buat menenangkan hati sebelum mengecek bagian soal yang keliru",
        "satu nilai ujian nggak pernah menentukan seluruh masa depan atau kepintaranmu",
    ),
    (
        "kesal karena teman kelompok ngilang pas tugas hampir dikumpul",
        "kerjaan jadi numpuk sendirian padahal nilainya dibagi rata",
        "catat pembagian kerja yang jelas di grup dan amankan bagian utama supaya nilaimu sendiri selamat dulu",
        "wajar banget kamu gondok ketika tanggung jawab bersama malah dilepas begitu saja",
    ),
    (
        "grogi parah mau presentasi di depan banyak orang",
        "tangan terasa dingin dan takut tiba-tiba lupa kalimat pembuka",
        "siapkan tiga poin kunci di catatan kecil dan tarik napas empat hitungan sebelum mulai bicara",
        "pendengar biasanya fokus ke isi ceritamu, bukan menghitung getar kecil di suaramu",
    ),
    (
        "minder lihat teman sebaya kelihatan jauh lebih sukses di medsos",
        "rasanya jalan di tempat padahal umur terus bertambah",
        "tutup dulu aplikasi medsos sehari-dua hari lalu tulis tiga kemajuan kecil yang sudah kamu capai bulan ini",
        "linimasa cuma memajang cuplikan terbaik orang, bukan jatuh-bangun di belakang layarnya",
    ),
    (
        "kangen rumah dan suasana keluarga waktu lagi merantau",
        "kamar terasa sepi banget pas sore menjelang malam",
        "kirim pesan suara atau telepon orang rumah lima menit, lalu cari makanan hangat yang akrab di lidah",
        "rasa rindu itu tanda kamu punya tempat pulang yang hangat di dalam hati",
    ),
    (
        "overthinking malam-malam mikirin hari esok yang belum kejadian",
        "mata sebenarnya berat tapi otak memutar skenario buruk terus",
        "tuangkan semua kekhawatiran ke kertas catatan supaya otak merasa urusannya sudah dititipkan sampai besok",
        "pikiran larut malam sering membesar-besarkan masalah yang besok paginya ternyata masih bisa diatasi",
    ),
    (
        "habis ditegur atasan atau pengajar karena salah paham kecil",
        "dada rasanya mengganjal pengen menjelaskan tapi situasi tadi kurang pas",
        "tenangkan diri sampai emosi stabil, baru sampaikan klarifikasi singkat yang sopan dan jelas",
        "teguran memang bikin kaget, tapi kualitas dirimu nggak runtuh gara-gara satu kekeliruan",
    ),
    (
        "patah hati karena hubungan yang dijaga lama akhirnya selesai",
        "hal-hal kecil di jalan masih sering memicu ingatan lama",
        "rapikan dulu barang atau riwayat chat pemicu sedih dan izinkan dirimu pulih tanpa terburu-buru",
        "proses sembuh dari kehilangan memang naik-turun, jalani pelan-pelan hari demi hari",
    ),
    (
        "canggung masuk lingkungan kelas atau tempat kerja baru",
        "orang-orang di sekitar kelihatan sudah punya obrolan akrab sendiri",
        "mulai dari senyum dan sapaan ringan ke satu orang di sebelahmu tanpa menuntut langsung dekat",
        "hampir setiap orang baru sebenarnya menyimpan rasa kikuk yang mirip di minggu awal",
    ),
    (
        "jenuh sama rutinitas harian yang polanya berulang terus",
        "dari pagi ke malam rasanya datar tanpa hal yang ditunggu-tunggu",
        "selipkan satu variasi kecil seperti lewat jalan berbeda, ganti sudut duduk, atau coba minuman baru",
        "rasa bosan itu sinyal alami bahwa pikiranmu butuh sedikit udara segar",
    ),
    (
        "kecewa karena lamaran kerja atau seleksi beasiswa belum lolos",
        "berkas yang disiapkan berminggu-minggu berujung pesan penolakan",
        "jeda dulu sehari dari membuka portal pengumuman, besok baru evaluasi bagian CV yang bisa dipertajam",
        "belum lolos di satu pintu sering kali soal kuota dan kecocokan, bukan bukti kamu gagal total",
    ),
    (
        "kepikiran terus gara-gara merasa salah ngomong waktu ngobrol tadi",
        "takut kalimat spontan tadi bikin teman tersinggung diam-diam",
        "kalau memang terasa mengganjal, sapa ringan untuk meluruskan maksudmu lalu lepaskan bebannya",
        "lawan bicara umumnya sudah sibuk dengan urusannya sendiri dan jarang mengingat selip kata sedetail kita",
    ),
    (
        "lega sekaligus terharu akhirnya tugas besar kelar juga",
        "beban berat berminggu-minggu rasanya langsung plong dari pundak",
        "hadiahi dirimu dengan tidur lebih awal atau menyantap makanan kesukaanmu dengan tenang",
        "ketekunanmu menyelesaikan urusan sampai garis akhir itu layak banget dirayakan",
    ),
    (
        "kewalahan karena semua urusan mendadak datang berbarengan",
        "bingung harus menyentuh yang mana duluan saking penuhnya daftar",
        "ambil satu tugas paling pendek yang selesai dalam sepuluh menit supaya langkahmu mulai bergerak",
        "begitu satu beban kecil beres, kabut panik di kepala biasanya langsung berkurang banyak",
    ),
    (
        "kesal gara-gara kehujanan di jalan sampai pakaian dan sepatu basah",
        "jadwal jadi molor dan badan terasa lengket kedinginan",
        "segera ganti baju kering, sumbat sepatu dengan kertas koran, dan minum teh atau air hangat",
        "mengalami kejadian apes di jalan memang wajar banget bikin suasana hati langsung turun",
    ),
    (
        "takut mengecewakan orang tua yang sudah menaruh harapan besar",
        "setiap mau melangkah rasanya takut salah ambil keputusan",
        "ajak orang tua mengobrol jujur soal proses yang sedang kamu hadapi sedikit demi sedikit",
        "orang tua umumnya jauh lebih tenang melihat anaknya sehat dan jujur daripada memendam tekanan sendirian",
    ),
    (
        "merasa tertinggal waktu belajar materi baru yang temannya cepat paham",
        "penjelasan di kelas lewat cepat sementara kita masih mencerna dasar",
        "catat satu bagian spesifik yang belum nyambung lalu pelajari ulang pakai contoh paling sederhana",
        "kecepatan orang menangkap hal baru memang beda-beda, yang penting konsisten paham akarnya",
    ),
    (
        "gugup menunggu pengumuman penting yang keluarnya besok",
        "perut rasanya mules dan bolak-balik mengecek layar HP",
        "alihkan tangan ke kegiatan fisik ringan seperti merapikan meja atau jalan sore dua puluh menit",
        "bagian usahamu sudah tuntas dikerjakan, jadi cemas berlebih sekarang nggak mengubah hasilnya",
    ),
    (
        "sedih karena sahabat dekat sekarang jarang punya waktu ngobrol",
        "masing-masing makin sibuk sampai obrolan terasa menjauh",
        "kirim pesan singkat tulus menanyakan kabar tanpa menuntut dia harus membalas panjang saat itu juga",
        "pertemanan yang dewasa kadang memang jarang bertemu, tapi hangatnya tetap nyambung saat ada waktu",
    ),
]

CURHAT_CONTEXTS = [
    ("di hari Senin yang padat ini", "Awal pekan memang sering langsung tancap gas, jadi wajar kalau tenagamu berasa cepat terkuras."),
    ("padahal ini akhir pekan", "Saat hari libur pun pikiran belum tentu otomatis ikut libur kalau beban kemarin masih terbawa."),
    ("waktu lagi sendirian di kamar kos", "Suasana kos yang hening memang sering bikin perasaan di kepala terdengar dua kali lebih nyaring."),
    ("menjelang tanggal tua akhir bulan", "Tekanan hemat di akhir bulan memang suka bikin sumbu sabar kita jadi sedikit lebih tipis."),
    ("setelah beberapa hari kurang tidur", "Kurang tidur beruntun bikin emosi jauh lebih sensitif terhadap hal yang biasanya terasa ringan."),
    ("padahal tadi pagi mood-ku sempat bagus", "Perubahan suasana hati mendadak dari pagi yang cerah ke sore yang berat memang bikin kaget."),
    ("waktu cuaca di luar mendung seharian", "Langit mendung dan kurang cahaya matahari kadang memang ikut bikin energi terasa agak redup."),
    ("sampai rasanya malas membalas pesan siapa pun", "Menarik diri sebentar dari keramaian chat itu manusiawi kok waktu baterai sosialmu lagi habis."),
    ("padahal aku merasa sudah berusaha keras", "Justru karena kamu sudah peduli dan mengerahkan tenaga, rasa kecewanya jadi terasa lebih nyata."),
    ("di tengah minggu yang jadwalnya rapat banget", "Pertengahan minggu memang titik rawan lelah karena sisa tenaga mulai menipis sementara tugas masih antre."),
    ("waktu baru aja sampai rumah sore ini", "Momen baru melepas sepatu sepulang aktivitas memang sering jadi waktu semua rasa lelah tumpah sekaligus."),
    ("sambil nunggu jemputan atau kendaraan umum", "Bengong di sela perjalanan sering bikin pikiran melayang ke mana-mana tanpa rem."),
    ("waktu lagi nggak enak badan dikit", "Kondisi fisik yang kurang fit otomatis bikin daya tahan hati ikut menurun, jadi jangan keras-keras ke diri sendiri."),
    ("pas lihat kalender ternyata bulan cepat banget lewat", "Melihat tanggal berganti cepat memang kadang memicu rasa dikejar waktu tanpa sadar."),
]

CURHAT_Q_STYLES = [
    "nara, aku lagi {sit} {ctx}, rasanya {feel}...",
    "jujur {ctx} aku {sit}, gimana ya biar hati agak tenang?",
    "eh nara temenin cerita dong, aku {sit} dan {feel} {ctx}",
    "wajar nggak sih kalau aku {sit} {ctx} terus jadi {feel}?",
    "aduh {feel} nih nara, soalnya aku {sit} {ctx}",
    "kak nara, bagi semangat dong, aku {sit} {ctx}",
    "gimana cara ngatasin perasaan pas {sit} {ctx}? soalnya {feel}",
]

CURHAT_A_STYLES = [
    "Sini tarik napas pelan dulu bareng Nara. {ctx_note} Ketika {feel}, ingat satu hal: {reassure}. Kalau sudah agak lega, coba {action}.",
    "Terima kasih sudah mau cerita ke aku ya. {ctx_note} Untuk langkah paling dekat saat {feel}, mending {action}. Pegang juga pengingat ini: {reassure}.",
    "Wajar banget kok kamu merasakan itu! {ctx_note} Daripada dipaksa tegar terus padahal {feel}, coba {action}. Pelan-pelan aja, sebab {reassure}.",
    "Aku dengerin ceritamu dengan saksama. {ctx_note} Saat kondisi {feel}, kamu nggak harus membereskan semuanya sekaligus—mulai saja dengan {action}. Percaya deh, {reassure}.",
    "Nggak apa-apa banget buat ngaku lelah di momen begini. {ctx_note} Biar kepalamu agak longgar dari rasa {feel}, coba {action}. Dan ingat ya, {reassure}.",
    "Kebayang beratnya berada di posisimu sekarang. {ctx_note} Coba ambil jeda sebentar lalu {action}. Satu hal yang perlu kamu yakini: {reassure}.",
    "Hei, kamu sudah bertahan sejauh ini aja sudah keren lho. {ctx_note} Waktu {feel}, langkah paling ramah buat dirimu sendiri adalah {action}, karena {reassure}.",
]


# --------------------------------------------------------------------------- #
# 2. Makanan, Masak Praktis Anak Kos, & Dapur Harian (22 bahan x 12 situasi x 6 gaya)
# --------------------------------------------------------------------------- #
INGREDIENTS_RECIPES = [
    ("telur dan kecap manis", "telur ceplok masak kecap bawang iris", "ceplok telur setengah garing, tumis bawang merah-putih sebentar, lalu kucuri sedikit air dan kecap manis sampai meresap"),
    ("tahu putih dan bawang putih", "tahu cabai garam renyah", "potong dadu tahu lalu goreng berkulit, kemudian aduk cepat bersama tumisan bawang putih cincang, cabai iris, dan sejumput garam"),
    ("tempe dan tepung bumbu", "tempe mendoan hangat", "iris tipis tempe melebar, celupkan ke adonan tepung encer berdaun bawang, lalu goreng sebentar supaya dalamnya tetap lembut"),
    ("mie instan dan sawi hijau", "mie kuah sayur telur rebus", "rebus sawi dan telur di air bersih, ganti air rebusan bila suka kuah bening, lalu tambahkan bumbu secukupnya"),
    ("nasi sisa semalam dan telur", "nasi goreng kampung bawang merah", "orak-arik telur di sedikit minyak, tumis ulekan bawang merah-putih-cabai sampai wangi, baru aduk nasi dingin di api agak besar"),
    ("dada ayam dan saus tiram", "ayam tumis saus tiram lada hitam", "iris tipis ayam agar cepat matang, tumis bersama bawang bombai, satu sendok saus tiram, dan taburan lada"),
    ("kentang dan wortel", "sup bening kentang wortel hangat", "rebus potongan kentang dan wortel di air mendidih bersama geprekan bawang putih, daun bawang, seledri, dan garam"),
    ("roti tawar dan pisang matang", "roti panggang pisang teflon", "oles tipis margarin di permukaan roti, isi irisan pisang manis, lalu panggang bolak-balik di teflon api kecil"),
    ("kangkung dan bawang putih", "tumis kangkung bawang putih cepat", "tumis bawang putih geprek dan cabai di api besar, masukkan kangkung bersih dan sedikit saus tiram, lalu angkat selagi hijau segar"),
    ("sosis dan margarin", "sosis bakar teflon pedas manis", "kerat serong sosis, panggang dengan sedikit margarin sambil dioles campuran saus sambal dan kecap manis"),
    ("bayam dan jagung manis", "sayur bening bayam jagung segar", "rebus pipilan jagung manis lebih dulu sampai empuk, baru masukkan daun bayam dan irisan bawang merah satu menit saja"),
    ("oatmeal dan susu cair", "bubur oat pisang hangat", "masak oatmeal bersama susu atau air hangat selama dua menit, lalu beri irisan pisang di atasnya sebagai pemanis alami"),
    ("kornet dan dua butir telur", "dadar gulung kornet daun bawang", "kocok telur dengan satu sendok kornet serta irisan daun bawang, lalu dadar tipis merata di wajan antilengket"),
    ("terong ungu dan tomat merah", "terong panggang sambal tomat", "belah terong lalu panggang di teflon sedikit minyak sampai empuk, kemudian siram tumisan sambal tomat matang di atasnya"),
    ("jamur tiram dan daun bawang", "tumis jamur tiram suwir gurih", "suwir jamur lalu peras air cuciannya, kemudian tumis cepat dengan bawang putih, daun bawang, dan sejumput merica"),
    ("sarden kaleng dan jeruk nipis", "sarden tumis bawang iris segar", "tumis bawang merah iris dan cabai dulu sebelum memasukkan sarden serta perasan sedikit jeruk nipis agar tidak amis"),
    ("tahu kuning dan tauge", "tumis tahu tauge renyah", "goreng sebentar potongan tahu kuning, tumis bawang putih, lalu masukkan tauge tiga puluh detik terakhir supaya tetap garing"),
    ("kol, wortel, dan sebutir telur", "orak-arik sayur telur praktis", "buat orak-arik telur lalu pinggirkan di wajan, tumis bawang putih, kemudian aduk irisan wortel dan kol dengan api sedang"),
    ("kentang dan telur", "perkedel kentang teflon simpel", "haluskan kentang rebus hangat dengan garam-merica, bentuk pipih, celup kocokan telur, lalu panggang di sedikit minyak"),
    ("udang kupas dan mentega", "udang tumis mentega bawang putih", "tumis bawang putih cincang di lelehan mentega, masukkan udang sampai berubah kemerahan sekitar tiga menit, lalu beri sedikit kecap Inggris"),
    ("tempe dan kecap pedas", "orek tempe basah manis pedas", "potong korek api tempe lalu goreng setengah kering, kemudian masak bersama tumisan bawang, lengkuas, cabai, dan kecap manis"),
    ("bihun kering dan telur", "bihun goreng rumahan simpel", "rendam bihun di air hangat sampai lentur lalu tiriskan, kemudian tumis bersama bawang putih, telur orak-arik, kol, dan kecap"),
]

MEAL_SITUATIONS = [
    ("buat sarapan buru-buru 10 menit", "Karena waktumu mepet di pagi hari, potongan bahannya bikin agak kecil aja supaya matang dalam hitungan menit."),
    ("buat makan siang hemat tanggal tua", "Menu ini ramah banget di dompet tapi tetap mengenyangkan sampai sore tanpa perlu jajan tambahan."),
    ("buat makan malam hangat pas hujan deras", "Disantap selagi mengepul waktu di luar hujan deras bakal bikin perut langsung terasa nyaman."),
    ("waktu lagi mager berat keluar kamar kos", "Cucian alat masaknya cuma satu wajan, jadi cocok banget pas lagi malas beres-beres panjang."),
    ("buat bekal simpel dibawa ke kampus atau kantor", "Masakan ini tetap enak dimakan di suhu ruang dan nggak gampang tumpah di kotak bekal."),
    ("waktu perut keroncongan jam sembilan malam", "Porsinya bisa kamu atur secukupnya aja supaya perut tenang tanpa bikin begah waktu dibawa tidur."),
    ("pas baru banget belajar masak sendiri", "Bumbunya sangat dasar dan toleran takaran, jadi pemula pun hampir pasti berhasil rasanya."),
    ("supaya minggu ini nggak pesan makanan online terus", "Masak sendiri menu cepat kayak gini lumayan banget memangkas ongkos kirim harian."),
    ("waktu lagi agak flu dan butuh makanan rumahan", "Tambahkan sedikit irisan jahe atau lada hangat supaya tenggorokan dan hidung terasa lebih lega."),
    ("buat makan berdua bareng teman kos", "Tinggal gandakan sedikit porsi bahannya, sudah cukup banget buat lauk patungan berdua."),
    ("pas kompor cuma punya satu tungku kecil", "Semua langkahnya dikerjakan berurutan di satu wajan yang sama, jadi praktis di dapur sempit."),
    ("waktu pengen lauk pendamping nasi putih hangat", "Perpaduan gurihnya pas banget ketemu nasi hangat, bahkan tanpa kerupuk tambahan pun sudah nikmat."),
]

COOK_Q_STYLES = [
    "nara, di dapur cuma ada {ing}, enaknya dimasak apa {sit}?",
    "punya bahan {ing} nih, kasih ide masakan gampang {sit} dong!",
    "gimana cara mengolah {ing} yang cepat {sit}?",
    "bingung mau masak apa dari {ing} {sit}, bantu ide dong nara",
    "ada {ing} di kos, bikinin ide menu simpel {sit} ya",
    "kalau cuma modal {ing}, bisa jadi lauk apa {sit}?",
]

COOK_A_STYLES = [
    "Modal {ing} itu pas banget dibikin **{dish}** {sit}! Caranya ringkas: {steps}. {ctx_tip}",
    "Cobain masak **{dish}** aja {sit}. Langkahnya gampang kok, cukup {steps}. {ctx_tip}",
    "Wah, {ing} mah penyelamat dapur banget! Olah aja jadi **{dish}**—tinggal {steps}. {ctx_tip}",
    "Ide paling sat-set dari {ing} {sit} jelas **{dish}**. Kamu cuma perlu {steps}. {ctx_tip}",
    "Kalau lagi cari menu anti-ribet {sit}, sulap {ing} jadi **{dish}**. Caranya: {steps}. {ctx_tip}",
    "Aku saranin bikin **{dish}** dari {ing} itu. Praktis banget: {steps}. {ctx_tip}",
]


# --------------------------------------------------------------------------- #
# 3. Urusan Praktis Rumah Tangga & Anak Kos (16 masalah x 10 konteks x 6 gaya)
# --------------------------------------------------------------------------- #
HOUSEHOLD_PROBLEMS = [
    ("nasi di penanak nasi terlanjur agak kelembekan", "cabut kabelnya sebentar lalu buka tutupnya 5-10 menit agar uap berlebih keluar, atau taruh selembar roti tawar bersih di atas permukaan nasi untuk menyerap uap air", "takaran air awal tadi kemungkinan kelebihan sekitar setengah ruas jari"),
    ("sayur berkuah nggak sengaja keasinan", "tuang sedikit air matang hangat lalu masukkan potongan kentang mentah atau tahu putih agar ikut menyerap rasa asin saat mendidih", "menambahkan banyak gula saja justru bikin kuahnya terasa aneh di lidah"),
    ("jemuran baju berbau apek gara-gara mendung", "larutkan dua sendok cuka makan ke air bilasan terakhir atau gantung baju berjarak longgar di depan hembusan kipas angin", "bau apek berasal dari bakteri yang berkembang di kain lembap terlalu lama"),
    ("sepatu kain basah kuyup habis kehujanan", "lepas sol dalamnya, padatkan gumpalan kertas koran kering ke dalam sepatu dan ganti tiap dua jam sambil diangin-anginkan", "jemur terik langsung bisa membuat lem sol cepat getas dan warna kain pudar"),
    ("kamar kos terasa pengap dan panas saat siang", "buka jendela dan beri sedikit celah udara, lalu hadapkan kipas angin ke arah luar jendela lima menit untuk membuang udara panas terperangkap", "aliran udara silang jauh lebih sejuk daripada memutar udara panas di ruang tertutup"),
    ("noda kopi baru menetes di kemeja warna terang", "serap segera dengan menepuk tisu kering tanpa menggosoknya, lalu bilas dari sisi balik kain memakai air dingin dan setetes sabun cuci piring", "air panas justru mengikat noda tanin kopi semakin kuat ke serat benang"),
    ("barisan semut kecil muncul terus di meja belajar", "bersihkan sisa remah makanan lalu usap permukaan meja memakai campuran air dan perasan jeruk nipis atau cuka dapur", "aroma asam menghapus jejak penciuman yang dipakai semut memanggil koloninya"),
    ("stok cabai rawit cepat busuk padahal di kulkas", "buang tangkai hijaunya tanpa mencuci cabai, lap sampai kering betul, lalu simpan di kotak kedap beralas tisu kering bersama satu siung bawang putih kupas", "tangkai basah adalah titik awal pembusukan yang menular ke cabai sebelahnya"),
    ("layar laptop dan lensa kacamata buram kena minyak jari", "tiup partikel debunya dulu, lalu lap memutar perlahan menggunakan kain mikrofiber bersih dengan setetes air matang", "tisu kasar atau cairan pembersih kaca rumah tangga bisa mengikis lapisan pelindungnya"),
    ("kabel pengisi daya sering melintir dan cepat mengelupas", "gulung melingkar longgar selebar telapak tangan tanpa menekuk pangkal kepala kabelnya, lalu ikat memakai pengikat velcro", "tarikan tajam di leher konektor adalah penyebab utama serabut tembaga putus di dalam"),
    ("kulkas mulai menyimpan bau campuran makanan", "singkirkan sisa makanan basi, seka rak memakai air hangat, lalu letakkan wadah terbuka berisi bubuk kopi kering atau soda kue", "bubuk kopi dan soda kue bekerja efektif mengikat molekul bau di udara dingin"),
    ("telur selalu lengket hancur waktu digoreng di wajan biasa", "panaskan wajan kosong sampai benar-benar hangat merata sebelum menuang minyak, lalu kecilkan api sedikit saat telur masuk", "menuang telur ke minyak yang belum panas membuat protein langsung mengikat pori logam"),
    ("stiker harga meninggalkan bekas lem lengket di botol atau piring baru", "oleskan sedikit minyak goreng atau minyak kayu putih di atas sisa lem selama lima menit, lalu gosok lembut memakai kain kering sebelum dicuci sabun", "minyak melarutkan perekat berbasis resin yang tahan terhadap air biasa"),
    ("handuk mandi terasa kaku dan kurang menyerap air", "cuci handuk dengan air hangat tanpa pelembut pakaian berlebih, dan tambahkan sedikit cuka putih saat pembilasan sebulan sekali", "lapisan silikon dari pelembut kain yang menumpuk justru menutup daya serap serat handuk"),
    ("pisau dapur mulai terasa agak tumpul waktu mengiris tomat", "gesekkan mata pisau miring sekitar 20 derajat searah pada bagian bawah alas cangkir keramik yang kasar beberapa kali lalu bilas bersih", "lingkar keramik tanpa glasir di bawah piring atau cangkir punya tekstur mirip batu asah halus"),
    ("kamar mandi kos muncul bau kurang enak dari lubang pembuangan", "siramkan air panas dicampur sedikit sabun dan soda kue ke saluran, lalu tutup lubang saringan dengan penutup karet saat tidak dipakai", "bau sering naik ketika perangkap air di pipa mengering saat jarang disiram"),
]

HH_CONTEXTS = [
    ("pas lagi buru-buru mau berangkat pagi", "Karena waktumu sempit sekarang, lakukan langkah penyelamatan tercepatnya dulu aja dalam dua menit."),
    ("waktu di kos cuma punya bahan seadanya", "Untungnya cara ini cuma mengandalkan barang yang hampir selalu ada di dapur atau meja kos."),
    ("padahal besok pagi barangnya harus langsung dipakai", "Kalau ditangani malam ini juga, besok pagi kondisinya sudah jauh lebih siap dipakai."),
    ("tanpa perlu beli cairan pembersih mahal ke toko", "Solusi rumahan sederhana ini jauh lebih hemat dan nggak kalah ampuh buat penanganan awal."),
    ("waktu kejadiannya malam-malam toko sudah tutup", "Nggak perlu bingung keluar malam, bahan darurat di dalam rumah sudah cukup buat mengatasinya."),
    ("supaya barangnya awet dan nggak cepat rusak", "Perawatan kecil yang tepat kayak gini lumayan banget memperpanjang umur pakai barang harianmu."),
    ("waktu baru pertama kali ngurus kamar sendiri", "Skill kecil anak rantau kayak gini memang paling terasa manfaatnya waktu ngurus semuanya mandiri."),
    ("pas akhir pekan lagi sekalian bersih-bersih", "Mumpung lagi sesi beres-beres akhir pekan, sekalian dituntaskan biar minggu depan terasa nyaman."),
    ("waktu cuaca lagi lembap banget belakangan ini", "Di musim lembap begini, menjaga sirkulasi udara setelahnya bakal mencegah masalahnya balik lagi."),
    ("biar nggak panik kalau kejadian lagi nanti", "Sekali kamu tahu trik dasarnya, lain kali kejadian serupa bakal beres dalam hitungan menit."),
]

HH_Q_STYLES = [
    "nara, gimana cara ngatasin {prob} {ctx}?",
    "tolong kasih tips praktis dong, {prob} {ctx}!",
    "aduh {prob} nih {ctx}, solusinya gimana ya?",
    "ada trik gampang buat beresin masalah {prob} {ctx}?",
    "eh nara, kalau {prob} {ctx}, harus diapain dulu?",
    "bantuin tips harian dong: {prob} {ctx}, enaknya gimana?",
]

HH_A_STYLES = [
    "Tenang, masalah itu gampang kok diakali! Coba {fix}. {ctx_note} Sekadar info, {note}.",
    "Langkah praktisnya begini: {fix}. {ctx_note} Oh iya, perlu diingat bahwa {note}.",
    "Jangan panik dulu! Kamu bisa langsung {fix}. {ctx_note} Catatan kecil buat ke depannya, {note}.",
    "Bisa diberesin pakai trik sederhana: {fix}. {ctx_note} Kenapa bisa begitu? Soalnya {note}.",
    "Cara paling aman untuk menanganinya adalah {fix}. {ctx_note} Hindari keliru langkah ya, karena {note}.",
    "Solusi cepat yang bisa langsung kamu coba: {fix}. {ctx_note} Ingat juga, {note}.",
]


# --------------------------------------------------------------------------- #
# 4. Fokus Belajar, Kebiasaan Produktif, & Energi Harian (16 topik x 12 konteks x 6 gaya)
# --------------------------------------------------------------------------- #
STUDY_TOPICS = [
    ("cepat ngantuk tiap baru baca materi 15 menit", "duduk tegak di kursi meja belajar sambil merangkum poin penting memakai kalimat sendiri tiap dua halaman", "membaca pasif sambil rebahan di kasur memberi sinyal kuat ke otak untuk beristirahat"),
    ("tangan refleks buka medsos terus waktu ngerjain tugas", "simpan HP di luar jangkauan tangan atau nyalakan mode pesawat selama sesi fokus 25 menit penuh", "menahan godaan notifikasi jauh lebih mudah lewat jarak fisik daripada sekadar niat"),
    ("sering menunda tugas besar sampai mepet batas waktu", "pecah tugasnya jadi target super kecil—misalnya buka dokumen dan tulis tiga poin kerangka dulu selama lima menit", "penundaan biasanya muncul karena otak terintimidasi melihat ukuran tugas yang belum dipecah"),
    ("hafalan cepat hilang lagi keesokan harinya", "tutup catatanmu lalu jelaskan ulang konsepnya dengan suara pelan seakan sedang mengajari teman yang belum tahu", "memanggil ulang ingatan secara aktif menguatkan jalur memori jauh lebih baik daripada membaca berulang"),
    ("bingung merangkum bacaan yang halamannya tebal", "baca subjudul dan kalimat utama tiap paragraf dulu, lalu sarikan maksimal lima poin inti per bab dengan kata-kata singkat", "menandai hampir seluruh baris pakai stabilo sama saja memindahkan kebingungan ke warna baru"),
    ("susah konsentrasi karena suara sekitar ramai", "gunakan penyumbat telinga atau putar suara latar konstan seperti rintik hujan tanpa vokal penyanyi", "musik berlirik bahasa yang kita mengerti ikut menyita kapasitas pemrosesan kata di otak"),
    ("pikiran buntu waktu mau menulis kalimat pembuka laporan", "lompati bagian pembuka dan tulis dulu bagian isi atau data yang paling kamu kuasai tanpa mengedit ejaan", "paragraf pengantar justru jauh lebih mudah mengalir setelah batang tubuh tulisannya jadi"),
    ("jadwal belajar harian selalu berantakan di tengah jalan", "batasi maksimal tiga target prioritas sehari dan sisakan jeda kosong buat mengantisipasi urusan mendadak", "jadwal yang terlalu padat menit per menit langsung tumbang begitu satu urusan saja bergeser"),
    ("belajar hitungan atau pemrograman pusing kalau cuma baca teori", "salin satu contoh paling pendek lalu ubah angkanya sendiri sambil menebak perubahan hasilnya", "pemahaman logika baru terkunci waktu tangan langsung bereksperimen dengan kasus kecil"),
    ("badan lemas dan otak berkabut sehabis makan siang", "ambil porsi makan siang secukupnya tanpa gula berlebih, minum air putih, dan jalan kaki ringan lima menit", "lonjakan gula serta porsi terlalu besar membuat tubuh mengantuk saat mencerna makanan"),
    ("catatan kelas berantakan sampai malas dibaca ulang", "bagi halaman buku jadi dua kolom: sisi lebar untuk catatan cepat di kelas, sisi sempit untuk kata kunci kesimpulan", "catatan yang punya ruang lega memudahkan mata menangkap inti materi dalam sekali lirik"),
    ("grogi dan takut salah waktu mau bertanya di kelas atau rapat", "tulis dulu satu kalimat inti pertanyaanmu di kertas beserta bagian mana yang sudah kamu coba pahami", "pertanyaan yang spesifik justru disukai pengajar maupun rekan karena membantu diskusi lebih jelas"),
    ("susah bangun pagi tepat waktu setelah keasyikan begadang", "majukan jam tidur secara bertahap 20 menit tiap malam dan letakkan alarm agak jauh supaya kaki harus menapak lantai", "menggeser jam biologis mendadak dua jam sekaligus sering gagal kalau malamnya masih menatap layar terang"),
    ("bingung membagi waktu antara kegiatan organisasi dan akademik", "tetapkan batas jam malam khusus tugas wajib yang tidak boleh diganggu rapat kecuali kondisi darurat", "berani berkata belum sanggup pada tambahan kepanitiaan adalah kunci menjaga nilai tetap aman"),
    ("cepat lupa daftar barang atau urusan kecil harian", "biasakan langsung mencatat ke satu daftar tunggal di saku atau HP detik itu juga begitu tugasnya terlintas", "otak manusia dirancang hebat untuk memikirkan ide, bukan menjadi gudang pengingat puluhan hal remeh"),
    ("mata cepat perih dan pegal karena menatap layar seharian", "terapkan jeda 20-20-20: tiap 20 menit alihkan pandangan ke objek sejauh 6 meter selama 20 detik sambil berkedip penuh", "saat fokus menatap monitor, frekuensi berkedip kita turun drastis sehingga permukaan mata cepat kering"),
]

STUDY_CONTEXTS = [
    ("menjelang minggu ujian yang padat", "Di masa ujian, menjaga stamina tidur sama pentingnya dengan menambah jam belajar."),
    ("waktu belajar mandiri malam hari di kamar", "Karena malam hari tenaga sudah berkurang, pilih sesi singkat tapi benar-benar fokus daripada lama tapi melamun."),
    ("pas ngerjain tugas dari rumah tanpa pengawas", "Saat kerja mandiri di rumah, aturan kecil yang kamu buat sendiri jadi pagar pengaman utamanya."),
    ("waktu baru mulai belajar topik baru dari nol", "Di minggu pertama kenal materi baru, wajar kalau jalannya terasa lambat—fokus ke paham dasar dulu."),
    ("pas akhir pekan pengen nyicil materi minggu depan", "Nyicil santai satu jam di akhir pekan bakal bikin hari Seninmu terasa jauh lebih ringan."),
    ("di jam rawan sore antara pukul tiga sampai lima", "Sore hari memang titik turunnya fokus alami tubuh, jadi selingi peregangan ringan sebelum mulai."),
    ("waktu target minggu ini lagi numpuk barengan", "Saat beban lagi tinggi, konsistensi 30 menit tiap hari jauh mengalahkan sistem kebut semalam."),
    ("pas lagi belajar bareng teman tapi malah kebanyakan ngobrol", "Sepakati timer hening 25 menit dulu bareng temanmu, baru bebas ngobrol seru pas waktu istirahatnya bunyi."),
    ("setelah libur panjang dan harus balik fokus lagi", "Habis liburan panjang, pemanasan dari tugas paling ringan bantu mesin fokusmu panas pelan-pelan."),
    ("waktu cuma punya waktu luang 30 menit di sela jadwal", "Waktu setengah jam yang fokus tanpa gangguan sering menghasilkan lebih banyak daripada dua jam sambil terdistraksi."),
    ("pas lagi kejar revisi laporan atau tugas akhir", "Untuk revisi bertahap, bereskan komentar yang paling mudah dulu supaya daftarnya cepat menyusut."),
    ("supaya kebiasaan baiknya tahan lama nggak cuma sehari", "Pasang target awal yang saking kecilnya kamu nggak punya alasan buat melewatkannya hari ini."),
]


def build_chat_daily(col: CategoryCollector, limit: int | None = None) -> None:
    pair_idx = 0
    # 1. Curhat & emosi sehari-hari (20 * 14 * 7 = 1.960)
    for sit, feel, action, reassure in EMOTION_SCENARIOS:
        for ctx, ctx_note in CURHAT_CONTEXTS:
            pair_idx += 1
            for k in range(len(CURHAT_Q_STYLES)):
                if limit and len(col.rows) >= limit:
                    return
                q = CURHAT_Q_STYLES[k].format(sit=sit, ctx=ctx, feel=feel)
                a = CURHAT_A_STYLES[(k + pair_idx) % len(CURHAT_A_STYLES)].format(
                    feel=feel, action=action, reassure=reassure, ctx_note=ctx_note
                )
                col.add(q, a)

    # 2. Ide masak & makan sehari-hari (22 * 12 * 6 = 1.584)
    for ing, dish, steps in INGREDIENTS_RECIPES:
        for sit, ctx_tip in MEAL_SITUATIONS:
            pair_idx += 1
            for k in range(len(COOK_Q_STYLES)):
                if limit and len(col.rows) >= limit:
                    return
                q = COOK_Q_STYLES[k].format(ing=ing, sit=sit)
                a = COOK_A_STYLES[(k + pair_idx) % len(COOK_A_STYLES)].format(
                    ing=ing, dish=dish, sit=sit, steps=steps, ctx_tip=ctx_tip
                )
                col.add(q, a)

    # 3. Masalah praktis rumah tangga & kos (16 * 10 * 6 = 960)
    for prob, fix, note in HOUSEHOLD_PROBLEMS:
        for ctx, ctx_note in HH_CONTEXTS:
            pair_idx += 1
            for k in range(len(HH_Q_STYLES)):
                if limit and len(col.rows) >= limit:
                    return
                q = HH_Q_STYLES[k].format(prob=prob, ctx=ctx)
                a = HH_A_STYLES[(k + pair_idx) % len(HH_A_STYLES)].format(
                    fix=fix, note=note, ctx_note=ctx_note
                )
                col.add(q, a)

    # 4. Fokus belajar & produktivitas (16 * 12 * 6 = 1.152)
    s_q_styles = [
        "nara, aku mengalami kendala {prob} {sub}, gimana cara ngakalinnya?",
        "kasih tips dong biar terhindar dari {prob} {sub}!",
        "kenapa ya aku sering terkendala {prob} {sub}? solusinya apa?",
        "bantu saran praktis nara: {prob} {sub}",
        "gimana trik efektif mengatasi {prob} {sub}?",
        "eh nara, kalau kejadian {prob} {sub}, enaknya mulai perbaiki dari mana?",
    ]
    s_a_styles = [
        "Masalah itu akrab banget dialami banyak orang {sub}. Trik paling manjur: {tip}. {sub_note} Soalnya, {why}.",
        "Coba ubah sedikit strategimu {sub}: {tip}. {sub_note} Alasannya sederhana, {why}.",
        "Daripada dipaksa terus tapi hasilnya mental, mending {tip}. {sub_note} Perlu diingat, {why}.",
        "Kalau boleh kasih saran santai {sub}, mulai dengan {tip}. {sub_note} Kenapa efektif? Karena {why}.",
        "Kuncinya ada di mengatur kebiasaan kecil: {tip}. {sub_note} Ingat juga bahwa {why}.",
        "Langkah sederhana yang langsung terasa bedanya {sub} adalah {tip}. {sub_note} Sebab, {why}.",
    ]
    for prob, tip, why in STUDY_TOPICS:
        for sub, sub_note in STUDY_CONTEXTS:
            pair_idx += 1
            for k in range(len(s_q_styles)):
                if limit and len(col.rows) >= limit:
                    return
                q = s_q_styles[k].format(prob=prob, sub=sub)
                a = s_a_styles[(k + pair_idx) % len(s_a_styles)].format(
                    tip=tip, why=why, sub=sub, sub_note=sub_note
                )
                col.add(q, a)
