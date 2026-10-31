import { useEffect, useId, useState } from 'react';
import { NavLink } from 'react-router-dom';
import { useAuth } from '../../lib/auth/AuthContext';
import { Button, ButtonLink } from '../ui/Button';
import { Logo } from './Logo';
import { ThemeToggle } from './ThemeToggle';
import { UserMenu } from './UserMenu';
import { PUBLIC_NAV } from './navItems';

export function Navbar() {
  const { user } = useAuth();
  const [menuOpen, setMenuOpen] = useState(false);
  const [scrolled, setScrolled] = useState(false);
  const menuId = useId();
  const closeMenu = () => setMenuOpen(false);

  // Efek ke sistem eksternal (window), bukan setState langsung di render.
  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > 8);
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
    return () => window.removeEventListener('scroll', onScroll);
  }, []);

  useEffect(() => {
    if (!menuOpen) return;
    const onKeyDown = (event: KeyboardEvent) => {
      if (event.key === 'Escape') setMenuOpen(false);
    };
    document.addEventListener('keydown', onKeyDown);
    return () => document.removeEventListener('keydown', onKeyDown);
  }, [menuOpen]);

  const linkClass = ({ isActive }: { isActive: boolean }) =>
    `relative rounded-lg px-3 py-2 text-sm font-medium transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent-400 ${
      isActive
        ? 'text-ink-900 dark:text-ink-50'
        : 'text-ink-600 hover:text-ink-900 dark:text-ink-400 dark:hover:text-ink-50'
    }`;

  return (
    <header
      className={`sticky top-0 z-30 border-b transition-colors duration-200 ${
        scrolled
          ? 'border-ink-200/80 bg-ink-50/90 shadow-sm backdrop-blur-md dark:border-ink-800/80 dark:bg-ink-950/90'
          : 'border-transparent bg-ink-50/70 backdrop-blur dark:bg-ink-950/70'
      }`}
    >
      <div className="mx-auto flex h-16 w-full max-w-6xl items-center justify-between gap-4 px-4 sm:px-6">
        <Logo />

        <nav aria-label="Navigasi utama" className="hidden items-center gap-0.5 lg:flex">
          {PUBLIC_NAV.map((item) => (
            <NavLink key={item.to} to={item.to} end={item.to === '/'} className={linkClass}>
              {({ isActive }) => (
                <>
                  {item.label}
                  <span
                    aria-hidden="true"
                    className={`absolute inset-x-3 -bottom-[3px] h-0.5 rounded-full bg-accent-400 transition-opacity ${
                      isActive ? 'opacity-100' : 'opacity-0'
                    }`}
                  />
                </>
              )}
            </NavLink>
          ))}
        </nav>

        <div className="hidden items-center gap-2 lg:flex">
          <ThemeToggle compact />
          {user ? (
            <>
              <ButtonLink to="/chat" variant="primary" size="sm">
                Buka chat
              </ButtonLink>
              <UserMenu />
            </>
          ) : (
            <>
              <ButtonLink to="/login" variant="ghost" size="sm">
                Masuk
              </ButtonLink>
              <ButtonLink to="/register" variant="primary" size="sm">
                Daftar
              </ButtonLink>
            </>
          )}
        </div>

        <div className="flex items-center gap-2 lg:hidden">
          <ThemeToggle compact />
          <Button
            variant="secondary"
            size="sm"
            aria-expanded={menuOpen}
            aria-controls={menuId}
            aria-label={menuOpen ? 'Tutup menu' : 'Buka menu'}
            onClick={() => setMenuOpen((value) => !value)}
            className="!px-2.5"
          >
            <svg aria-hidden="true" viewBox="0 0 24 24" className="h-4 w-4" fill="none" stroke="currentColor" strokeWidth="2">
              {menuOpen ? (
                <path d="m6 6 12 12M18 6 6 18" strokeLinecap="round" />
              ) : (
                <path d="M4 7h16M4 12h16M4 17h16" strokeLinecap="round" />
              )}
            </svg>
          </Button>
        </div>
      </div>

      {menuOpen ? (
        <div
          id={menuId}
          className="border-t border-ink-200 bg-ink-50/95 px-4 pb-4 pt-3 backdrop-blur lg:hidden dark:border-ink-800 dark:bg-ink-950/95"
        >
          <nav aria-label="Navigasi seluler" className="flex flex-col gap-0.5">
            {PUBLIC_NAV.map((item) => (
              <NavLink
                key={item.to}
                to={item.to}
                end={item.to === '/'}
                onClick={closeMenu}
                className={({ isActive }) =>
                  `rounded-lg px-3 py-2.5 text-sm font-medium transition-colors ${
                    isActive
                      ? 'bg-accent-400/15 text-accent-800 dark:text-accent-200'
                      : 'text-ink-700 hover:bg-ink-100 dark:text-ink-200 dark:hover:bg-ink-800'
                  }`
                }
              >
                {item.label}
              </NavLink>
            ))}
            {user ? (
              <>
                <NavLink
                  to="/profile"
                  onClick={closeMenu}
                  className="rounded-lg px-3 py-2.5 text-sm font-medium text-ink-700 hover:bg-ink-100 dark:text-ink-200 dark:hover:bg-ink-800"
                >
                  Profil
                </NavLink>
                <NavLink
                  to="/chat"
                  onClick={closeMenu}
                  className="mt-2 rounded-xl bg-accent-400 px-3 py-2.5 text-center text-sm font-semibold text-ink-950"
                >
                  Buka chat
                </NavLink>
              </>
            ) : (
              <div className="mt-2 grid grid-cols-2 gap-2">
                <ButtonLink to="/login" variant="secondary" size="sm">
                  Masuk
                </ButtonLink>
                <ButtonLink to="/register" size="sm">
                  Daftar
                </ButtonLink>
              </div>
            )}
          </nav>
        </div>
      ) : null}

    </header>
  );
}
