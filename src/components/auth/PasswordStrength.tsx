import { scorePassword } from '../../lib/passwordStrength';

const barColors = ['bg-ink-300 dark:bg-ink-700', 'bg-red-500', 'bg-amber-500', 'bg-emerald-500'];

export function PasswordStrength({ password }: { password: string }) {
  const { score, label } = scorePassword(password);
  const filled = score === 0 ? 0 : score;

  return (
    <div className="space-y-1" aria-live="polite">
      <div className="flex gap-1" aria-hidden="true">
        {[1, 2, 3].map((step) => (
          <span
            key={step}
            className={`h-1 flex-1 rounded-full ${step <= filled ? barColors[filled] : 'bg-ink-200 dark:bg-ink-800'}`}
          />
        ))}
      </div>
      <p className="text-xs text-ink-500 dark:text-ink-400">
        Kekuatan password: <span className="font-medium text-ink-700 dark:text-ink-200">{label}</span>{' '}
        (minimal 8 karakter)
      </p>
    </div>
  );
}
