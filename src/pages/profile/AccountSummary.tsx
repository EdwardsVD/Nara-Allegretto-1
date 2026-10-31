import { Avatar } from '../../components/ui/Avatar';
import { Card, CardBody } from '../../components/ui/Card';
import type { User } from '../../lib/auth/types';

export function AccountSummary({
  user,
  joinedLabel,
  providerText,
}: {
  user: User;
  joinedLabel: string;
  providerText: string;
}) {
  return (
    <Card as="section" className="overflow-hidden">
      <div className="h-20 bg-gradient-to-r from-accent-400/70 via-accent-300/40 to-transparent dark:from-accent-500/30 dark:via-accent-400/10" />
      <CardBody className="-mt-10 space-y-3">
        <div className="flex items-end justify-between gap-3">
          <div className="rounded-full ring-4 ring-white dark:ring-ink-900">
            <Avatar name={user.displayName} email={user.email} size="lg" />
          </div>
        </div>
        <div className="space-y-1">
          <h2 className="text-xl font-semibold tracking-tight text-ink-900 dark:text-ink-50" data-testid="profile-display-name">
            {user.displayName}
          </h2>
          <p className="text-sm text-ink-600 dark:text-ink-300">{user.email}</p>
        </div>
        <ul className="flex flex-wrap items-center gap-2 pt-1 text-xs">
          <li className="rounded-full border border-ink-200 bg-ink-100 px-2.5 py-1 font-medium text-ink-700 dark:border-ink-700 dark:bg-ink-800 dark:text-ink-200">
            Akun {providerText}
          </li>
          {user.verified ? (
            <li className="inline-flex items-center gap-1 rounded-full border border-emerald-300 bg-emerald-50 px-2.5 py-1 font-medium text-emerald-800 dark:border-emerald-800 dark:bg-emerald-950/60 dark:text-emerald-200">
              <svg aria-hidden="true" viewBox="0 0 20 20" className="h-3.5 w-3.5" fill="currentColor">
                <path d="M10 1.5 12.3 4l3.4.3.3 3.4 2.5 2.3-2.5 2.3-.3 3.4-3.4.3L10 18.5 7.7 16l-3.4-.3-.3-3.4L1.5 10l2.5-2.3.3-3.4L7.7 4 10 1.5Zm-1 11.2 4.3-4.3-1.1-1.1L9 10.5 7.3 8.8 6.2 9.9 9 12.7Z" />
              </svg>
              Terverifikasi
            </li>
          ) : (
            <li className="rounded-full border border-amber-300 bg-amber-50 px-2.5 py-1 font-medium text-amber-800 dark:border-amber-800 dark:bg-amber-950/60 dark:text-amber-200">
              Belum terverifikasi
            </li>
          )}
          <li className="text-ink-500 dark:text-ink-400">Bergabung {joinedLabel}</li>
        </ul>
      </CardBody>
    </Card>
  );
}
