import { forwardRef, useId, type InputHTMLAttributes, type ReactNode } from 'react';

export interface InputProps extends InputHTMLAttributes<HTMLInputElement> {
  label: string;
  hint?: ReactNode;
  error?: string;
  /** Sembunyikan label secara visual (tetap ada untuk pembaca layar). */
  hideLabel?: boolean;
  trailing?: ReactNode;
}

export const inputClasses =
  'w-full rounded-xl border bg-white px-3 py-2.5 text-ink-900 placeholder:text-ink-400 ' +
  'border-ink-300 focus-visible:border-accent-400 focus-visible:outline-none ' +
  'focus-visible:ring-2 focus-visible:ring-accent-400/60 ' +
  'dark:bg-ink-900 dark:text-ink-50 dark:border-ink-700 dark:placeholder:text-ink-500 ' +
  'aria-[invalid=true]:border-red-500 aria-[invalid=true]:ring-red-500/40 ' +
  'disabled:opacity-60';

export const Input = forwardRef<HTMLInputElement, InputProps>(function Input(
  { label, hint, error, hideLabel, trailing, id, className = '', ...props },
  ref,
) {
  const generatedId = useId();
  const inputId = id ?? `input-${generatedId}`;
  const hintId = hint ? `${inputId}-hint` : undefined;
  const errorId = error ? `${inputId}-error` : undefined;

  return (
    <div className="space-y-1.5">
      <label
        htmlFor={inputId}
        className={hideLabel ? 'sr-only' : 'block text-sm font-medium text-ink-800 dark:text-ink-100'}
      >
        {label}
      </label>
      <div className="relative">
        <input
          ref={ref}
          id={inputId}
          aria-invalid={error ? true : undefined}
          aria-describedby={[hintId, errorId].filter(Boolean).join(' ') || undefined}
          className={`${inputClasses} ${trailing ? 'pr-12' : ''} ${className}`}
          {...props}
        />
        {trailing ? (
          <span className="absolute inset-y-0 right-1 flex items-center">{trailing}</span>
        ) : null}
      </div>
      {hint ? (
        <p id={hintId} className="text-xs text-ink-500 dark:text-ink-400">
          {hint}
        </p>
      ) : null}
      {error ? (
        <p id={errorId} className="text-xs font-medium text-red-600 dark:text-red-400">
          {error}
        </p>
      ) : null}
    </div>
  );
});
