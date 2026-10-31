import { useState } from 'react';
import { Banner } from '../../components/ui/Banner';
import { Button } from '../../components/ui/Button';
import { Card, CardBody, CardHeader } from '../../components/ui/Card';
import { useToast } from '../../components/ui/Toast';
import type { OAuthProvider, Provider } from '../../lib/auth/types';

const PROVIDERS: Array<{ id: OAuthProvider; label: string; description: string }> = [
  {
    id: 'github',
    label: 'GitHub',
    description: 'Masuk cepat dengan akun GitHub (simulasi).',
  },
  {
    id: 'google',
    label: 'Google',
    description: 'Masuk cepat dengan akun Google (simulasi).',
  },
];

export function ConnectedAccounts({ provider }: { provider: Provider }) {
  const { showToast } = useToast();
  const [linked, setLinked] = useState<Record<OAuthProvider, boolean>>({
    github: provider === 'github',
    google: provider === 'google',
  });

  // Simulasi: hanya satu metode login yang "berfungsi", jadi memutus
  // koneksi terakhir tidak boleh dilakukan. Provider akun saat ini selalu
  // dianggap metode login utama dan tidak bisa diputus.
  const primaryProvider = provider === 'email' ? null : provider;
  const linkedCount = Object.values(linked).filter(Boolean).length;

  const toggle = (id: OAuthProvider, label: string) => {
    if (id === primaryProvider) {
      showToast(`Akun dikelola oleh ${label}, tidak bisa diputus di sini.`, 'error');
      return;
    }
    if (linked[id] && linkedCount <= 1) {
      showToast('Tidak bisa memutus satu-satunya metode login.', 'error');
      return;
    }
    setLinked((current) => ({ ...current, [id]: !current[id] }));
    showToast(
      linked[id] ? `${label} diputuskan (simulasi).` : `${label} terhubung (simulasi).`,
      'success',
    );
  };

  return (
    <Card as="section">
      <CardHeader title="Akun terhubung" description="Metode masuk alternatif (hanya simulasi)." />
      <CardBody className="space-y-3">
        <ul className="divide-y divide-ink-200 dark:divide-ink-800">
          {PROVIDERS.map((item) => {
            const isLinked = linked[item.id];
            const isPrimary = item.id === primaryProvider;
            return (
              <li key={item.id} className="flex flex-wrap items-center justify-between gap-3 py-3 first:pt-0 last:pb-0">
                <div className="space-y-0.5">
                  <p className="flex items-center gap-2 text-sm font-medium text-ink-900 dark:text-ink-50">
                    {item.label}
                    <span
                      className={`rounded-full px-2 py-0.5 text-[11px] font-semibold ${
                        isLinked || isPrimary
                          ? 'bg-emerald-100 text-emerald-800 dark:bg-emerald-950/60 dark:text-emerald-200'
                          : 'bg-ink-200 text-ink-700 dark:bg-ink-800 dark:text-ink-300'
                      }`}
                    >
                      {isLinked || isPrimary ? 'Terhubung' : 'Belum terhubung'}
                    </span>
                  </p>
                  <p className="text-xs text-ink-500 dark:text-ink-400">{item.description}</p>
                </div>
                <Button
                  variant={isLinked || isPrimary ? 'secondary' : 'primary'}
                  size="sm"
                  aria-label={`${isLinked || isPrimary ? 'Putuskan' : 'Hubungkan'} ${item.label}`}
                  disabled={isPrimary}
                  onClick={() => toggle(item.id, item.label)}
                >
                  {isPrimary
                    ? 'Metode login utama'
                    : isLinked
                      ? 'Putuskan'
                      : 'Hubungkan'}
                </Button>
              </li>
            );
          })}
        </ul>
        <Banner tone="info">
          Koneksi di atas hanya simulasi dan tidak menghubungi GitHub atau Google. Metode login
          utama akun ini tidak dapat diputus.
        </Banner>
      </CardBody>
    </Card>
  );
}
