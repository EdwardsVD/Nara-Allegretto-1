# Nara-Allegretto-3 — Dataset Latihan Bahasa Indonesia 100 MB (±50 Juta Parameter)

Dataset percakapan & instruksi berbahasa Indonesia untuk model bahasa kecil
**Nara-Allegretto-3**, penerus `Nara-Allegretto-2` (PR #2). Berkas mentah v3
berukuran tepat di kelas **100 MB** dan disimpan utuh di **Google Drive**,
sedangkan repositori ini menyimpan ZIP identik, seluruh kode pembangun
(`tools/`), laporan validasi (`reports/v3/`), dan dataset v2.

## Unduh (Google Drive)

| Berkas | Lokasi | Ukuran | Baris | SHA-256 |
| --- | --- | ---: | ---: | --- |
| **`Nara-Allegretto-3.jsonl`** (v3, aktif) | [Drive: folder `Nara-Allegretto-3`](https://drive.google.com/drive/folders/11d_UIFwyc5qnXR262mFvcZCjNu80yLVQ) · [buka berkas](https://drive.google.com/file/d/1-LmmNOmn4uJJdtJ8lD7X_yF6mt1fCB6a/view?usp=drivesdk) · [unduh langsung](https://drive.google.com/uc?id=1-LmmNOmn4uJJdtJ8lD7X_yF6mt1fCB6a&export=download) | **104.852.761 B (104,85 MB / 100,0 MiB)** | **301.497** | `02ecf69378fd872ca685df31ae615d74719739481989da0fc5cdb9acbfa0949e` |
| `Nara-Allegretto-3.zip` (cadangan di repo ini) | berkas `Nara-Allegretto-3.zip` | 26.860.256 B (25,62 MiB) | berisi JSONL yang sama persis | ZIP: `74ea713a2837d89f8e01fd52f3407fe832ee0dba0393814451fc5079953625cd` |
| `Nara-Allegretto-2.jsonl` (v2, arsip) | [Drive: folder `Nara-Allegretto-2`](https://drive.google.com/drive/folders/1lO3dPq1N65B4fk3EmBeGcvgCh4ny4YhA) · [buka berkas](https://drive.google.com/file/d/1Uk4eeXZ53uXX9gq3CARTTynDFJXhftFE/view?usp=drivesdk) · [unduh langsung](https://drive.google.com/uc?id=1Uk4eeXZ53uXX9gq3CARTTynDFJXhftFE&export=download) | 53.313.731 B (53,31 MB / 50,84 MiB) | 141.311 | `eff893716eada2fbb8b56cac4d19fe19783cb66e309e297508d2370142245ff4` |
| `data_chat.jsonl` (v0, arsip) | berkas di repo ini | 11.280.828 B | — | — |

> **Kenapa ukurannya 104.852.761 byte?** Batas transfer satu berkas ke Google
> Drive yang terukur adalah **100 MiB persis (104.857.600 byte)** — berkas pada
> ukuran itu diterima, lebih besar ditolak. Jadi v3 dikalibrasi **4.839 byte di
> bawah batas tersebut**: 104,85 MB (desimal) ≈ 100,0 MiB. Satu-satunya master
> v3 adalah berkas ini (Drive = ZIP di repo = hasil `tools/v3/build_v3.py`,
> dapat diverifikasi dari SHA-256 di atas). Berkas mentah **tidak** dimasukkan
> ke Git karena melampaui batas berkas GitHub; gunakan ZIP di repo ini.

## Statistik v3 (tervalidasi)

- Contoh: **301.497** pasangan `user` → `assistant`
  (= 141.311 basis v2 yang dipertahankan + **160.186 contoh baru**).
- **Identitas dimigrasi manual**: hanya 10 baris di v2 yang menyebut
  `Nara-Allegretto-2`; kesepuluh baris itu ditulis ulang satu per satu menjadi
  identitas `Nara-Allegretto-3` (termasuk perbaikan frasa "generasi kedua" →
  "generasi ketiga"). Penyebutan v2 yang tersisa di v3 hanya 3 baris, semuanya
  dalam konteks membahas versi lama secara eksplisit. Pengakuan diri sebagai
  versi lama: **0**.
- Validasi menyeluruh (`tools/v3/validate_v3.py`): **0 isu** —
  duplikat pertanyaan/jawaban (lower+trim & normalisasi) **0**, mojibake **0**,
  persamaan aritmetika diperiksa **91.372 (0 salah)**, blok kode diperiksa
  **38.659 (0 gagal, maks. 8 baris)**. Panjang jawaban: min 45, median 149,
  rata-rata 188,6, maks 543 karakter.
- Uji pilot (`build --pilot` + `pilot_train_check.py`, 2 epoch):
  `train_loss 3,38 -> 0,57`, `val_loss 3,38 -> 0,80`.

### Komposisi per kategori

| Kategori | Contoh v2 | Contoh baru v3 | Total v3 | Ukuran total (±) |
| --- | ---: | ---: | ---: | ---: |
| `chat` | 43.983 | 22.157 | **66.140** | 36,96 MiB |
| `kode` | 16.571 | 22.088 | **38.659** | 16,18 MiB |
| `pengetahuan` | 3.172 | 3.816 | **6.988** | 1,81 MiB |
| `bahasa` | 41.085 | 58.182 | **99.267** | 21,43 MiB |
| `math` | 36.500 | 53.943 | **90.443** | 23,62 MiB |
| **Total** | **141.311** | **160.186** | **301.497** | **±100,0 MiB** |

Cara contoh baru dihasilkan (anti-salah, semua disaring terhadap seluruh isi
v2 sehingga dijamin bukan duplikat):

- **chat**: tabel topik baru tulisan tangan v3 (kos, uang, belajar/kerja,
  makan/dapur, sosial, gadget — 96 topik tips), 18 skenario curhat baru,
  22 resep baru, sapaan komposisional, draf pesan, kejujuran "aku nggak tahu"
  untuk info real-time, penolakan aman, dan 24 pasangan identitas v3.
- **kode**: keluarga tugas berparameter lebar baru (Python, JS, TS, HTML, CSS,
  SQL, Bash, JSON) — setiap cuplikan **dieksekusi/divalidasi otomatis** oleh
  `tools/v2/code_verifier.py` sebelum masuk (29.671 percobaan, 0 gagal uji
  pada yang diterbitkan).
- **bahasa**: teka-teki kata lama dengan 3 benih acak baru + 11 jenis tugas
  analisis kata baru yang semuanya **dihitung Python** dari `words_id.txt`.
- **math**: pembangun matematika teruji v1/v2 dengan 3 benih acak baru —
  semua jawaban dihitung Python.
- **pengetahuan**: basis fakta terkurasi yang sama dengan v1/v2 dengan gaya
  tanya baru + fakta yang bisa dihitung (kalender/hari dari `datetime`, tahun
  kabisat, perbandingan gunung/unsur/peristiwa, urutan planet/bulan/arah,
  sila Pancasila). Tidak ada fakta karangan baru.

## Perkiraan untuk model ±50 juta parameter (`tools/v3/estimate_params.py`)

- Konten user+assistant: **78.597.851 karakter**, **12.187.595 kata**,
  **17.041.733 token** (tokenizer regex kata+tanda baca ala pilot check).
- Perkiraan token subword (BPE) bahasa Indonesia dengan asumsi terbuka
  3,2–4,2 karakter/token: **±18,7–24,6 juta token** (tengah ±21,6 juta).
- Rasio untuk 50 juta parameter: **±0,43 token/parameter per epoch**. Artinya
  dataset ini adalah porsi latihan **multi-epoch** untuk model ±50 juta
  parameter (latih banyak epoch sambil memantau validation loss dan berhenti
  sebelum overfitting) — **bukan** porsi satu epoch ala Chinchilla, yang untuk
  50 juta parameter akan membutuhkan ±1 miliar token unik.
- Contoh arsitektur yang jumlah parameternya dihitung persis (decoder-only,
  embedding terikat): vocab 8.192, konteks 512, `d_model` 560, 12 lapis,
  `d_ff` 2.240 → **50.121.120 parameter**. Bobotnya saja berukuran kasar
  **±100,2 MB pada FP16** (2 byte/parameter) atau **±50,1 MB pada INT8**,
  belum termasuk metadata format berkas.

## Format baris

Sama persis dengan v2 agar kompatibel dengan pipeline latihan yang ada:

```json
{"messages": [{"role": "user", "content": "p nara"}, {"role": "assistant", "content": "Hadir! Mau ngobrol santai, bahas koding tipis-tipis, atau tanya sesuatu nih?"}]}
```

## Membangun ulang & memvalidasi

```bash
# 1. Pilot dulu (±140 KB contoh baru per kategori + uji latih 2 epoch)
python3 tools/v3/build_v3.py --pilot --report build/v3_pilot/build_report.json
python3 tools/v2/pilot_train_check.py build/v3_pilot/pilot_merged.jsonl --epochs 2

# 2. Build penuh deterministik (membutuhkan Nara-Allegretto-2.jsonl di root)
python3 tools/v3/build_v3.py --report build/v3/build_report.json

# 3. Validasi menyeluruh + perkiraan parameter
python3 tools/v3/validate_v3.py Nara-Allegretto-3.jsonl
python3 tools/v3/estimate_params.py Nara-Allegretto-3.jsonl
sha256sum Nara-Allegretto-3.jsonl   # harus: 02ecf69378fd... (lihat tabel unduh)
```

Laporan hasil build yang diterbitkan tersimpan di `reports/v3/`
(`build_report.json`, `validation_report.json`, `param_estimate.json`,
`pilot_build_report.json`). Pipeline v2 (`tools/v2/`) dan v1 (`tools/*.py`)
dipertahankan utuh untuk reproduksi versi sebelumnya.

## Lisensi

MIT — lihat `LICENSE`.
