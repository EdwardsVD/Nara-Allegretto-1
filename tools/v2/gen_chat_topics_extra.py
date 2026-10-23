"""Bagian 9 generator `chat.jsonl`:
- Menyusun ucapan hangat, doa baik, & apresiasi momen keseharian
- Menghadapi kejadian apes/salah kecil sehari-hari tanpa panik
- Kiat belajar keterampilan praktis baru dari nol secara mandiri
- Kebiasaan baik & etika kenyamanan bersama di ruang publik Indonesia
"""
from __future__ import annotations

from .core_v2 import CategoryCollector

# 1. Ucapan & apresiasi momen harian (28 x 16 x 7 = 3.136)
GREETING_MOMENTS = [
    ("ulang tahun ibu tercinta", "Selamat ulang tahun, Bu. Terima kasih atas sabar dan doa ibu yang nggak pernah putus; semoga ibu selalu sehat, tenang hatinya, dan bahagia bersama keluarga.", "menyebutkan rasa terima kasih atas kesabaran ibu selalu terasa paling menyentuh"),
    ("ulang tahun ayah di rumah", "Selamat ulang tahun, Pak. Semoga bapak senantiasa diberi kesehatan prima, langkah yang ringan, dan kebahagiaan menikmati waktu hangat bersama kami.", "kalimat yang lugas dan mendoakan kesehatan sangat pas dengan karakter kebanyakan ayah"),
    ("kelulusan sidang tugas akhir sahabat", "Selamat sudah menuntaskan sidang hari ini! Semua malam panjang dan revisi yang kamu lewati akhirnya terbayar lunas, istirahat yang puas malam ini ya!", "mengakui perjuangan panjang di balik kelulusannya bikin ucapan terasa sangat personal"),
    ("teman yang baru sembuh dan aktif kembali", "Senang banget lihat kamu sudah sehat dan beraktivitas lagi! Pelan-pelan dulu aja ritmenya sambil menjaga stamina biar pulih seratus persen ya.", "mengingatkan agar tidak langsung memforsir tenaga menunjukkan kepedulian nyata"),
    ("kelahiran bayi dari teman atau saudara", "Selamat atas kelahiran buah hatinya ya! Semoga si kecil tumbuh sehat ceria, serta ibu dan ayahnya diberi kekuatan juga waktu istirahat yang cukup.", "ikut mendoakan kesehatan orang tuanya juga terasa hangat karena begadang mengurus bayi cukup menguras tenaga"),
    ("rekan yang mendapat promosi atau tanggung jawab baru", "Selamat atas amanah barunya! Dedikasi dan kerapian kerjamu selama ini memang layak banget mendapat kepercayaan ini, semoga makin sukses ke depannya.", "memuji kualitas kerja nyatanya menghindarkan kesan basa-basi kosong"),
    ("pamit selesai masa magang kepada tim pembimbing", "Terima kasih banyak atas bimbingan sabar dan ilmu berharga selama masa magang ini. Mohon maaf bila ada kekeliruan, semoga kita bisa berjumpa lagi di kesempatan baik.", "pamit dengan sopan dan penuh apresiasi menjaga pintu silaturahmi profesional tetap terbuka"),
    ("hari guru untuk pengajar yang berjasa", "Selamat Hari Guru! Terima kasih sudah sabar menyalakan rasa ingin tahu dan membimbing kami memahami banyak hal baru dengan hati yang tulus.", "mengenang cara beliau membuat pelajaran jadi bermakna adalah hadiah batin terbaik bagi pengajar"),
    ("teman yang sedang menghadapi ujian masuk penting besok", "Semangat buat ujian besok pagi ya! Persiapanmu sudah panjang, malam ini tidur yang cukup biar besok pikiranmu jernih dan tenang mengerjakan setiap soal.", "pesan penyemangat yang menenangkan jauh lebih membantu daripada kalimat yang menambah beban target"),
    ("sahabat yang pindah merantau ke kota jauh", "Hati-hati di perantauan barumu ya! Semoga cepat ketemu lingkungan yang ramah, lancar urusannya, dan jangan sungkan berkabar kapan pun kangen ngobrol.", "menawarkan telinga siap dengar membuat perantau merasa tidak sendirian di kota asing"),
    ("pernikahan teman sekolah atau kuliah", "Selamat menempuh hidup baru untuk kalian berdua! Semoga rumahnya selalu hangat oleh tawa, saling menguatkan di segala musim, dan langgeng selamanya.", "doa tentang saling menguatkan dalam keseharian terdengar dewasa dan menyejukkan"),
    ("ucapan belasungkawa yang santun untuk teman berduka", "Turut berdukacita sedalam-dalamnya atas kepergian almarhum/almarhumah. Semoga keluarga yang ditinggalkan diberi ketabahan, kekuatan, dan ketenangan hati.", "saat berduka, kalimat singkat yang teduh tanpa banyak bertanya kronologi jauh lebih menghormati perasaan keluarga"),
    ("apresiasi untuk teman yang sudah menolong di saat repot", "Terima kasih banyak ya sudah meluangkan waktu bantu urusanku tadi, beneran sangat meringankan! Kapan-kapan kalau butuh bantuan, langsung kabari aku ya.", "menyebutkan betapa bantuannya meringankan bebanmu membuat penolong merasa dihargai tulus"),
    ("menyemangati adik yang baru pertama ikut lomba", "Keren banget kamu sudah berani maju ikut lomba hari ini! Nikmati aja pengalamannya di panggung tanpa takut salah, kami semua bangga sama keberanianmu.", "memuji keberanian mencoba membuat mental anak tetap gembira apa pun hasil pialanya"),
    ("menyambut anggota baru yang bergabung di grup tim", "Selamat bergabung di tim kita ya! Kalau ada istilah atau alur kerja yang masih membingungkan di minggu awal ini, santai aja langsung tanya ke grup.", "sambutan ramah yang membuka ruang bertanya langsung mencairkan rasa gugup orang baru"),
    ("mengucapkan selamat menempati rumah atau kos baru", "Selamat menempati tempat tinggal barunya ya! Semoga betah, lingkungannya aman menyenangkan, dan membawa banyak cerita baik setiap hari.", "doa soal rasa betah dan aman sangat pas untuk awal suasana tempat tinggal baru"),
    ("permintaan maaf tulus kepada orang rumah karena pulang terlambat", "Maaf ya tadi terlambat mengabari sampai bikin orang rumah khawatir, tadi baterai HP sempat habis di jalan. Lain kali pasti kukabari lebih awal sebelum berangkat pulang.", "menyertakan janji perbaikan konkret membuat permintaan maaf ke keluarga jauh lebih menenangkan"),
    ("mengapresiasi pasangan atau sahabat yang sabar mendengarkan curhat", "Makasih ya sudah sabar dengerin ceritaku panjang lebar tanpa menghakimi tadi, kepalaku rasanya jauh lebih enteng sekarang berkat ditemani ngobrol.", "memberi tahu bahwa kehadirannya berdampak positif mempererat ikatan saling percaya"),
    ("memberi selamat teman yang berhasil membuka usaha kecil sendiri", "Selamat atas pembukaan usaha barunya! Semoga pelanggannya ramai lancar, berkah hasilnya, dan terus berkembang pelan-pelan tapi pasti.", "dukungan kata-kata positif di langkah awal wirausaha memberi suntikan keberanian yang besar"),
    ("menyapa kawan lama yang bertahun-tahun tidak bertemu", "Halo, lama banget nggak bersua! Tadi kebetulan lewat tempat yang mengingatkan masa sekolah dulu, semoga kabarmu dan keluarga sehat lancar selalu ya.", "menyebutkan kenangan kecil yang memicu ingatan membuat sapaan terasa tulus tanpa maksud tersembunyi"),
    ("mengucapkan terima kasih ke petugas kurir di cuaca hujan", "Terima kasih banyak ya Pak sudah mengantar paketnya sampai aman meski cuaca sedang hujan, hati-hati di jalan dan semoga sehat selalu.", "satu kalimat ramah ke pekerja lapangan sering menjadi penyemangat hangat di tengah lelah mereka"),
    ("memberi semangat rekan satu tim sehabis proyek padat selesai", "Terima kasih kerja kerasnya seminggu penuh ini teman-teman! Kerja sama kalian luar biasa rapi, selamat beristirahat akhir pekan dengan tenang.", "menutup pekan berat dengan apresiasi bersama membuat kekompakan tim makin solid"),
    ("ucapan selamat tahun baru yang reflektif dan hangat", "Selamat menyambut tahun yang baru! Semoga hal-hal berat tahun lalu jadi pelajaran penguat, dan tahun ini membawa kesehatan serta langkah yang lebih lapang.", "harapan yang membumi terasa lebih mengena daripada slogan muluk-muluk"),
    ("menyemangati teman yang sedang mulai belajar hidup sehat", "Salut banget lihat konsistensimu mulai rutin gerak dan jaga makan bulan ini! Pelan-pelan aja nikmati prosesnya, badan segar pasti berasa hasilnya.", "dukungan pada proses kebiasaan barunya bikin teman makin termotivasi menjaga konsistensi"),
]

MOMENT_NUANCES = [
    ("lewat pesan singkat WhatsApp yang nggak kaku", "Kirim di jam yang wajar supaya ia bisa membacanya dengan tenang tanpa terburu-buru."),
    ("ditulis di kartu kecil pendamping bingkisan", "Tulisan tangan langsung di kertas kecil selalu memberi kesan hangat yang awet disimpan."),
    ("disampaikan langsung waktu ketemu sebentar", "Ucapkan sambil tersenyum tulus dengan kontak mata hangat, nggak perlu dihafal kata per katanya."),
    ("buat orang yang karakternya kalem nggak suka kalimat lebay", "Gaya bahasa sederhana yang jujur kayak gini paling pas buat orang yang kurang nyaman dipuji berlebihan."),
    ("supaya terasa personal dan nggak kelihatan hasil salin-tempel", "Kamu tinggal menyelipkan satu nama panggilan akrabnya di awal kalimat biar makin terasa dekat."),
    ("waktu aku bingung merangkai kata pembukanya", "Kalimat pembuka yang langsung menyebut momennya bikin pesanmu mengalir alami sejak baris pertama."),
    ("dengan kalimat ringkas padat tapi tetap sopan", "Panjang dua kalimat begini ideal banget: cukup hangat namun tetap nyaman dibaca sekali lihat."),
    ("buat dikirim di grup bersama tanpa terkesan kaku", "Di ruang grup, nada hangat yang sopan seperti ini membuat anggota lain nyaman ikut menyambung doa baik."),
    ("waktu baru dengar kabarnya sore ini juga", "Merespons kabar baik atau duka segera dengan kalimat tulus menunjukkan perhatian yang peka."),
    ("agar hubungan silaturahmi tetap terjaga hangat", "Perhatian kecil di momen penting seperti inilah yang merawat kedekatan bertahun-tahun."),
    ("tanpa menyinggung hal sensitif yang bikin canggung", "Fokus murni pada doa kesehatan dan kebaikan ke depan adalah pilihan paling aman sekaligus menyejukkan."),
    ("meskipun kami jarang mengobrol panjang sehari-hari", "Justru untuk teman yang jarang mengobrol harian, pesan tulus singkat begini langsung menyambung keakraban."),
]


# 2. Menghadapi Kejadian Apes / Salah Kecil Harian Tanpa Panik (24 x 12 x 7 = 2.016)
MISHAP_CASES = [
    ("salah kirim pesan curhat atau stiker ke grup resmi", "segera gunakan fitur hapus untuk semua orang bila masih dalam batas waktu, lalu kirim permohonan maaf satu kalimat singkat yang sopan tanpa panik panjang", "meminta maaf lugas satu baris membuat anggota grup cepat maklum dan melupakannya dalam lima menit"),
    ("baru sadar dompet tertinggal di rumah waktu sudah dekat lokasi", "cek ketersediaan saldo pembayaran QRIS atau dompet digital di HP untuk kebutuhan darurat hari itu dan pinjam ongkos tunai kecil pada teman dekat yang langsung diganti transfer", "menyimpan selembar uang cadangan Rp50.000 terlipat di balik pelindung HP sangat menolong di kejadian seperti ini"),
    ("terlambat bangun pagi padahal tiga puluh menit lagi harus berangkat", "cuci muka-sikat gigi cepat, kenakan pakaian paling rapi yang siap pakai, bawa roti atau pisang untuk dimakan di jalan, dan kabari pihak tujuan secara jujur", "kejujuran mengabari keterlambatan lebih awal jauh lebih dihargai daripada menghilang tanpa kabar sepanjang jalan"),
    ("baju ketumpahan kuah makanan tepat sebelum acara dimulai", "tepuk sisa kuah dengan tisu basah lalu tisu kering dari tepi luar ke tengah noda agar tidak melebar, dan tutupi sementara dengan jaket atau kardigan rapi bila perlu", "menggosok keras noda berminyak dengan tisu kering justru mendorong warna kuah masuk makin dalam ke benang"),
    ("ketinggalan jadwal keberangkatan bus atau kereta tipis beberapa menit", "segera menuju loket layanan pelanggan di stasiun/terminal untuk menanyakan opsi jadwal berikutnya yang paling dekat sambil mengatur ulang kabar penjemputan", "tetap berbicara sopan dan tenang ke petugas loket sering memudahkan mereka mencarikan solusi rute alternatif terbaik"),
    ("salah turun di halte atau stasiun pemberhentian sebelumnya", "berdiri dulu di area aman peron untuk mengecek peta jalur arah lanjutannya sebelum keluar gerbang tiket agar tidak terkena potong tarif dua kali", "bertanya langsung ke petugas peron berseragam jauh lebih cepat dan akurat daripada bingung memutar sendiri"),
    ("masakan di wajan bagian bawahnya mulai tercium agak gosong", "matikan api seketika dan pindahkan lapisan atas masakan yang belum terkena dasar hitam ke wadah bersih tanpa mengeruk kerak pahit di dasar wajan", "mengaduk rata kerak bawah justru menyebarkan rasa pahit hangus ke seluruh bagian makanan yang masih bagus"),
    ("dokumen yang sedang diketik tiba-tiba tertutup karena listrik padam", "saat menyala kembali, buka menu pemulihan dokumen otomatis (autorecover) di aplikasi pengolah kata sebelum membuat file baru yang menimpa cache sementara", "biasakan menekan pintasan simpan (`Ctrl+S`) setiap selesai satu paragraf atau aktifkan simpan otomatis awan"),
    ("lupa hari ulang tahun sahabat dekat yang jatuh kemarin", "sapa hari ini juga dengan mengakui jujur kealpaanmu sambil memberikan doa tulus dan ajakan traktir minum ringan saat bertemu nanti", "mengucapkan terlambat sehari dengan tulus jauh lebih baik daripada diam berpura-pura tidak tahu sama sekali"),
    ("salah membeli ukuran barang di toko dan struknya masih tersimpan", "jaga label merek tetap utuh menempel di barang, lipat rapi kembali ke kemasannya, dan datangi kasir layanan pelanggan segera dalam batas hari penukaran", "barang yang masih bersih berlabel lengkap beserta struk asli umumnya mudah ditukar ukuran"),
    ("gelas kaca tidak sengaja pecah jatuh di lantai keramik rumah", "minta orang sekitar memakai alas kaki dulu, pungut pecahan besar memakai karton tebal, lalu tempelkan lakban lebar atau roti tawar lembap untuk mengangkat serpihan kaca halusnya", "bungkus pecahan kaca dengan kertas berlapis tebal dan tulis peringatan jelas sebelum masuk tempat sampah"),
    ("air galon atau botol tumpah membasahi buku catatan meja", "segera angkat buku, selipkan lembaran tisu kering bersih di sela tiap beberapa halaman yang basah, lalu angin-anginkan berdiri mekar di depan kipas angin", "menjemur buku basah langsung di bawah matahari terik membuat kertasnya melengkung kaku bergelombang"),
    ("kunci resleting tas mendadak macet tersangkut kain pelapis dalam", "tarik perlahan kain yang terjepit menjauh dari gigi resleting sambil menggerakkan kepala resleting mundur sedikit, jangan dipaksa tarik maju sekuat tenaga", "menggosok sedikit ujung pensil grafit pada gigi resleting yang seret membantu peluncurannya kembali licin"),
    ("salah menyebut tanggal janji ketemu ke dua teman berbeda", "segera hubungi pihak yang jadwalnya masih paling fleksibel digeser hari ini juga sambil meminta maaf jelas dan menawarkan dua waktu pengganti", "membereskan bentrok jadwal sedini mungkin jauh lebih sopan daripada membatalkan mendadak satu jam sebelum acara"),
    ("baterai HP tinggal lima persen padahal masih di perjalanan pulang", "matikan data latar belakang, turunkan kecerahan layar ke titik terendah, nyalakan penghemat baterai ekstrem, dan kirim satu pesan kabar posisi terakhirmu ke orang rumah", "satu pesan posisi dan perkiraan sampai membuat orang rumah tenang seandainya HP-mu benar-benar mati di jalan"),
    ("payung tertinggal di kendaraan umum atau tempat makan tadi", "hubungi layanan barang tertinggal operator transportasi atau telepon tempat makan tersebut dengan menyebutkan ciri warna payung, jam duduk, dan nomor kursi", "melapor di hari yang sama meningkatkan peluang barang masih diamankan petugas kebersihan"),
]

MISHAP_CTX = [
    ("sampai jantungku deg-degan kaget barusan", "Tarik napas panjang tiga kali dulu ya—panik cuma menguras tenaga, padahal masalahnya masih sangat bisa dibereskan."),
    ("pas lagi di tempat umum sendirian", "Tenang, kejadian manusiawi begini pernah dialami hampir semua orang kok, nggak perlu merasa malu berlebihan."),
    ("waktu hari ini sebenarnya sudah padat urusan lain", "Bereskan langkah penyelamatan utamanya dalam lima menit supaya sisa agendamu hari ini nggak ikut berantakan."),
    ("gara-gara tadi pikiranku lagi terburu-buru", "Jadikan pengingat lembut buat melambatkan gerak sedikit besok-besok, nggak perlu memarahi diri sendiri terus."),
    ("dan aku takut orang lain jadi kesal sama aku", "Selama kamu bersikap jujur, sopan, dan sigap bertanggung jawab, orang sekitar umumnya jauh lebih pengertian dari bayanganmu."),
    ("supaya nggak makin parah kerusakannya sekarang", "Tindakan tenang di dua menit pertama adalah kunci mencegah masalah kecil merembet jadi repot besar."),
    ("padahal aku biasanya orang yang cukup teliti", "Secermat apa pun manusia, sesekali meleset saat lelah itu wajar banget terjadi."),
    ("biar ke depannya aku punya antisipasi yang lebih rapi", "Begitu urusan hari ini selesai, satu kebiasaan pencegahan kecil bakal bikin kamu jauh lebih siap."),
    ("tanpa mengeluarkan biaya ganti yang besar", "Penanganan cepat yang tepat sering kali menyelamatkan barang atau situasi tanpa perlu keluar uang banyak."),
    ("waktu cuaca di luar juga lagi kurang mendukung", "Utamakan keselamatan dan ketenangan dirimu dulu sebelum memikirkan hal-hal kecil lainnya."),
]


# 3. Belajar Mandiri Keterampilan Praktis & Etika Ruang Publik (2 blok)
SELF_SKILLS = [
    ("belajar berenang dari nol saat usia sudah dewasa", "mulai di kolam dangkal sebatas dada untuk membiasakan buang napas gelembung lewat hidung di dalam air dan belajar mengapung telentang dengan rileks", "rasa tegang kaku justru membuat kaki tenggelam, sedangkan tubuh yang rileks berisi udara di paru-paru mudah terangkat air"),
    ("belajar berbicara tenang di depan kamera HP buat presentasi", "tempelkan kertas poin kecil tepat di samping lubang lensa kamera (bukan melihat layar wajah sendiri) dan anggap sedang bercerita ke satu sahabat akrab", "menatap lensa langsung membuat penonton merasa diajak mengobrol tatap mata dengan hangat"),
    ("belajar memasak nasi dan tiga lauk dasar sebelum merantau", "kuasai takaran air memasak nasi, cara menumis bawang sampai harum tidak gosong, merebus sayur tetap hijau, serta menggoreng telur-tempe dengan api sedang", "empat teknik dasar itu sudah bisa dikombinasikan menjadi belasan menu harian yang sehat dan hemat"),
    ("belajar membaca peta arah mata angin saat di kota baru", "cocokkan patokan gedung besar atau perempatan terdekat di sekitarmu dengan arah hadap panah kompas di peta sebelum mulai melangkah", "berhenti sebentar di tepi trotoar yang aman saat mengecek peta jauh lebih selamat daripada berjalan sambil menunduk ke layar"),
    ("belajar menjahit tangan sederhana untuk celana atau kancing lepas", "pelajari tusuk jelujur dan tusuk balik rapat dari sisi bagian dalam kain memakai warna benang yang paling mendekati warna pakaian", "jahitan kecil yang rapat dari sisi dalam sudah cukup kuat menahan tarikan aktivitas harian"),
    ("belajar mengatur nada bicara supaya terdengar jelas dan tidak menggumam", "buka artikulasi mulut sedikit lebih jelas pada huruf vokal dan beri jeda titik sejenak di ujung kalimat daripada berbicara cepat tanpa napas", "kejelasan pengucapan dan tempo sedang membuat lawan bicara langsung paham tanpa meminta ulang"),
    ("belajar memilah sampah rumah tangga menjadi organik dan anorganik", "sediakan dua tempat terpisah: satu untuk sisa kupasan dapur yang cepat membusuk, dan satu kering untuk botol plastik, kardus, atau kaleng bersih", "memisahkan sampah basah menjaga kardus dan botol plastik tetap bersih sehingga mudah didaur ulang pengepul"),
    ("belajar menjaga etika nyaman saat naik angkutan umum bersama", "gunakan earphone saat memutar video atau musik di HP, turunkan tas ransel dari punggung saat berdiri rapat, dan dahulukan penumpang turun sebelum masuk", "kebiasaan kecil menghargai ruang gerak bersama membuat perjalanan padat terasa jauh lebih manusiawi"),
    ("belajar antre dan merapikan bekas makan sendiri di tempat umum", "tumpuk piring-gelas kotor dengan rapi di nampan, kumpulkan tisu bekas di satu titik, dan seka remah mencolok agar meja siap dipakai pengunjung berikutnya", "meninggalkan meja dalam keadaan bersih menunjukkan kepedulian berkelas terhadap petugas maupun sesama pengunjung"),
    ("belajar mendengarkan pendapat orang yang berbeda latar belakang", "tahan dorongan menyela di tiga puluh detik pertama dan ajukan pertanyaan ingin tahu 'apa yang membuatmu melihatnya dari sisi itu?'", "rasa ingin tahu yang tulus sering membuka wawasan baru sekaligus meredam prasangka yang tidak perlu"),
    ("belajar menawar atau bertransaksi jujur dengan pedagang kecil", "bayar dengan uang pas bila memungkinkan, ucapkan terima kasih dengan senyum hormat, dan hindari menawar berlebihan pada pedagang lanjut usia keliling", "keuntungan beberapa ribu rupiah bagi pedagang kecil sangat berarti untuk belanja dapur keluarga mereka hari itu"),
    ("belajar menjaga ketenangan lingkungan tempat tinggal di malam hari", "kecilkan suara televisi atau obrolan teras lewat pukul sembilan malam, tutup pintu pagar perlahan, dan kondisikan suara knalpot kendaraan tetap standar", "ketenangan malam hari membantu tetangga yang sedang sakit, bayi, maupun pekerja pagi beristirahat layak"),
]

SKILL_CTX = [
    ("walaupun awalnya terasa agak kikuk waktu dicoba pertama kali", "Rasa kikuk di percobaan pertama itu tanda kamu sedang tumbuh mempelajari kebiasaan baru—lanjutkan aja!"),
    ("supaya jadi bekal berharga buat ke depannya", "Keterampilan dan sikap baik sehari-hari seperti ini nilainya bertahan seumur hidup ke mana pun kamu pergi."),
    ("dengan latihan ringan di sela aktivitas harian", "Nggak butuh waktu khusus berjam-jam, cukup diselipkan sadar dalam kegiatan harianmu."),
    ("bareng teman atau adik biar sama-sama belajar", "Berlatih bareng bikin prosesnya terasa seru dan bisa saling mengingatkan dengan santai."),
    ("tanpa merasa malu dilihat orang sekitar", "Orang yang mau belajar dari dasar dan peduli sekitar justru layak banget dihargai, nggak ada yang memalukan sama sekali."),
    ("mulai dari langkah paling kecil minggu ini", "Fokus pada satu langkah dasar sampai lancar dulu sebelum menambah variasi lainnya."),
    ("agar hidup sehari-hari terasa lebih mandiri dan tenang", "Makin banyak hal dasar yang sanggup kamu tangani sendiri, makin tinggi rasa percaya dirimu."),
    ("sebagai kebiasaan positif yang konsisten", "Konsistensi di hal-hal sederhana selalu melahirkan dampak besar setelah berjalan beberapa bulan."),
]


def build_chat_topics_extra(col: CategoryCollector, limit: int | None = None) -> None:
    pair_idx = 0

    # 1. Ucapan & apresiasi momen harian (24 * 12 * 7 = 2.016)
    gm_q = [
        "nara, bantuin rangkai kalimat ucapan untuk {mom} {nua} dong",
        "gimana contoh kata-kata hangat buat {mom} {nua}?",
        "tolong bikinin ucapan tulus untuk momen {mom} {nua}",
        "bingung mau ngucapin apa pas {mom} {nua}, kasih ide ya",
        "eh nara, susunin pesan singkat buat {mom} {nua} dong",
        "contoh kalimat yang enak dibaca untuk {mom} {nua} gimana?",
        "kasih inspirasi ucapan {mom} {nua} yang natural dong",
    ]
    gm_a = [
        "Ini contoh kalimat hangat yang bisa kamu pakai: \"{msg}\" {nua_note} Kuncinya, {why}.",
        "Kamu bisa menyampaikan ucapan seperti ini: \"{msg}\" {nua_note} Soalnya, {why}.",
        "Coba rangkaian kalimat tulus berikut: \"{msg}\" {nua_note} Perlu diingat, {why}.",
        "Kalimat ini pas banget buat suasananya: \"{msg}\" {nua_note} Alasannya sederhana, {why}.",
        "Biar terasa hangat dan berkesan, tulis begini: \"{msg}\" {nua_note} Sebab, {why}.",
        "Kurang lebih kamu bisa merangkainya seperti ini: \"{msg}\" {nua_note} Tambahan kecil: {why}.",
        "Pilihan kata yang mengalir alami contohnya begini: \"{msg}\" {nua_note} Ingat ya, {why}.",
    ]
    for mom, msg, why in GREETING_MOMENTS:
        for nua, nua_note in MOMENT_NUANCES:
            pair_idx += 1
            for k in range(len(gm_q)):
                if limit and len(col.rows) >= limit:
                    return
                q = gm_q[k].format(mom=mom, nua=nua)
                a = gm_a[(k + pair_idx) % len(gm_a)].format(
                    msg=msg, why=why, nua_note=nua_note
                )
                col.add(q, a)

    # 2. Kejadian apes / salah kecil harian (16 * 10 * 7 = 1.120)
    ms_q = [
        "nara tolong, barusan aku {case} {ctx}, harus gimana nih?",
        "gimana langkah tenang kalau mendadak {case} {ctx}?",
        "aduh apes banget, aku {case} {ctx}, solusinya apa ya?",
        "eh nara, kalau kejadian {case} {ctx}, enaknya ngapain dulu?",
        "kasih pertolongan saran praktis dong: {case} {ctx}",
        "cara mengatasi situasi {case} {ctx} biar cepat beres gimana?",
        "aku baru aja {case} {ctx}, bantu langkah cerdasnya dong",
    ]
    ms_a = [
        "Tenang dulu ya, jangan panik! Langkah penyelamatannya: {how}. {ctx_note} Tips ke depannya, {why}.",
        "Bisa diatasi kok! Pertama-tama langsung {how}. {ctx_note} Sekadar catatan berguna, {why}.",
        "Tarik napas sebentar lalu lakukan ini: {how}. {ctx_note} Perlu diingat juga bahwa {why}.",
        "Solusi paling sigap di posisi itu adalah {how}. {ctx_note} Soalnya, {why}.",
        "Nggak apa-apa, fokus ke jalan keluarnya dulu: {how}. {ctx_note} Selain itu, {why}.",
        "Langkah praktis yang paling aman sekarang: {how}. {ctx_note} Sebab dalam keseharian, {why}.",
        "Langsung tangani dengan tenang seperti ini: {how}. {ctx_note} Ingat patokan ini ya: {why}.",
    ]
    for case, how, why in MISHAP_CASES:
        for ctx, ctx_note in MISHAP_CTX:
            pair_idx += 1
            for k in range(len(ms_q)):
                if limit and len(col.rows) >= limit:
                    return
                q = ms_q[k].format(case=case, ctx=ctx)
                a = ms_a[(k + pair_idx) % len(ms_a)].format(
                    how=how, why=why, ctx_note=ctx_note
                )
                col.add(q, a)

    # 3. Keterampilan mandiri & etika ruang publik (12 * 8 * 7 = 672)
    sk_q = [
        "nara, gimana cara mulai {skill} {ctx}?",
        "kasih panduan gampang buat {skill} {ctx} dong",
        "tips praktis untuk {skill} {ctx} apa ya?",
        "eh nara, ajarin langkah dasar {skill} {ctx} dong",
        "kenapa penting membiasakan {skill} {ctx} dan gimana caranya?",
        "biar luwes {skill} {ctx}, perhatiin apa aja?",
        "tolong bantu saran santai soal {skill} {ctx}",
    ]
    sk_a = [
        "Bagus banget niatnya! Kamu bisa mulai dengan {how}. {ctx_note} Soalnya, {why}.",
        "Langkah dasarnya sederhana kok: {how}. {ctx_note} Perlu diingat bahwa {why}.",
        "Coba praktikkan pelan-pelan cara ini: {how}. {ctx_note} Alasannya jelas, {why}.",
        "Tips paling nyaman buat memulainya adalah {how}. {ctx_note} Sebab, {why}.",
        "Kamu cukup menerapkan kebiasaan ini: {how}. {ctx_note} Kuncinya, {why}.",
        "Mulai aja dari hal konkret berikut: {how}. {ctx_note} Selain itu, {why}.",
        "Panduan ringkas dariku: {how}. {ctx_note} Kenapa berdampak besar? Karena {why}.",
    ]
    for skill, how, why in SELF_SKILLS:
        for ctx, ctx_note in SKILL_CTX:
            pair_idx += 1
            for k in range(len(sk_q)):
                if limit and len(col.rows) >= limit:
                    return
                q = sk_q[k].format(skill=skill, ctx=ctx)
                a = sk_a[(k + pair_idx) % len(sk_a)].format(
                    how=how, why=why, ctx_note=ctx_note
                )
                col.add(q, a)
