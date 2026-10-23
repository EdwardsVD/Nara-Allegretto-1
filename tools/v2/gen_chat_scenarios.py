"""Bagian 6 generator `chat.jsonl`:
- Camilan, minuman, & jajanan Nusantara sesuai cuaca dan suasana
- Belanja cerdas di pasar tradisional, swalayan, & toko online
- Komunikasi hangat bareng orang tua, kakak-adik, & keluarga di rumah
- Merawat hewan peliharaan & tanaman di rumah/kos
- Olahraga ringan, peregangan, & kebiasaan bugar harian
- Keterampilan hidup mandiri (life skills) & kesiapsiagaan ringan
- Refleksi diri, kebiasaan mental sehat, & motivasi membumi
- Obrolan hiburan: buku, film, musik, & waktu santai
"""
from __future__ import annotations

from .core_v2 import CategoryCollector

# 1. Camilan & minuman sesuai cuaca/suasana (28 x 18 x 6 = 3.024)
SNACK_DRINKS = [
    ("wedang jahe gula merah hangat", "geprek jahe bakar sebentar lalu rebus bersama irisan gula aren dan selembar daun pandan", "hangatnya jahe langsung membantu menghangatkan badan dan melegakan tenggorokan"),
    ("pisang goreng wijen renyah", "pilih pisang kepok matang yang padat, celupkan ke adonan tepung beras sedikit kapur sirih dan wijen", "tekstur garing di luar dan manis lembut di dalam paling pas dinikmati selagi hangat"),
    ("es timun serut jeruk nipis", "serut kasar timun segar tanpa biji tengahnya lalu beri air dingin, perasan jeruk nipis, dan sedikit sirup", "kandungan air timun dan asam segar jeruk cepat mengusir rasa gerah di siang terik"),
    ("jagung rebus manis oles margarin", "rebus jagung manis beserta selembar kulit dalamnya agar aromanya wangi lalu oles tipis margarin selagi panas", "karbohidrat berserat pada jagung membuat perut kenyang nyaman tanpa rasa berminyak"),
    ("kacang hijau rebus pandan santan encer", "rendam kacang hijau sejam lebih dulu supaya cepat empuk mekar saat direbus bersama daun pandan dan jahe", "kacang hijau kaya protein nabati dan vitamin yang bagus memulihkan tenaga sore hari"),
    ("ubi cilembu panggang atau kukus hangat", "cuci bersih kulitnya lalu kukus atau panggang utuh dengan api kecil supaya madunya keluar alami", "manis alaminya mengenyangkan tanpa perlu tambahan gula pasir sedikit pun"),
    ("teh tawar melati seduh panas", "seduh daun teh melati dengan air panas dua-tiga menit saja lalu saring agar tidak berubah terlalu sepat", "aroma melatinya menenangkan pikiran dan cocok mendampingi camilan gurih apa saja"),
    ("tahu isi sayur tauge wortel hangat", "isi tahu pong dengan tumisan wortel-tauge berbumbu bawang putih lada lalu goreng di minyak panas merata", "isian sayurnya memberi tekstur renyah segar di setiap gigitan"),
    ("potongan buah pepaya dan semangka dingin", "potong dadu sekali suap lalu simpan di wadah tertutup dalam kulkas setengah jam sebelum disantap", "buah berair tinggi membantu mencukupi cairan tubuh sekaligus ramah pencernaan"),
    ("roti bakar selai kacang pisang", "panggang roti sampai permukaannya garing tipis, oles selai kacang, lalu susun irisan pisang di atasnya", "paduan protein kacang dan pisang memberi energi stabil untuk lanjut belajar atau kerja"),
    ("singkong rebus bawang putih merekah", "pilih singkong kupas yang putih bersih, rebus bersama bawang putih halus dan garam, lalu beri es batu sedikit saat mendidih", "kejutan suhu membuat serat singkong merekah empuk saat matang"),
    ("es kelapa muda jeruk peras murni", "campurkan air kelapa muda segar beserta kerukan dagingnya dengan perasan jeruk manis tanpa gula berlebih", "elektrolit alami air kelapa cepat menggantikan keringat sehabis beraktivitas di luar"),
    ("bakwan jagung udang renyah pinggir", "pipil kasar jagung manis, aduk dengan daun bawang, bumbu halus, dan sedikit tepung lalu tuang melebar di tepi wajan", "butiran jagung manisnya meletup gurih waktu digigit hangat-hangat"),
    ("wedang serai jeruk nipis madu", "rebus batang serai geprek hingga harum, tunggu hangat kuku, baru tambahkan madu dan perasan jeruk nipis", "menuang madu saat air sudah agak turun suhunya menjaga kualitas rasa dan aromanya"),
    ("bubur sumsum lembut kuah gula merah", "aduk tepung beras dan santan bersama pandan di api kecil terus-menerus sampai meletup halus tanpa menggumpal", "teksturnya yang super lembut nyaman di perut saat baru pulih dari lelah"),
    ("kacang tanah rebus kulit gurih", "cuci bersih tanah di kulit kacang lalu rebus dengan garam dan daun salam sampai bijinya empuk", "camilan tradisional ini asyik dikupas pelan-pelan sambil mengobrol santai"),
    ("susu hangat kayu manis menjelang istirahat", "hangatkan susu tanpa sampai mendidih meluap lalu aduk sejumput bubuk kayu manis wangi", "minuman hangat bebas kafein di malam hari membantu tubuh bersiap tidur pulas"),
    ("klepon ketan pandan isi gula merah", "bulatkan adonan tepung ketan hijau berisi sisiran gula merah lalu gulingkan di kelapa parut kukus sedikit garam", "kelapa parut yang dikukus sebentar membuat klepon tidak mudah basi sampai sore"),
    ("salad buah segar saus yoghurt ringan", "campur potongan apel, pir, melon, dan anggur dengan saus yoghurt tawar sedikit madu serta parutan keju tipis", "memakai yoghurt menggantikan mayones berlebih bikin rasanya jauh lebih segar dan tidak enek"),
    ("kopi tubruk tipis sore hari", "seduh bubuk kopi murni dengan air panas baru mendidih lalu diamkan empat menit sampai ampasnya turun sempurna", "menunggu ampas mengendap alami membuat tegukan kopinya bersih tanpa serbuk di lidah"),
    ("tempe goreng tepung ketumbar bawang", "haluskan bawang putih dan ketumbar utuh untuk adonan pelapis tempe iris tipis lalu goreng api sedang", "aroma ketumbar segar yang baru diulek bikin wangi gorengan rumahan jauh lebih sedap"),
    ("puding susu cokelat dingin lembut", "masak bubuk agar-agar bersama susu dan cokelat bubuk sambil diaduk rata sebelum dituang ke cetakan kecil", "camilan dingin dari kulkas ini praktis disiapkan pagi hari untuk dinikmati sore nanti"),
    ("edamame atau kedelai rebus tabur garam tipis", "rebus polong kedelai di air mendidih lima menit saja agar warnanya tetap hijau cerah dan bijinya renyah", "tinggi protein dan bersih di jari, jadi aman dimakan sambil baca buku atau mengetik"),
    ("air infus irisan lemon dan daun mint", "masukkan irisan tipis lemon tanpa biji serta beberapa pucuk daun mint ke botol air dingin selama satu jam", "aroma segar sitrus membuat kita lebih rajin minum air putih sepanjang hari"),
    ("martabak telur kulit lumpia teflon", "kocok telur bersama irisan daun bawang banyak dan sedikit daging cincang, bungkus kulit lumpia, lalu panggang sedikit minyak", "kulit lumpia menghasilkan tekstur renyah cepat tanpa perlu menguleni adonan kulit dari nol"),
    ("kolak pisang ubi santan ringan", "rebus ubi dulu sampai setengah empuk baru masukkan potongan pisang tanduk, gula merah, pandan, dan santan encer", "urutan memasukkan ubi lebih dulu menjaga pisang tidak hancur lembek saat kuah matang"),
    ("keripik pangsit panggang atau goreng bawang", "potong kotak kulit pangsit siap pakai lalu panggang atau goreng sebentar hingga kuning keemasan dan tiriskan tuntas", "disimpan di toples kedap udara, renyahnya bisa bertahan seminggu buat teman belajar"),
    ("jus alpukat kocok sedikit cokelat", "keruk daging alpukat matang mentega lalu kocok kasar memakai garpu bersama es serut dan sedikit susu", "lemak baik pada alpukat membuat perut kenyang lama saat belum sempat makan besar"),
]

SNACK_MOODS = [
    ("waktu sore di luar lagi hujan rintik-rintik", "Ditemani suara rintik hujan di jendela, suasananya bakal terasa dua kali lebih syahdu."),
    ("pas siang bolong udara lagi gerah banget", "Cocok banget disantap pelan-pelan di ruang teduh buat menurunkan rasa gerah."),
    ("buat teman belajar atau ngetik tugas malam", "Siapkan di piring kecil sebelah meja supaya tangan nggak mengotori papan ketik."),
    ("waktu ada teman dekat mampir main ke rumah", "Disajikan hangat-hangat di piring tengah langsung bikin obrolan ruang tamu makin cair."),
    ("pas lagi pengen ngemil tapi takut terlalu berat di perut", "Atur porsinya secukupnya aja supaya lidah senang tapi perut tetap terasa ringan."),
    ("di akhir pekan sambil nonton film santai", "Bikin satu porsi sebelum film diputar supaya kamu nggak bolak-balik ke dapur di tengah cerita."),
    ("waktu anggaran jajan minggu ini lagi dihemat", "Bahan dasarnya murah meriah di pasar atau warung sebelah dan bisa jadi beberapa porsi sekaligus."),
    ("pas tenggorokan pengen sesuatu yang segar alami", "Bahan segarnya terasa jauh lebih bersih di tenggorokan daripada jajanan berpengawet tinggi."),
    ("sehabis pulang kehujanan atau kedinginan di jalan", "Setelah mandi dan ganti baju kering, sajian ini cepat mengembalikan rasa nyaman di badan."),
    ("waktu kumpul santai bareng orang rumah sore hari", "Momen duduk bareng keluarga sepulang kegiatan jadi makin hangat kalau ada teman kudapan meja."),
    ("pas lagi bosan sama camilan kemasan pabrik", "Rasa masakan dapur sendiri punya aroma segar yang nggak tergantikan bungkus instan."),
    ("sebagai pengganjal perut jam empat sore sebelum makan malam", "Porsi kecil di sore hari mencegah kita kalap makan berlebihan waktu jam makan malam tiba."),
    ("waktu pengen nyoba bikin sendiri dalam 15 menit", "Langkahnya ringkas banget sehingga pemula pun nggak bakal kerepotan di dapur."),
    ("pas lagi kerja dari rumah butuh penyegar fokus", "Jeda lima menit menikmati ini lumayan banget menyegarkan otak sebelum lanjut sesi kerja berikutnya."),
]


# 2. Belanja cerdas pasar, swalayan, & toko online (24 x 14 x 6 = 2.016)
SHOPPING_TIPS = [
    ("memilih ikan segar waktu belanja pagi di pasar", "perhatikan matanya yang bening cembung, insang berwarna merah segar bukan cokelat pucat, dan dagingnya membal kembali saat ditekan", "ikan segar beraroma khas laut ringan, bukan bau menyengat tajam"),
    ("memilih telur ayam yang masih bagus kualitasnya", "pilih cangkang yang utuh bersih tidak retak, terasa agak berat di tangan, dan tidak berbunyi kocak saat digoyangkan pelan", "telur baru punya putih telur yang masih kental memeluk kuningnya saat dipecahkan"),
    ("membeli sayur daun hijau supaya tahan beberapa hari", "pilih batang yang masih renyah tegak, daun tidak berlendir atau menguning di tepinya, dan hindari ikatan yang terlalu basah tergenang air", "bungkus kertas atau tisu kering sebelum masuk laci sayur kulkas agar tidak cepat busuk"),
    ("membeli sepatu secara online tanpa mencoba langsung", "ukur panjang telapak kakimu memakai penggaris di atas kertas dalam satuan sentimeter lalu cocokkan tabel ukuran insole merek tersebut", "nomor ukuran 40 antar merek bisa selisih satu sentimeter, jadi patokan panjang sentimeter paling akurat"),
    ("mengecek keaslian dan keamanan toko saat belanja online", "baca ulasan pembeli yang menyertakan foto asli barang terbaru serta periksa ulasan bintang rendah untuk melihat cara penjual menangani keluhan", "jangan tergiur harga miring jauh di bawah pasaran dari akun baru tanpa riwayat transaksi jelas"),
    ("memilih buah jeruk atau mangga yang manis matang", "cium pangkal tangkainya yang beraroma harum buah segar dan pilih buah yang terasa padat berisi dibanding ukurannya", "kulit yang mulus mengilap belum tentu manis kalau bobotnya terasa ringan kering"),
    ("membandingkan harga barang kebutuhan pokok di swalayan", "lihat angka harga per 100 gram atau per mililiter pada label rak, bukan sekadar terpaku pada tulisan kemasan hemat", "kadang dua kemasan sedang sedang diskon justru lebih murah per gramnya daripada satu kemasan jumbo"),
    ("memilih daging ayam potong yang segar dan higienis", "pastikan warna daging putih kemerahan segar, permukaan kulit tidak berlendir lengket, dan seratnya kenyal tidak berair berlebihan", "segera simpan di pembeku dalam porsi sekali masak begitu tiba di rumah"),
    ("membeli pakaian kaos atau kemeja harian biar adem dipakai", "raba ketebalan serat katunnya di bawah cahaya, periksa kerapian jahitan ketiak serta kancing, dan pilih bahan yang menyerap keringat", "bahan sintetis penuh yang tidak berpori memang murah tapi terasa panas menyengat di iklim tropis"),
    ("merekam bukti pembukaan paket (unboxing) belanja online", "rekam video utuh tanpa jeda mulai dari label resi yang terbaca jelas, semua sisi kardus masih tersegel, hingga pengetesan fungsi barang", "rekaman utuh tanpa potong menjadi syarat mutlak kalau barang datang kurang atau pecah di jalan"),
    ("memilih tempe dan tahu yang baru jadi di pasar", "pilih tempe yang rajutan jamurnya putih rapat merata dan terasa hangat padat, serta tahu yang beraroma kedelai segar tidak asam", "tahu putih segar sebaiknya direndam air matang bersih yang diganti harian di dalam kulkas"),
    ("membeli peralatan listrik kecil seperti ketel atau setrika", "periksa tanda standar keselamatan resmi, daya watt yang sesuai kapasitas listrik rumah/kos, serta ketersediaan kartu garansi", "alat pemanas berdaya watt terlalu tinggi bisa membuat meteran listrik kamar kos langsung jeglek"),
    ("berbelanja bulanan supaya tidak melebihi anggaran rencana", "makan secukupnya sebelum berangkat belanja agar tidak lapar mata di lorong camilan, dan ikuti daftar catatan yang sudah disusun", "berbelanja dalam keadaan perut keroncongan terbukti bikin keranjang penuh jajanan tak terencana"),
    ("memilih beras yang pulen dan bersih dari kutu", "amati butiran beras yang utuh tidak banyak patah menir, tidak berbau apek lembap, serta bebas serbuk putih halus di dasar karung", "simpan beras di wadah tertutup rapat bersama beberapa lembar daun jeruk kering agar kutu enggan bersarang"),
    ("membeli kacamata atau pelindung mata yang nyaman", "pastikan jembatan penyangga hidungnya pas tidak melorot saat menunduk dan gagang samping tidak menekan pelipis terlalu keras", "gagang yang terlalu menjepit di menit pertama biasanya memicu pusing setelah dipakai dua jam"),
    ("memilih tas ransel untuk membawa laptop dan buku berat", "cari tali bahu lebar berbantalan busa tebal, jahitan penguat silang di pangkal tali, dan sekat khusus berlapis busa di bagian dalam", "tali tipis tanpa bantalan cepat membuat bahu nyeri saat beban tas penuh"),
    ("memeriksa masa kedaluwarsa produk makanan kemasan", "biasakan mengambil kemasan di baris agak belakang rak jika baru akan dikonsumsi minggu depan dan pastikan kaleng tidak penyok menggembung", "kemasan kaleng yang menggembung menandakan aktivitas bakteri berbahaya di dalamnya walau tanggalnya belum lewat"),
    ("membeli perlengkapan alat tulis dan buku catatan", "coba ketebalan kertasnya minimal 70-80 gsm supaya tinta pulpen gel tidak tembus membayang ke halaman sebaliknya", "kertas yang nyaman membuat kegiatan mencatat jauh lebih rapi dan awet dibaca ulang"),
    ("menawar harga dengan sopan di pasar tradisional", "sapa pedagang dengan ramah, tawar secara wajar tanpa merendahkan kualitas dagangannya, dan tersenyum bila belum ketemu harga cocok", "pedagang pasar justru sering memberi bonus timbangan ramah kepada pembeli yang sopan tutur katanya"),
    ("membeli perangkat elektronik bekas pakai yang masih layak", "uji langsung semua tombol, layar, baterai, kamera, dan konektivitas di tempat terang tanpa terburu-buru sebelum membayar", "hindari transaksi transfer langsung ke penjual perorangan tanpa rekening bersama atau temu langsung"),
]

SHOPPING_CTX = [
    ("waktu baru belajar belanja kebutuhan sendiri", "Pelan-pelan aja mengamatinya, lama-kelamaan matamu bakal terlatih membedakan mana yang bagus dalam sekali lihat."),
    ("supaya uang belanja mingguan nggak terbuang sia-sia", "Teliti satu menit sebelum membayar menyelamatkan kita dari kecewa barang terbuang di rumah."),
    ("pas kondisi pasar atau toko lagi lumayan ramai", "Meski suasana ramai, jangan sungkan mengecek fisik barangnya dengan tenang sebelum masuk kantong."),
    ("buat stok persediaan seminggu ke depan di kos", "Karena buat disimpan beberapa hari, memilih kesegaran terbaik di awal bakal bikin stokmu awet sampai akhir pekan."),
    ("apalagi sebelumnya pernah kecewa salah pilih barang", "Pengalaman salah beli kemarin wajar banget kok, sekarang kamu jadi punya patokan jelas yang harus dicek."),
    ("dengan tetap menjaga anggaran tetap hemat", "Barang bagus nggak selalu yang paling mahal, melainkan yang paling sehat kondisinya dan pas fungsinya."),
    ("waktu belanja buat dimasak bareng keluarga", "Bahan yang segar sejak dari pasar bikin bumbu sederhana pun rasanya langsung naik kelas waktu matang."),
    ("menjelang hari besar yang permintaannya lagi naik", "Di musim ramai, berangkat belanja lebih pagi memberi pilihan stok yang jauh lebih segar dan lengkap."),
    ("biar barang yang dibeli awet dipakai lama", "Mengecek detail jahitan atau segel di awal jauh lebih mudah daripada mengurus penukaran barang belakangan."),
    ("tanpa gampang kemakan iklan yang berlebihan", "Fokus pada spesifikasi nyata dan kebutuhan harianmu bikin kamu kebal dari rayuan promosi semata."),
]


# 3. Komunikasi Keluarga, Hewan/Tanaman, Olahraga Ringan, & Life Skills Mandiri
FAMILY_TOPICS = [
    ("berbeda pandangan soal pilihan jurusan atau karier dengan orang tua", "dengarkan dulu kekhawatiran beliau sampai tuntas tanpa memotong, lalu tunjukkan rencana konkret dan prospek nyata bidang pilihanmu", "orang tua sering menolak sesuatu semata-mata karena belum terbayang gambaran keamanannya bagi masa depanmu"),
    ("adik di rumah susah diajak berbagi tugas beres-beres rumah", "ajak mengerjakan bareng sambil membagi porsi yang jelas dan ringan daripada sekadar menyuruh dari jauh dengan nada tinggi", "contoh langsung dan pembagian adil jauh lebih mempan menggerakkan adik daripada omelan panjang"),
    ("ingin mulai memberi sedikit uang hasil kerja pertama untuk orang tua", "berikan dengan tulus sambil meminta doa restu tanpa memikirkan besar-kecilnya nominal yang baru sanggup disisihkan", "bagi orang tua, perhatian dan ingatan tulus dari anaknya jauh lebih mengharukan daripada jumlah angkanya"),
    ("suasana meja makan rumah terasa sepi karena semua sibuk menatap HP", "mulai dari dirimu sendiri menaruh HP menghadap bawah saat makan lalu lontarkan cerita ringan soal kejadian lucu hari ini", "satu orang yang memulai obrolan hangat biasanya pelan-pelan memancing anggota rumah lain ikut menaruh gawai"),
    ("orang tua mudah percaya pesan berantai kesehatan yang belum tentu benar", "apresiasi dulu niat peduli beliau, lalu carikan penjelasan dokter resmi yang bahasanya santun tanpa menyalahkan beliau", "menjaga perasaan hormat saat meluruskan informasi membuat orang tua lebih terbuka mendengar fakta medis"),
    ("merasa dibanding-bandingkan dengan saudara atau anak tetangga", "tarik napas tenang, sampaikan pelan bahwa kamu sedang fokus memperjuangkan jalurmu sendiri, dan jangan serap perbandingan itu ke harga dirimu", "setiap orang punya garis start dan musim tumbuh yang berbeda-beda"),
    ("ingin meminta izin pergi acara luar kota bersama teman-teman", "sampaikan jadwal keberangkatan, tempat menginap, daftar teman yang ikut, serta nomor kontak darurat dengan transparan sejak jauh hari", "informasi lengkap di awal memangkas setengah kecemasan orang tua sebelum kamu berangkat"),
    ("menemani kakek atau nenek mengobrol supaya beliau senang", "minta beliau menceritakan kisah masa muda atau resep masakan lamanya sambil mendengarkan dengan antusias", "didengarkan kenangan hidupnya dengan tulus adalah hadiah kebahagiaan besar bagi lansia"),
    ("menyelesaikan salah paham kecil antar kakak-beradik di rumah", "sapa duluan lewat hal sepele seperti menawarkan makanan hangat lalu bicarakan intinya singkat tanpa mengungkit kesalahan lama", "gengsi diam-diaman berhari-hari di satu atap hanya menguras energi batin sendiri"),
    ("membantu orang tua memahami pemakaian fitur baru di ponsel pintar", "ajarkan pelan-pelan sambil membiarkan jari beliau menekan sendiri tombolnya dan tuliskan langkah urutannya di kertas besar", "kesabaran mengulang tanpa berdecak kesal adalah wujud sayang paling sederhana di era digital"),
]

FAMILY_CTX = [
    ("supaya suasana rumah tetap adem dan nggak berujung debat", "Memilih waktu bicara saat semua sudah kenyang dan santai sore hari sangat menentukan tenangnya obrolan."),
    ("apalagi aku kadang suka grogi kalau bicara serius di rumah", "Kalau lidah terasa kaku, mulai saja dari obrolan ringan lima menit sebelum masuk ke intinya."),
    ("waktu pulang kampung setelah lama merantau", "Momen kumpul yang singkat sayang banget kalau habis buat tegang—utamakan kehangatan kebersamaannya."),
    ("padahal niat kita sama-sama baik cuma beda cara nyampein", "Sering kali gesekan keluarga itu bukan kurang sayang, melainkan gaya bahasanya saja yang belum ketemu."),
    ("tanpa terkesan menggurui atau membantah kasar", "Nada suara yang rendah dan lembut adalah setengah dari keberhasilan komunikasi di rumah."),
    ("biar hubungan di rumah makin terbuka dan saling dukung", "Keterbukaan dibangun dari obrolan kecil rutin tiap minggu, bukan cuma saat ada masalah besar."),
    ("waktu kondisi di rumah lagi sama-sama capek kerja", "Kalau lihat beliau baru pulang lelah, tunda obrolan beratnya sampai besok pas suasana sudah segar."),
    ("agar aku tetap bisa jujur soal perasaanku sendiri", "Menyampaikan perasaan pakai kalimat 'aku merasa...' jauh lebih teduh daripada kalimat menuduh."),
]

PET_PLANT_LIFE = [
    ("merawat kucing kampung yang baru diadopsi di rumah", "siapkan bak pasir bersih jauh dari mangkuk makan-minumnya, beri pakan sesuai umur, dan jadwalkan vaksinasi serta obat cacing dasar", "kucing baru butuh sudut tenang dua-tiga hari pertama untuk mengenali bau rumah barunya"),
    ("menjaga kebersihan bak pasir kucing supaya tidak bau di sekitar rumah", "serok gumpalan kotoran minimal sekali-dua kali sehari dan cuci jemur baknya dengan sabun lembut setiap minggu", "bak yang bersih juga mencegah kucing buang air sembarangan di karpet atau kasur"),
    ("memelihara ikan hias kecil seperti cupang atau guppy di meja", "gunakan air yang sudah diendapkan semalam agar klorinnya menguap dan beri pakan secukupnya yang habis dalam dua menit", "sisa pelet berlebih yang membusuk di dasar air justru meracuni insang ikan dengan cepat"),
    ("mengatasi daun tanaman hias dalam pot yang ujungnya mulai menguning", "cek drainase lubang bawah pot agar air tidak menggenang, kurangi frekuensi siram bila tanah masih lembap, dan kenakan cahaya pagi tidak langsung", "daun menguning lembek paling sering disebabkan akar kekurangan oksigen akibat kelebihan air"),
    ("memindahkan bibit tanaman baru ke pot yang lebih besar", "lakukan sore hari agar tanaman tidak stres panas terik, jaga bola tanah akar utamanya jangan pecah, lalu siram secukupnya", "adaptasi semalam penuh dalam suhu sejuk membantu akar cepat pulih"),
    ("melakukan peregangan tubuh pagi lima menit setelah bangun tidur", "duduk di tepi kasur, putar leher dan bahu perlahan, tarik kedua lengan ke atas sambil mengambil napas dalam, lalu regangkan betis", "gerakan lembut melancarkan aliran darah sebelum tubuh langsung berdiri cepat"),
    ("mulai kebiasaan jalan cepat 25 menit tiap sore", "gunakan sepatu beralas empuk yang pas ukurannya, ayunkan lengan rileks, dan jaga langkah stabil di jalur yang aman dari kendaraan", "jalan cepat rutin sangat ramah bagi persendian lutut sekaligus menyehatkan jantung"),
    ("menyiapkan kotak pertolongan pertama (P3K) dasar di kamar kos", "sediakan plester luka, kasa steril, cairan antiseptik pembersih luka, oralit, termometer digital, dan obat pereda demam dasar", "periksa tanggal kedaluwarsa isi kotak setiap enam bulan sekali agar selalu siap pakai"),
    ("menghadapi luka gores kecil saat memasak di dapur", "alirkan air bersih mengalir untuk membilas kotoran, tekan lembut memakai kasa bersih sampai darah berhenti, lalu tutup plester", "hindari menaburkan bubuk kopi atau pasta gigi ke luka terbuka karena justru memicu infeksi"),
    ("menghemat tagihan listrik bulanan di rumah atau kamar kos", "matikan lampu saat ruangan terang cahaya matahari, bersihkan saringan debu kipas atau pendingin udara rutin, dan cabut pemanas air bila tak dipakai", "debu tebal di saringan pendingin udara memaksa mesin bekerja jauh lebih berat dan boros daya"),
    ("merawat pakaian warna gelap supaya tidak cepat pudar kusam", "balik bagian dalam pakaian ke luar sebelum dicuci, gunakan air dingin dengan deterjen secukupnya, dan jemur di tempat teduh berangin", "sinar matahari terik langsung pada sisi luar kain cepat memecah pigmen warna gelap"),
    ("menjaga privasi dan keamanan kata sandi akun digital", "gunakan kombinasi kalimat sandi panjang yang berbeda untuk email utama dan perbankan, serta aktifkan autentikasi dua faktor", "satu sandi yang dipakai seragam di puluhan situs berisiko membuka semua akun bila satu situs bocor"),
]

PPL_CTX = [
    ("buat pemula yang baru pertama kali nyoba ngurus ini", "Tenang aja, asal konsisten sama langkah dasarnya, lama-lama jadi kebiasaan otomatis yang gampang kok."),
    ("waktu jadwal harian lumayan sibuk tapi pengen tetap terawat", "Cukup sisihkan lima menit rutin di jam yang sama supaya nggak terasa membebani jadwalmu."),
    ("di ruang rumah atau kos yang ukurannya terbatas", "Di ruang mungil, kerapian dan kebersihan rutin bikin suasananya tetap sehat dan nyaman ditinggali."),
    ("dengan peralatan sederhana yang mudah dicari di sekitar", "Nggak perlu beli perlengkapan mahal; alat dasar yang bersih dan tepat guna sudah sangat memadai."),
    ("supaya hasilnya sehat dan tahan jangka panjang", "Merawat sedikit demi sedikit secara teratur selalu jauh lebih hemat daripada mengobati saat telanjur rusak."),
    ("pas musim hujan dan udara lagi lembap-lembapnya", "Di cuaca lembap, perhatikan sirkulasi udara dan kebersihan ekstra supaya jamur nggak gampang tumbuh."),
    ("waktu musim kemarau udara terasa kering dan panas", "Saat cuaca panas kering, cek kecukupan air dan teduhan sedikit lebih sering dari biasanya ya."),
    ("agar jadi rutinitas positif yang bikin betah di rumah", "Kebiasaan kecil merawat sesuatu di rumah terbukti memberi rasa tenang sepulang beraktivitas."),
]


def build_chat_scenarios(col: CategoryCollector, limit: int | None = None) -> None:
    pair_idx = 0

    # 1. Camilan & minuman (28 * 14 * 6 = 2.352)
    s_q = [
        "nara, ide kudapan atau minuman kaya {item} pas nggak {mood}?",
        "gimana cara bikin {item} yang enak {mood}?",
        "pengen nyoba {item} nih {mood}, tips simpelnya gimana?",
        "cocok nggak menikmati {item} {mood}? cara buatnya gimana?",
        "eh nara, kasih saran praktis bikin {item} {mood} dong",
        "kalau mau nyiapin {item} {mood}, kuncinya apa ya?",
    ]
    s_a = [
        "Cocok banget! Buat menyajikan **{item}**, kamu cukup {how}. {mood_note} Enaknya lagi, {why}.",
        "Wah mantap pilihannya! Cara simpel bikin **{item}**: {how}. {mood_note} Selain itu, {why}.",
        "Pas banget buat suasana itu! Untuk **{item}**, tinggal {how}. {mood_note} Soalnya, {why}.",
        "Ide yang sedap tuh! Langkah ringkas membuat **{item}** adalah {how}. {mood_note} Perlu dicatat, {why}.",
        "Setuju banget, **{item}** memang juara! Caranya: {how}. {mood_note} Kenapa pas? Karena {why}.",
        "Bisa banget langsung dicoba! Untuk **{item}**, {how}. {mood_note} Tambahan lagi, {why}.",
    ]
    for item, how, why in SNACK_DRINKS:
        for mood, mood_note in SNACK_MOODS:
            pair_idx += 1
            for k in range(len(s_q)):
                if limit and len(col.rows) >= limit:
                    return
                q = s_q[k].format(item=item, mood=mood)
                a = s_a[(k + pair_idx) % len(s_a)].format(
                    item=item, how=how, why=why, mood_note=mood_note
                )
                col.add(q, a)

    # 2. Belanja cerdas (20 * 10 * 6 = 1.200)
    sh_q = [
        "nara, gimana tips {tip_topic} {ctx}?",
        "kasih panduan singkat cara {tip_topic} {ctx} dong",
        "biar nggak salah beli waktu {tip_topic} {ctx}, cek apa aja?",
        "eh nara, ajarin trik {tip_topic} {ctx} ya",
        "apa yang harus diperhatiin pas {tip_topic} {ctx}?",
        "bantu tips praktis soal {tip_topic} {ctx} dong!",
    ]
    sh_a = [
        "Biar belanjamu tepat sasaran, {how}. {ctx_note} Ingat patokan ini: {why}.",
        "Trik gampangnya waktu di sana: {how}. {ctx_note} Soalnya, {why}.",
        "Cukup perhatikan ciri utamanya: {how}. {ctx_note} Alasannya jelas, {why}.",
        "Langkah paling aman adalah {how}. {ctx_note} Sekadar catatan tambahan, {why}.",
        "Kamu bisa cek dengan cara sederhana ini: {how}. {ctx_note} Sebab, {why}.",
        "Supaya dapat yang bagus, {how}. {ctx_note} Perlu diingat juga bahwa {why}.",
    ]
    for tip_topic, how, why in SHOPPING_TIPS:
        for ctx, ctx_note in SHOPPING_CTX:
            pair_idx += 1
            for k in range(len(sh_q)):
                if limit and len(col.rows) >= limit:
                    return
                q = sh_q[k].format(tip_topic=tip_topic, ctx=ctx)
                a = sh_a[(k + pair_idx) % len(sh_a)].format(
                    how=how, why=why, ctx_note=ctx_note
                )
                col.add(q, a)

    # 3. Komunikasi keluarga (10 * 8 * 6 = 480)
    fm_q = [
        "nara, gimana cara menyikapi situasi {sit} {ctx}?",
        "kasih saran bijak dong kalau {sit} {ctx}",
        "bingung nih di rumah, {sit} {ctx}, enaknya gimana?",
        "eh nara, langkah yang baik saat {sit} {ctx} apa ya?",
        "menurutmu gimana menghadapi {sit} {ctx}?",
        "tolong bantu masukan hangat soal {sit} {ctx}",
    ]
    fm_a = [
        "Urusan keluarga memang butuh kesabaran ekstra: coba {how}. {ctx_note} Soalnya, {why}.",
        "Pendekatan paling sejuk yang bisa kamu coba adalah {how}. {ctx_note} Ingat bahwa {why}.",
        "Pelan-pelan aja menyikapinya, kamu bisa {how}. {ctx_note} Alasannya sederhana: {why}.",
        "Saran dariku, mulai dengan langkah hangat ini: {how}. {ctx_note} Sebab di rumah, {why}.",
        "Coba komunikasikan dengan tenang: {how}. {ctx_note} Pegang satu hal ini ya: {why}.",
        "Biar hati sama-sama lega, coba {how}. {ctx_note} Kenapa penting? Karena {why}.",
    ]
    for sit, how, why in FAMILY_TOPICS:
        for ctx, ctx_note in FAMILY_CTX:
            pair_idx += 1
            for k in range(len(fm_q)):
                if limit and len(col.rows) >= limit:
                    return
                q = fm_q[k].format(sit=sit, ctx=ctx)
                a = fm_a[(k + pair_idx) % len(fm_a)].format(
                    how=how, why=why, ctx_note=ctx_note
                )
                col.add(q, a)

    # 4. Hewan peliharaan, tanaman, kebugaran, & life skills mandiri (12 * 8 * 6 = 576)
    pp_q = [
        "nara, gimana cara {topic} {ctx}?",
        "kasih tips gampang buat {topic} {ctx} dong",
        "kalau mau mulai {topic} {ctx}, langkah dasarnya apa?",
        "eh nara, ajarin panduan ringkas {topic} {ctx} ya",
        "biar berhasil {topic} {ctx}, harus perhatiin apa aja?",
        "tolong bagi trik harian untuk {topic} {ctx}",
    ]
    pp_a = [
        "Gampang kok dipraktikkan! Kamu cukup {how}. {ctx_note} Catatan pentingnya: {why}.",
        "Langkah dasar yang paling efektif adalah {how}. {ctx_note} Soalnya, {why}.",
        "Kamu bisa mulai dari kebiasaan sederhana ini: {how}. {ctx_note} Ingat juga, {why}.",
        "Panduan ringkasnya begini: {how}. {ctx_note} Alasannya, {why}.",
        "Coba terapkan cara praktis ini: {how}. {ctx_note} Sebab dalam praktiknya, {why}.",
        "Biar aman dan hasilnya bagus, {how}. {ctx_note} Perlu diketahui, {why}.",
    ]
    for topic, how, why in PET_PLANT_LIFE:
        for ctx, ctx_note in PPL_CTX:
            pair_idx += 1
            for k in range(len(pp_q)):
                if limit and len(col.rows) >= limit:
                    return
                q = pp_q[k].format(topic=topic, ctx=ctx)
                a = pp_a[(k + pair_idx) % len(pp_a)].format(
                    how=how, why=why, ctx_note=ctx_note
                )
                col.add(q, a)
