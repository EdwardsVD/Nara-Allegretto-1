import { Link } from 'react-router-dom';
import { ButtonLink } from '../components/ui/Button';
import { useAuth } from '../lib/auth/AuthContext';
import { usePageTitle } from '../lib/usePageTitle';

const FEATURES = [
  {
    title: 'Ngobrol tanpa berisik',
    body: 'Satu kolom percakapan, tanpa notifikasi dan tanpa distraksi. Enter untuk kirim, Shift+Enter untuk baris baru.',
    icon: (
      <svg aria-hidden="true" viewBox="0 0 24 24" className="h-5 w-5" fill="none" stroke="currentColor" strokeWidth="1.7">
        <path d="M4 5.5A1.5 1.5 0 0 1 5.5 4h13A1.5 1.5 0 0 1 20 5.5v9a1.5 1.5 0 0 1-1.5 1.5H9l-5 4V5.5Z" strokeLinecap="round" strokeLinejoin="round" />
      </svg>
    ),
  },
  {
    title: 'Privasi sejak awal',
    body: 'Riwayat percakapan tidak disimpan di server maupun perangkat. Mulai percakapan kosong kapan pun.',
    icon: (
      <svg aria-hidden="true" viewBox="0 0 24 24" className="h-5 w-5" fill="none" stroke="currentColor" strokeWidth="1.7">
        <path d="M12 3.5 19 6v5.5c0 4.2-2.9 7.6-7 9-4.1-1.4-7-4.8-7-9V6l7-2.5Z" strokeLinejoin="round" />
        <path d="m9.2 11.8 2 2 3.6-3.8" strokeLinecap="round" strokeLinejoin="round" />
      </svg>
    ),
  },
  {
    title: 'Akun yang jujur',
    body: 'Kelola nama tampilan, keamanan, dan ekspor data dari satu halaman profil. Tanpa menu tersembunyi.',
    icon: (
      <svg aria-hidden="true" viewBox="0 0 24 24" className="h-5 w-5" fill="none" stroke="currentColor" strokeWidth="1.7">
        <circle cx="12" cy="8.5" r="3.5" />
        <path d="M5 20c.8-3.4 3.6-5.2 7-5.2s6.2 1.8 7 5.2" strokeLinecap="round" />
      </svg>
    ),
  },
];

const CHAT_PREVIEW = [
  { role: 'user' as const, text: 'Apa itu uang rupiah?' },
  {
    role: 'nara' as const,
    text: 'Rupiah adalah mata uang Indonesia, dan uang pertama Republik Indonesia diterbitkan tahun 1946.',
  },
  { role: 'user' as const, text: 'Terima kasih!' },
  { role: 'nara' as const, text: 'Sama-sama. Ada lagi yang ingin ditanyakan?' },
];

export function Landing() {
  usePageTitle('Beranda');
  const { user } = useAuth();

  return (
    <div className="bg-canvas">
      {/* Hero */}
      <section className="relative overflow-hidden">
        <div aria-hidden="true" className="pointer-events-none absolute inset-0 bg-grid" />
        <div className="relative mx-auto grid w-full max-w-6xl items-center gap-14 px-4 pb-20 pt-14 sm:px-6 sm:pt-20 lg:grid-cols-[1.02fr_0.98fr] lg:gap-16">
          <div className="space-y-7">
            <p className="inline-flex items-center gap-2 rounded-full border border-accent-400/50 bg-accent-50/80 px-3 py-1 text-[11px] font-semibold uppercase tracking-[0.16em] text-accent-800 backdrop-blur dark:bg-accent-400/10 dark:text-accent-200">
              <span className="relative flex h-1.5 w-1.5">
                <span className="absolute inline-flex h-full w-full animate-ping rounded-full bg-accent-500 opacity-70 motion-reduce:animate-none" />
                <span className="relative inline-flex h-1.5 w-1.5 rounded-full bg-accent-500" />
              </span>
              Nara · asisten AI bahasa Indonesia
            </p>

            <h1 className="text-balance text-4xl font-semibold leading-[1.06] tracking-tight text-ink-900 sm:text-5xl lg:text-[3.4rem] dark:text-ink-50">
              Tempat tenang untuk{' '}
              <span className="relative inline-block">
                <span className="relative z-10">bertanya</span>
                <span
                  aria-hidden="true"
                  className="absolute inset-x-0 bottom-1 z-0 h-3 rounded-sm bg-accent-300/70 dark:bg-accent-400/30"
                />
              </span>{' '}
              dan berpikir.
            </h1>

            <p className="max-w-xl text-pretty text-lg leading-relaxed text-ink-600 dark:text-ink-300">
              Nara menjawab dalam bahasa Indonesia dengan gaya ringkas dan jelas. Buka chat,
              ketik pertanyaan, selesai — tanpa membuat akun pun bisa.
            </p>

            <div className="flex flex-wrap items-center gap-3">
              <ButtonLink to="/chat" size="lg" className="shadow-lift">
                Mulai chat
                <svg aria-hidden="true" viewBox="0 0 20 20" className="h-4 w-4" fill="none" stroke="currentColor" strokeWidth="1.8">
                  <path d="M4 10h11m0 0-4-4m4 4-4 4" strokeLinecap="round" strokeLinejoin="round" />
                </svg>
              </ButtonLink>
              {user ? (
                <ButtonLink to="/profile" variant="secondary" size="lg">
                  Kelola profil
                </ButtonLink>
              ) : (
                <ButtonLink to="/register" variant="secondary" size="lg">
                  Buat akun
                </ButtonLink>
              )}
            </div>

            <dl className="grid max-w-md grid-cols-3 gap-4 border-t border-ink-200 pt-5 dark:border-ink-800">
              <div>
                <dt className="text-[11px] uppercase tracking-wide text-ink-500 dark:text-ink-400">Riwayat</dt>
                <dd className="mt-0.5 text-sm font-semibold text-ink-900 dark:text-ink-50">Tidak disimpan</dd>
              </div>
              <div>
                <dt className="text-[11px] uppercase tracking-wide text-ink-500 dark:text-ink-400">Akun</dt>
                <dd className="mt-0.5 text-sm font-semibold text-ink-900 dark:text-ink-50">Opsional</dd>
              </div>
              <div>
                <dt className="text-[11px] uppercase tracking-wide text-ink-500 dark:text-ink-400">Bahasa</dt>
                <dd className="mt-0.5 text-sm font-semibold text-ink-900 dark:text-ink-50">Indonesia</dd>
              </div>
            </dl>
          </div>

          {/* Pratinjau chat */}
          <div className="relative">
            <div
              aria-hidden="true"
              className="absolute -inset-4 rounded-[2rem] bg-gradient-to-br from-accent-300/30 via-transparent to-transparent blur-2xl dark:from-accent-400/15"
            />
            <div className="relative overflow-hidden rounded-3xl border border-ink-200/80 bg-white/90 shadow-lift backdrop-blur dark:border-ink-800 dark:bg-ink-900/80">
              <div className="flex items-center justify-between border-b border-ink-200/80 px-4 py-3 dark:border-ink-800">
                <div className="flex items-center gap-2 text-xs font-medium text-ink-500 dark:text-ink-400">
                  <span className="flex gap-1.5" aria-hidden="true">
                    <span className="h-2 w-2 rounded-full bg-red-400/80" />
                    <span className="h-2 w-2 rounded-full bg-amber-400/80" />
                    <span className="h-2 w-2 rounded-full bg-emerald-400/80" />
                  </span>
                  <span className="ml-1.5">nara · percakapan baru</span>
                </div>
                <span className="rounded-full bg-ink-100 px-2 py-0.5 text-[10px] font-medium text-ink-500 dark:bg-ink-800 dark:text-ink-400">
                  demo
                </span>
              </div>

              <div className="space-y-3 px-4 py-4" aria-hidden="true">
                {CHAT_PREVIEW.map((message, index) => (
                  <div
                    key={index}
                    className={`flex ${message.role === 'user' ? 'justify-end' : 'justify-start'}`}
                  >
                    <div
                      className={`max-w-[85%] rounded-2xl px-4 py-2.5 text-sm leading-relaxed ${
                        message.role === 'user'
                          ? 'rounded-br-md bg-accent-400 text-ink-950'
                          : 'rounded-bl-md border border-ink-200/80 bg-ink-50 text-ink-700 dark:border-ink-800 dark:bg-ink-800 dark:text-ink-200'
                      }`}
                    >
                      {message.text}
                    </div>
                  </div>
                ))}
              </div>

              <div className="border-t border-ink-200/80 px-4 py-3 dark:border-ink-800">
                <div className="flex items-center gap-2 rounded-xl border border-ink-200 px-3 py-2.5 text-sm text-ink-400 dark:border-ink-800 dark:text-ink-500">
                  <span className="flex-1">Tulis pesan…</span>
                  <span className="rounded-md bg-accent-400 px-2.5 py-1 text-xs font-semibold text-ink-950">
                    Kirim
                  </span>
                </div>
              </div>
            </div>

            <span className="absolute -bottom-4 -left-4 hidden rounded-xl border border-ink-200 bg-white px-3 py-2 text-[11px] font-medium text-ink-600 shadow-card sm:block dark:border-ink-800 dark:bg-ink-900 dark:text-ink-300">
              ✓ Tidak ada riwayat tersimpan
            </span>
          </div>
        </div>
      </section>

      {/* Fitur */}
      <section className="border-y border-ink-200 bg-white/70 py-16 dark:border-ink-800 dark:bg-ink-900/40">
        <div className="mx-auto w-full max-w-6xl px-4 sm:px-6">
          <div className="mb-10 max-w-2xl">
            <h2 className="text-2xl font-semibold tracking-tight text-ink-900 sm:text-3xl dark:text-ink-50">
              Dirancang untuk dipakai, bukan dipamerkan.
            </h2>
            <p className="mt-2 text-ink-600 dark:text-ink-300">
              Tiga hal yang paling sering diminta pengguna chat AI, dikerjakan dengan sederhana.
            </p>
          </div>
          <div className="grid gap-5 sm:grid-cols-3">
            {FEATURES.map((feature) => (
              <div
                key={feature.title}
                className="group rounded-2xl border border-ink-200 bg-white p-5 transition-all hover:-translate-y-0.5 hover:shadow-card motion-reduce:hover:translate-y-0 dark:border-ink-800 dark:bg-ink-900"
              >
                <span className="mb-4 inline-grid h-10 w-10 place-items-center rounded-xl border border-accent-400/40 bg-accent-50 text-accent-800 dark:bg-accent-400/10 dark:text-accent-200">
                  {feature.icon}
                </span>
                <h3 className="text-base font-semibold text-ink-900 dark:text-ink-50">
                  {feature.title}
                </h3>
                <p className="mt-1.5 text-sm leading-relaxed text-ink-600 dark:text-ink-400">
                  {feature.body}
                </p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Cara kerja */}
      <section className="mx-auto w-full max-w-6xl px-4 py-16 sm:px-6">
        <div className="grid gap-10 lg:grid-cols-[0.9fr_1.1fr] lg:items-start">
          <div className="space-y-3">
            <h2 className="text-2xl font-semibold tracking-tight text-ink-900 sm:text-3xl dark:text-ink-50">
              Tiga langkah, tanpa basa-basi.
            </h2>
            <p className="text-ink-600 dark:text-ink-300">
              Tidak perlu verifikasi email untuk mencoba. Akun hanya dibutuhkan untuk halaman
              profil.
            </p>
            <Link
              to="/tos"
              className="inline-flex items-center gap-1 text-sm font-medium text-accent-700 underline underline-offset-4 hover:text-accent-800 dark:text-accent-300"
            >
              Baca syarat penggunaan
              <span aria-hidden="true">↗</span>
            </Link>
          </div>

          <ol className="space-y-3">
            {[
              ['Buka chat', 'Tamu bisa langsung mengetik. Tidak ada layar pembuka yang memaksa daftar.'],
              ['Ajukan pertanyaan', 'Kirim dengan Enter. Riwayat percakapan dibersihkan saat halaman dimuat ulang.'],
              ['Kelola akun (opsional)', 'Ganti nama tampilan, unduh data, atau hapus akun dari halaman profil.'],
            ].map(([title, body], index) => (
              <li
                key={title}
                className="flex gap-4 rounded-2xl border border-ink-200 bg-white p-4 dark:border-ink-800 dark:bg-ink-900"
              >
                <span className="grid h-8 w-8 shrink-0 place-items-center rounded-full bg-accent-400 text-sm font-semibold text-ink-950">
                  {index + 1}
                </span>
                <div>
                  <p className="font-medium text-ink-900 dark:text-ink-50">{title}</p>
                  <p className="mt-0.5 text-sm leading-relaxed text-ink-600 dark:text-ink-400">{body}</p>
                </div>
              </li>
            ))}
          </ol>
        </div>
      </section>

      {/* CTA */}
      <section className="mx-auto w-full max-w-6xl px-4 pb-20 sm:px-6">
        <div className="relative overflow-hidden rounded-3xl border border-ink-200 bg-ink-900 p-8 text-ink-50 shadow-lift sm:p-10 dark:border-ink-800 dark:bg-ink-900">
          <div
            aria-hidden="true"
            className="pointer-events-none absolute -right-24 -top-24 h-64 w-64 rounded-full bg-accent-400/20 blur-3xl"
          />
          <div className="relative flex flex-col items-start justify-between gap-6 md:flex-row md:items-center">
            <div className="space-y-2">
              <h2 className="text-2xl font-semibold tracking-tight sm:text-3xl">Siap mencoba?</h2>
              <p className="max-w-lg text-sm leading-relaxed text-ink-300">
                Bisa langsung tanpa akun. Mode demo saat ini memakai data lokal — tidak ada
                email atau OAuth sungguhan.
              </p>
            </div>
            <div className="flex flex-wrap gap-3">
              <ButtonLink to="/chat">Buka chat</ButtonLink>
              <Link
                to="/download"
                className="inline-flex h-11 items-center rounded-xl border border-white/20 px-4 text-sm font-medium text-ink-100 transition-colors hover:bg-white/10 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent-400"
              >
                Lihat unduhan
              </Link>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}
