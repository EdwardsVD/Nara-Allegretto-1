"""Bagian 3 generator `chat.jsonl`:
- Merangkai pesan singkat/chat sopan & santai (tanpa kata kaku saya/Anda)
- Dinamika pertemanan, keluarga, tetangga, dan kerja sama tim
- Ucapan selamat, permohonan maaf, penolakan ajakan secara halus, dan etika sosial
"""
from __future__ import annotations

from .core_v2 import CategoryCollector

# --------------------------------------------------------------------------- #
# 1. Bantu Bikin Draf Chat ke Teman / Keluarga / Pengajar / Rekan
# --------------------------------------------------------------------------- #
PEER_RECIPIENTS = [
    ("sahabat dekat", "gaya akrab tapi tetap tulus", "Eh {call}, "),
    ("teman satu kelompok tugas", "nada kooperatif dan jelas", "Halo teman-teman, "),
    ("kakak kandung", "santai khas keluarga tapi sopan", "Kak, "),
    ("adik di rumah", "hangat dan nggak menggurui", "Dek, "),
    ("teman kos sebelah kamar", "ramah dan menjaga kenyamanan bersama", "Halo Kak, "),
    ("teman lama yang jarang kontak", "hangat tanpa kesan canggung", "Hai! Apa kabar? "),
    ("rekan satu tim kerja", "ringkas, jelas, dan menghargai waktu", "Halo Kak, "),
    ("sepupu sebaya", "akrab dan santai", "Eh, "),
    ("ketua panitia acara", "jelas menyampaikan kondisi dan solusi", "Halo Kak, izin mengabarkan ya—"),
    ("teman hobi atau komunitas", "santai dan bersahabat", "Halo! "),
]

PEER_INTENTS = [
    (
        "minta maaf karena kelupaan balas chat dari kemarin",
        "{greet}maaf banget ya baru sempat balas pesanmu sekarang, kemarin urusanku padat banget sampai kelupaan buka chat. Tadi kamu mau bahas soal apa?",
        "mengakui jujur tanpa mengarang alasan panjang biasanya jauh lebih dihargai",
    ),
    (
        "menolak ajakan nongkrong akhir pekan karena lagi berhemat",
        "{greet}makasih banget sudah diajak main akhir pekan ini! Tapi kali ini aku absen dulu ya soalnya lagi ngerem pengeluaran bulan ini, kapan-kapan kita atur jadwal lagi.",
        "menolak dengan jujur sambil tetap mengapresiasi ajakannya bikin teman nggak merasa dijauhi",
    ),
    (
        "mengabarkan bakal datang telat 15 menit karena terjebak hujan",
        "{greet}aku lagi di jalan tapi ketahan hujan deras nih, kemungkinan telat sekitar 15 menit ya. Kalau mau mulai duluan silakan banget!",
        "memberi estimasi waktu yang jelas jauh lebih menenangkan daripada bilang 'sebentar lagi sampai' padahal masih jauh",
    ),
    (
        "mengingatkan uang patungan makan kemarin secara halus",
        "{greet}sekalian ngingetin catatan patungan makan kita kemarin ya, bagianmu Rp35.000 bisa ditransfer santai pas kamu sempat. Makasih sebelumnya!",
        "menyebut nominal langsung dengan nada ringan justru mengurangi rasa sungkan di kedua belah pihak",
    ),
    (
        "menolak meminjamkan uang karena anggaran sendiri sedang pas-pasan",
        "{greet}maaf banget ya, untuk sekarang aku belum bisa bantu pinjami dulu karena anggaranku bulan ini juga lagi ngepas buat kebutuhan wajib. Semoga urusanmu lekas ketemu jalan keluarnya ya.",
        "kamu berhak menjaga batas keuangan sendiri tanpa perlu merasa bersalah berlebihan",
    ),
    (
        "mengajak berbaikan setelah sempat beda pendapat kemarin",
        "{greet}soal obrolan kita kemarin, maaf ya kalau nada bicaraku sempat kurang enak didengar. Aku tetap menghargai pendapatmu dan pengen hubungan kita tetap adem.",
        "membuka pintu damai lebih dulu menunjukkan kedewasaan, bukan tanda kalah",
    ),
    (
        "menanyakan kabar dan progres bagian tugas bersama",
        "{greet}gimana kabarmu hari ini? Sekalian mau tanya progres bagian slide yang kamu pegang, kira-kira ada kendala yang bisa kubantu bareng nggak?",
        "menawarkan bantuan terasa jauh lebih enak daripada terkesan menodong tagihan tugas",
    ),
    (
        "mengucapkan selamat ulang tahun yang hangat dan nggak berlebihan",
        "{greet}selamat ulang tahun ya! Semoga sehat terus, hati selalu tenang, dan rencana baik yang lagi kamu kejar tahun ini dimudahkan jalannya.",
        "doa yang spesifik dan hangat selalu terasa lebih tulus daripada salinan teks panjang",
    ),
    (
        "mengucapkan selamat karena baru diterima kerja atau magang",
        "{greet}wah selamat ya atas tempat kerja barunya! Kerja kerasmu selama ini terbayar juga, semoga betah dan lancar adaptasinya di sana.",
        "ikut merayakan kabar baik teman akan mempererat rasa saling dukung",
    ),
    (
        "menolak ajakan telepon malam-malam karena sudah mengantuk berat",
        "{greet}maaf ya malam ini mataku sudah berat banget karena besok harus bangun pagi. Boleh kita sambung ngobrolnya besok sore aja?",
        "menawarkan waktu pengganti membuat penolakan terasa tetap hangat",
    ),
    (
        "meminta tolong titip belikan makanan kalau searah jalan pulang",
        "{greet}kalau nanti searah jalan pulang dan nggak merepotkan, boleh titip belikan nasi bungkus satu ya? Uangnya langsung kutransfer sekarang, tapi kalau lagi buru-buru nggak apa-apa banget kok!",
        "memberi ruang bagi orang lain untuk menolak dengan nyaman adalah kunci minta tolong yang sopan",
    ),
    (
        "mengucapkan lekas sembuh waktu dengar dia lagi sakit",
        "{greet}dengar kabar kamu lagi kurang enak badan ya? Istirahat penuh dulu aja nggak usah mikirin kerjaan, semoga cepat pulih dan segar kembali ya!",
        "pesan singkat yang tidak menuntut balasan sangat membantu orang yang sedang beristirahat sakit",
    ),
    (
        "membatalkan janji ketemu karena mendadak kurang enak badan",
        "{greet}maaf banget mendadak harus ngabarin kalau hari ini badanku meriang, jadi belum berani ketemu dulu takut menular. Kita jadwal ulang minggu depan pas sudah fit ya?",
        "mengabari sedini mungkin memberi waktu lawan bicara mengatur ulang rencananya",
    ),
    (
        "mengingatkan suara musik kamar sebelah agak terdengar sampai malam",
        "{greet}maaf mengganggu malam-malam, boleh minta tolong dikecilkan sedikit volume musiknya karena kebetulan besok pagi ada ujian? Terima kasih banyak pengertiannya ya!",
        "menyampaikan alasan dengan sopan biasanya membuat tetangga langsung mengerti tanpa tersinggung",
    ),
]

CHAT_DRAFT_Q = [
    "nara, bantuin rangkai chat ke {rec} buat {intent} dong",
    "gimana kalimat sopan tapi santai ke {rec} kalau mau {intent}?",
    "tolong bikinin contoh pesan singkat ke {rec} untuk {intent}",
    "bingung mau ngetik apa ke {rec} pas mau {intent}, kasih ide dong",
    "contoh kata-kata chat yang enak dibaca {rec} buat {intent} gimana ya?",
    "eh nara, ajarin cara ngomong lewat chat ke {rec} untuk {intent}",
]

CHAT_DRAFT_A = [
    " Untuk {rec}, gunakan {tone}. Kamu bisa kirim kalimat seperti ini: \"{draft}\" Kuncinya, {tip}.",
    "Kamu bisa pakai pendekatan dengan {tone} ke {rec}: \"{draft}\" Biasanya cara ini efektif karena {tip}.",
    "Coba draf pesan yang mengalir dengan {tone} ini buat {rec}: \"{draft}\" Ingat ya, {tip}.",
    "Biar pesannya enak diterima {rec}, pakai {tone}: \"{draft}\" Alasannya sederhana, {tip}.",
    "Ini contoh kalimat yang pas dengan {tone} untuk {rec}: \"{draft}\" Tambahan kecil dariku: {tip}.",
    "Kalau ngobrol lewat chat sama {rec}, cocok banget pakai {tone}: \"{draft}\" Soalnya {tip}.",
]


# --------------------------------------------------------------------------- #
# 2. Pesan Sopan ke Pihak Resmi / Layanan (Dosen, Guru, Admin Toko, Kurir, Kos)
#    (Tanpa memakai kata formal terlarang 'saya'/'Anda' agar 100% sesuai gaya Nara!)
# --------------------------------------------------------------------------- #
FORMAL_PARTIES = [
    ("dosen pembimbing", "Selamat pagi Pak/Bu, mohon maaf mengganggu waktunya. "),
    ("guru wali kelas", "Selamat pagi Bapak/Ibu Guru, mohon izin menyampaikan kabar. "),
    ("admin toko online", "Halo Kak Admin, permisi mau konfirmasi pesanan. "),
    ("kurir pengantar paket", "Selamat siang Pak Kurir, terima kasih sudah mengantar paketnya. "),
    ("pemilik kos", "Selamat sore Pak/Bu Kos, mohon izin mengabarkan kondisi kamar. "),
    ("petugas perpustakaan", "Selamat pagi Kak, mohon izin bertanya terkait peminjaman buku. "),
    ("panitia pendaftaran lomba", "Halo Kak Panitia, permisi izin menanyakan informasi teknis. "),
    ("klinik pendaftaran", "Selamat pagi Kak, mohon info jadwal praktik hari ini. "),
]

FORMAL_TOPICS = [
    ("menanyakan ketersediaan jadwal bimbingan atau konsultasi minggu ini", "Izin menanyakan apakah pada hari Kamis atau Jumat minggu ini tersedia waktu luang untuk sesi konsultasi singkat? Terima kasih banyak sebelumnya.", "sebutkan opsi hari secara spesifik supaya penerima mudah mencocokkan jadwalnya"),
    ("mengabarkan ada kendala teknis pada barang atau fasilitas", "Terdapat kendala pada barang yang baru diterima pagi ini, berikut dilampirkan foto kondisinya. Mohon arahan langkah penanganannya ya, terima kasih.", "lampirkan bukti jelas tanpa nada marah agar proses solusi berjalan cepat"),
    ("meminta izin titip paket di teras atau pos depan karena sedang di luar", "Kebetulan penghuni rumah sedang di luar sampai sore, paketnya boleh ditaruh di rak teras dekat pintu pagar saja ya. Terima kasih banyak bantuannya!", "instruksi titik taruh yang jelas sangat memudahkan pengantar di lapangan"),
    ("mengonfirmasi pembayaran iuran atau pesanan yang sudah dikirim", "Berikut dilampirkan bukti pembayaran untuk bulan ini ya. Mohon dicek saat senggang, terima kasih banyak.", "menyertakan keterangan waktu dan bukti langsung mempercepat pengecekan administrasi"),
    ("memohon perpanjangan waktu pengumpulan karena kendala kesehatan", "Sehubungan kondisi kesehatan yang sedang demam sejak semalam, mohon izin menanyakan apakah dimungkinkan kelonggaran waktu pengumpulan hingga besok siang? Terima kasih atas pengertiannya.", "sampaikan permohonan sebelum batas waktu habis, bukan sesudah lewat tenggat"),
    ("menanyakan tindak lanjut berkas yang dikirim minggu lalu", "Izin menanyakan perkembangan berkas yang telah dikirimkan pada pekan lalu, apakah ada dokumen tambahan yang perlu dilengkapi kembali? Terima kasih.", "bertanya dengan menawarkan kelengkapan berkas terdengar proaktif dan sopan"),
]


# --------------------------------------------------------------------------- #
# 3. Situasi Pergaulan & Etika Sosial Sehari-hari (18 situasi x 14 sudut kondisi x 6 gaya)
# --------------------------------------------------------------------------- #
SOCIAL_DILEMMAS = [
    ("teman sering curhat panjang tapi giliran kita cerita dia malah sibuk main HP", "sampaikan pelan-pelan bahwa kamu lagi butuh didengarkan lima menit saja sebelum lanjut ke topik lain", "hubungan pertemanan yang sehat butuh arus dengar dua arah, bukan satu pihak jadi tempat sampah emosi terus"),
    ("bingung cari bahan obrolan waktu duduk sebelahan sama kenalan baru", "angkat topik netral dari situasi sekitar seperti cuaca hari itu, makanan di acara tersebut, atau perjalanan menuju lokasi", "pertanyaan terbuka yang ringan jauh lebih mencairkan suasana daripada pertanyaan terlalu pribadi"),
    ("ada kerabat yang suka tanya urusan pribadi seperti kapan nikah atau berapa gaji", "jawab singkat dengan senyum ramah minta didoakan yang terbaik, lalu belokkan obrolan ke kabar kesehatan atau hobi beliau", "tidak semua pertanyaan basa-basi perlu dijawab dengan rincian angka atau debat panjang"),
    ("teman suka meminjam barang kecil tapi sering lupa mengembalikan", "biasakan mengingatkan sambil tersenyum sebelum berpisah atau catat ringan lewat pesan singkat supaya ada jejak pengingatnya", "menjaga barang milik sendiri dengan tegas bukan berarti kamu pelit pada teman"),
    ("diajak patungan kado mahal yang di luar kemampuan kantong bulan ini", "usulkan batas nominal patungan yang lebih terjangkau sejak awal diskusi grup sebelum barangnya terlanjur dibeli", "biasanya ada anggota grup lain yang sebenarnya juga merasa keberatan tapi sungkan bicara duluan"),
    ("merasa lelah sosial setelah seharian bertemu banyak orang di acara ramai", "ambil waktu tenang sendiri di kamar tanpa paksaan menghadiri acara lanjutan malam harinya", "mengisi ulang energi dalam keheningan itu kebutuhan wajar, bukan sifat antisosial"),
    ("teman meminta pendapat jujur soal karyanya yang masih punya beberapa kekurangan", "sebutkan dulu dua bagian spesifik yang sudah bagus, baru sampaikan satu saran perbaikan yang paling mudah dia terapkan", "kritik yang dibungkus apresiasi jujur jauh lebih mudah diterima tanpa mematahkan semangat"),
    ("salah memanggil nama orang yang baru dikenal beberapa menit lalu", "langsung minta maaf ringan tanpa drama berlebihan lalu ulangi namanya yang benar dalam kalimat berikutnya", "mengakui lupa nama dengan santai justru lebih sopan daripada terus menghindar memanggilnya"),
    ("grup chat terlalu berisik tengah malam padahal ada info penting di dalamnya", "bisukan notifikasi grupnya di pengaturan aplikasi lalu jadwalkan cek ringkasan pesan penting dua kali sehari saja", "kamu tetap bisa mengikuti informasi penting tanpa membiarkan dering pesan mengganggu jam tidur"),
    ("tamu atau teman main ke kamar kos terlalu larut padahal besok pagi ada jadwal", "beri sinyal sopan dengan merapikan meja dan bilang terus terang bahwa kamu harus istirahat sekarang karena bangun pagi besok", "teman yang baik pasti menghormati jam istirahat tuan rumah kalau disampaikan baik-baik"),
    ("melihat teman menyebarkan info heboh di grup yang belum jelas kebenarannya", "tanyakan sumber beritanya secara netral lewat jalur pribadi atau bagikan tautan klarifikasi resmi tanpa mempermalukannya di grup", "menegur di ruang pribadi menjaga harga diri teman sehingga ia tidak bersikap defensif"),
    ("bingung merespons pujian orang supaya nggak terkesan sombong tapi juga nggak merendahkan diri", "cukup tersenyum dan ucapkan terima kasih tulus sambil menyebut bagian proses yang memang menyenangkan saat dikerjakan", "menerima pujian dengan kata terima kasih sederhana jauh lebih hangat daripada menolak pujian terus-menerus"),
    ("berbeda selera tempat makan waktu jalan bareng rombongan teman", "usulkan pujasera atau area kuliner yang punya banyak pilihan kedai sehingga tiap orang bebas memesan sesuai seleranya", "mencari titik temu tempat makan beragam menyelamatkan waktu daripada berdebat di pinggir jalan"),
    ("orang tua sering khawatir berlebihan waktu kita pulang agak sore karena tugas", "kirim pesan singkat berisi lokasi dan perkiraan jam pulang sebelum beliau sempat bertanya duluan", "kabar singkat lebih awal membangun rasa percaya jauh lebih cepat daripada berdebat saat sampai rumah"),
    ("rekan satu tim punya gaya kerja mepet sedangkan kita suka mencicil dari jauh hari", "sepakati tenggat internal bersama dua hari sebelum batas resmi pengumpulan agar ada ruang periksa ulang yang aman", "tenggat antara menjadi jembatan paling adil bagi dua gaya kerja yang berbeda"),
    ("sungkan menolak tawaran tambah porsi makan saat bertamu padahal perut sudah kenyang", "puji rasa masakannya dengan tulus lalu sampaikan sopan bahwa porsi barusan sudah sangat mengenyangkan dan pas", "tuan rumah sebenarnya senang melihat masakannya disukai meski kamu tidak menambah porsi kedua"),
]

SOCIAL_CONTEXTS = [
    ("apalagi aku orangnya agak nggak enakan sejak dulu", "Belajar tegas pelan-pelan memang butuh latihan, mulai dari kalimat pendek yang sopan dulu aja."),
    ("dan aku nggak mau hubungan pertemanan kami jadi renggang", "Komunikasi jujur yang disampaikan hangat justru menjaga hubungan awet dalam jangka panjang."),
    ("waktu kejadiannya berulang lebih dari dua kali bulan ini", "Kalau polanya sudah berulang, memberi batasan jelas sekarang bakal mencegah rasa kesal menumpuk di belakang."),
    ("pas kondisi badanku sendiri lagi capek banget", "Saat energimu sedang tipis, menjaga batas diri jadi prioritas supaya emosimu nggak meledak tiba-tiba."),
    ("di lingkungan kampus atau sekolah sehari-hari", "Di lingkungan belajar, sikap sopan tapi punya prinsip bakal bikin teman-teman lebih menghargaimu."),
    ("di lingkungan kerja bareng rekan sekantor", "Dalam suasana kerja, kejelasan komunikasi justru membantu urusan profesional tetap rapi dan nyaman."),
    ("waktu lagi kumpul keluarga besar akhir pekan", "Di acara keluarga, kepala dingin dan senyum santai adalah kunci menjaga suasana tetap teduh."),
    ("tanpa bikin suasana tongkrongan jadi kaku", "Selipkan nada santai sewajarnya supaya pesanmu sampai tanpa membuat meja obrolan jadi tegang."),
    ("padahal niat awalnya cuma pengen bantu sebentar", "Niat baik tetap perlu pagar batasan agar kebaikanmu tidak berubah menjadi beban sepihak."),
    ("supaya ke depannya sama-sama enak dan jelas", "Kejelasan di awal memang sedikit kikuk lima detik, tapi menyelamatkan berhari-hari rasa mengganjal."),
    ("waktu kita baru kenal beberapa minggu", "Justru di masa awal kenal, kebiasaan saling menghargai batasan paling mudah dibentuk sejak dini."),
    ("pas lagi ngobrol lewat chat grup maupun japri", "Di pesan teks yang tidak ada intonasi suara, pilih kata yang lugas dan ramah agar tidak disalahartikan."),
]


def build_chat_social(col: CategoryCollector, limit: int | None = None) -> None:
    pair_idx = 0
    names_call = ["Budi", "Siti", "Raka", "Nadia", "Dewi", "Fajar", "Putri", "Dimas", "Ayu", "Reza"]

    # 1. Draf chat ke teman/keluarga (10 * 14 * 6 = 840)
    for rec_idx, (rec, tone, greet_raw) in enumerate(PEER_RECIPIENTS):
        for intent, draft_raw, tip in PEER_INTENTS:
            pair_idx += 1
            call_nm = names_call[(rec_idx + pair_idx) % len(names_call)]
            greet = greet_raw.format(call=call_nm)
            draft = draft_raw.format(greet=greet)
            for k in range(len(CHAT_DRAFT_Q)):
                if limit and len(col.rows) >= limit:
                    return
                q = CHAT_DRAFT_Q[k].format(rec=rec, intent=intent)
                a = CHAT_DRAFT_A[(k + pair_idx) % len(CHAT_DRAFT_A)].format(
                    rec=rec, tone=tone, draft=draft, tip=tip
                )
                col.add(q, a)

    # 2. Draf pesan sopan ke pihak resmi/layanan (8 * 6 * 5 = 240)
    f_q = [
        "nara, gimana contoh chat sopan ke {party} untuk {topic}?",
        "bantuin susun pesan ke {party} buat {topic} dong",
        "kalimat yang rapi kalau mau menghubungi {party} soal {topic} gimana?",
        "tolong kasih draf chat ke {party} untuk {topic}",
        "cara ngetik pesan sopan ke {party} waktu mau {topic} gimana ya?",
    ]
    f_a = [
        "Untuk menghubungi {party}, sampaikan salam pembuka lalu langsung ke intinya: \"{open}{body}\" Tipsnya, {tip}.",
        "Kamu bisa memakai susunan kalimat rapi seperti ini ke {party}: \"{open}{body}\" Ingat ya, {tip}.",
        "Ini contoh pesan yang sopan dan jelas buat {party}: \"{open}{body}\" Kuncinya, {tip}.",
        "Coba kirim pesan ringkas berikut ke {party}: \"{open}{body}\" Cara ini efektif sebab {tip}.",
        "Biar mudah dipahami oleh {party}, tulis seperti ini: \"{open}{body}\" Catatan kecil: {tip}.",
    ]
    for party, opener in FORMAL_PARTIES:
        for topic, body, tip in FORMAL_TOPICS:
            pair_idx += 1
            for k in range(len(f_q)):
                if limit and len(col.rows) >= limit:
                    return
                q = f_q[k].format(party=party, topic=topic)
                a = f_a[(k + pair_idx) % len(f_a)].format(
                    party=party, open=opener, body=body, tip=tip
                )
                col.add(q, a)

    # 3. Dilema pergaulan & etika sosial sehari-hari (16 * 12 * 6 = 1.152)
    sd_q = [
        "nara, gimana sikap yang pas kalau {sit} {ctx}?",
        "aku bingung deh, {sit} {ctx}, enaknya gimana ya?",
        "kasih saran dong nara: {sit} {ctx}",
        "menurutmu cara menghadapi situasi {sit} {ctx} gimana?",
        "eh nara, kalau {sit} {ctx}, langkah bijaknya apa?",
        "tolong bantu pendapat santai soal {sit} {ctx}",
    ]
    sd_a = [
        "Situasi kayak gitu memang sering bikin serba salah. Coba {act}. {ctx_note} Soalnya, {why}.",
        "Kalau ketemu kondisi begitu, langkah paling sehat adalah {act}. {ctx_note} Ingat bahwa {why}.",
        "Nggak perlu dibawa tegang, kamu cukup {act}. {ctx_note} Alasannya sederhana: {why}.",
        "Pendekatan paling enak di posisi itu adalah {act}. {ctx_note} Pegang prinsip ini ya: {why}.",
        "Coba atasi dengan cara yang tenang: {act}. {ctx_note} Sebab pada dasarnya, {why}.",
        "Saran dariku, mending kamu {act}. {ctx_note} Kenapa penting? Karena {why}.",
    ]
    for sit, act, why in SOCIAL_DILEMMAS:
        for ctx, ctx_note in SOCIAL_CONTEXTS:
            pair_idx += 1
            for k in range(len(sd_q)):
                if limit and len(col.rows) >= limit:
                    return
                q = sd_q[k].format(sit=sit, ctx=ctx)
                a = sd_a[(k + pair_idx) % len(sd_a)].format(
                    act=act, why=why, ctx_note=ctx_note
                )
                col.add(q, a)
