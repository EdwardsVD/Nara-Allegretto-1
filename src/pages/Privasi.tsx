import { usePageTitle } from '../lib/usePageTitle';

const SECTIONS = [
  {
    title: 'Data yang disimpan',
    body: 'Dalam mode demo, data akun (email, nama tampilan, status verifikasi, tanggal bergabung) hanya disimpan di localStorage peramban Anda. Password tidak pernah disimpan dalam bentuk apa pun.',
  },
  {
    title: 'Riwayat chat',
    body: 'Percakapan tidak disimpan di perangkat maupun di server. Riwayat hanya hidup di memori halaman dan hilang saat halaman dimuat ulang.',
  },
  {
    title: 'Ekspor dan hapus',
    body: 'Anda dapat mengunduh data akun dalam format JSON atau menghapus akun sepenuhnya dari halaman Profil. Penghapusan bersifat langsung dan tidak dapat dibatalkan.',
  },
  {
    title: 'Cookie dan penyimpanan lokal',
    body: 'Aplikasi memakai localStorage untuk preferensi tema (nara_theme) dan data akun demo, serta sessionStorage untuk email yang menunggu verifikasi (nara_pending_email). Tidak ada cookie pelacak.',
  },
  {
    title: 'Analitik dan pihak ketiga',
    body: 'Aplikasi ini tidak memuat skrip analitik, pixel, atau pelacak pihak ketiga. Font memakai font sistem, bukan CDN eksternal.',
  },
  {
    title: 'Hak Anda',
    body: 'Anda berhak mengetahui data apa yang tersimpan (unduh data), memperbaikinya (ubah nama tampilan), dan menghapusnya (hapus akun). Semua tindakan tersedia di halaman Profil.',
  },
];

export function Privasi() {
  usePageTitle('Kebijakan Privasi');

  return (
    <div className="bg-canvas">
      <article className="mx-auto w-full max-w-3xl px-4 py-12 sm:px-6 sm:py-16">
        <header className="mb-8 space-y-2 border-b border-ink-200 pb-5 dark:border-ink-800">
          <p className="text-[11px] font-semibold uppercase tracking-[0.16em] text-accent-700 dark:text-accent-300">
            Legal
          </p>
          <h1 className="text-3xl font-semibold tracking-tight text-ink-900 sm:text-4xl dark:text-ink-50">
            Kebijakan Privasi
          </h1>
          <p className="text-sm text-ink-500 dark:text-ink-400">
            Terakhir diperbarui: 1 Januari 2026 · Berlaku untuk versi demo
          </p>
        </header>

        <div className="mb-8 grid gap-3 sm:grid-cols-3">
          {[
            ['Riwayat chat', 'Tidak disimpan'],
            ['Password', 'Tidak disimpan'],
            ['Pelacak', 'Tidak ada'],
          ].map(([label, value]) => (
            <div
              key={label}
              className="rounded-xl border border-ink-200 bg-white/80 px-4 py-3 dark:border-ink-800 dark:bg-ink-900/70"
            >
              <p className="text-[11px] uppercase tracking-wide text-ink-500 dark:text-ink-400">{label}</p>
              <p className="mt-0.5 text-sm font-semibold text-ink-900 dark:text-ink-50">{value}</p>
            </div>
          ))}
        </div>

        <div className="space-y-8">
          {SECTIONS.map((section, index) => (
            <section key={section.title} className="space-y-2">
              <h2 className="text-lg font-semibold text-ink-900 dark:text-ink-50">
                {index + 1}. {section.title}
              </h2>
              <p className="text-sm leading-relaxed text-ink-700 dark:text-ink-300">{section.body}</p>
            </section>
          ))}
        </div>
      </article>
    </div>
  );
}
