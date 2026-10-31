import { NavLink, useLocation, useNavigate } from 'react-router-dom';
import { useAuth } from '../../lib/auth/AuthContext';
import { useChatSession } from '../../lib/chat/ChatSessionContext';
import { Avatar } from '../ui/Avatar';
import { Button } from '../ui/Button';
import { Logo } from './Logo';
import { ThemeToggle } from './ThemeToggle';
import { SIDEBAR_NAV } from './navItems';

const NAV_ICONS: Record<string, React.ReactNode> = {
  '/': (
    <svg aria-hidden="true" viewBox="0 0 24 24" className="h-4 w-4" fill="none" stroke="currentColor" strokeWidth="1.7">
      <path d="M4 10.5 12 4l8 6.5V20a1 1 0 0 1-1 1h-4v-6H9v6H5a1 1 0 0 1-1-1v-9.5Z" strokeLinecap="round" strokeLinejoin="round" />
    </svg>
  ),
  '/chat': (
    <svg aria-hidden="true" viewBox="0 0 24 24" className="h-4 w-4" fill="none" stroke="currentColor" strokeWidth="1.7">
      <path d="M4 5.5A1.5 1.5 0 0 1 5.5 4h13A1.5 1.5 0 0 1 20 5.5v9a1.5 1.5 0 0 1-1.5 1.5H9l-5 4V5.5Z" strokeLinecap="round" strokeLinejoin="round" />
    </svg>
  ),
  '/profile': (
    <svg aria-hidden="true" viewBox="0 0 24 24" className="h-4 w-4" fill="none" stroke="currentColor" strokeWidth="1.7">
      <circle cx="12" cy="8.5" r="3.5" />
      <path d="M5 20c.8-3.4 3.6-5.2 7-5.2s6.2 1.8 7 5.2" strokeLinecap="round" />
    </svg>
  ),
  '/download': (
    <svg aria-hidden="true" viewBox="0 0 24 24" className="h-4 w-4" fill="none" stroke="currentColor" strokeWidth="1.7">
      <path d="M12 4v10m0 0 4-4m-4 4-4-4M5 19h14" strokeLinecap="round" strokeLinejoin="round" />
    </svg>
  ),
  '/tos': (
    <svg aria-hidden="true" viewBox="0 0 24 24" className="h-4 w-4" fill="none" stroke="currentColor" strokeWidth="1.7">
      <path d="M7 3.5h7L19 8v12.5H7a2 2 0 0 1-2-2v-13a2 2 0 0 1 2-2Z" strokeLinejoin="round" />
      <path d="M14 3.5V8h4.5M9 12h6M9 15.5h4" strokeLinecap="round" strokeLinejoin="round" />
    </svg>
  ),
  '/privasi': (
    <svg aria-hidden="true" viewBox="0 0 24 24" className="h-4 w-4" fill="none" stroke="currentColor" strokeWidth="1.7">
      <path d="M12 3.5 19 6v5.5c0 4.2-2.9 7.6-7 9-4.1-1.4-7-4.8-7-9V6l7-2.5Z" strokeLinejoin="round" />
      <path d="m9.2 11.8 2 2 3.6-3.8" strokeLinecap="round" strokeLinejoin="round" />
    </svg>
  ),
};

export function AppSidebar({ onNavigate }: { onNavigate?: () => void }) {
  const { user, status, logout } = useAuth();
  const { startNew, messages } = useChatSession();
  const navigate = useNavigate();
  const location = useLocation();
  const onChatRoute = location.pathname === '/chat';

  const goToChat = () => {
    onNavigate?.();
    if (!onChatRoute) navigate('/chat');
  };

  const handleNewChat = () => {
    if (onChatRoute) startNew();
    goToChat();
  };

  const handleLogout = async () => {
    onNavigate?.();
    // Navigasi dulu supaya guard /profile tidak menimpa tujuan keluar.
    navigate('/', { replace: true });
    await logout();
  };

  return (
    <div className="flex h-full flex-col gap-4 bg-white px-3 py-4 dark:bg-ink-900">
      <div className="flex items-center justify-between px-1">
        <Logo />
      </div>

      <Button variant="primary" onClick={handleNewChat} fullWidth className="justify-start shadow-sm">
        <svg aria-hidden="true" viewBox="0 0 24 24" className="h-4 w-4" fill="none" stroke="currentColor" strokeWidth="2">
          <path d="M12 5v14M5 12h14" strokeLinecap="round" />
        </svg>
        Chat baru
        {messages.length > 0 && onChatRoute ? (
          <span className="ml-auto rounded-full bg-ink-950/10 px-2 py-0.5 text-[10px] font-semibold dark:bg-ink-950/20">
            {messages.filter((message) => message.role === 'user').length} pesan
          </span>
        ) : null}
      </Button>

      <nav aria-label="Navigasi aplikasi" className="min-h-0 flex-1 overflow-y-auto">
        <p className="px-2.5 pb-1.5 text-[10px] font-semibold uppercase tracking-[0.16em] text-ink-400 dark:text-ink-500">
          Navigasi
        </p>
        <ul className="space-y-0.5">
          {SIDEBAR_NAV.filter((item) => !item.authOnly || status === 'authenticated').map((item) => (
            <li key={item.to}>
              <NavLink
                to={item.to}
                end={item.to === '/'}
                onClick={onNavigate}
                className={({ isActive }) =>
                  `group flex items-center gap-2.5 rounded-lg px-2.5 py-2 text-sm transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent-400 ${
                    isActive
                      ? 'bg-accent-400/15 font-semibold text-accent-800 dark:text-accent-200'
                      : 'font-medium text-ink-600 hover:bg-ink-100 hover:text-ink-900 dark:text-ink-400 dark:hover:bg-ink-800 dark:hover:text-ink-100'
                  }`
                }
              >
                <span
                  className={`transition-colors ${
                    location.pathname === item.to
                      ? 'text-accent-700 dark:text-accent-300'
                      : 'text-ink-400 group-hover:text-ink-600 dark:text-ink-500 dark:group-hover:text-ink-300'
                  }`}
                >
                  {NAV_ICONS[item.to]}
                </span>
                {item.label}
              </NavLink>
            </li>
          ))}
        </ul>
        <p className="mt-3 flex items-start gap-1.5 px-2.5 text-[11px] leading-relaxed text-ink-400 dark:text-ink-500">
          <svg aria-hidden="true" viewBox="0 0 20 20" className="mt-0.5 h-3 w-3 shrink-0" fill="none" stroke="currentColor" strokeWidth="1.6">
            <circle cx="10" cy="10" r="7.2" />
            <path d="M10 6.2v.2M10 9v4.6" strokeLinecap="round" />
          </svg>
          Riwayat percakapan tidak disimpan.
        </p>
      </nav>

      <div className="space-y-3 border-t border-ink-200 pt-3 dark:border-ink-800">
        {user ? (
          <div className="space-y-2">
            <div className="flex items-center gap-2.5 rounded-xl px-1">
              <Avatar name={user.displayName} email={user.email} size="sm" />
              <div className="min-w-0 flex-1">
                <p
                  className="truncate text-sm font-semibold text-ink-900 dark:text-ink-50"
                  data-testid="sidebar-display-name"
                >
                  {user.displayName}
                </p>
                <p className="truncate text-[11px] text-ink-500 dark:text-ink-400">{user.email}</p>
              </div>
            </div>
            <div className="flex gap-2">
              <Button
                variant="secondary"
                size="sm"
                className="flex-1"
                onClick={() => {
                  onNavigate?.();
                  navigate('/profile');
                }}
              >
                Profil
              </Button>
              <Button variant="ghost" size="sm" className="flex-1" onClick={handleLogout}>
                Keluar
              </Button>
            </div>
          </div>
        ) : (
          <div className="space-y-2">
            <div className="flex gap-2">
              <Button
                variant="secondary"
                size="sm"
                className="flex-1"
                onClick={() => {
                  onNavigate?.();
                  navigate('/login');
                }}
              >
                Masuk
              </Button>
              <Button
                size="sm"
                className="flex-1"
                onClick={() => {
                  onNavigate?.();
                  navigate('/register');
                }}
              >
                Daftar
              </Button>
            </div>
            <p className="px-1 text-[11px] leading-relaxed text-ink-500 dark:text-ink-500">
              Masuk untuk mengelola profil. Chat tetap bisa dipakai tanpa akun.
            </p>
          </div>
        )}

        <div className="flex items-center justify-between pl-1">
          <span className="text-[11px] font-medium uppercase tracking-wide text-ink-400 dark:text-ink-500">
            Tema
          </span>
          <ThemeToggle />
        </div>
      </div>
    </div>
  );
}
