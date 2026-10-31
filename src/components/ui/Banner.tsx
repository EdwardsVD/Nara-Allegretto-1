import type { ReactNode } from 'react';

type Tone = 'info' | 'success' | 'warning' | 'danger' | 'demo';

const tones: Record<Tone, string> = {
  info: 'border-sky-300 bg-sky-50 text-sky-900 dark:border-sky-800 dark:bg-sky-950/50 dark:text-sky-100',
  success:
    'border-emerald-300 bg-emerald-50 text-emerald-900 dark:border-emerald-800 dark:bg-emerald-950/50 dark:text-emerald-100',
  warning:
    'border-amber-300 bg-amber-50 text-amber-900 dark:border-amber-700 dark:bg-amber-950/50 dark:text-amber-100',
  danger:
    'border-red-300 bg-red-50 text-red-900 dark:border-red-800 dark:bg-red-950/50 dark:text-red-100',
  demo: 'border-accent-400/60 bg-accent-50 text-accent-900 dark:border-accent-500/40 dark:bg-accent-400/10 dark:text-accent-100',
};

export function Banner({
  tone = 'info',
  children,
  className = '',
  role,
}: {
  tone?: Tone;
  children: ReactNode;
  className?: string;
  role?: 'status' | 'alert';
}) {
  return (
    <div
      role={role}
      className={`rounded-xl border px-4 py-3 text-sm leading-relaxed ${tones[tone]} ${className}`}
    >
      {children}
    </div>
  );
}

/** Versi ringkas satu baris untuk strip atas layout. */
export function DemoStrip() {
  return (
    <div className="border-b border-accent-400/40 bg-accent-50 px-3 py-1.5 text-center text-[11px] font-medium text-accent-900 dark:border-accent-500/30 dark:bg-accent-400/10 dark:text-accent-100 sm:text-xs">
      <strong className="font-semibold">MODE DEMO:</strong> akun dan verifikasi email hanya
      simulasi. Kode verifikasi: <code className="font-mono font-semibold">123456</code>.
    </div>
  );
}

/** Banner permanen mode demo (dipakai di layout auth dan chat). */
export function DemoBanner({ className = '' }: { className?: string }) {
  return (
    <Banner tone="demo" className={className}>
      <strong className="font-semibold">MODE DEMO:</strong> akun dan verifikasi email hanya
      simulasi. Kode verifikasi: <code className="font-mono font-semibold">123456</code>.
    </Banner>
  );
}
