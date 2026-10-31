import { useState, type FormEvent } from 'react';
import { Banner } from '../../components/ui/Banner';
import { Button } from '../../components/ui/Button';
import { Card, CardBody, CardHeader } from '../../components/ui/Card';
import { PasswordInput } from '../../components/ui/PasswordInput';
import { useToast } from '../../components/ui/Toast';
import { AuthError, type Provider } from '../../lib/auth/types';

export function SecuritySection({
  provider,
  providerText,
  onChangePassword,
  onLogout,
  onLogoutAll,
}: {
  provider: Provider;
  providerText: string;
  onChangePassword(current: string, next: string): Promise<void>;
  onLogout(): void | Promise<void>;
  onLogoutAll(): void | Promise<void>;
}) {
  const { showToast } = useToast();
  const [current, setCurrent] = useState('');
  const [next, setNext] = useState('');
  const [repeat, setRepeat] = useState('');
  const [error, setError] = useState<string | null>(null);
  const [saving, setSaving] = useState(false);
  const usesEmail = provider === 'email';

  const onSubmit = async (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    setError(null);
    if (!usesEmail) return;
    if (next.length < 8) {
      setError('Password baru minimal 8 karakter.');
      return;
    }
    if (next !== repeat) {
      setError('Ulangi password baru dengan benar.');
      return;
    }
    if (next === current) {
      setError('Password baru harus berbeda dari password lama.');
      return;
    }
    setSaving(true);
    try {
      await onChangePassword(current, next);
      setCurrent('');
      setNext('');
      setRepeat('');
      showToast('Password diperbarui (simulasi).', 'success');
    } catch (caught) {
      const message = caught instanceof AuthError ? caught.message : 'Gagal memperbarui password.';
      setError(message);
      showToast(message, 'error');
    } finally {
      setSaving(false);
    }
  };

  return (
    <Card as="section">
      <CardHeader title="Keamanan" description="Password dan sesi masuk perangkat Anda." />
      <CardBody className="space-y-5">
        <form className="space-y-3" onSubmit={onSubmit} noValidate>
          <div className="space-y-3">
            <PasswordInput
              label="Password lama"
              name="currentPassword"
              autoComplete="current-password"
              value={current}
              onChange={(event) => setCurrent(event.target.value)}
              disabled={!usesEmail || saving}
            />
            <PasswordInput
              label="Password baru"
              name="nextPassword"
              autoComplete="new-password"
              value={next}
              onChange={(event) => setNext(event.target.value)}
              disabled={!usesEmail || saving}
              hint="Minimal 8 karakter dan berbeda dari password lama."
            />
            <PasswordInput
              label="Ulangi password baru"
              name="repeatPassword"
              autoComplete="new-password"
              value={repeat}
              onChange={(event) => setRepeat(event.target.value)}
              disabled={!usesEmail || saving}
            />
          </div>

          {!usesEmail ? (
            <Banner tone="info">
              Akun dikelola oleh {providerText}. Ubah password melalui{' '}
              {provider === 'github' ? 'pengaturan GitHub' : 'Akun Google'} Anda.
            </Banner>
          ) : null}

          {error ? (
            <Banner tone="danger" role="alert">
              {error}
            </Banner>
          ) : null}

          <div className="flex justify-end">
            <Button
              type="submit"
              size="sm"
              disabled={!usesEmail || saving}
              title={usesEmail ? undefined : `Akun dikelola oleh ${providerText}.`}
            >
              {saving ? 'Menyimpan…' : 'Ganti password'}
            </Button>
          </div>
        </form>

        <div className="space-y-2 border-t border-ink-200 pt-4 dark:border-ink-800">
          <div className="flex flex-wrap gap-2">
            <Button variant="secondary" size="sm" onClick={() => void onLogout()}>
              Keluar
            </Button>
            <Button variant="secondary" size="sm" onClick={() => void onLogoutAll()}>
              Keluar dari semua perangkat
            </Button>
          </div>
          <p className="text-xs text-ink-500 dark:text-ink-400">
            Simulasi: "Keluar dari semua perangkat" hanya mengakhiri sesi di peramban ini.
          </p>
        </div>
      </CardBody>
    </Card>
  );
}
