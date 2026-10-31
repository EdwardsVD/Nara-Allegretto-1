import { useTheme } from '../../lib/useTheme';

export function ThemeToggle({ compact = false }: { compact?: boolean }) {
  const { isDark, toggle } = useTheme();
  const label = isDark ? 'Aktifkan tema terang' : 'Aktifkan tema gelap';

  return (
    <button
      type="button"
      onClick={toggle}
      aria-label={label}
      title={label}
      className={`inline-flex items-center justify-center gap-2 rounded-xl border border-ink-200 text-ink-700 transition-colors hover:bg-ink-100 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent-400 dark:border-ink-800 dark:text-ink-200 dark:hover:bg-ink-800 ${
        compact ? 'h-9 w-9' : 'h-9 px-3 text-xs font-medium'
      }`}
    >
      <svg
        aria-hidden="true"
        viewBox="0 0 24 24"
        className="h-4 w-4"
        fill="none"
        stroke="currentColor"
        strokeWidth="1.8"
      >
        {isDark ? (
          <>
            <circle cx="12" cy="12" r="4" />
            <path
              d="M12 2v2m0 16v2M2 12h2m16 0h2M4.9 4.9l1.4 1.4m11.4 11.4 1.4 1.4M19.1 4.9l-1.4 1.4M6.3 17.7l-1.4 1.4"
              strokeLinecap="round"
            />
          </>
        ) : (
          <path
            d="M20 14.5A8 8 0 0 1 9.5 4a8.5 8.5 0 1 0 10.5 10.5Z"
            strokeLinecap="round"
            strokeLinejoin="round"
          />
        )}
      </svg>
      {compact ? null : <span>{isDark ? 'Terang' : 'Gelap'}</span>}
    </button>
  );
}
