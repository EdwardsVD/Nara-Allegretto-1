import { Link } from 'react-router-dom';
import { PUBLIC_NAV } from './navItems';
import { Logo } from './Logo';
import { SHOW_DEMO_BANNER } from '../../lib/env';

export function Footer() {
  const year = new Date().getFullYear();

  return (
    <footer className="border-t border-ink-200 bg-white/70 dark:border-ink-800 dark:bg-ink-950/70">
      <div className="mx-auto w-full max-w-6xl px-4 py-10 sm:px-6">
        <div className="flex flex-col gap-8 md:flex-row md:items-start md:justify-between">
          <div className="max-w-sm space-y-3">
            <Logo subtitle="asisten AI" />
            <p className="text-sm leading-relaxed text-ink-600 dark:text-ink-400">
              Ruang chat sederhana berbahasa Indonesia. Riwayat percakapan tidak disimpan di
              server maupun perangkat.
            </p>
            {SHOW_DEMO_BANNER ? (
              <p className="inline-flex items-center gap-1.5 rounded-full border border-accent-400/40 bg-accent-50 px-2.5 py-1 text-[11px] font-medium text-accent-800 dark:bg-accent-400/10 dark:text-accent-200">
                <span aria-hidden="true" className="h-1.5 w-1.5 rounded-full bg-accent-500" />
                Mode demo · data lokal
              </p>
            ) : null}
          </div>

          <div className="grid grid-cols-2 gap-8 sm:gap-14">
            <nav aria-label="Navigasi footer">
              <p className="mb-3 text-[11px] font-semibold uppercase tracking-[0.14em] text-ink-400 dark:text-ink-500">
                Produk
              </p>
              <ul className="space-y-2 text-sm">
                {PUBLIC_NAV.filter((item) => ['/', '/chat', '/download'].includes(item.to)).map(
                  (item) => (
                    <li key={item.to}>
                      <Link
                        to={item.to}
                        className="focus-ring rounded text-ink-600 transition-colors hover:text-ink-900 dark:text-ink-400 dark:hover:text-ink-50"
                      >
                        {item.label}
                      </Link>
                    </li>
                  ),
                )}
              </ul>
            </nav>
            <nav aria-label="Navigasi legal">
              <p className="mb-3 text-[11px] font-semibold uppercase tracking-[0.14em] text-ink-400 dark:text-ink-500">
                Legal
              </p>
              <ul className="space-y-2 text-sm">
                {PUBLIC_NAV.filter((item) => ['/tos', '/privasi'].includes(item.to)).map((item) => (
                  <li key={item.to}>
                    <Link
                      to={item.to}
                      className="focus-ring rounded text-ink-600 transition-colors hover:text-ink-900 dark:text-ink-400 dark:hover:text-ink-50"
                    >
                      {item.label}
                    </Link>
                  </li>
                ))}
                <li>
                  <Link
                    to="/login"
                    className="focus-ring rounded text-ink-600 transition-colors hover:text-ink-900 dark:text-ink-400 dark:hover:text-ink-50"
                  >
                    Masuk
                  </Link>
                </li>
              </ul>
            </nav>
          </div>
        </div>

        <div className="mt-8 flex flex-col gap-2 border-t border-ink-200 pt-5 text-xs text-ink-500 sm:flex-row sm:items-center sm:justify-between dark:border-ink-800 dark:text-ink-500">
          <p>© {year} Nara. Dibuat untuk eksperimen terbuka.</p>
          <p>Nara bisa salah. Jangan jadikan rujukan utama.</p>
        </div>
      </div>
    </footer>
  );
}
