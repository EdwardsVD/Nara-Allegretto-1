# Nara-Allegretto-2 — Dataset Latihan Bahasa Indonesia (~51 MiB)

Repositori ini berisi dataset latihan percakapan dan instruksi berbahasa Indonesia untuk model bahasa kecil **Nara-Allegretto-2** (beserta versi terdahulu **Nara-Allegretto-1** yang tetap disimpan utuh agar mudah melakukan *rollback*).

Pada **v2 (`Nara-Allegretto-2`)**, fokus dataset digeser secara signifikan dari dominasi matematika menjadi **percakapan sehari-hari yang alami** serta **pemrograman sederhana teruji otomatis** (`Python`, `JavaScript`, `TypeScript`, `HTML`, `CSS`, `C++`, `C`, `SQL`, `Bash`, `JSON`).

## Berkas Utama (Versi Aktif & Arsip)

| Berkas | Versi | Ukuran | Keterangan |
| --- | :---: | ---: | --- |
| `Nara-Allegretto-2.jsonl` | **v2 (Aktif)** | **53.313.731 B (50,84 MiB)** | Dataset utama v2, 141.311 baris JSONL UTF-8 terverifikasi |
| `Nara-Allegretto-2.zip` | **v2 (Aktif)** | **14,53 MB (13,86 MiB)** | Arsip ZIP rilis v2 berisi `Nara-Allegretto-2.jsonl` dan `README.md` |
| `tools/v2/` | **v2** | — | Pipeline modular per kategori, penguji kode 10 bahasa, validator ketat, & uji latih cepat |
| `data_Nara_Allegretto_1.jsonl` | v1 | 31.857.993 B (30,38 MiB) | Dataset rilis v1 (126.397 baris), disimpan utuh untuk *rollback* |
| `data_Nara_Allegretto_1.zip` | v1 | 4.970.078 B (4,74 MiB) | Arsip ZIP rilis v1 |
| `data_chat.jsonl` | v0 | 11.280.828 B (10,76 MiB) | Arsip dataset awal |

## Statistik `Nara-Allegretto-2.jsonl` (v2)

- Ukuran berkas: **53.313.731 byte (50,84 MiB / 53,31 MB)**
- Jumlah contoh: **141.311 pasangan (`user` -> `assistant`)**
- Duplikat pertanyaan (`lowercase + trim` & normalisasi): **0**
- Duplikat jawaban (`lowercase + trim` & normalisasi): **0**
- Karakter rusak / mojibake: **0**
- Kegagalan uji kode (`16.571` cuplikan kode, maks. 8 baris): **0**
- Kesalahan persamaan aritmetika (`36.582` persamaan dicek): **0**
- Panjang jawaban: min **45**, median **159**, rata-rata **212,8**, maks **543** karakter

### Komposisi per Kategori (`build/v2/*.jsonl`)

| File Kategori | Contoh | Ukuran | Porsi Byte | Cakupan Materi |
| --- | ---: | ---: | ---: | --- |
| `chat.jsonl` | **43.983** | **25,26 MiB** | **49,7%** | Sapaan beragam (`halo`, `hai`, `p`, `woi`), persona konsisten `Nara-Allegretto-2` (`aku/kamu`), curhat & keseharian, kuliner/budaya Nusantara, kerja kelompok, etika sosial, jujur `"aku nggak tahu"` untuk info *real-time*, & penolakan aman |
| `kode.jsonl` | **16.571** | **7,18 MiB** | **14,1%** | Cuplikan pendek (`<= 8` baris) teruji otomatis: Python (6.618), JS (3.502), TS (2.451), CSS (2.151), HTML (2.150), C++ (1.700), SQL (550), C (400), Bash (301), JSON (300), serta konsep coding/Git |
| `pengetahuan.jsonl` | **3.172** | **0,75 MiB** | **1,5%** | Provinsi, taman nasional, rumah adat, alat musik daerah, kerajaan Nusantara, sains harian, tokoh, besaran SI, & teknologi |
| `bahasa.jsonl` | **41.085** | **8,23 MiB** | **16,2%** | Kata baku KBBI, sinonim/antonim, peribahasa, ungkapan, kalimat efektif, imbuhan, terjemahan dasar, & analisis kata |
| `math.jsonl` | **36.500** | **9,43 MiB** | **18,6%** | Aritmetika dasar, soal cerita harian, pecahan, persen/diskon, rasio, geometri dasar, KPK/FPB, & pola bilangan |
| **Total Gabungan** | **141.311** | **50,84 MiB** | **100%** | Digabung & diacak secara deterministik ke `Nara-Allegretto-2.jsonl` |

## Prinsip Kualitas & Pipeline v2 (`tools/v2/`)

1. **Pisah per kategori sebelum digabung** (`build/v2/{chat,kode,pengetahuan,bahasa,math}.jsonl`) sehingga pelacakan *bug* langsung merujuk ke satu berkas spesifik.
2. **Serialisasi murni Python** menggunakan `json.dumps(obj, ensure_ascii=False)` — tanpa `echo` Bash agar kutip dan karakter khusus selalu aman.
3. **Semua kode diuji otomatis sebelum masuk dataset** (`tools/v2/code_verifier.py`):
   - **Python**: `ast.parse()` + eksekusi langsung & pencocokan `stdout` terhadap jawaban penjelasan.
   - **JavaScript & TypeScript**: strip tipe TS (`node:module`) + eksekusi sandbox `vm` + `node --check`.
   - **C++ & C**: kompilasi nyata dengan `g++ -std=c++17` / `gcc -std=c11`, eksekusi biner, dan pencocokan keluaran.
   - **SQL, Bash, HTML, CSS, JSON**: diuji di `sqlite3` *in-memory*, `bash -n`, `HTMLParser`, pemeriksa CSS, dan `json.loads`.
   - Seluruh cuplikan kode dibatasi **maksimal 8 baris** agar ramah bagi kapasitas model kecil.
4. **Persona & variasi percakapan**: gaya santai akrab `aku`/`kamu` (tanpa `saya`/`anda`), 5–10 variasi gaya bertanya per topik, jawaban bervariasi nyata, serta kejujuran mengakui batas pengetahuan (`"aku nggak tahu"` untuk cuaca/harga/lalu lintas *real-time*).
5. **Uji latih skala kecil (`--pilot`, `EPOCHS=2`) & audit manual**: diuji pada 500 contoh/kategori sebelum generasi penuh, lalu diaudit manual pada sampel acak tiap kategori.

## Format Baris & Cara Memuat

```json
{"messages": [{"role": "user", "content": "p nara"}, {"role": "assistant", "content": "Hadir! Mau ngobrol santai, bahas koding tipis-tipis, atau tanya sesuatu nih?"}]}
```

```python
import json

with open("Nara-Allegretto-2.jsonl", encoding="utf-8") as f:
    for line in f:
        row = json.loads(line)
```

## Membangun Ulang & Memvalidasi (v2)

```bash
# 1. Uji skala kecil dulu (500 contoh per kategori + sanity check EPOCHS=2)
python3 tools/v2/build_v2.py --pilot
python3 tools/v2/pilot_train_check.py build/v2_pilot/pilot_merged.jsonl --epochs 2

# 2. Bangun dataset penuh (~50,84 MiB) & validasi menyeluruh
python3 tools/v2/build_v2.py --report build/v2/build_report.json
python3 tools/v2/validate_v2.py Nara-Allegretto-2.jsonl

# 3. Ambil sampel acak 30-50 baris per kategori untuk cek manual
python3 tools/v2/manual_sample.py build/v2 --count 40 --out build/v2/manual_audit_samples.txt
```

Untuk membangun ulang dataset **v1 (`Nara-Allegretto-1`)**, skrip asli di `tools/build_dataset.py` dan `tools/validate_dataset.py` tetap dipertahankan tanpa perubahan.

## Lisensi

MIT — lihat `LICENSE`.
