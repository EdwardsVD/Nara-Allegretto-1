import { Link } from 'react-router-dom';

export function LogoMark({ className = '' }: { className?: string }) {
  return (
    <span
      aria-hidden="true"
      className={`inline-grid place-items-center rounded-xl bg-accent-400 text-ink-950 ${className}`}
    >
      <svg viewBox="0 0 24 24" className="h-5 w-5" fill="none" stroke="currentColor" strokeWidth="2.2">
        <path d="M5 18V6l14 12V6" strokeLinecap="round" strokeLinejoin="round" />
      </svg>
    </span>
  );
}

export function Logo({ subtitle }: { subtitle?: string }) {
  return (
    <Link
      to="/"
      className="group inline-flex items-center gap-2.5 rounded-lg focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent-400 focus-visible:ring-offset-2 focus-visible:ring-offset-ink-50 dark:focus-visible:ring-offset-ink-950"
      aria-label="Nara, ke beranda"
    >
      <LogoMark className="h-9 w-9 transition-transform motion-safe:group-hover:-rotate-3" />
      <span className="flex flex-col leading-none">
        <span className="text-lg font-semibold tracking-tight text-ink-900 dark:text-ink-50">
          Nara
        </span>
        {subtitle ? (
          <span className="mt-1 text-[11px] font-medium uppercase tracking-[0.16em] text-ink-500 dark:text-ink-400">
            {subtitle}
          </span>
        ) : null}
      </span>
    </Link>
  );
}
