import { usePageTitle } from '../lib/usePageTitle';
import { ButtonLink } from '../components/ui/Button';

const LINKS = [
  { to: '/', label: 'Beranda', detail: 'Kembali ke halaman utama' },
  { to: '/chat', label: 'Chat', detail: 'Mulai percakapan baru' },
  { to: '/download', label: 'Download', detail: 'Informasi platform' },
  { to: '/tos', label: 'Syarat', detail: 'Ketentuan penggunaan' },
];

export function NotFound() {
  usePageTitle('Halaman tidak ditemukan');

  return (
    <div className="bg-canvas">
      <div className="mx-auto flex w-full max-w-2xl flex-col items-start gap-6 px-4 py-20 sm:px-6 sm:py-28">
        <p className="font-mono text-sm font-semibold tracking-[0.25em] text-accent-700 dark:text-accent-300">
          404
        </p>
        <div className="space-y-3">
          <h1 className="text-3xl font-semibold tracking-tight text-ink-900 sm:text-4xl dark:text-ink-50">
            Halaman tidak ditemukan
          </h1>
          <p className="max-w-md text-ink-600 dark:text-ink-300">
            Alamat yang Anda buka tidak ada atau sudah dipindahkan. Pilih salah satu tujuan di
            bawah untuk melanjutkan.
          </p>
        </div>

        <ButtonLink to="/">Kembali ke beranda</ButtonLink>

        <ul className="mt-2 grid w-full gap-2 sm:grid-cols-2">
          {LINKS.map((link) => (
            <li key={link.to}>
              <a
                href={link.to}
                className="focus-ring block rounded-xl border border-ink-200 bg-white/70 px-4 py-3 transition-colors hover:border-accent-400 dark:border-ink-800 dark:bg-ink-900/70 dark:hover:border-accent-500/60"
              >
                <span className="block text-sm font-medium text-ink-900 dark:text-ink-50">
                  {link.label}
                </span>
                <span className="block text-xs text-ink-500 dark:text-ink-400">{link.detail}</span>
              </a>
            </li>
          ))}
        </ul>

        <p className="mt-2 w-full break-all rounded-lg bg-ink-100 px-3 py-2 font-mono text-[11px] text-ink-500 dark:bg-ink-900 dark:text-ink-500">
          {typeof window !== 'undefined' ? window.location.pathname : ''}
        </p>
      </div>
    </div>
  );
}
