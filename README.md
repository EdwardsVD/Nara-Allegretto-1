# Nara-Allegretto-1 — Dataset Latihan

Repositori ini berisi dataset latihan untuk **Nara-Allegretto-1**, sebuah model AI kecil
berbahasa Indonesia. Dataset lama (`data_chat.jsonl`) digantikan oleh berkas baru yang
seluruh isinya dibuat ulang, bebas duplikat, dan sudah divalidasi.

## Berkas utama

| Berkas | Keterangan |
| --- | --- |
| `data_Nara_Allegretto_1.jsonl` | Dataset final, 1 contoh per baris (JSONL, UTF-8) |
| `data_Nara_Allegretto_1.zip` | Arsip ZIP berisi dataset dan README ini |
| `tools/` | Pembuat dan pemeriksa dataset (Python 3, tanpa dependensi eksternal) |
| `data_chat.jsonl` | Dataset lama, disimpan hanya sebagai arsip |

## Statistik

- Ukuran: **31.857.993 byte (30,38 MiB)**
- Jumlah contoh: **126.397**
- Format: satu objek JSON per baris
- Duplikat pertanyaan: **0**
- Duplikat jawaban: **0**
- Baris terpanjang: 360 byte (baris kode memakai `\n` yang di-escape, bukan newline asli)
- Panjang jawaban: min 34, median 136, maks 233 karakter

### Komposisi

| Bagian | Contoh |
| --- | ---: |
| Matematika (aritmetika, persen, geometri, soal cerita, deret, KPK/FPB, dll.) | 84.096 |
| Bahasa Indonesia (ejaan, huruf, sinonim/antonim, peribahasa, tata bahasa, terjemahan) | 40.529 |
| Pengetahuan (negara, provinsi, gunung, unsur, hewan, tokoh, peristiwa, sains, teknologi, kesehatan) | 1.489 |
| Percakapan (sapaan, jati diri, empati, keamanan, meta, lelucon, teka-teki) | 283 |
| Kode (Python, JavaScript, HTML, CSS) | 40 |

## Format baris

```json
{"messages": [{"role": "user", "content": "berapa 12 + 7?"}, {"role": "assistant", "content": "19, itu hasilnya. Aku jumlahkan 12 dengan 7, lalu ..."}]}
```

Setiap baris berisi tepat dua pesan: `user` lalu `assistant`. Tidak ada newline mentah
di dalam teks; baris baru pada contoh kode ditulis sebagai `\n`.

## Cara memuat

```python
import json

with open("data_Nara_Allegretto_1.jsonl", encoding="utf-8") as f:
    data = [json.loads(line) for line in f]
```

Contoh di atas memuat 126 ribu objek; untuk data besar sebaiknya baca baris per baris.

## Membangun ulang

```bash
cd tools
python3 build_dataset.py --scale 2.25 --out ../data_Nara_Allegretto_1.jsonl
python3 validate_dataset.py ../data_Nara_Allegretto_1.jsonl
```

- Generator memakai seed tetap `20261022`, jadi hasilnya deterministik.
- `--scale` mengatur jumlah latihan matematika (2.25 menghasilkan ±30 MB).
- Tanpa dependensi pihak ketiga; cukup Python 3.10+.

## Pemeriksaan

`tools/validate_dataset.py` memeriksa:

1. Setiap baris adalah JSON valid dengan kunci `messages` dan dua peran yang benar.
2. Tidak ada spasi berlebih, `\r`, tab, atau newline mentah.
3. Tidak ada kata `saya`/`anda` dan tidak ada nama lama `Nara Ai`/`Nara N1`.
4. Tidak ada pertanyaan atau jawaban duplikat (setelah normalisasi).
5. Panjang jawaban minimal 30 karakter.
6. Setiap persamaan aritmetika dijawab dengan benar (87.799 persamaan diperiksa).

Hasil pemeriksaan terakhir: **0 masalah**.

## Lisensi

MIT — lihat `LICENSE`.
