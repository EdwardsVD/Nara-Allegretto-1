import { Outlet } from 'react-router-dom';
import { Navbar } from './Navbar';
import { Footer } from './Footer';
import { DemoStrip } from '../ui/Banner';
import { SHOW_DEMO_BANNER } from '../../lib/env';

/**
 * Layout halaman publik: skip-link, header, main, footer.
 * Halaman auth memakai AuthLayout (tanpa navbar penuh).
 */
export function PublicLayout() {
  return (
    <div className="flex min-h-dvh flex-col bg-ink-50 text-ink-900 dark:bg-ink-950 dark:text-ink-50">
      <a
        href="#konten"
        className="sr-only focus:not-sr-only focus:absolute focus:left-4 focus:top-4 focus:z-50 focus:rounded-lg focus:bg-accent-400 focus:px-4 focus:py-2 focus:text-sm focus:font-semibold focus:text-ink-950"
      >
        Lewati ke konten
      </a>
      {SHOW_DEMO_BANNER ? <DemoStrip /> : null}
      <Navbar />
      <main id="konten" tabIndex={-1} className="flex-1 focus:outline-none">
        <Outlet />
      </main>
      <Footer />
    </div>
  );
}
