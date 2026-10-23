"""Bagian 10 generator `chat.jsonl`:
- Obrolan santai kuliner daerah, tradisi makan, & suasana keseharian Nusantara
- Diskusi reflektif ringan sehari-hari ("kenapa ya...", "menurutmu gimana...")
- Dinamika kerja kelompok, kepanitiaan, & kolaborasi harian pelajar/pekerja muda
"""
from __future__ import annotations

from .core_v2 import CategoryCollector

# 1. Kuliner Daerah & Suasana Keseharian Nusantara (24 x 16 x 7 = 2.688)
NUSANTARA_CHATS = [
    ("semangkuk soto hangat di pagi hari", "kuah kaldu rempah bening atau santannya yang hangat langsung menyegarkan badan sebelum mulai beraktivitas, apalagi ditambah perasan jeruk nipis dan sambal sedikit", "hampir tiap daerah di Indonesia punya racikan soto khasnya masing-masing, dari Soto Lamongan berbubuk koya sampai Soto Banjar yang harum kayu manis"),
    ("gudeg Yogyakarta yang dimasak berjam-jam", "nangka muda yang dimasak perlahan bersama santan dan gula merah menghasilkan perpaduan manis-gurih lembut, makin mantap disandingkan krecek pedas", "kesabaran memasak dengan api kecil berjam-jam itulah yang membuat bumbunya meresap sampai ke serat terdalam"),
    ("rendang rempah khas Minangkabau", "santan dan puluhan bumbu rempahnya dimasak sabar sampai mengering pekat kecokelatan sehingga gurihnya tahan lama meski disimpan berhari-hari", "dulu teknik memasak kering ini juga jadi bekal cerdas para perantau dalam perjalanan jauh"),
    ("pempek Palembang dengan kuah cuko segar", "tekstur kenyal gurih olahan ikan dan sagu berpadu kontras dengan kuah cuko asam-manis-pedas dari gula aren serta asam jawa", "irisan timun segar kecil di atasnya bikin rasa di mulut tetap ringan seimbang"),
    ("rawon kuah hitam khas Jawa Timur", "warna gelap gurihnya yang khas berasal dari biji kluwek pilihan yang diolah matang, disajikan hangat dengan kecambah pendek renyah dan telur asin", "kecambah mentah pendek memberi sensasi kres segar di tengah kuah kaldu yang pekat"),
    ("papeda hangat dengan ikan kuah kuning khas timur Indonesia", "olahan sagu yang lembut bening diseruput bersama kuah ikan kunyit-jeruk nipis yang asam segar tanpa rasa amis sama sekali", "sagu menjadi sumber energi kearifan lokal kepulauan Maluku dan Papua sejak turun-temurun"),
    ("coto Makassar dengan bumbu kacang rempah", "kuah kental gurih dari kacang tanah sangrai halus dan puluhan rempah paling pas disantap bersama potongan ketupat daun pandan", "aroma serai, lengkuas, dan ketumbar sangrainya langsung menggugah selera sejak disajikan hangat"),
    ("nasi kuning tumpeng atau kotak di acara syukuran", "warna kuning harum kunyit dan santan selalu identik dengan rasa syukur hangat, ditemani kering tempe, perkedel, dan irisan telur dadar tipis", "makan nasi kuning bareng keluarga atau tetangga selalu menghadirkan suasana guyub yang akrab"),
    ("bubur kacang hijau ketan hitam di sore hari", "perpaduan lembut kacang hijau, legitnya ketan hitam, dan siraman santan gurih beraroma daun pandan pas banget mengganjal perut sore", "selain mengenyangkan nyaman, kacang hijau kaya serat dan protein nabati yang baik buat tubuh"),
    ("es cendol atau dawet gula aren di siang terik", "tetesan kenyal tepung beras pandan dengan lelehan gula aren kental dan santan dingin langsung mengusir gerah matahari siang", "wangi khas gula aren asli memberi rasa manis karamel alami yang nggak bikin enek"),
    ("tradisi makan bersama di atas hamparan daun pisang", "aroma alami daun pisang yang terkena nasi hangat menambah selera makan, sekaligus mencairkan batas kaku karena semua duduk sejajar", "kebersamaan sederhana seperti ini sering melahirkan tawa paling lepas dibanding jamuan formal"),
    ("jajanan pasar pagi di atas tampah bambu", "klepon, kue lapis, lemper, dan cenil warna-warni menawarkan porsi kecil manis-gurih tradisional yang dibuat segar sejak subuh", "membeli jajanan pasar pagi sekaligus ikut menghidupi perajin kue rumahan di lingkungan kita"),
    ("teh melati hangat di teko tanah liat", "aroma bunga melati dan sepet lembut daun teh lokal yang diseduh panas memberikan jeda tenang di sela obrolan santai", "di banyak daerah Jawa, seduhan teh wangi kental bersama gula batu punya cita rasa nostalgia tersendiri"),
    ("wedang ronde jahe hangat di malam dingin", "kuah jahe bakar yang pedas hangat memeluk tenggorokan, sementara bola ketan berisi kacang tumbuk memberi kejutan gurih manis", "minuman rempah tradisional seperti ini ampuh menghangatkan badan sehabis kehujanan"),
    ("sate ayam bumbu kacang yang dibakar arang", "asap panggangan arang batok kelapa memberi aroma wangi khas pada kecap dan bumbu kacang halus yang nggak tergantikan kompor biasa", "tambahan irisan bawang merah dan perasan jeruk limau bikin bumbunya terasa makin hidup"),
    ("gado-gado sayur rebus siram bumbu kacang ulek", "aneka sayur rebus segar, tahu-tempe, dan lontong disatukan saus kacang ulek dadakan plus kerupuk renyah yang mengenyangkan", "ini salah satu cara paling lezat menikmati porsi besar sayuran khas Nusantara"),
    ("bakwan sayur hangat waktu hujan turun di luar", "pinggiran adonan kol-wortel yang renyah gurih saat baru diangkat dari wajan memang pasangan klasik melihat rintik hujan dari teras", "bikin sendiri di dapur dengan irisan daun bawang banyak juga gampang dan jauh lebih bersih minyaknya"),
    ("nasi uduk gurih pagi hari sebelum berangkat", "nasi yang ditanak bersama santan, daun salam, dan serai punya wangi gurih lembut meski hanya ditemani bihun, tempe orek, dan sambal kacang", "sarapan hangat berbungkus daun pisang di pagi buta sudah jadi pemandangan akrab kota-kota kita"),
    ("sayur asem segar di siang hari yang panas", "rasa asam segar dari asam muda, jagung manis, labu siam, dan melinjo bikin makan siang terasa ringan menyegarkan", "dipasangkan ikan asin kecil atau tempe goreng hangat serta sambal terasi sudah nikmat luar biasa"),
    ("kebiasaan saling mengantar sepiring masakan ke tetangga sebelah", "piring yang berpindah antar-rumah membawa pesan ramah 'kami ingat kalian' yang mempererat kerukunan bertetangga tanpa banyak kata", "tradisi mengembalikan piring dalam keadaan terisi kembali adalah wujud manis gotong royong kecil harian"),
    ("kopi tubruk hitam hangat di teras pagi", "ampas kopi bubuk yang mengendap perlahan menyisakan aroma panggang kuat buat menemani lima belas menit tenang sebelum hari sibuk dimulai", "biji kopi Nusantara dari Gayo, Toraja, sampai Flores punya karakter rasa unik yang diakui dunia"),
    ("ketupat sayur santan di momen kumpul keluarga", "anyaman janur kelapa memberi kepadatan tekstur khas pada beras yang meresap kuah opor atau lodeh labu dengan sempurna", "proses menganyam dan memasaknya bersama anggota keluarga sering jadi kenangan hangat tersendiri"),
    ("jagung bakar oles mentega pedas manis malam hari", "bulir jagung manis yang terkaramelisasi di atas bara api selalu sukses mengumpulkan teman atau keluarga mengobrol melingkar", "sederhana bahannya, tapi suasana menunggu jagung matang bareng itulah yang paling berkesan"),
    ("rujak buah potong sambal gula merah ulek siang hari", "mangga mengkal, nanas, bengkuang, dan jambu air segar dicocol bumbu kacang gula jawa pedas langsung mengusir kantuk siang", "perpaduan manis, asam, segar, dan pedas dalam satu piring memang ciri khas kegembiraan kuliner kita"),
]

NUSANTARA_CTX = [
    ("kalau lagi kangen suasana rumah dan kampung halaman", "Makanan dan kebiasaan akrab memang punya kekuatan ajaib menghadirkan rasa pulang walau kita sedang jauh merantau."),
    ("pas ngobrol santai sore-sore kayak gini", "Ngobrolin kekayaan rasa harian Nusantara gini emang selalu bikin suasana hati ikut hangat ya!"),
    ("buat dikenalkan ke teman dari daerah lain", "Mengajak teman mencicipi hidangan khas daerah sambil menceritakan kisah di baliknya selalu jadi jembatan pertemanan yang seru."),
    ("waktu cuaca di luar lagi mendukung banget", "Pas banget momennya—suasana cuaca yang cocok bikin kenikmatan sederhananya naik berkali lipat."),
    ("sebagai bukti betapa kayanya budaya keseharian kita", "Betul banget, dari sepiring hidangan harian aja kita bisa melihat jejak alam dan kearifan masyarakat lokalnya."),
    ("kalau dinikmati pelan-pelan bareng orang terdekat", "Rasa masakan enak bakal terasa dua kali lebih berkesan waktu dibagi sambil mengobrol hangat tanpa buru-buru."),
    ("meskipun kelihatannya sederhana dan merakyat", "Justru hal-hal merakyat yang jujur rasanya itulah yang paling dirindukan siapa pun ke mana pun pergi."),
    ("waktu akhir pekan pengen menikmati hari dengan santai", "Menghadiahi diri sendiri dengan santapan atau tradisi hangat begini di akhir pekan itu kebahagiaan murah meriah yang nyata."),
    ("yang sering bikin orang senyum sendiri waktu mengingatnya", "Kenangan rasa dan aroma memang tersimpan awet banget di ingatan masa kecil sampai dewasa kita."),
    ("kalau kita perhatikan keunikan racikan bumbunya", "Kekayaan rempah tropis kita bikin bahan sederhana pun bisa punya lapisan rasa yang dalam banget."),
    ("waktu pengen mencari penghibur hati sehabis pekan sibuk", "Kadang obat lelah paling manjur memang sesederhana menikmati sajian akrab yang menenangkan perut dan hati."),
    ("yang selalu punya tempat spesial di keseharian masyarakat kita", "Kebiasaan kuliner ini terus hidup dari generasi ke generasi karena memang dekat dengan keseharian kita."),
    ("kalau mau coba bikin atau hadirkan sendiri suasananya di rumah", "Menghadirkan versinya di dapur rumah sendiri juga seru banget buat mengisi waktu luang."),
    ("dibandingkan makanan cepat saji modern yang seragam", "Cita rasa tradisional punya kehangatan dan keunikan karakter yang nggak pernah membosankan."),
    ("waktu lagi ngumpul lintas generasi bareng orang tua dan adik", "Topik dan hidangan akrab Nusantara selalu berhasil menyatukan selera kakek-nenek sampai anak muda."),
    ("yang bikin kita makin bersyukur tinggal di negeri kaya rasa", "Keragaman dari barat sampai timur Indonesia memang nggak ada habisnya buat dikagumi dan disyukuri."),
]


# 2. Diskusi Reflektif Ringan Sehari-hari (24 x 16 x 7 = 2.688)
REFLECT_TOPICS = [
    ("kenapa waktu terasa cepat banget pas lagi senang tapi lambat pas menunggu", "saat senang perhatian kita tenggelam penuh menikmati kegiatan sehingga otak tidak memantau detak menit, sedangkan saat bosan menunggu fokus kita justru tertuju terus pada jarum jam", "mengisi waktu tunggu dengan membaca atau mengamati sekitar membuat menit-menit terasa jauh lebih bersahabat"),
    ("bedanya sekadar menghafal materi sama benar-benar paham konsepnya", "hafalan hanya menyimpan urutan kalimat yang mudah menguap besok lusa, sedangkan pemahaman membuatmu sanggup menjelaskan ulang idenya dengan bahasa sederhana ke adik kecil sekalipun", "coba uji pemahamanmu dengan bertanya 'kenapa bisa begitu?' dan merangkumnya tanpa melihat buku"),
    ("kenapa menulis catatan pakai tangan sering bikin kita lebih mudah ingat", "gerakan motorik tangan saat menggores huruf memaksa otak menyaring dan mengolah inti kalimat secara aktif, bukan sekadar mengetik ulang kata demi kata secara otomatis", "mencatat poin kunci dengan panah sederhana di kertas kecil sangat efektif menguatkan daya ingat"),
    ("lebih enak mulai berkarya pagi-pagi hening atau malam hari yang tenang", "pagi buta unggul pada kesegaran energi sebelum gangguan pesan masuk, sementara malam tenang cocok buat perenungan kreatif asal tidak mengorbankan jam tidur utamamu", "kuncinya adalah mengenali jam biologis paling jernihmu sendiri lalu melindunginya secara konsisten"),
    ("kenapa wangi tanah basah waktu hujan pertama turun terasa menenangkan", "aroma alami yang disebut petrikor dari minyak tumbuhan dan senyawa tanah kering yang tersentuh air hujan memicu asosiasi sejuk serta rasa teduh di ingatan kita", "duduk sebentar menghirup udara sejuk sehabis hujan sering jadi jeda relaksasi alami yang menyegarkan"),
    ("gimana cara menyadari bahwa diri kita sudah bertumbuh dibanding setahun lalu", "lihat dari bagaimana kamu merespons masalah yang dulu sempat membuatmu panik luar biasa—kalau sekarang kamu lebih tenang mencari jalan keluar, itu bukti kedewasaan nyata", "pertumbuhan batin memang sering terjadi hening tanpa gembar-gembor, baru terasa saat kita menoleh ke belakang"),
    ("kenapa membereskan meja dan kamar sering bikin pikiran ikut terasa lega", "keruwetan benda visual di sekitar tanpa sadar menambah beban perhatian mata kita, sehingga ruang yang lapang teratur memberi sinyal aman dan kendali pada pikiran", "lima menit merapikan permukaan meja sudah cukup menjadi pemanasan fokus yang jitu"),
    ("pentingnya punya satu hobi yang murni buat senang-senang tanpa target uang", "memiliki ruang bermain tempat kamu boleh mencoba-coba tanpa dinilai untung-ruginya menjaga jiwa tetap segar dari tekanan harus selalu tampil sempurna", "entah menggambar, merawat tanaman, atau memetik gitar santai, hobi murni merawat kegembiraan batinmu"),
    ("kenapa sapaan ramah singkat dari orang sekitar bisa memperbaiki suasana hati", "senyum dan ucapan 'terima kasih' tulus mengingatkan bahwa kita hidup saling terhubung sebagai sesama manusia yang saling menghargai keberadaan satu sama lain", "kebaikan kecil berdurasi tiga detik sering kali menjadi titik terang di hari seseorang yang sedang berat"),
    ("bedanya menikmati waktu menyendiri dengan rasa kesepian", "menyendiri yang sehat adalah pilihan sadar untuk mengisi ulang energi dengan tenang, sedangkan kesepian muncul saat kita merindukan koneksi hangat namun merasa terasing", "keduanya sama-sama manusiawi: nikmati waktu tenangmu, dan sapa sahabat saat hatimu butuh berbagi"),
    ("kenapa tidur siang singkat bikin segar tapi kalau kelamaan malah pusing", "istirahat 15–20 menit menjaga tubuh tetap di tidur ringan yang memulihkan fokus, sedangkan lewat satu jam tubuh telanjur masuk tidur dalam sehingga terasa berat saat terbangun", "memasang alarm dua puluh menit di siang hari adalah trik terbaik mendapatkan kesegaran cepat"),
    ("gimana pertemanan dewasa bisa tetap hangat walau jarang ketemu tiap minggu", "kedekatan yang matang tidak diukur dari seberapa sering mengobrol tiap jam, melainkan dari rasa aman bahwa saat bertemu lagi obrolan langsung nyambung tanpa penghakiman", "mengirim kabar tulus sesekali saat teringat sudah cukup menjaga api silaturahmi tetap hidup"),
    ("kenapa mendengar lagu lama bisa seketika memutar ingatan masa lalu", "irama musik diproses otak sangat dekat dengan pusat emosi dan memori jangka panjang, sehingga satu melodi sanggup membangkitkan kembali suasana tempat serta perasaan masa itu", "membuat daftar putar lagu kenangan positif bisa jadi teman perjalanan yang menghangatkan hati"),
    ("pentingnya belajar merasa 'cukup' di tengah arus informasi yang serba cepat", "tanpa batas rasa cukup kita mudah kelelahan mengejar standar orang lain yang tidak pernah habis, padahal ketenangan lahir saat kita menghargai apa yang sedang kita jalani hari ini", "rasa cukup bukan berarti berhenti maju, melainkan melangkah tanpa diperbudak rasa kurang terus-menerus"),
    ("kenapa jalan kaki santai tanpa melihat layar sering memunculkan ide segar", "saat kaki melangkah ritmis dan pikiran dibiarkan mengembara bebas tanpa jejalan konten baru, otak justru merangkai hubungan kreatif antar-gagasan yang sebelumnya buntu", "banyak penulis dan ilmuwan mengandalkan jalan kaki lima belas menit setiap kali menemui jalan buntu"),
    ("bedanya kelihatan sibuk seharian sama benar-benar produktif bermakna", "sibuk sering habis untuk merespons puluhan hal kecil mendesak tanpa arah, sedangkan produktif berarti menuntaskan satu-dua hal terpenting yang benar-benar memajukan tujuanmu", "tanyakan tiap pagi: 'satu hal apa yang kalau selesai hari ini bikin hatiku tenang?'"),
    ("kenapa memasak makanan sendiri bikin kita lebih menghargai isi piring", "saat mengupas, memotong, dan menjaga api sendiri, kita menyaksikan langsung usaha di balik sepiring hidangan sehingga makan lebih sadar dan enggan menyisakan makanan", "kemandirian dapur sederhana sekaligus menyehatkan badan dan menenangkan dompet"),
    ("gimana cara menerima pujian orang lain dengan tulus tanpa salah tingkah", "cukup tersenyum hangat dan ucapkan 'terima kasih banyak ya, senang mendengarnya' tanpa buru-buru merendahkan hasil kerjamu sendiri karena rasa sungkan", "menerima apresiasi dengan anggun justru menghormati ketulusan orang yang sedang memujimu"),
    ("kenapa mencoba menjelaskan materi ke teman justru bikin kita makin paham", "saat menyusun kalimat agar mudah dimengerti orang lain, kita langsung menemukan celah bagian mana yang ternyata belum benar-benar kita kuasai lalu melengkapinya", "belajar sambil berbagi ilmu tidak pernah mengurangi milikmu, malah menggandakan ketajamannya"),
    ("manfaat memberi jeda hening sepuluh menit sehari tanpa layar dan suara", "keheningan sejenak menurunkan ketegangan saraf yang seharian dibombardir notifikasi, memberi ruang bagi pikiran untuk mengendapkan pengalaman hari itu dengan jernih", "duduk tenang menatap pepohonan atau langit sore sepuluh menit sudah terasa sangat memulihkan"),
    ("kenapa membaca buku cerita atau fiksi baik untuk melatih kepekaan empati", "masuk ke sudut pandang tokoh dengan latar hidup berbeda melatih batin kita memahami alasan di balik perasaan dan pilihan manusia yang beragam di dunia nyata", "cerita yang baik memperluas wawasan kemanusiaan kita tanpa terasa menggurui"),
    ("bedanya hidup hemat yang bijak dengan sikap pelit ke diri sendiri", "hemat bijak memangkas pengeluaran gengsi yang tidak perlu demi masa depan tenang, tapi tetap rela memenuhi gizi sehat, keamanan, dan kebutuhan belajar yang esensial", "jangan sampai demi menabung ekstrem kamu malah mengorbankan kesehatan tubuhmu sendiri"),
    ("kenapa merayakan keberhasilan kecil sehari-hari itu penting buat semangat", "mengakui langkah kecil yang tuntas memberi sinyal positif pada diri sendiri bahwa usahamu berarti, sehingga tenaga mentalmu terjaga sepanjang perjalanan panjang", "apresiasi sederhana seperti menyeduh minuman favorit sehabis menyelesaikan tugas berat itu sah banget"),
    ("gimana menjaga hati tetap membumi saat dipuji dan tetap tegak saat dikritik", "ingat bahwa pujian adalah apresiasi atas proses saat ini untuk disyukuri, sementara kritik yang sehat adalah masukan untuk karya atau cara kerjamu—bukan serangan atas nilai dirimu", "pegangan ini membuat langkahmu stabil, tidak mudah melambung tinggi maupun tumbang mendadak"),
]

REFLECT_CTX = [
    ("pas aku lagi merenung santai malam ini", "Momen tenang malam hari gini emang waktu paling enak buat melihat keseharian dari sudut pandang yang lebih jernih."),
    ("soalnya akhir-akhir ini aku sering kepikiran hal itu", "Wajar banget kok kepikiran soal itu—tandanya kamu peka mengamati apa yang sedang kamu jalani."),
    ("kalau dilihat dari pengalaman hidup sehari-hari", "Di keseharian nyata, hal-hal sederhana seperti ini memang terasa langsung dampaknya ke ketenangan batin."),
    ("biar aku bisa menyikapinya dengan lebih dewasa", "Cara pandang yang seimbang bikin langkah harianmu jauh lebih ringan dan nggak gampang terombang-ambing."),
    ("waktu ngobrol santai tukar pikiran bareng kamu", "Senang banget bisa tukar pikiran topik reflektif ringan kayak gini bareng kamu!"),
    ("menurut sudut pandangmu yang praktis dan membumi", "Kalau ditarik ke langkah praktisnya, intinya selalu kembali ke kebiasaan sadar yang kita rawat pelan-pelan."),
    ("supaya hidup sehari-hari terasa lebih bermakna", "Makna keseharian memang sering bersembunyi di perhatian penuh kita terhadap hal-hal kecil di depan mata."),
    ("tanpa harus pakai teori yang terlalu rumit", "Setuju, penjelasan yang membumi justru paling mudah langsung kita rasakan dan terapkan hari ini juga."),
    ("pas lagi istirahat sejenak di sela kesibukan", "Jeda sebentar buat merenungkan hal positif gini bikin kepala segar lagi sebelum lanjut beraktivitas."),
    ("yang sering dialami banyak anak muda sekarang", "Banyak banget teman seusia yang merasakan hal serupa, jadi kamu sama sekali nggak sendirian memikirkannya."),
    ("biar pikiran nggak gampang jenuh sama rutinitas", "Melihat rutinitas dengan kacamata ingin tahu bikin hari-hari biasa terasa jauh lebih berwarna."),
    ("kalau mau dipraktikkan pelan-pelan mulai minggu ini", "Cukup pilih satu kebiasaan kecil yang paling sreg di hatimu lalu rasakan bedanya seminggu ke depan."),
    ("waktu ngopi atau ngeteh sore sendirian", "Teman renungan sore yang pas banget nih, hangat dan menenangkan pikiran."),
    ("sebagai pengingat lembut buat diri sendiri", "Menyimpan pengingat lembut kayak gini menjaga kita tetap ramah pada diri sendiri di hari yang padat."),
    ("yang kadang luput kita sadari karena buru-buru", "Begitu kita melambatkan langkah sebentar, hal berharga ini langsung kelihatan jelas."),
    ("kalau dibahas santai pakai bahasa obrolan biasa", "Dibahas santai begini justru bikin intisarinya langsung nempel di ingatan tanpa beban."),
]


# 3. Kolaborasi, Kerja Kelompok, & Kepanitiaan Harian (18 x 16 x 7 = 2.016)
COLLAB_TOPICS = [
    ("membagi tugas kerja kelompok supaya adil dan nggak ada yang numpang nama", "pecah proyek menjadi bagian konkret terukur (pencarian bahan, penyusunan isi, salindia, penyuntingan akhir) lengkap dengan nama penanggung jawab dan tenggat per bagian tertulis di grup", "kejelasan porsi kerja di awal mencegah kesalahpahaman dan rasa sungkan saling menunggu"),
    ("memimpin rapat kelompok atau panitia biar ringkas nggak molor berjam-jam", "bagikan tiga poin bahasan utama sebelum rapat dimulai, tetapkan batas waktu tiap poin, dan tutup dengan rangkuman keputusan siapa mengerjakan apa", "rapat tiga puluh menit yang fokus jauh lebih disukai anggota daripada kumpul dua jam tanpa kesimpulan"),
    ("mengingatkan teman sekelompok yang belum mengumpulkan bagiannya dengan sopan", "sapa baik-baik menanyakan progresnya lebih dulu: 'Hai, bagian bab dua gimana kabarnya? Ada kendala yang perlu kita diskusikan bareng sebelum digabung malam ini?'", "nada kolaboratif yang menawarkan diskusi membuat teman terdorong menyelesaikan tugas tanpa merasa dipojokkan"),
    ("menyatukan dua usulan ide teman tim yang sama-sama bagus", "cari benang merah tujuan utamanya lalu gabungkan keunggulan praktis ide pertama dengan sentuhan kreatif ide kedua melalui kesepakatan bersama", "mengakui nilai positif kedua gagasan membuat seluruh pengusul merasa dihargai dan kompak menjalankannya"),
    ("mencatat notula rapat yang rapi dan langsung jelas tindak lanjutnya", "pisahkan catatan menjadi tiga kolom ringkas: pokok bahasan singkat, keputusan yang disepakati, serta nama penanggung jawab beserta batas tanggalnya", "kirimkan rangkumannya ke grup maksimal satu jam setelah rapat selesai selagi ingatan semua orang masih segar"),
    ("menghadapi perbedaan gaya kerja teman yang serba cepat vs yang sangat teliti", "tempatkan rekan yang gesit di tahap pembuka draf awal dan rekan yang teliti di tahap pemeriksaan kualitas akhir sehingga keduanya saling melengkapi", "perbedaan karakter kerja justru menjadi kekuatan tim kalau ditempatkan di urutan proses yang tepat"),
    ("meminta perpanjangan waktu pengumpulan tugas secara jujur dan bertanggung jawab", "sampaikan permohonan sebelum batas waktu habis (bukan sesudah lewat), tunjukkan progres yang sudah dikerjakan sejauh ini, dan sebutkan jam pasti penyelesaian barunya", "menunjukkan bukti progres nyata membuktikan bahwa kamu serius bekerja, bukan sekadar menunda-nunda"),
    ("menyiapkan salindia presentasi kelompok biar ringkas dan enak dilihat", "batasi satu salindia hanya memuat satu gagasan utama dalam tiga-lima poin pendek berhuruf jelas, sementara penjelasan lengkapnya disampaikan secara lisan", "salindia yang lapang membuat audiens menyimak pembicaranya, bukan sibuk membaca tembok teks rapat"),
    ("menjawab pertanyaan sulit waktu sesi tanya jawab presentasi kelas", "apresiasi pertanyaannya dulu, jawab bagian yang datanya kamu kuasai dengan jernih, dan akui jujur aspek yang perlu dicek lebih lanjut tanpa mengarang jawaban", "kejujuran akademis yang tenang justru meninggalkan kesan matang dan dapat dipercaya"),
    ("merangkul anggota kelompok yang pendiam supaya nyaman ikut berpendapat", "beri kesempatan khusus di putaran diskusi dengan sapaan ramah seperti 'Menurutmu gimana bagian ini? Kita pengen dengar sudut pandangmu juga'", "banyak anggota pendiam sebenarnya menyimpan pengamatan tajam, hanya butuh ruang sapaan yang tidak mengintimidasi"),
    ("membereskan salah paham pembagian kerja yang sempat memanas di chat grup", "ajak bicara singkat lewat panggilan suara atau temu langsung lima menit karena nada tulisan di layar sering terdengar lebih dingin dari maksud aslinya", "mendengar intonasi suara ramah secara langsung meluruskan sembilan puluh persen salah tafsir teks"),
    ("merapikan dokumen gabungan dari banyak anggota biar gayanya seragam", "sepakati satu jenis huruf, ukuran judul, dan gaya penulisan istilah sejak awal, lalu tunjuk satu penyunting akhir untuk menghaluskan sambungan antar-bagian", "dokumen yang rapi seragam terlihat seperti satu kesatuan utuh yang dikerjakan tim solid"),
    ("menjaga semangat teman satu tim waktu draf harus direvisi lagi", "ingatkan bahwa revisi adalah bagian wajar menyempurnakan karya, bagi rata poin perbaikannya ke anggota, dan selesaikan satu per satu tanpa saling menyalahkan", "suasana tim yang saling menguatkan membuat pekerjaan revisi terasa separuh lebih ringan"),
    ("menyampaikan apresiasi tulus ke rekan tim sehabis acara atau tugas beres", "sebutkan kontribusi spesifik tiap teman di grup bersama supaya setiap orang tahu kerja keras mereka di balik layar benar-benar diperhatikan", "ucapan terima kasih yang tulus membuat rekan senang bekerja sama lagi denganmu di kesempatan berikutnya"),
    ("menyerahkan catatan kepanitiaan ke pengurus berikutnya dengan rapi", "kumpulkan daftar kontak vendor, rincian anggaran nyata, serta catatan hal yang berhasil maupun perlu diperbaiki dalam satu folder tertata jelas", "warisan dokumentasi yang rapi menyelamatkan kepanitiaan adik tingkat dari mengulang kesalahan dari nol"),
    ("menolak halus tambahan tugas baru waktu beban kerja tim sedang penuh", "jelaskan kapasitas pengerjaan saat ini secara transparan dan tawarkan opsi realistis: menyelesaikan prioritas pertama dulu atau menggeser jadwal tugas tambahan tersebut", "komunikasi kapasitas yang jujur menjaga mutu hasil kerja tim tetap terjaga baik"),
    ("melakukan evaluasi seusai kegiatan tanpa menjatuhkan mental pribadi teman", "fokuskan pembahasan pada sistem kerja dan kejadian ('alur pendaftaran kemarin antre panjang, ke depan kita tambah meja') alih-alih menunjuk kesalahan personal", "evaluasi yang fokus pada perbaikan sistem membuat semua anggota terbuka belajar tanpa sikap defensif"),
    ("menjaga keseimbangan sehat antara aktif berorganisasi dan kewajiban kuliah/sekolah", "jadwalkan jam belajar dan tenggat akademik sebagai prioritas tetap di kalender lebih dulu sebelum menyanggupi rapat atau tambahan kepanitiaan luar", "organisasi yang baik mengasah kepemimpinanmu tanpa mengorbankan tanggung jawab pendidikan utamamu"),
]

COLLAB_CTX = [
    ("di tugas kelompok semester ini", "Praktik komunikasi rapi di kelompok kuliah begini jadi latihan berharga banget buat dunia kerja nanti."),
    ("waktu anggota timnya baru pertama kali kerja bareng", "Di tim yang baru kenal, kesepakatan aturan main yang jelas di awal langsung membangun rasa saling percaya."),
    ("supaya hasilnya maksimal tapi hubungan pertemanan tetap enak", "Keseimbangan antara target beres dan komunikasi santun memang kunci kolaborasi yang dewasa."),
    ("pas waktu pengerjaannya lumayan mepet minggu ini", "Saat tenggat dekat, pembagian peran yang tegas tanpa banyak debat menghemat banyak sekali energi."),
    ("biar aku bisa belajar jadi rekan tim yang menyenangkan", "Orang yang komunikatif, tepat janji, dan menghargai teman selalu jadi rekan favorit di tim mana pun."),
    ("waktu dikerjakan sebagian secara daring lewat grup chat", "Di koordinasi daring, pesan yang ringkas bernomor poin mencegah informasi penting tenggelam di obrolan."),
    ("tanpa bikin suasana kelompok jadi tegang kaku", "Bahas dengan nada santai tapi tetap jelas poinnya—tegas soal jadwal bukan berarti galak ke teman kok."),
    ("di kepanitiaan acara sekolah atau kampus", "Pengalaman mengurus acara bareng teman-teman selalu meninggalkan pelajaran kerja sama yang awet dikenang."),
    ("kalau posisiku cuma anggota biasa bukan ketua", "Anggota yang proaktif merapikan alur dengan sopan sangat membantu meringankan beban koordinator tim."),
    ("pas aku kebetulan ditunjuk jadi koordinatornya", "Pemimpin tim yang baik nggak harus mengerjakan semuanya sendiri, melainkan memudahkan anggota mengeluarkan potensi terbaiknya."),
    ("supaya nggak menumpuk dikerjakan semalam sebelum kumpul", "Mencicil tenggat kecil di tengah jalan menyelamatkan seluruh tim dari begadang panik di malam terakhir."),
    ("menghadapi teman-teman yang jadwal hariannya beda-beda", "Menyepakati jam kerja mandiri dengan papan progres bersama efektif banget menyiasati jadwal yang sulit ketemu."),
    ("biar semua anggota merasa dilibatkan secara setara", "Rasa memiliki muncul waktu setiap orang punya ruang kontribusi yang jelas dan dihargai."),
    ("waktu proyeknya lumayan besar dan butuh beberapa minggu", "Untuk proyek panjang, cek progres singkat sepuluh menit tiap pekan menjaga arah tim tetap di relnya."),
    ("dengan komunikasi yang lugas, ramah, dan solutif", "Gaya bicara yang langsung menawarkan solusi selalu disambut positif oleh rekan kerja mana pun."),
    ("supaya selesai tepat waktu dengan hati sama-sama lega", "Menuntaskan tanggung jawab bersama tepat waktu rasanya selalu memuaskan dan melegakan semua pihak."),
]


def build_chat_nusantara_reflect(col: CategoryCollector, limit: int | None = None) -> None:
    pair_idx = 0

    # 1. Kuliner & suasana Nusantara (24 * 16 * 7 = 2.688)
    nu_q = [
        "nara, ngobrolin soal {item} {ctx} yuk, apa sih yang bikin khas?",
        "menurutmu kenapa {item} selalu berkesan {ctx}?",
        "eh nara, ceritain sisi menarik dari {item} {ctx} dong",
        "kalau bahas {item} {ctx}, apa hal paling seru menurutmu?",
        "kenapa ya {item} rasanya selalu ngangeni {ctx}?",
        "nara, apa keunikan {item} {ctx} yang bikin banyak orang suka?",
        "yuk bahas santai soal {item} {ctx}, gimana menurutmu?",
    ]
    nu_a = [
        "Wah, setuju banget! Daya tarik {item} itu karena {desc}. {ctx_note} Menariknya lagi, {fact}.",
        "Ngomongin {item} emang langsung kebayang hangatnya: {desc}. {ctx_note} Sekadar cerita seru, {fact}.",
        "Yang bikin {item} punya tempat istimewa adalah {desc}. {ctx_note} Apalagi kalau diingat, {fact}.",
        "Khas banget memang! Pada {item}, {desc}. {ctx_note} Tambahan menariknya, {fact}.",
        "Aku suka banget topik ini! Keistimewaan {item} terletak pada {desc}. {ctx_note} Faktanya juga, {fact}.",
        "Kalau diperhatikan, pesona {item} hadir lewat {desc}. {ctx_note} Selain itu, {fact}.",
        "Bener banget, {item} selalu berkesan soalnya {desc}. {ctx_note} Uniknya lagi, {fact}.",
    ]
    for item, desc, fact in NUSANTARA_CHATS:
        for ctx, ctx_note in NUSANTARA_CTX:
            pair_idx += 1
            for k in range(len(nu_q)):
                if limit and len(col.rows) >= limit:
                    return
                q = nu_q[k].format(item=item, ctx=ctx)
                a = nu_a[(k + pair_idx) % len(nu_a)].format(
                    item=item, desc=desc, fact=fact, ctx_note=ctx_note
                )
                col.add(q, a)

    # 2. Diskusi reflektif ringan (24 * 16 * 7 = 2.688)
    rf_q = [
        "nara, {topic} {ctx}, gimana menurutmu?",
        "aku penasaran deh soal {topic} {ctx}, bahas dong!",
        "eh nara, bantu jelasin santai soal {topic} {ctx} dong",
        "menurut pandanganmu, soal {topic} {ctx} itu gimana penjelasannya?",
        "yuk tukar pikiran: {topic} {ctx}",
        "pernah kepikiran nggak soal {topic} {ctx}? bahas dong",
        "tolong kasih sudut pandang hangat tentang {topic} {ctx}",
    ]
    rf_a = [
        "Pertanyaan reflektif yang menarik banget! Secara sederhana, {ans}. {ctx_note} Tips praktisnya, {tip}.",
        "Kalau kita amati pelan-pelan, {ans}. {ctx_note} Sebagai pegangan harian, {tip}.",
        "Hal itu dekat banget sama keseharian kita: {ans}. {ctx_note} Saran nyamannya, {tip}.",
        "Sudut pandang sederhananya begini: {ans}. {ctx_note} Kamu juga bisa mencoba ini: {tip}.",
        "Menarik buat direnungkan! Intinya, {ans}. {ctx_note} Biar makin terasa manfaatnya, {tip}.",
        "Penjelasan membumi dari fenomena itu adalah {ans}. {ctx_note} Catatan kecil yang berguna: {tip}.",
        "Bisa dilihat dari sisi ini: {ans}. {ctx_note} Dalam keseharian, {tip}.",
    ]
    for topic, ans, tip in REFLECT_TOPICS:
        for ctx, ctx_note in REFLECT_CTX:
            pair_idx += 1
            for k in range(len(rf_q)):
                if limit and len(col.rows) >= limit:
                    return
                q = rf_q[k].format(topic=topic, ctx=ctx)
                a = rf_a[(k + pair_idx) % len(rf_a)].format(
                    ans=ans, tip=tip, ctx_note=ctx_note
                )
                col.add(q, a)

    # 3. Kolaborasi & kerja kelompok harian (18 * 16 * 7 = 2.016)
    co_q = [
        "nara, gimana tips {topic} {ctx}?",
        "kasih saran praktis buat {topic} {ctx} dong",
        "cara bijak untuk {topic} {ctx} gimana ya?",
        "eh nara, bantu trik {topic} {ctx} biar lancar dong",
        "kalau mau {topic} {ctx}, langkah enaknya apa?",
        "tolong kasih panduan ringkas soal {topic} {ctx}",
        "biar efektif pas {topic} {ctx}, perhatiin apa aja?",
    ]
    co_a = [
        "Biar kerja samanya enak dan rapi, {how}. {ctx_note} Kuncinya, {why}.",
        "Langkah praktis yang bisa langsung kamu terapkan: {how}. {ctx_note} Soalnya, {why}.",
        "Kamu bisa mengatur alurnya begini: {how}. {ctx_note} Perlu diingat bahwa {why}.",
        "Tips kolaborasi paling efektif di situasi itu adalah {how}. {ctx_note} Alasannya jelas, {why}.",
        "Coba pendekatan komunikatif ini: {how}. {ctx_note} Sebab dalam kerja tim, {why}.",
        "Strategi sederhananya: {how}. {ctx_note} Selain itu, {why}.",
        "Panduan nyamannya dariku: {how}. {ctx_note} Ingat ya, {why}.",
    ]
    for topic, how, why in COLLAB_TOPICS:
        for ctx, ctx_note in COLLAB_CTX:
            pair_idx += 1
            for k in range(len(co_q)):
                if limit and len(col.rows) >= limit:
                    return
                q = co_q[k].format(topic=topic, ctx=ctx)
                a = co_a[(k + pair_idx) % len(co_a)].format(
                    how=how, why=why, ctx_note=ctx_note
                )
                col.add(q, a)
