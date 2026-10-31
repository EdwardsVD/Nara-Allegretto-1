import { Link } from 'react-router-dom';
import { Card, CardBody, CardHeader } from '../components/ui/Card';
import { usePageTitle } from '../lib/usePageTitle';
import { useAuth } from '../lib/auth/AuthContext';

const PLATFORMS = [
  {
    name: 'Web',
    status: 'Tersedia',
    detail: 'Chrome, Firefox, Safari, Edge versi terbaru.',
    ready: true,
  },
  {
    name: 'Pasang sebagai aplikasi',
    status: 'Tersedia',
    detail: 'Gunakan "Tambahkan ke layar utama" pada menu browser.',
    ready: true,
  },
  {
    name: 'Desktop',
    status: 'Belum tersedia',
    detail: 'Installer native akan menyusul setelah backend tersedia.',
    ready: false,
  },
  {
    name: 'Android / iOS',
    status: 'Belum tersedia',
    detail: 'Aplikasi mobile direncanakan setelah API stabil.',
    ready: false,
  },
];

export function Download() {
  usePageTitle('Download');
  const { user } = useAuth();

  return (
    <div className="bg-canvas">
      <div className="mx-auto w-full max-w-4xl px-4 py-12 sm:px-6 sm:py-16">
        <header className="mb-8 max-w-2xl space-y-3">
          <p className="text-[11px] font-semibold uppercase tracking-[0.16em] text-accent-700 dark:text-accent-300">
            Download
          </p>
          <h1 className="text-3xl font-semibold tracking-tight text-ink-900 sm:text-4xl dark:text-ink-50">
            Nara berjalan di peramban Anda.
          </h1>
          <p className="text-ink-600 dark:text-ink-300">
            Tidak ada installer yang perlu diunduh. Semua fitur tersedia langsung di web, dan
            bisa dipasang sebagai aplikasi ringan dari menu browser.
          </p>
        </header>

        <div className="mb-6 flex flex-wrap gap-3">
          <Link
            to="/chat"
            className="focus-ring inline-flex h-11 items-center gap-2 rounded-xl bg-accent-400 px-5 text-sm font-semibold text-ink-950 transition-colors hover:bg-accent-300"
          >
            Buka chat
            <svg aria-hidden="true" viewBox="0 0 20 20" className="h-4 w-4" fill="none" stroke="currentColor" strokeWidth="1.8">
              <path d="M4 10h11m0 0-4-4m4 4-4 4" strokeLinecap="round" strokeLinejoin="round" />
            </svg>
          </Link>
          {!user ? (
            <Link
              to="/register"
              className="focus-ring inline-flex h-11 items-center rounded-xl border border-ink-300 px-5 text-sm font-medium text-ink-800 transition-colors hover:bg-ink-100 dark:border-ink-700 dark:text-ink-100 dark:hover:bg-ink-800"
            >
              Buat akun opsional
            </Link>
          ) : null}
        </div>

        <Card>
          <CardHeader title="Ketersediaan platform" description="Status saat ini." />
          <CardBody className="p-0">
            <ul className="divide-y divide-ink-200 dark:divide-ink-800">
              {PLATFORMS.map((platform) => (
                <li key={platform.name} className="flex items-start justify-between gap-4 px-5 py-4">
                  <div>
                    <p className="text-sm font-medium text-ink-900 dark:text-ink-50">{platform.name}</p>
                    <p className="mt-0.5 text-xs text-ink-500 dark:text-ink-400">{platform.detail}</p>
                  </div>
                  <span
                    className={`shrink-0 rounded-full px-2.5 py-1 text-[11px] font-semibold ${
                      platform.ready
                        ? 'bg-emerald-100 text-emerald-800 dark:bg-emerald-950/60 dark:text-emerald-200'
                        : 'bg-ink-200 text-ink-600 dark:bg-ink-800 dark:text-ink-300'
                    }`}
                  >
                    {platform.status}
                  </span>
                </li>
              ))}
            </ul>
          </CardBody>
        </Card>

        <div className="mt-6 grid gap-4 sm:grid-cols-2">
          <Card>
            <CardBody className="space-y-2">
              <h2 className="text-sm font-semibold text-ink-900 dark:text-ink-50">Yang perlu disiapkan</h2>
              <ul className="list-disc space-y-1 pl-5 text-sm text-ink-600 dark:text-ink-400">
                <li>Peramban modern (rilis 2 tahun terakhir).</li>
                <li>JavaScript aktif.</li>
                <li>Tidak perlu akun untuk mulai chat.</li>
              </ul>
            </CardBody>
          </Card>
          <Card>
            <CardBody className="space-y-2">
              <h2 className="text-sm font-semibold text-ink-900 dark:text-ink-50">Catatan mode demo</h2>
              <p className="text-sm text-ink-600 dark:text-ink-400">
                Akun pada build ini disimulasikan di perangkat Anda. Jangan memakai password
                asli, dan jangan mengandalkan data untuk jangka panjang.
              </p>
            </CardBody>
          </Card>
        </div>
      </div>
    </div>
  );
}
