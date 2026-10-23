"""Pengetahuan umum: negara, provinsi, tempat terkenal, alam, dan budaya."""
from __future__ import annotations

from nara_core import Builder, fmt_id

COUNTRIES = [
    ("Indonesia", "Jakarta", "Asia", "Rupiah", "Bahasa Indonesia"),
    ("Malaysia", "Kuala Lumpur", "Asia", "Ringgit", "Bahasa Melayu"),
    ("Singapura", "Singapura", "Asia", "Dolar Singapura", "Bahasa Inggris, Melayu, Mandarin, dan Tamil"),
    ("Thailand", "Bangkok", "Asia", "Baht", "Bahasa Thai"),
    ("Vietnam", "Hanoi", "Asia", "Dong", "Bahasa Vietnam"),
    ("Filipina", "Manila", "Asia", "Peso Filipina", "Bahasa Filipino dan Inggris"),
    ("Myanmar", "Naypyidaw", "Asia", "Kyat", "Bahasa Burma"),
    ("Kamboja", "Phnom Penh", "Asia", "Riel", "Bahasa Khmer"),
    ("Laos", "Vientiane", "Asia", "Kip", "Bahasa Lao"),
    ("Brunei Darussalam", "Bandar Seri Begawan", "Asia", "Dolar Brunei", "Bahasa Melayu"),
    ("India", "New Delhi", "Asia", "Rupee India", "Bahasa Hindi dan Inggris"),
    ("Pakistan", "Islamabad", "Asia", "Rupee Pakistan", "Bahasa Urdu dan Inggris"),
    ("Bangladesh", "Dhaka", "Asia", "Taka", "Bahasa Bengali"),
    ("Nepal", "Kathmandu", "Asia", "Rupee Nepal", "Bahasa Nepal"),
    ("Sri Lanka", "Sri Jayawardenepura Kotte", "Asia", "Rupee Sri Lanka", "Bahasa Sinhala dan Tamil"),
    ("Tiongkok", "Beijing", "Asia", "Yuan", "Bahasa Mandarin"),
    ("Jepang", "Tokyo", "Asia", "Yen", "Bahasa Jepang"),
    ("Korea Selatan", "Seoul", "Asia", "Won", "Bahasa Korea"),
    ("Korea Utara", "Pyongyang", "Asia", "Won Korea Utara", "Bahasa Korea"),
    ("Mongolia", "Ulaanbaatar", "Asia", "Tugrik", "Bahasa Mongolia"),
    ("Arab Saudi", "Riyadh", "Asia", "Riyal Saudi", "Bahasa Arab"),
    ("Uni Emirat Arab", "Abu Dhabi", "Asia", "Dirham UEA", "Bahasa Arab"),
    ("Qatar", "Doha", "Asia", "Riyal Qatar", "Bahasa Arab"),
    ("Kuwait", "Kota Kuwait", "Asia", "Dinar Kuwait", "Bahasa Arab"),
    ("Yordania", "Amman", "Asia", "Dinar Yordania", "Bahasa Arab"),
    ("Lebanon", "Beirut", "Asia", "Pound Lebanon", "Bahasa Arab"),
    ("Irak", "Baghdad", "Asia", "Dinar Irak", "Bahasa Arab dan Kurdi"),
    ("Suriah", "Damaskus", "Asia", "Pound Suriah", "Bahasa Arab"),
    ("Iran", "Teheran", "Asia", "Rial Iran", "Bahasa Persia"),
    ("Uzbekistan", "Tashkent", "Asia", "Som Uzbekistan", "Bahasa Uzbek"),
    ("Afghanistan", "Kabul", "Asia", "Afghani", "Bahasa Pashto dan Dari"),
    ("Maladewa", "Male", "Asia", "Rufiyaa", "Bahasa Divehi"),
    ("Bhutan", "Thimphu", "Asia", "Ngultrum", "Bahasa Dzongkha"),
    ("Timor Leste", "Dili", "Asia", "Dolar Amerika Serikat", "Bahasa Tetun dan Portugis"),
    ("Inggris", "London", "Eropa", "Pound Sterling", "Bahasa Inggris"),
    ("Prancis", "Paris", "Eropa", "Euro", "Bahasa Prancis"),
    ("Jerman", "Berlin", "Eropa", "Euro", "Bahasa Jerman"),
    ("Italia", "Roma", "Eropa", "Euro", "Bahasa Italia"),
    ("Spanyol", "Madrid", "Eropa", "Euro", "Bahasa Spanyol"),
    ("Portugal", "Lisabon", "Eropa", "Euro", "Bahasa Portugis"),
    ("Belanda", "Amsterdam", "Eropa", "Euro", "Bahasa Belanda"),
    ("Belgia", "Brussel", "Eropa", "Euro", "Bahasa Belanda, Prancis, dan Jerman"),
    ("Austria", "Wina", "Eropa", "Euro", "Bahasa Jerman"),
    ("Swiss", "Bern", "Eropa", "Franc Swiss", "Bahasa Jerman, Prancis, Italia, dan Romansh"),
    ("Yunani", "Athena", "Eropa", "Euro", "Bahasa Yunani"),
    ("Irlandia", "Dublin", "Eropa", "Euro", "Bahasa Irlandia dan Inggris"),
    ("Finlandia", "Helsinki", "Eropa", "Euro", "Bahasa Finlandia dan Swedia"),
    ("Swedia", "Stockholm", "Eropa", "Krona Swedia", "Bahasa Swedia"),
    ("Norwegia", "Oslo", "Eropa", "Krone Norwegia", "Bahasa Norwegia"),
    ("Denmark", "Kopenhagen", "Eropa", "Krone Denmark", "Bahasa Denmark"),
    ("Polandia", "Warsawa", "Eropa", "Zloty", "Bahasa Polandia"),
    ("Ceko", "Praha", "Eropa", "Koruna Ceko", "Bahasa Ceko"),
    ("Hongaria", "Budapest", "Eropa", "Forint", "Bahasa Hongaria"),
    ("Rumania", "Bukares", "Eropa", "Leu Rumania", "Bahasa Rumania"),
    ("Ukraina", "Kyiv", "Eropa", "Hryvnia", "Bahasa Ukraina"),
    ("Kroasia", "Zagreb", "Eropa", "Euro", "Bahasa Kroasia"),
    ("Serbia", "Beograd", "Eropa", "Dinar Serbia", "Bahasa Serbia"),
    ("Islandia", "Reykjavik", "Eropa", "Krona Islandia", "Bahasa Islandia"),
    ("Rusia", "Moskow", "Eropa dan Asia", "Rubel", "Bahasa Rusia"),
    ("Amerika Serikat", "Washington, D.C.", "Amerika Utara", "Dolar Amerika Serikat", "Bahasa Inggris"),
    ("Kanada", "Ottawa", "Amerika Utara", "Dolar Kanada", "Bahasa Inggris dan Prancis"),
    ("Meksiko", "Kota Meksiko", "Amerika Utara", "Peso Meksiko", "Bahasa Spanyol"),
    ("Kuba", "Havana", "Amerika Utara", "Peso Kuba", "Bahasa Spanyol"),
    ("Brasil", "Brasilia", "Amerika Selatan", "Real", "Bahasa Portugis"),
    ("Argentina", "Buenos Aires", "Amerika Selatan", "Peso Argentina", "Bahasa Spanyol"),
    ("Chili", "Santiago", "Amerika Selatan", "Peso Chili", "Bahasa Spanyol"),
    ("Kolombia", "Bogota", "Amerika Selatan", "Peso Kolombia", "Bahasa Spanyol"),
    ("Peru", "Lima", "Amerika Selatan", "Sol", "Bahasa Spanyol"),
    ("Venezuela", "Caracas", "Amerika Selatan", "Bolivar", "Bahasa Spanyol"),
    ("Ekuador", "Quito", "Amerika Selatan", "Dolar Amerika Serikat", "Bahasa Spanyol"),
    ("Uruguay", "Montevideo", "Amerika Selatan", "Peso Uruguay", "Bahasa Spanyol"),
    ("Mesir", "Kairo", "Afrika", "Pound Mesir", "Bahasa Arab"),
    ("Afrika Selatan", "Pretoria", "Afrika", "Rand", "Bahasa Inggris dan sebelas bahasa resmi lainnya"),
    ("Nigeria", "Abuja", "Afrika", "Naira", "Bahasa Inggris"),
    ("Kenya", "Nairobi", "Afrika", "Shilling Kenya", "Bahasa Swahili dan Inggris"),
    ("Ethiopia", "Addis Ababa", "Afrika", "Birr", "Bahasa Amharik"),
    ("Ghana", "Accra", "Afrika", "Cedi", "Bahasa Inggris"),
    ("Maroko", "Rabat", "Afrika", "Dirham Maroko", "Bahasa Arab dan Berber"),
    ("Aljazair", "Aljir", "Afrika", "Dinar Aljazair", "Bahasa Arab dan Berber"),
    ("Tunisia", "Tunis", "Afrika", "Dinar Tunisia", "Bahasa Arab"),
    ("Tanzania", "Dodoma", "Afrika", "Shilling Tanzania", "Bahasa Swahili dan Inggris"),
    ("Uganda", "Kampala", "Afrika", "Shilling Uganda", "Bahasa Inggris dan Swahili"),
    ("Senegal", "Dakar", "Afrika", "Franc CFA", "Bahasa Prancis"),
    ("Australia", "Canberra", "Oseania", "Dolar Australia", "Bahasa Inggris"),
    ("Selandia Baru", "Wellington", "Oseania", "Dolar Selandia Baru", "Bahasa Inggris dan Maori"),
    ("Fiji", "Suva", "Oseania", "Dolar Fiji", "Bahasa Inggris, Fiji, dan Hindi"),
    ("Papua Nugini", "Port Moresby", "Oseania", "Kina", "Bahasa Inggris, Tok Pisin, dan Hiri Motu"),
]

PROVINCES = [
    ("Aceh", "Banda Aceh", "Pulau Sumatra"),
    ("Sumatera Utara", "Medan", "Pulau Sumatra"),
    ("Sumatera Barat", "Padang", "Pulau Sumatra"),
    ("Riau", "Pekanbaru", "Pulau Sumatra"),
    ("Kepulauan Riau", "Tanjungpinang", "Pulau Sumatra dan kepulauan sekitarnya"),
    ("Jambi", "Jambi", "Pulau Sumatra"),
    ("Bengkulu", "Bengkulu", "Pulau Sumatra"),
    ("Sumatera Selatan", "Palembang", "Pulau Sumatra"),
    ("Kepulauan Bangka Belitung", "Pangkalpinang", "Pulau Bangka dan Belitung"),
    ("Lampung", "Bandar Lampung", "Pulau Sumatra"),
    ("Banten", "Serang", "Pulau Jawa"),
    ("DKI Jakarta", "Jakarta", "Pulau Jawa"),
    ("Jawa Barat", "Bandung", "Pulau Jawa"),
    ("Jawa Tengah", "Semarang", "Pulau Jawa"),
    ("DI Yogyakarta", "Yogyakarta", "Pulau Jawa"),
    ("Jawa Timur", "Surabaya", "Pulau Jawa"),
    ("Bali", "Denpasar", "Pulau Bali"),
    ("Nusa Tenggara Barat", "Mataram", "Kepulauan Nusa Tenggara"),
    ("Nusa Tenggara Timur", "Kupang", "Kepulauan Nusa Tenggara"),
    ("Kalimantan Barat", "Pontianak", "Pulau Kalimantan"),
    ("Kalimantan Tengah", "Palangka Raya", "Pulau Kalimantan"),
    ("Kalimantan Selatan", "Banjarbaru", "Pulau Kalimantan"),
    ("Kalimantan Timur", "Samarinda", "Pulau Kalimantan"),
    ("Kalimantan Utara", "Tanjung Selor", "Pulau Kalimantan"),
    ("Sulawesi Utara", "Manado", "Pulau Sulawesi"),
    ("Gorontalo", "Gorontalo", "Pulau Sulawesi"),
    ("Sulawesi Tengah", "Palu", "Pulau Sulawesi"),
    ("Sulawesi Barat", "Mamuju", "Pulau Sulawesi"),
    ("Sulawesi Selatan", "Makassar", "Pulau Sulawesi"),
    ("Sulawesi Tenggara", "Kendari", "Pulau Sulawesi"),
    ("Maluku", "Ambon", "Kepulauan Maluku"),
    ("Maluku Utara", "Sofifi", "Kepulauan Maluku"),
    ("Papua", "Jayapura", "Pulau Papua"),
    ("Papua Barat", "Manokwari", "Pulau Papua"),
    ("Papua Barat Daya", "Sorong", "Pulau Papua"),
    ("Papua Tengah", "Nabire", "Pulau Papua"),
    ("Papua Pegunungan", "Jayawijaya", "Pulau Papua"),
    ("Papua Selatan", "Merauke", "Pulau Papua"),
]

LANDMARKS = [
    ("Monumen Nasional", "Jakarta", "Indonesia"),
    ("Candi Borobudur", "Magelang, Jawa Tengah", "Indonesia"),
    ("Candi Prambanan", "Sleman, DI Yogyakarta", "Indonesia"),
    ("Danau Toba", "Sumatera Utara", "Indonesia"),
    ("Gunung Bromo", "Jawa Timur", "Indonesia"),
    ("Kawah Ijen", "Banyuwangi, Jawa Timur", "Indonesia"),
    ("Taj Mahal", "Agra", "India"),
    ("Tembok Besar", "Tiongkok utara", "Tiongkok"),
    ("Menara Eiffel", "Paris", "Prancis"),
    ("Menara Pisa", "Pisa", "Italia"),
    ("Colosseum", "Roma", "Italia"),
    ("Ka'bah", "Mekah", "Arab Saudi"),
    ("Piramida Giza", "Giza", "Mesir"),
    ("Machu Picchu", "Cusco", "Peru"),
    ("Patung Kristus Penebus", "Rio de Janeiro", "Brasil"),
    ("Patung Liberty", "New York", "Amerika Serikat"),
    ("Big Ben", "London", "Inggris"),
    ("Sagrada Familia", "Barcelona", "Spanyol"),
    ("Petra", "Ma'an", "Yordania"),
    ("Angkor Wat", "Siem Reap", "Kamboja"),
    ("Gunung Rushmore", "South Dakota", "Amerika Serikat"),
    ("Sydney Opera House", "Sydney", "Australia"),
    ("Tower Bridge", "London", "Inggris"),
    ("Kremlin", "Moskow", "Rusia"),
    ("Alhambra", "Granada", "Spanyol"),
    ("Stonehenge", "Wiltshire", "Inggris"),
    ("Golden Gate Bridge", "San Francisco", "Amerika Serikat"),
    ("Burj Khalifa", "Dubai", "Uni Emirat Arab"),
    ("Menara Petronas", "Kuala Lumpur", "Malaysia"),
    ("Marina Bay Sands", "Singapura", "Singapura"),
]

MOUNTAINS = [
    ("Gunung Everest", 8849, "Nepal dan Tiongkok"),
    ("Gunung K2", 8611, "Pakistan dan Tiongkok"),
    ("Gunung Kangchenjunga", 8586, "Nepal dan India"),
    ("Gunung Lhotse", 8516, "Nepal dan Tiongkok"),
    ("Gunung Makalu", 8485, "Nepal dan Tiongkok"),
    ("Gunung Cho Oyu", 8188, "Nepal dan Tiongkok"),
    ("Gunung Dhaulagiri", 8167, "Nepal"),
    ("Gunung Manaslu", 8163, "Nepal"),
    ("Gunung Nanga Parbat", 8126, "Pakistan"),
    ("Gunung Annapurna I", 8091, "Nepal"),
    ("Gunung Gasherbrum I", 8080, "Pakistan dan Tiongkok"),
    ("Gunung Broad Peak", 8051, "Pakistan dan Tiongkok"),
    ("Puncak Jaya", 4884, "Indonesia, Papua"),
    ("Gunung Kerinci", 3805, "Indonesia, Sumatera Barat dan Jambi"),
    ("Gunung Rinjani", 3726, "Indonesia, Lombok"),
    ("Gunung Semeru", 3676, "Indonesia, Jawa Timur"),
    ("Gunung Slamet", 3428, "Indonesia, Jawa Tengah"),
    ("Gunung Merapi", 2930, "Indonesia, Jawa Tengah dan DI Yogyakarta"),
    ("Gunung Sinabung", 2460, "Indonesia, Sumatera Utara"),
    ("Gunung Fuji", 3776, "Jepang"),
    ("Gunung Kilimanjaro", 5895, "Tanzania"),
    ("Mont Blanc", 4808, "Prancis dan Italia"),
    ("Gunung Denali", 6190, "Amerika Serikat, Alaska"),
    ("Gunung Aconcagua", 6961, "Argentina"),
    ("Gunung Elbrus", 5642, "Rusia"),
    ("Gunung Vinson", 4892, "Antartika"),
]

ELEMENTS = [
    ("hidrogen", "H", 1), ("helium", "He", 2), ("litium", "Li", 3),
    ("berilium", "Be", 4), ("boron", "B", 5), ("karbon", "C", 6),
    ("nitrogen", "N", 7), ("oksigen", "O", 8), ("fluor", "F", 9),
    ("neon", "Ne", 10), ("natrium", "Na", 11), ("magnesium", "Mg", 12),
    ("aluminium", "Al", 13), ("silikon", "Si", 14), ("fosfor", "P", 15),
    ("belerang", "S", 16), ("klorin", "Cl", 17), ("argon", "Ar", 18),
    ("kalium", "K", 19), ("kalsium", "Ca", 20), ("besi", "Fe", 26),
    ("tembaga", "Cu", 29), ("seng", "Zn", 30), ("perak", "Ag", 47),
    ("emas", "Au", 79), ("raksa", "Hg", 80), ("timbal", "Pb", 82),
    ("uranium", "U", 92), ("plutonium", "Pu", 94), ("radon", "Rn", 86),
]

ANIMALS = [
    ("harimau", "daging", "hutan", "belang di tubuhnya"),
    ("singa", "daging", "sabana Afrika", "surai pada jantan"),
    ("gajah", "tumbuhan", "hutan dan sabana", "belalai yang panjang"),
    ("jerapah", "daun", "sabana Afrika", "leher yang sangat panjang"),
    ("zebra", "rumput", "sabana Afrika", "garis hitam putih di tubuhnya"),
    ("badak", "tumbuhan", "hutan tropis", "cula di hidungnya"),
    ("kuda", "rumput", "padang rumput", "kaki kuat untuk berlari"),
    ("sapi", "rumput", "peternakan", "lambung yang bisa memamah biak"),
    ("kambing", "rumput dan daun", "peternakan", "tanduk di kepalanya"),
    ("ayam", "biji-bijian", "peternakan", "jengger di atas kepalanya"),
    ("bebek", "tumbuhan air", "danau dan sungai", "paruh lebar dan kaki berselaput"),
    ("kucing", "daging", "rumah dan lingkungan manusia", "kumis dan pendengaran tajam"),
    ("anjing", "daging", "rumah dan lingkungan manusia", "penciuman yang sangat tajam"),
    ("kelinci", "sayur dan rumput", "padang rumput", "telinga panjang"),
    ("tikus", "biji-bijian", "sawah dan rumah", "gigi depan yang terus tumbuh"),
    ("kelelawar", "buah dan serangga", "gua dan pohon", "kemampuan terbang pada malam hari"),
    ("burung hantu", "serangga dan tikus", "hutan", "mata besar dan pendengaran tajam"),
    ("elang", "daging", "pegunungan", "penglihatan tajam dari udara"),
    ("merpati", "biji-bijian", "kota dan desa", "kemampuan pulang ke sarang"),
    ("penguin", "ikan", "kutub selatan", "bisa berenang tetapi tidak bisa terbang"),
    ("beruang kutub", "ikan dan anjing laut", "Arktik", "bulu tebal dan lapisan lemak"),
    ("panda", "bambu", "hutan Tiongkok", "bulu hitam putih"),
    ("koala", "daun eukaliptus", "hutan Australia", "tidur sangat lama di pohon"),
    ("kanguru", "rumput", "Australia", "kantung di perut betina"),
    ("serigala", "daging", "hutan", "hidup berkelompok"),
    ("rubah", "daging", "hutan", "ekor yang lebat"),
    ("rusa", "rumput", "hutan", "tanduk bercabang"),
    ("monyet", "buah", "hutan", "pandai memanjat pohon"),
    ("orangutan", "buah", "hutan Kalimantan dan Sumatra", "lengan panjang"),
    ("gorila", "tumbuhan", "hutan Afrika", "tubuh besar dan kuat"),
    ("simpanse", "buah", "hutan Afrika", "pandai memakai alat"),
    ("ular", "daging", "hutan dan semak", "tubuh panjang tanpa kaki"),
    ("komodo", "daging", "Pulau Komodo", "kadal terbesar di dunia"),
    ("buaya", "daging", "sungai dan rawa", "rahang yang sangat kuat"),
    ("kura-kura", "tumbuhan dan hewan kecil", "darat dan air", "tempurung pelindung"),
    ("katak", "serangga", "air dan tanah lembap", "kemampuan melompat jauh"),
    ("hiu", "daging", "laut", "kerangka tulang rawan"),
    ("paus", "plankton", "laut", "bernapas dengan paru-paru"),
    ("dolfin", "ikan", "laut", "kecerdasan tinggi dan suka berkelompok"),
    ("gurita", "daging", "laut", "delapan lengan"),
    ("cumi-cumi", "ikan", "laut", "tinta untuk melindungi diri"),
    ("udang", "plankton", "laut dan tambak", "antena panjang di kepalanya"),
    ("kepiting", "daging", "pantai dan laut", "capit yang kuat"),
    ("semut", "gula dan sisa makanan", "tanah dan pepohonan", "hidup dalam koloni"),
    ("lebah", "nektar", "bunga dan sarang", "menghasilkan madu"),
    ("kupu-kupu", "nektar", "taman dan hutan", "sayap berwarna indah"),
    ("labah-labah", "serangga", "sudut rumah dan hutan", "membuat jaring"),
    ("cacing", "zat organik di tanah", "tanah", "tubuh lunak dan panjang"),
]

FOODS = [
    ("rendang", "Sumatera Barat", "daging sapi dan santan"),
    ("sate", "Jawa", "daging dan bumbu kacang"),
    ("soto", "Indonesia", "kaldu dan daging"),
    ("nasi goreng", "Indonesia", "nasi dan bumbu"),
    ("gado-gado", "Jakarta", "sayur dan saus kacang"),
    ("ketoprak", "Jakarta", "tahu, bihun, dan saus kacang"),
    ("bakso", "Indonesia", "daging giling"),
    ("rawon", "Jawa Timur", "daging dan kluwek"),
    ("pempek", "Palembang", "ikan dan sagu"),
    ("kerak telor", "Jakarta", "beras ketan dan telur"),
    ("nasi uduk", "Jakarta", "beras dan santan"),
    ("tumpeng", "Jawa", "nasi kuning dan lauk"),
    ("gudeg", "Yogyakarta", "nangka muda dan santan"),
    ("sate klathak", "Yogyakarta", "daging kambing"),
    ("cendol", "Jawa", "tepung beras dan gula aren"),
    ("martabak", "Indonesia", "tepung dan telur"),
    ("klepon", "Jawa", "ketan dan gula merah"),
    ("onde-onde", "Jawa", "ketan dan kacang hijau"),
    ("lumpia", "Semarang", "kulit tepung dan rebung"),
    ("papeda", "Papua", "sagu"),
    ("bika ambon", "Medan", "tepung dan santan"),
    ("mi aceh", "Aceh", "mi dan bumbu pedas"),
    ("ayam betutu", "Bali", "ayam dan bumbu"),
    ("lawar", "Bali", "sayur dan kelapa"),
    ("sate lilit", "Bali", "daging dan kelapa"),
    ("coto makassar", "Sulawesi Selatan", "daging dan kacang"),
    ("pallubasa", "Sulawesi Selatan", "daging dan kelapa"),
    ("tinutuan", "Sulawesi Utara", "beras dan sayur"),
    ("kue lapis", "Indonesia", "tepung dan santan"),
    ("serabi", "Jawa", "tepung dan santan"),
    ("nagasari", "Jawa", "pisang dan tepung"),
    ("bolu kukus", "Indonesia", "tepung dan gula"),
    ("pisang goreng", "Indonesia", "pisang dan tepung"),
    ("tempe mendoan", "Banyumas", "tempe"),
    ("pecel lele", "Jawa", "ikan lele dan sambal"),
    ("sambal terasi", "Indonesia", "cabai dan terasi"),
    ("nasi padang", "Sumatera Barat", "nasi dan lauk"),
]

CULTURE = [
    ("Tari Kecak", "tarian", "Bali", "ditarikan banyak orang sambil bersuara cak"),
    ("Tari Legong", "tarian", "Bali", "ditarikan dengan gerakan halus dan penuh hiasan"),
    ("Tari Pendet", "tarian", "Bali", "dipakai untuk menyambut tamu"),
    ("Tari Saman", "tarian", "Aceh", "ditarikan sambil duduk dan bertepuk tangan"),
    ("Tari Piring", "tarian", "Sumatera Barat", "menggunakan piring sebagai properti"),
    ("Tari Jaipong", "tarian", "Jawa Barat", "gerakannya enerjik dan diiringi gendang"),
    ("Tari Serimpi", "tarian", "Yogyakarta", "ditarikan dengan gerakan pelan dan anggun"),
    ("Tari Bedhaya", "tarian", "Yogyakarta", "tarian sakral dari keraton"),
    ("Tari Reog", "tarian", "Ponorogo, Jawa Timur", "memakai topeng singa besar"),
    ("Tari Gandrung", "tarian", "Banyuwangi", "ditarikan sebagai ucapan syukur"),
    ("Tari Tor-tor", "tarian", "Sumatera Utara", "diiringi musik gondang"),
    ("Tari Kipas", "tarian", "Sulawesi Selatan", "menggunakan kipas sebagai properti"),
    ("Tari Maengket", "tarian", "Sulawesi Utara", "ditarikan saat panen"),
    ("Tari Sajojo", "tarian", "Papua", "ditarikan bersama-sama dengan gerakan riang"),
    ("Rumah Gadang", "rumah adat", "Sumatera Barat", "atapnya melengkung seperti tanduk kerbau"),
    ("Rumah Joglo", "rumah adat", "Jawa", "punya pendopo dan atap bertingkat"),
    ("Rumah Honai", "rumah adat", "Papua", "berbentuk bulat dengan atap jerami"),
    ("Rumah Tongkonan", "rumah adat", "Sulawesi Selatan", "atapnya menjulang di kedua ujung"),
    ("Rumah Kebaya", "rumah adat", "Jakarta", "atapnya mirip lipatan kebaya"),
    ("Rumah Baileo", "rumah adat", "Maluku", "dipakai untuk musyawarah warga"),
    ("Rumah Mbaru Niang", "rumah adat", "Flores", "berbentuk kerucut dan dibangun bertingkat"),
    ("Angklung", "alat musik", "Jawa Barat", "terbuat dari bambu dan dimainkan dengan digoyang"),
    ("Gamelan", "alat musik", "Jawa dan Bali", "terdiri dari banyak alat musik pukul"),
    ("Sasando", "alat musik", "Nusa Tenggara Timur", "berbentuk seperti kipas dan dipetik"),
    ("Kolintang", "alat musik", "Sulawesi Utara", "terbuat dari kayu dan dipukul"),
    ("Tifa", "alat musik", "Papua dan Maluku", "berbentuk tabung dan dipukul"),
    ("Kecapi", "alat musik", "Jawa Barat", "dipetik dengan jari"),
    ("Rebab", "alat musik", "Jawa", "digesek dan bernuansa melankolis"),
    ("Saluang", "alat musik", "Sumatera Barat", "terbuat dari bambu dan ditiup"),
    ("Serune Kalee", "alat musik", "Aceh", "terbuat dari kayu dan kuningan"),
    ("Wayang Kulit", "seni pertunjukan", "Jawa", "boneka kulit dimainkan di balik layar"),
    ("Wayang Golek", "seni pertunjukan", "Jawa Barat", "boneka kayu yang dimainkan dalang"),
    ("Batik", "kain", "Jawa", "motifnya dibuat dengan canting atau cap"),
    ("Tenun Ikat", "kain", "Nusa Tenggara", "benangnya diikat sebelum ditenun"),
    ("Ulos", "kain", "Sumatera Utara", "punya makna adat dalam upacara"),
    ("Songket", "kain", "Palembang", "ditenun dengan benang emas"),
    ("Keris", "senjata tradisional", "Jawa", "berbentuk bilah berlekuk dan punya nilai adat"),
    ("Rencong", "senjata tradisional", "Aceh", "bentuknya khas dan menjadi simbol keberanian"),
    ("Mandau", "senjata tradisional", "Kalimantan", "dipakai suku Dayak"),
    ("Kujang", "senjata tradisional", "Jawa Barat", "berbentuk khas dan dianggap pusaka"),
]

FIGURES = [
    ("Soekarno", "politik", "menjadi presiden pertama Indonesia dan membacakan teks Proklamasi"),
    ("Mohammad Hatta", "politik", "menjadi wakil presiden pertama dan ikut menandatangani teks Proklamasi"),
    ("Ki Hajar Dewantara", "pendidikan", "mendirikan Taman Siswa dan dikenal sebagai bapak pendidikan nasional"),
    ("R.A. Kartini", "pendidikan", "memperjuangkan pendidikan bagi perempuan Indonesia"),
    ("Cut Nyak Dien", "perjuangan", "memimpin perlawanan rakyat Aceh melawan penjajah"),
    ("Pangeran Diponegoro", "perjuangan", "memimpin Perang Jawa pada abad ke-19"),
    ("Sultan Hasanuddin", "perjuangan", "memimpin perlawanan rakyat Makassar"),
    ("Pattimura", "perjuangan", "memimpin perlawanan rakyat Maluku"),
    ("Tuanku Imam Bonjol", "perjuangan", "memimpin Perang Padri di Sumatera Barat"),
    ("Sisingamangaraja XII", "perjuangan", "memimpin perlawanan rakyat Batak"),
    ("I Gusti Ngurah Rai", "perjuangan", "memimpin perlawanan rakyat Bali"),
    ("Bung Tomo", "perjuangan", "membangkitkan semangat rakyat Surabaya pada 1945"),
    ("Jenderal Sudirman", "militer", "menjadi panglima besar Tentara Nasional Indonesia"),
    ("B.J. Habibie", "teknologi", "dikenal sebagai ahli pesawat terbang dan presiden ketiga Indonesia"),
    ("Adam Malik", "politik", "berperan dalam diplomasi Indonesia dan menjadi wakil presiden"),
    ("Mohammad Yamin", "sastra dan politik", "berperan merumuskan dasar negara dan menulis karya sastra"),
    ("Chairil Anwar", "sastra", "menjadi pelopor puisi modern Indonesia"),
    ("Pramoedya Ananta Toer", "sastra", "menulis novel dan cerita yang dikenal luas"),
    ("W.R. Supratman", "musik", "menciptakan lagu Indonesia Raya"),
    ("Ismail Marzuki", "musik", "menciptakan banyak lagu perjuangan"),
    ("Affandi", "seni", "dikenal sebagai pelukis ekspresionis Indonesia"),
    ("Raden Saleh", "seni", "menjadi pelukis Indonesia yang dikenal di Eropa"),
    ("Albert Einstein", "fisika", "mengembangkan teori relativitas"),
    ("Isaac Newton", "fisika", "merumuskan hukum gravitasi dan gerak"),
    ("Charles Darwin", "biologi", "mengemukakan teori evolusi melalui seleksi alam"),
    ("Marie Curie", "kimia dan fisika", "meneliti radioaktivitas dan meraih dua Nobel"),
    ("Louis Pasteur", "biologi", "mengembangkan pasteurisasi dan vaksin rabies"),
    ("Alexander Fleming", "kedokteran", "menemukan penisilin"),
    ("Nikola Tesla", "teknologi", "mengembangkan sistem arus bolak-balik"),
    ("Thomas Edison", "teknologi", "mengembangkan lampu pijar yang praktis"),
    ("Wright Bersaudara", "teknologi", "membuat pesawat terbang bermesin pertama"),
    ("Guglielmo Marconi", "teknologi", "mengembangkan komunikasi radio"),
    ("Tim Berners-Lee", "teknologi", "menciptakan World Wide Web"),
    ("Alan Turing", "komputer", "meletakkan dasar ilmu komputer dan mesin Turing"),
    ("Nelson Mandela", "politik", "memperjuangkan penghapusan apartheid di Afrika Selatan"),
    ("Mahatma Gandhi", "politik", "memimpin perjuangan kemerdekaan India tanpa kekerasan"),
    ("Ibnu Sina", "kedokteran", "menulis karya kedokteran yang dipakai berabad-abad"),
    ("Al-Khawarizmi", "matematika", "dikenal sebagai salah satu peletak dasar aljabar"),
]

EVENTS = [
    ("Proklamasi Kemerdekaan Indonesia", 1945, "Soekarno dan Mohammad Hatta membacakan teks proklamasi di Jakarta"),
    ("Sumpah Pemuda", 1928, "para pemuda Indonesia bersumpah untuk satu tanah air, satu bangsa, dan satu bahasa"),
    ("Perang Dunia I", 1914, "perang besar yang melibatkan banyak negara di Eropa dan sekitarnya"),
    ("Perang Dunia II", 1939, "perang global yang berlangsung hingga 1945"),
    ("Penemuan benua Amerika oleh Columbus", 1492, "Columbus sampai di benua Amerika dalam pelayarannya"),
    ("Reformasi Indonesia", 1998, "gerakan yang membawa perubahan besar dalam pemerintahan Indonesia"),
    ("Krisis Moneter Asia", 1997, "krisis ekonomi yang melanda banyak negara Asia"),
    ("Gempa dan tsunami Aceh", 2004, "gempa besar di Samudra Hindia memicu tsunami yang melanda Aceh"),
    ("Letusan Krakatau", 1883, "letusan besar yang menimbulkan gelombang dan abu vulkanik"),
    ("Letusan Tambora", 1815, "letusan besar yang memengaruhi iklim dunia"),
    ("Pemilu pertama Indonesia", 1955, "pemilihan umum pertama setelah Indonesia merdeka"),
    ("Konferensi Asia Afrika", 1955, "pertemuan negara-negara Asia dan Afrika di Bandung"),
    ("ASEAN didirikan", 1967, "negara-negara Asia Tenggara membentuk organisasi ASEAN"),
    ("PBB didirikan", 1945, "organisasi internasional dibentuk setelah Perang Dunia II"),
    ("Deklarasi HAM Universal", 1948, "PBB mengadopsi pernyataan hak asasi manusia sedunia"),
    ("Revolusi Prancis", 1789, "perubahan besar dalam pemerintahan dan masyarakat Prancis"),
    ("Kemerdekaan India", 1947, "India lepas dari pemerintahan kolonial Inggris"),
    ("Akhir apartheid di Afrika Selatan", 1994, "pemilu multipartai pertama menandai berakhirnya apartheid"),
    ("Tembok Berlin runtuh", 1989, "pembatas Berlin dibuka dan menjadi simbol berakhirnya Perang Dingin"),
    ("Uni Soviet bubar", 1991, "beberapa republik memisahkan diri dan Uni Soviet berakhir"),
    ("Manusia pertama ke bulan", 1969, "misi Apollo 11 membawa manusia ke permukaan bulan"),
    ("Penerbangan pertama Wright Bersaudara", 1903, "pesawat bermesin pertama berhasil terbang"),
    ("Titanic tenggelam", 1912, "kapal penumpang Titanic tenggelam setelah menabrak gunung es"),
    ("Serangan 11 September", 2001, "serangan teroris di Amerika Serikat mengubah kebijakan keamanan dunia"),
    ("Pandemi COVID-19", 2020, "wabah virus corona menyebar ke seluruh dunia"),
    ("Olimpiade modern pertama", 1896, "Olimpiade modern digelar di Athena"),
    ("Piala Dunia pertama", 1930, "turnamen sepak bola Piala Dunia digelar di Uruguay"),
    ("Indonesia masuk PBB", 1950, "Indonesia resmi menjadi anggota Perserikatan Bangsa-Bangsa"),
    ("Hong Kong kembali ke Tiongkok", 1997, "Hong Kong diserahkan kembali oleh Inggris kepada Tiongkok"),
    ("Euro mulai dipakai", 1999, "mata uang Euro mulai digunakan secara elektronik di Eropa"),
]


def build_world(b: Builder) -> None:
    for negara, kota, benua, uang, bahasa in COUNTRIES:
        key = f"negara-{negara}"
        q = b.pick(
            [
                "ibu kota {n} apa?",
                "{n} ibu kotanya di mana?",
                "kalau mau ke ibu kota {n}, ke kota apa?",
            ],
            key + "ibu",
        ).format(n=negara)
        if negara == "Afrika Selatan":
            a = b.pick(
                [
                    f"Afrika Selatan punya tiga kota pusat pemerintahan. {kota} adalah salah satunya dan menjadi pusat pemerintahan eksekutif.",
                    f"{kota} termasuk salah satu ibu kota Afrika Selatan, tepatnya untuk cabang eksekutif. Negara ini memang memakai tiga kota pusat pemerintahan.",
                ],
                key + "ibu",
            )
        else:
            a = b.pick(
                [
                    f"Ibu kota {negara} adalah {kota}. Kota ini menjadi pusat pemerintahan dan kegiatan politik negara tersebut.",
                    f"{kota} adalah ibu kota {negara}. Di sana terdapat kantor pemerintahan pusat dan perwakilan negara lain.",
                    f"Ibu kotanya {kota}. Nama kota ini sering muncul di berita karena menjadi pusat administrasi {negara}.",
                ],
                key + "ibu",
            )
        b.add(q, a, "pengetahuan", fact=key + ":ibu")

        q = b.pick(
            ["{n} ada di benua apa?", "{n} terletak di benua mana?", "benua {n} apa?"],
            key + "benua",
        ).format(n=negara)
        a = b.pick(
            [
                f"{negara} terletak di benua {benua}. Letak ini memengaruhi iklim, budaya, dan hubungan dengan negara tetangga.",
                f"{negara} berada di benua {benua}. Posisinya membuat negara ini punya ciri khas tersendiri.",
                f"Benua {benua} adalah tempat {negara} berada. Kawasan ini punya banyak negara dengan budaya yang beragam.",
            ],
            key + "benua",
        )
        b.add(q, a, "pengetahuan", fact=key + ":benua")

        q = b.pick(
            ["mata uang {n} apa?", "{n} pakai mata uang apa?", "uang resmi {n} namanya apa?"],
            key + "uang",
        ).format(n=negara)
        a = b.pick(
            [
                f"Mata uang {negara} adalah {uang}. Nilai tukarnya bisa berubah setiap hari mengikuti pasar.",
                f"{negara} memakai {uang} sebagai mata uang resmi. Setiap negara punya kebijakan sendiri soal mata uangnya.",
                f"Mata uang resmi {negara} adalah {uang}. Kalau menukar uang di sana, hasilnya memakai satuan ini.",
            ],
            key + "uang",
        )
        b.add(q, a, "pengetahuan", fact=key + ":uang")

        q = b.pick(
            ["bahasa apa yang dipakai di {n}?", "bahasa utama {n} apa?", "orang {n} sehari-hari bicara pakai bahasa apa?"],
            key + "bahasa",
        ).format(n=negara)
        a = b.pick(
            [
                f"Bahasa yang paling banyak digunakan di {negara} adalah {bahasa}. Selain itu, ada bahasa daerah dan bahasa asing yang dipakai di kota besar.",
                f"Di {negara}, bahasa utamanya {bahasa}. Banyak penduduk juga bisa berbahasa Inggris, terutama di daerah wisata.",
                f"Bahasa utama {negara} adalah {bahasa}. Keragaman bahasa di sana cukup tinggi karena ada banyak kelompok masyarakat.",
            ],
            key + "bahasa",
        )
        b.add(q, a, "pengetahuan", fact=key + ":bahasa")

        if kota not in ("Singapura", "Washington, D.C."):
            q = b.pick(
                ["{k} itu ibu kota negara apa?", "kota {k} adalah ibu kota negara mana?"],
                key + "balik",
            ).format(k=kota)
            a = b.pick(
                [
                    f"{kota} adalah ibu kota {negara}. Kota ini menjadi pusat pemerintahan negara tersebut.",
                    f"Kota {kota} merupakan ibu kota {negara}. Nama kota ini sering muncul dalam berita internasional.",
                ],
                key + "balik",
            )
            b.add(q, a, "pengetahuan", fact=key + ":balik")

    for prov, kota, pulau in PROVINCES:
        key = f"provinsi-{prov}"
        q = b.pick(
            ["ibu kota Provinsi {p} apa?", "Provinsi {p} beribu kota di mana?", "kalau ke ibu kota {p}, ke kota apa?"],
            key + "ibu",
        ).format(p=prov)
        a = b.pick(
            [
                f"Ibu kota Provinsi {prov} adalah {kota}. Provinsi ini berada di {pulau}.",
                f"{kota} adalah ibu kota Provinsi {prov}. Wilayahnya mencakup bagian dari {pulau}.",
                f"Ibu kota {prov} adalah {kota}, yang menjadi pusat pemerintahan provinsi di {pulau}.",
            ],
            key + "ibu",
        )
        b.add(q, a, "pengetahuan", fact=key + ":ibu")

        q = b.pick(
            ["Provinsi {p} terletak di pulau apa?", "{p} ada di wilayah mana?", "{p} masuk pulau apa?"],
            key + "pulau",
        ).format(p=prov)
        a = b.pick(
            [
                f"Provinsi {prov} terletak di {pulau}. Ibu kotanya {kota}.",
                f"{prov} berada di {pulau}, dengan ibu kota {kota}. Wilayah ini punya ciri geografis tersendiri.",
                f"Provinsi {prov} mencakup wilayah {pulau}. Pusat pemerintahannya ada di {kota}.",
            ],
            key + "pulau",
        )
        b.add(q, a, "pengetahuan", fact=key + ":pulau")

        q = b.pick(["{k} itu ibu kota provinsi apa?", "kota {k} ibu kota provinsi mana?"], key + "balik").format(k=kota)
        a = b.pick(
            [
                f"{kota} adalah ibu kota Provinsi {prov}. Provinsi ini berada di {pulau}.",
                f"Kota {kota} menjadi pusat pemerintahan Provinsi {prov}, yang terletak di {pulau}.",
            ],
            key + "balik",
        )
        b.add(q, a, "pengetahuan", fact=key + ":balik")

    for nama, lokasi, negara in LANDMARKS:
        key = f"landmark-{nama}"
        q = b.pick(
            ["di negara mana {n} berada?", "{n} terletak di negara apa?", "{n} ada di negara mana?"],
            key + "negara",
        ).format(n=nama)
        a = b.pick(
            [
                f"{nama} berada di {negara}, tepatnya di {lokasi}. Tempat ini menjadi salah satu tujuan wisata terkenal.",
                f"{nama} terletak di {negara}, yaitu di {lokasi}. Banyak orang datang untuk melihatnya langsung.",
                f"{nama} ada di {negara}. Lokasinya di {lokasi} dan sering jadi ikon wisata negara tersebut.",
            ],
            key + "negara",
        )
        b.add(q, a, "pengetahuan", fact=key + ":negara")

        q = b.pick(
            ["{n} terletak di kota atau daerah mana?", "di mana tepatnya {n} berada?", "{n} lokasinya di mana?"],
            key + "lokasi",
        ).format(n=nama)
        a = b.pick(
            [
                f"{nama} berada di {lokasi}, {negara}. Lokasi ini bisa dicari di peta kalau mau berkunjung.",
                f"Lokasinya di {lokasi}, yang berada di {negara}. Tempat ini punya nilai sejarah dan wisata.",
                f"{nama} terletak di {lokasi}. Wilayah itu termasuk bagian dari {negara}.",
            ],
            key + "lokasi",
        )
        b.add(q, a, "pengetahuan", fact=key + ":lokasi")

    for nama, tinggi, lokasi in MOUNTAINS:
        key = f"gunung-{nama}"
        q = b.pick(
            ["berapa tinggi {n}?", "tinggi {n} berapa meter?", "{n} punya ketinggian berapa?"],
            key + "tinggi",
        ).format(n=nama)
        a = b.pick(
            [
                f"Tinggi {nama} sekitar {fmt_id(tinggi)} meter di atas permukaan laut. Angka ini bisa sedikit berbeda tergantung metode pengukuran.",
                f"{nama} memiliki ketinggian sekitar {fmt_id(tinggi)} meter. Gunung ini berada di {lokasi}.",
                f"Ketinggian {nama} sekitar {fmt_id(tinggi)} meter di atas permukaan laut, dan letaknya di {lokasi}.",
            ],
            key + "tinggi",
        )
        b.add(q, a, "pengetahuan", fact=key + ":tinggi")

        q = b.pick(
            ["{n} terletak di mana?", "di negara mana {n} berada?", "lokasi {n} di mana?"],
            key + "lokasi",
        ).format(n=nama)
        a = b.pick(
            [
                f"{nama} terletak di {lokasi}. Ketinggiannya sekitar {fmt_id(tinggi)} meter di atas permukaan laut.",
                f"Gunung {nama} berada di {lokasi}. Gunung ini terkenal karena ketinggian dan pemandangannya.",
                f"Lokasi {nama} ada di {lokasi}. Tingginya sekitar {fmt_id(tinggi)} meter.",
            ],
            key + "lokasi",
        )
        b.add(q, a, "pengetahuan", fact=key + ":lokasi")

    for unsur, simbol, nomor in ELEMENTS:
        key = f"unsur-{unsur}"
        q = b.pick(
            ["apa lambang kimia {u}?", "lambang unsur {u} apa?", "{u} punya lambang apa dalam tabel periodik?"],
            key + "simbol",
        ).format(u=unsur)
        a = b.pick(
            [
                f"Lambang kimia {unsur} adalah {simbol}. Unsur ini punya nomor atom {nomor}.",
                f"{unsur} dilambangkan dengan {simbol} dan memiliki nomor atom {nomor}.",
                f"Lambang {unsur} adalah {simbol}. Dalam tabel periodik, nomor atomnya {nomor}.",
            ],
            key + "simbol",
        )
        b.add(q, a, "pengetahuan", fact=key + ":simbol")

        q = b.pick(
            ["berapa nomor atom {u}?", "nomor atom unsur {u} berapa?", "{u} berada di nomor atom berapa?"],
            key + "nomor",
        ).format(u=unsur)
        a = b.pick(
            [
                f"Nomor atom {unsur} adalah {nomor}, dengan lambang {simbol}.",
                f"{unsur} memiliki nomor atom {nomor}. Nomor ini menunjukkan jumlah proton di inti atomnya.",
                f"Nomor atom {unsur} adalah {nomor}. Lambangnya {simbol} dalam tabel periodik.",
            ],
            key + "nomor",
        )
        b.add(q, a, "pengetahuan", fact=key + ":nomor")

    for hewan, makanan, habitat, ciri in ANIMALS:
        key = f"hewan-{hewan}"
        q = b.pick(
            ["{h} makan apa?", "makanan {h} apa?", "{h} biasanya makan apa?"],
            key + "makan",
        ).format(h=hewan)
        a = b.pick(
            [
                f"{hewan} makan {makanan}. Di habitat aslinya, makanannya bisa berbeda tergantung ketersediaan.",
                f"Makanan {hewan} adalah {makanan}. Hewan ini hidup di {habitat}.",
                f"{hewan} termasuk pemakan {makanan}. Kalau di kebun binatang, menunya disesuaikan dengan kebutuhan.",
            ],
            key + "makan",
        )
        b.add(q, a, "pengetahuan", fact=key + ":makan")

        q = b.pick(
            ["{h} hidup di mana?", "habitat {h} di mana?", "di mana biasanya {h} tinggal?"],
            key + "habitat",
        ).format(h=hewan)
        a = b.pick(
            [
                f"{hewan} hidup di {habitat}. Ciri khasnya adalah {ciri}.",
                f"Habitat {hewan} adalah {habitat}. Hewan ini mudah dikenali dari {ciri}.",
                f"{hewan} biasanya tinggal di {habitat}. Salah satu cirinya, {ciri}.",
            ],
            key + "habitat",
        )
        b.add(q, a, "pengetahuan", fact=key + ":habitat")

        q = b.pick(
            ["apa ciri khas {h}?", "ciri {h} apa?", "bagaimana cara mengenali {h}?"],
            key + "ciri",
        ).format(h=hewan)
        a = b.pick(
            [
                f"Ciri khas {hewan} adalah {ciri}. Habitatnya di {habitat}, dan makanannya {makanan}.",
                f"{hewan} punya {ciri}. Hewan ini hidup di {habitat}.",
                f"Yang paling menonjol dari {hewan} adalah {ciri}. Di alam, ia mencari {makanan} di {habitat}.",
            ],
            key + "ciri",
        )
        b.add(q, a, "pengetahuan", fact=key + ":ciri")

    for makanan, asal, bahan in FOODS:
        key = f"makanan-{makanan}"
        q = b.pick(
            ["{m} berasal dari mana?", "asal {m} dari daerah mana?", "{m} itu makanan khas mana?"],
            key + "asal",
        ).format(m=makanan)
        a = b.pick(
            [
                f"{makanan} berasal dari {asal}. Makanan ini biasanya dibuat dari {bahan}.",
                f"{makanan} adalah makanan khas {asal}. Bahan utamanya {bahan}.",
                f"Asal {makanan} adalah {asal}. Rasanya khas karena diolah dari {bahan}.",
            ],
            key + "asal",
        )
        b.add(q, a, "pengetahuan", fact=key + ":asal")

        q = b.pick(
            ["bahan utama {m} apa?", "{m} dibuat dari apa?", "apa bahan pokok untuk membuat {m}?"],
            key + "bahan",
        ).format(m=makanan)
        a = b.pick(
            [
                f"Bahan utama {makanan} adalah {bahan}. Makanan ini berasal dari {asal}.",
                f"{makanan} dibuat dari {bahan}. Rasanya khas dan sering dijual di daerah {asal}.",
                f"Untuk membuat {makanan}, bahan utamanya {bahan}. Makanan ini berasal dari {asal}.",
            ],
            key + "bahan",
        )
        b.add(q, a, "pengetahuan", fact=key + ":bahan")

    for nama, jenis, asal, keterangan in CULTURE:
        key = f"budaya-{nama}"
        q = b.pick(
            ["{n} itu apa?", "apa itu {n}?", "{n} termasuk kesenian apa?"],
            key + "jenis",
        ).format(n=nama)
        a = b.pick(
            [
                f"{nama} adalah {jenis} yang berasal dari {asal}. Ciri khasnya, {keterangan}.",
                f"{nama} termasuk {jenis} dari {asal}. Yang menarik, {keterangan}.",
                f"{nama} merupakan {jenis} khas {asal}. Biasanya ditampilkan dengan ciri {keterangan}.",
            ],
            key + "jenis",
        )
        b.add(q, a, "pengetahuan", fact=key + ":jenis")

        q = b.pick(
            ["{n} berasal dari mana?", "asal {n} dari daerah mana?", "{n} itu khas daerah mana?"],
            key + "asal",
        ).format(n=nama)
        a = b.pick(
            [
                f"{nama} berasal dari {asal}. {nama} termasuk {jenis} yang dikenal karena {keterangan}.",
                f"Asal {nama} adalah {asal}. Kesenian ini termasuk {jenis}, dengan ciri {keterangan}.",
                f"{nama} adalah {jenis} dari {asal}. Ciri khasnya, {keterangan}.",
            ],
            key + "asal",
        )
        b.add(q, a, "pengetahuan", fact=key + ":asal")

    for nama, bidang, kontribusi in FIGURES:
        key = f"tokoh-{nama}"
        q = b.pick(
            ["siapa {n}?", "{n} itu tokoh apa?", "kenalan dong, {n} siapa?"],
            key + "siapa",
        ).format(n=nama)
        a = b.pick(
            [
                f"{nama} adalah tokoh di bidang {bidang}. Ia dikenal karena {kontribusi}.",
                f"{nama} dikenal sebagai tokoh {bidang}. Kontribusinya adalah {kontribusi}.",
                f"Namanya {nama}, seorang tokoh {bidang}. Yang membuatnya dikenang, ia {kontribusi}.",
            ],
            key + "siapa",
        )
        b.add(q, a, "pengetahuan", fact=key + ":siapa")

        q = b.pick(
            ["apa kontribusi {n}?", "jasa {n} apa?", "{n} dikenal karena apa?"],
            key + "jasa",
        ).format(n=nama)
        a = b.pick(
            [
                f"{nama} dikenal karena {kontribusi}. Bidang yang digelutinya adalah {bidang}.",
                f"Kontribusi {nama} adalah {kontribusi}. Itu sebabnya namanya tercatat dalam sejarah {bidang}.",
                f"Jasanya di bidang {bidang} adalah {kontribusi}. Banyak orang mengenangnya karena hal itu.",
            ],
            key + "jasa",
        )
        b.add(q, a, "pengetahuan", fact=key + ":jasa")

    for nama, tahun, keterangan in EVENTS:
        key = f"peristiwa-{nama}"
        q = b.pick(
            ["kapan {n} terjadi?", "{n} terjadi tahun berapa?", "tahun berapa {n} berlangsung?"],
            key + "tahun",
        ).format(n=nama)
        a = b.pick(
            [
                f"{nama} terjadi pada tahun {tahun}. {keterangan.capitalize()}.",
                f"Peristiwa {nama} berlangsung pada tahun {tahun}. Secara singkat, {keterangan}.",
                f"Tahun {tahun} adalah waktu terjadinya {nama}. {keterangan.capitalize()}.",
            ],
            key + "tahun",
        )
        b.add(q, a, "pengetahuan", fact=key + ":tahun")

        q = b.pick(
            ["apa itu {n}?", "ceritakan singkat tentang {n}", "{n} itu peristiwa apa?"],
            key + "apa",
        ).format(n=nama)
        a = b.pick(
            [
                f"{nama} adalah peristiwa yang terjadi pada tahun {tahun}. {keterangan.capitalize()}.",
                f"{nama} berlangsung tahun {tahun}. Intinya, {keterangan}.",
                f"Peristiwa {nama} terjadi pada {tahun}. Yang terjadi saat itu: {keterangan}.",
            ],
            key + "apa",
        )
        b.add(q, a, "pengetahuan", fact=key + ":apa")
