# Nara Web

Antarmuka chat **Nara** (Vite + React + TypeScript + Tailwind + React Router) dengan alur akun **dummy** di balik adapter autentikasi, sidebar aplikasi, dan halaman profil.

> **MODE DEMO** — tidak ada backend, OAuth, atau email sungguhan. Kode verifikasi: `123456`.

---

## Ringkasan cepat

| Hal | Nilai |
| --- | --- |
| Stack | React 19, TypeScript, Vite 8, Tailwind CSS 3, React Router 7 |
| Tes | Vitest + Testing Library + jsdom (33 tes) |
| Auth | `src/lib/auth` (adapter `dummy` / `http`) |
| Chat | `src/lib/chat` (mode `mock` / `http`) |
| Tema | Gelap default, tersimpan di `localStorage` kunci `nara_theme` |

## Menjalankan

```bash
npm install
npm run dev      # http://localhost:5173
npm run lint
npm run build
npm test
```

Konfigurasi lingkungan: salin `.env.example` menjadi `.env` lalu sesuaikan.

| Variabel | Nilai | Arti |
| --- | --- | --- |
| `VITE_AUTH_MODE` | `dummy` \| `http` | Adapter auth yang dipakai |
| `VITE_ALLOW_DUMMY_AUTH` | `true` \| `false` | Di build production, mode dummy hanya aktif bila `true`. Di dev selalu boleh. |
| `VITE_CHAT_MODE` | `mock` \| `http` | `mock` = balasan contoh lokal, `http` = `POST /api/chat` |
| `VITE_CHAT_REQUIRES_LOGIN` | `true` \| `false` | Bila `true`, tamu yang membuka `/chat` diarahkan ke `/login?next=/chat` |

Build production dengan `VITE_AUTH_MODE=dummy` + `VITE_ALLOW_DUMMY_AUTH=false` akan menampilkan halaman **“Autentikasi belum diaktifkan”** di `/login` dan `/register` (chat tamu tetap bisa dipakai).

## Peta rute

| Rute | Isi | Guard |
| --- | --- | --- |
| `/` | Landing | publik |
| `/login` | Form masuk | `GuestOnly` → `/chat` (atau `?next=/profile`) bila sudah login |
| `/register` | Form daftar | `GuestOnly` |
| `/register/verifikasi` | Kode 6 digit | `PendingOnly` → `/register` bila tidak ada pendaftaran menunggu |
| `/chat` | Chat + sidebar | publik, kecuali `VITE_CHAT_REQUIRES_LOGIN=true` |
| `/profile` | Profil & pengaturan | `RequireAuth` → `/login?next=/profile` |
| `/download`, `/tos`, `/privasi` | Halaman statis | publik |
| `*` | 404 + tombol kembali | publik |

Aturan `?next=` (allowlist): hanya `/chat` dan `/profile`. Nilai lain (`//evil.com`, `https://x.com`, `/tos`, `/\x`) diabaikan diam-diam dan diganti `/chat` — lihat `src/lib/navigation.ts`.

## Perilaku mode dummy

- Delay buatan **500–900 ms** per panggilan (deterministik, tanpa error acak).
- `localStorage.nara_dummy_users` — array `{ id, email, displayName, provider, verified, createdAt }`.
- `localStorage.nara_dummy_session` — `{ userId, expiresAt }`, berlaku **24 jam**.
- **Password tidak pernah disimpan**; hanya divalidasi panjangnya (min 8 karakter).
- Register dengan email yang sudah terdaftar memberi balasan yang sama persis (tidak membocorkan akun).
- Verifikasi: kode `123456`. Salah 5× → input terkunci 30 detik dengan hitung mundur; jatah percobaan pulih saat pengguna mengetik lagi setelah kunci berakhir.
- Kirim ulang kode: tombol nonaktif 60 detik.
- `loginWithProvider('github' | 'google')` → `demo-github@example.com` / `demo-google@example.com`, `verified: true`.
- `changePassword` hanya untuk akun `email` (akun OAuth: tombol nonaktif + keterangan “Akun dikelola oleh GitHub/Google.”).
- `deleteAccount` menghapus user + sesi; `exportData` mengembalikan profil + `createdAt` (tanpa chat).

## Struktur folder

```
src/
  components/
    auth/      OAuthButtons, PasswordStrength
    chat/      ChatComposer
    layout/    AppLayout, AppSidebar, AuthLayout, PublicLayout, Navbar, Footer, UserMenu, Logo, ThemeToggle, navItems
    ui/        Avatar, Banner, Button, Card, Input, Modal, PasswordInput, Spinner, Toast
  lib/
    auth/      types.ts, dummyAuthApi.ts, httpAuthApi.ts, AuthContext.tsx, guards.tsx, pendingEmail.ts, index.ts
    chat/      chatApi.ts, types.ts, ChatSessionContext.tsx, knowledge.json (sampel jawaban)
    email.ts, env.ts, format.ts, navigation.ts, storage.ts,
    themePreference.ts, useTheme.tsx, useCountdown.ts, useFocusTrap.ts, usePageTitle.ts
  pages/
    Landing, Login, Register, Verifikasi, Chat, Download, Tos, Privasi, NotFound, AuthDisabled
    profile/   ProfilePage, AccountSummary, SecuritySection, ConnectedAccounts, PreferencesSection, DataPrivacySection
  test/        setup + 11 skenario pengujian
  routes.tsx, main.tsx, index.css
```

## Yang ada di versi ini (setelah polish)

- **Sistem visual**: latar `bg-canvas` (gradien aksen + grid halus), kartu kaca, satu aksen amber, radius konsisten, transisi halus, hormati `prefers-reduced-motion`.
- **Landing**: hero dua kolom + pratinjau chat, fitur, langkah "cara kerja", CTA gelap, footer dua kolom.
- **Chat**: saran pertanyaan dengan ikon, sapaan personal untuk pengguna login, gelembung pesan + avatar + jam + tombol salin, render teks aman (tebal/kode/daftar tanpa `dangerouslySetInnerHTML`), indikator mengetik, tombol "pesan terbaru" saat pengguna menggulir ke atas, petunjuk saat memulai chat baru, penghitung karakter dan hint keyboard di composer.
- **Verifikasi**: 6 kotak digit terpisah, mendukung paste, `autocomplete="one-time-code"`, kunci 30 detik, kirim ulang 60 detik.
- **Profil**: navigasi bagian sticky, ringkasan akun, edit nama dengan "Urungkan", keamanan, akun terhubung, preferensi tema, ekspor data, zona bahaya dengan konfirmasi email.
- **Navigasi**: navbar dengan indikator link aktif + bayangan saat scroll, menu seluler, footer dengan kolom Produk/Legal.

## Keamanan & aksesibilitas

- Semua akses `localStorage`/`sessionStorage` lewat `src/lib/storage.ts` (try/catch + validator bentuk data; data rusak dibuang, tidak crash).
- Tidak ada `dangerouslySetInnerHTML`, tidak ada secret di frontend, tidak ada data sensitif di console.
- Input berlabel, `aria-live` untuk error, fokus terlihat, skip-link “Lewati ke konten”, landmark `header/nav/main/aside`, `document.title` per rute.
- Modal & drawer memakai focus trap (Esc menutup, fokus kembali ke pemicu).
- Animasi mengikuti `prefers-reduced-motion`.

## Cara mengganti ke backend sungguhan

1. Implementasikan `src/lib/auth/httpAuthApi.ts` (kontrak sudah ditulis sebagai TODO per fungsi), lalu set `VITE_AUTH_MODE=http`.
2. Implementasikan chat: set `VITE_CHAT_MODE=http` (sudah memanggil `POST /api/chat` relatif, siap di-proxy lewat `vite.config.ts`).

Endpoint yang diharapkan:

| Fungsi | Method & path | Body | Balasan |
| --- | --- | --- | --- |
| `register` | `POST /api/auth/register` | `{ email, password }` | `202 { email, existingAccount, message }` |
| `verify` | `POST /api/auth/verify` | `{ email, code }` | `200 User` + cookie sesi |
| `resend` | `POST /api/auth/resend` | `{ email }` | `204` |
| `login` | `POST /api/auth/login` | `{ email, password }` | `200 User` |
| `loginWithProvider` | `GET /api/auth/oauth/{provider}/start` | — | redirect → `200 User` |
| `logout` | `POST /api/auth/logout` | — | `204` |
| `me` | `GET /api/auth/me` | — | `200 User` \| `204` |
| `updateProfile` | `PATCH /api/account/profile` | `{ displayName }` | `200 User` |
| `changePassword` | `POST /api/account/password` | `{ currentPassword, nextPassword }` | `204` |
| `deleteAccount` | `DELETE /api/account` | — | `204` |
| `exportData` | `GET /api/account/export` | — | `200 ExportedData` |
| chat | `POST /api/chat` | `{ message, history }` | `200 { reply }` |

Kode error backend sebaiknya dipetakan ke `AuthErrorCode`: `INVALID_CREDENTIALS`, `NOT_VERIFIED`, `RATE_LIMITED`, `VALIDATION`, `NETWORK`.

## Catatan data

`data_chat.jsonl` adalah dataset milik repo ini (67.773 baris). Build aplikasi **tidak** memakainya sebagai data produksi; hanya 60 contoh jawaban yang diambil dan disimpan di `src/lib/chat/knowledge.json` (± 7 KB) untuk mode chat `mock`.

## Sengaja belum dibuat

- OAuth & pengiriman email sungguhan, backend FastAPI.
- Penyimpanan riwayat chat (di localStorage maupun server).
- Multi-perangkat nyata (“Keluar dari semua perangkat” hanya simulasi).
- Halaman pengaturan lanjutan (foto profil unggah, 2FA, dsb).
