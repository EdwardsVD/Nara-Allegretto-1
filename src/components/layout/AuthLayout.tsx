import { Link, Outlet } from 'react-router-dom';
import { DemoBanner } from '../ui/Banner';
import { SHOW_DEMO_BANNER } from '../../lib/env';
import { Logo } from './Logo';
import { ThemeToggle } from './ThemeToggle';

/**
 * Layout minimal untuk /login, /register, /register/verifikasi:
 * logo di atas, satu kartu di tengah dengan lebar maks 400px.
 */
export function AuthLayout() {
  return (
    <div className="flex min-h-dvh flex-col bg-canvas text-ink-900 dark:text-ink-50">
      <a
        href="#konten"
        className="sr-only focus:not-sr-only focus:absolute focus:left-4 focus:top-4 focus:z-50 focus:rounded-lg focus:bg-accent-400 focus:px-4 focus:py-2 focus:text-sm focus:font-semibold focus:text-ink-950"
      >
        Lewati ke konten
      </a>

      <header className="mx-auto flex w-full max-w-6xl items-center justify-between px-4 py-5 sm:px-6">
        <Logo subtitle="akun" />
        <div className="flex items-center gap-2">
          <ThemeToggle compact />
          <Link
            to="/"
            className="focus-ring inline-flex items-center gap-1.5 rounded-lg px-2 py-1.5 text-sm font-medium text-ink-600 hover:text-ink-900 dark:text-ink-400 dark:hover:text-ink-50"
          >
            <svg aria-hidden="true" viewBox="0 0 20 20" className="h-3.5 w-3.5" fill="none" stroke="currentColor" strokeWidth="1.8">
              <path d="M11 5 6 10l5 5" strokeLinecap="round" strokeLinejoin="round" />
            </svg>
            <span className="hidden sm:inline">Kembali ke beranda</span>
            <span className="sm:hidden">Beranda</span>
          </Link>
        </div>
      </header>

      <main
        id="konten"
        tabIndex={-1}
        className="flex flex-1 items-start justify-center px-4 pb-16 focus:outline-none sm:px-6"
      >
        <div className="w-full max-w-[400px] space-y-4 animate-fade-in motion-reduce:animate-none">
          {SHOW_DEMO_BANNER ? <DemoBanner /> : null}
          <div className="rounded-2xl border border-ink-200 bg-white p-6 shadow-lift dark:border-ink-800 dark:bg-ink-900 sm:p-7">
            <Outlet />
          </div>
          <p className="text-center text-xs leading-relaxed text-ink-500 dark:text-ink-400">
            Dengan melanjutkan, Anda menyetujui{' '}
            <Link to="/tos" className="underline underline-offset-2 hover:text-ink-800 dark:hover:text-ink-100">
              Syarat
            </Link>{' '}
            dan{' '}
            <Link to="/privasi" className="underline underline-offset-2 hover:text-ink-800 dark:hover:text-ink-100">
              Kebijakan Privasi
            </Link>
            .
          </p>
          <p className="text-center text-[11px] text-ink-400 dark:text-ink-500">
            Data akun demo hanya tersimpan di peramban ini.
          </p>
        </div>
      </main>
    </div>
  );
}
