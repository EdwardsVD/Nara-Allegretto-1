import { Link } from 'react-router-dom';
import { Banner } from '../components/ui/Banner';
import { usePageTitle } from '../lib/usePageTitle';

/**
 * Ditampilkan di /login dan /register saat build production tidak
 * mengizinkan mode dummy (VITE_ALLOW_DUMMY_AUTH bukan "true") dan mode
 * http belum tersedia.
 */
export function AuthDisabled({ action }: { action: 'login' | 'register' }) {
  usePageTitle(action === 'login' ? 'Masuk tidak tersedia' : 'Daftar tidak tersedia');

  return (
    <div className="space-y-4">
      <header className="space-y-1">
        <h1 className="text-2xl font-semibold tracking-tight text-ink-900 dark:text-ink-50">
          Autentikasi belum diaktifkan
        </h1>
        <p className="text-sm text-ink-600 dark:text-ink-300">
          {action === 'login'
            ? 'Fitur masuk akun belum tersedia pada build ini.'
            : 'Pendaftaran akun belum tersedia pada build ini.'}
        </p>
      </header>

      <Banner tone="warning">
        Mode demo tidak diizinkan di build produksi. Hubungi pengelola untuk mengaktifkan
        backend autentikasi (<code className="font-mono">VITE_AUTH_MODE=http</code>) atau
        mengatur <code className="font-mono">VITE_ALLOW_DUMMY_AUTH=true</code>.
      </Banner>

      <p className="text-sm text-ink-600 dark:text-ink-300">
        Anda tetap bisa memakai chat sebagai tamu.
      </p>
      <div className="flex flex-col gap-2">
        <Link
          to="/chat"
          className="inline-flex h-11 items-center justify-center rounded-xl bg-accent-400 px-4 text-sm font-semibold text-ink-950 transition-colors hover:bg-accent-300 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent-400 focus-visible:ring-offset-2 dark:focus-visible:ring-offset-ink-900"
        >
          Buka chat
        </Link>
        <Link
          to="/"
          className="inline-flex h-11 items-center justify-center rounded-xl border border-ink-300 px-4 text-sm font-medium text-ink-800 transition-colors hover:bg-ink-100 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent-400 dark:border-ink-700 dark:text-ink-100 dark:hover:bg-ink-800"
        >
          Kembali ke beranda
        </Link>
      </div>
    </div>
  );
}
