import { useCallback, useEffect, useId, useRef, useState, type KeyboardEvent } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { Avatar } from '../ui/Avatar';
import { useAuth } from '../../lib/auth/AuthContext';
import { providerLabel } from '../../lib/format';

/**
 * Dropdown menu akun yang bisa dioperasikan keyboard:
 * Enter/Space membuka, Esc menutup, panah atas/bawah berpindah item.
 */
export function UserMenu() {
  const { user, logout } = useAuth();
  const navigate = useNavigate();
  const [open, setOpen] = useState(false);
  const [activeIndex, setActiveIndex] = useState(0);
  const containerRef = useRef<HTMLDivElement>(null);
  const triggerRef = useRef<HTMLButtonElement>(null);
  const itemRefs = useRef<Array<HTMLElement | null>>([]);
  const menuId = useId();

  const close = useCallback((returnFocus = false) => {
    setOpen(false);
    if (returnFocus) triggerRef.current?.focus();
  }, []);

  useEffect(() => {
    if (!open) return;
    const onPointerDown = (event: MouseEvent) => {
      if (!containerRef.current?.contains(event.target as Node)) setOpen(false);
    };
    document.addEventListener('mousedown', onPointerDown);
    return () => document.removeEventListener('mousedown', onPointerDown);
  }, [open]);

  useEffect(() => {
    if (open) itemRefs.current[0]?.focus();
  }, [open]);

  if (!user) return null;

  const items = [
    { label: 'Chat', to: '/chat' },
    { label: 'Profil', to: '/profile' },
  ];

  const onKeyDown = (event: KeyboardEvent<HTMLDivElement>) => {
    if (event.key === 'Escape') {
      event.preventDefault();
      close(true);
      return;
    }
    if (!open) {
      if (event.key === 'ArrowDown' || event.key === 'Enter' || event.key === ' ') {
        if (event.target === triggerRef.current) {
          event.preventDefault();
          setOpen(true);
        }
      }
      return;
    }
    if (event.key === 'ArrowDown' || event.key === 'ArrowUp') {
      event.preventDefault();
      const count = items.length + 1; // + tombol keluar
      const delta = event.key === 'ArrowDown' ? 1 : -1;
      const next = (activeIndex + delta + count) % count;
      setActiveIndex(next);
      itemRefs.current[next]?.focus();
    }
  };

  const handleLogout = async () => {
    close();
    navigate('/', { replace: true });
    await logout();
  };

  return (
    <div ref={containerRef} className="relative" onKeyDown={onKeyDown}>
      <button
        ref={triggerRef}
        type="button"
        aria-haspopup="menu"
        aria-expanded={open}
        aria-controls={open ? menuId : undefined}
        onClick={() => setOpen((value) => !value)}
        className="inline-flex items-center gap-2 rounded-full border border-ink-200 py-1 pl-1 pr-3 text-sm font-medium text-ink-800 transition-colors hover:bg-ink-100 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent-400 dark:border-ink-800 dark:text-ink-100 dark:hover:bg-ink-800"
      >
        <Avatar name={user.displayName} email={user.email} size="sm" />
        <span className="max-w-[10rem] truncate">{user.displayName}</span>
        <svg aria-hidden="true" viewBox="0 0 20 20" className="h-3.5 w-3.5 opacity-70" fill="currentColor">
          <path d="M5.5 7.5 10 12l4.5-4.5" stroke="currentColor" strokeWidth="1.6" fill="none" strokeLinecap="round" />
        </svg>
      </button>

      {open ? (
        <div
          id={menuId}
          role="menu"
          aria-label="Menu akun"
          className="absolute right-0 z-40 mt-2 w-64 overflow-hidden rounded-xl border border-ink-200 bg-white shadow-card animate-fade-in motion-reduce:animate-none dark:border-ink-800 dark:bg-ink-900"
        >
          <div className="border-b border-ink-200 px-4 py-3 dark:border-ink-800">
            <p className="truncate text-sm font-semibold text-ink-900 dark:text-ink-50">
              {user.displayName}
            </p>
            <p className="truncate text-xs text-ink-500 dark:text-ink-400">{user.email}</p>
            <p className="mt-1 text-[11px] uppercase tracking-wide text-accent-600 dark:text-accent-300">
              Akun {providerLabel(user.provider)}
            </p>
          </div>
          <ul className="py-1">
            {items.map((item, index) => (
              <li key={item.to} role="none">
                <Link
                  ref={(element) => {
                    itemRefs.current[index] = element;
                  }}
                  role="menuitem"
                  to={item.to}
                  onClick={() => close()}
                  className="block px-4 py-2 text-sm text-ink-800 hover:bg-ink-100 focus:bg-ink-100 focus:outline-none dark:text-ink-100 dark:hover:bg-ink-800 dark:focus:bg-ink-800"
                >
                  {item.label}
                </Link>
              </li>
            ))}
            <li role="none">
              <button
                ref={(element) => {
                  itemRefs.current[items.length] = element;
                }}
                role="menuitem"
                type="button"
                onClick={handleLogout}
                className="block w-full px-4 py-2 text-left text-sm text-red-600 hover:bg-red-50 focus:bg-red-50 focus:outline-none dark:text-red-400 dark:hover:bg-red-950/50 dark:focus:bg-red-950/50"
              >
                Keluar
              </button>
            </li>
          </ul>
        </div>
      ) : null}
    </div>
  );
}
