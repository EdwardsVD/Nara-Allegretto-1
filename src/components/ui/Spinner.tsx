export function Spinner({
  label = 'Memuat…',
  size = 'md',
  inline = false,
}: {
  label?: string;
  size?: 'sm' | 'md' | 'lg';
  inline?: boolean;
}) {
  const dimension = size === 'sm' ? 'h-4 w-4' : size === 'lg' ? 'h-10 w-10' : 'h-6 w-6';
  return (
    <span
      className={inline ? 'inline-flex items-center gap-2' : 'flex items-center gap-3'}
      role="status"
      aria-live="polite"
    >
      <span
        aria-hidden="true"
        className={`${dimension} animate-spin rounded-full border-2 border-ink-300 border-t-accent-400 dark:border-ink-700 dark:border-t-accent-400`}
      />
      <span className="text-sm text-ink-600 dark:text-ink-300">{label}</span>
    </span>
  );
}
