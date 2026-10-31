import { forwardRef, type ButtonHTMLAttributes, type ReactNode } from 'react';
import { Link, type LinkProps } from 'react-router-dom';

type Variant = 'primary' | 'secondary' | 'ghost' | 'danger';
type Size = 'sm' | 'md' | 'lg';

const base =
  'inline-flex items-center justify-center gap-2 rounded-xl font-medium transition-colors ' +
  'focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent-400 ' +
  'focus-visible:ring-offset-2 focus-visible:ring-offset-ink-50 dark:focus-visible:ring-offset-ink-950 ' +
  'disabled:cursor-not-allowed disabled:opacity-50 motion-reduce:transition-none';

const variants: Record<Variant, string> = {
  primary:
    'bg-accent-400 text-ink-950 hover:bg-accent-300 active:bg-accent-500 shadow-sm',
  secondary:
    'border border-ink-300 bg-white text-ink-900 hover:bg-ink-100 dark:border-ink-700 dark:bg-ink-900 dark:text-ink-50 dark:hover:bg-ink-800',
  ghost:
    'text-ink-700 hover:bg-ink-200/70 dark:text-ink-200 dark:hover:bg-ink-800',
  danger:
    'bg-red-600 text-white hover:bg-red-500 active:bg-red-700 dark:bg-red-600 dark:hover:bg-red-500',
};

const sizes: Record<Size, string> = {
  sm: 'h-9 px-3 text-sm',
  md: 'h-11 px-4 text-sm',
  lg: 'h-12 px-5 text-base',
};

export interface ButtonProps extends ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: Variant;
  size?: Size;
  fullWidth?: boolean;
  leftIcon?: ReactNode;
}

export const Button = forwardRef<HTMLButtonElement, ButtonProps>(function Button(
  { variant = 'primary', size = 'md', fullWidth, leftIcon, className = '', children, ...props },
  ref,
) {
  return (
    <button
      ref={ref}
      className={`${base} ${variants[variant]} ${sizes[size]} ${fullWidth ? 'w-full' : ''} ${className}`}
      {...props}
    >
      {leftIcon}
      {children}
    </button>
  );
});

export function ButtonLink({
  variant = 'primary',
  size = 'md',
  fullWidth,
  className = '',
  children,
  ...props
}: LinkProps & { variant?: Variant; size?: Size; fullWidth?: boolean }) {
  return (
    <Link
      className={`${base} ${variants[variant]} ${sizes[size]} ${fullWidth ? 'w-full' : ''} ${className}`}
      {...props}
    >
      {children}
    </Link>
  );
}
