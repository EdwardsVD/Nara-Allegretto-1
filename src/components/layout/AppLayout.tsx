import { useCallback, useRef, useState } from 'react';
import { Outlet } from 'react-router-dom';
import { ChatSessionProvider } from '../../lib/chat/ChatSessionContext';
import { useFocusTrap } from '../../lib/useFocusTrap';
import { Button } from '../ui/Button';
import { AppSidebar } from './AppSidebar';
import { Logo } from './Logo';
import { ThemeToggle } from './ThemeToggle';
import { DemoStrip } from '../ui/Banner';
import { SHOW_DEMO_BANNER } from '../../lib/env';

/**
 * Layout aplikasi dua kolom:
 * - >= lg: sidebar tetap 280px di kiri
 * - < lg : sidebar menjadi drawer (tombol menu, Esc, klik luar, fokus terjebak)
 */
export function AppLayout() {
  const [drawerOpen, setDrawerOpen] = useState(false);
  const drawerRef = useRef<HTMLDivElement>(null);
  const drawerTriggerRef = useRef<HTMLButtonElement>(null);

  const closeDrawer = useCallback(() => {
    setDrawerOpen(false);
    drawerTriggerRef.current?.focus();
  }, []);

  useFocusTrap(drawerOpen, drawerRef, closeDrawer);

  return (
    <ChatSessionProvider>
      <div className="flex h-dvh overflow-hidden bg-canvas text-ink-900 dark:text-ink-50">
        <a
          href="#konten"
          className="sr-only focus:not-sr-only focus:absolute focus:left-4 focus:top-4 focus:z-50 focus:rounded-lg focus:bg-accent-400 focus:px-4 focus:py-2 focus:text-sm focus:font-semibold focus:text-ink-950"
        >
          Lewati ke konten
        </a>

        <aside
          aria-label="Sidebar aplikasi"
          className="hidden h-full w-[280px] shrink-0 border-r border-ink-200 lg:block dark:border-ink-800"
        >
          <AppSidebar />
        </aside>

        {drawerOpen ? (
          <div className="fixed inset-0 z-50 lg:hidden">
            <div
              className="absolute inset-0 bg-ink-950/60 backdrop-blur-sm animate-fade-in motion-reduce:animate-none"
              onClick={closeDrawer}
              aria-hidden="true"
            />
            <div
              ref={drawerRef}
              role="dialog"
              aria-modal="true"
              aria-label="Menu samping"
              tabIndex={-1}
              className="absolute inset-y-0 left-0 w-[280px] max-w-[85vw] border-r border-ink-200 shadow-card animate-fade-in motion-reduce:animate-none dark:border-ink-800"
            >
              <AppSidebar onNavigate={closeDrawer} />
            </div>
          </div>
        ) : null}

        <div className="flex min-w-0 flex-1 flex-col">
          {SHOW_DEMO_BANNER ? <DemoStrip /> : null}
          <header className="flex h-14 items-center justify-between gap-2 border-b border-ink-200 px-3 sm:px-5 lg:hidden dark:border-ink-800">
            <div className="flex items-center gap-2">
              <Button
                ref={drawerTriggerRef}
                variant="secondary"
                size="sm"
                aria-label="Buka menu samping"
                aria-expanded={drawerOpen}
                onClick={() => setDrawerOpen(true)}
                leftIcon={
                  <svg aria-hidden="true" viewBox="0 0 24 24" className="h-4 w-4" fill="none" stroke="currentColor" strokeWidth="2">
                    <path d="M4 7h16M4 12h16M4 17h16" strokeLinecap="round" />
                  </svg>
                }
              >
                Menu
              </Button>
              <Logo />
            </div>
            <ThemeToggle compact />
          </header>

          <main id="konten" tabIndex={-1} className="min-h-0 flex-1 overflow-hidden focus:outline-none">
            <Outlet />
          </main>
        </div>
      </div>
    </ChatSessionProvider>
  );
}
