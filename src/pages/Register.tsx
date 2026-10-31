import { useRef, useState, type FormEvent } from 'react';
import { Link, useLocation, useNavigate } from 'react-router-dom';
import { OAuthButtons } from '../components/auth/OAuthButtons';
import { PasswordStrength } from '../components/auth/PasswordStrength';
import { Banner } from '../components/ui/Banner';
import { Button } from '../components/ui/Button';
import { Input } from '../components/ui/Input';
import { PasswordInput } from '../components/ui/PasswordInput';
import { useAuth } from '../lib/auth/AuthContext';
import { AuthError, type OAuthProvider } from '../lib/auth/types';
import { MIN_PASSWORD_LENGTH } from '../lib/auth/dummyAuthApi';
import { isValidEmail, normalizeEmail } from '../lib/email';
import { AUTH_AVAILABLE } from '../lib/env';
import { usePageTitle } from '../lib/usePageTitle';
import { AuthDisabled } from './AuthDisabled';

interface LocationState {
  email?: string;
}

export function Register() {
  usePageTitle('Daftar');
  const { register, loginWithProvider } = useAuth();
  const navigate = useNavigate();
  const location = useLocation();
  const initialEmail = (location.state as LocationState | null)?.email ?? '';

  const [email, setEmail] = useState(initialEmail);
  const [password, setPassword] = useState('');
  const [agreed, setAgreed] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [fieldErrors, setFieldErrors] = useState<{
    email?: string;
    password?: string;
    agreed?: string;
  }>({});
  const [submitting, setSubmitting] = useState(false);
  const agreedRef = useRef<HTMLInputElement>(null);

  if (!AUTH_AVAILABLE) return <AuthDisabled action="register" />;

  const onSubmit = async (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    setError(null);
    const nextFieldErrors: typeof fieldErrors = {};
    const normalized = normalizeEmail(email);
    if (!normalized) nextFieldErrors.email = 'Email wajib diisi.';
    else if (!isValidEmail(normalized)) nextFieldErrors.email = 'Format email tidak valid.';
    if (!password) nextFieldErrors.password = 'Password wajib diisi.';
    else if (password.length < MIN_PASSWORD_LENGTH)
      nextFieldErrors.password = `Password minimal ${MIN_PASSWORD_LENGTH} karakter.`;
    if (!agreed) nextFieldErrors.agreed = 'Anda harus menyetujui Syarat dan Kebijakan Privasi.';
    setFieldErrors(nextFieldErrors);
    if (Object.keys(nextFieldErrors).length > 0) {
      if (nextFieldErrors.agreed) agreedRef.current?.focus();
      return;
    }

    setSubmitting(true);
    try {
      const result = await register(normalized, password);
      navigate('/register/verifikasi', {
        replace: true,
        state: { email: result.email },
      });
    } catch (caught) {
      setError(caught instanceof AuthError ? caught.message : 'Gagal mendaftar. Coba lagi.');
    } finally {
      setSubmitting(false);
    }
  };

  const onProvider = async (provider: OAuthProvider) => {
    setError(null);
    setSubmitting(true);
    try {
      await loginWithProvider(provider);
      navigate('/chat', { replace: true });
    } catch (caught) {
      setError(caught instanceof AuthError ? caught.message : 'Gagal masuk dengan provider.');
    } finally {
      setSubmitting(false);
    }
  };

  return (
    <div className="space-y-5">
      <header className="space-y-1">
        <h1 className="text-2xl font-semibold tracking-tight text-ink-900 dark:text-ink-50">
          Buat akun Nara
        </h1>
        <p className="text-sm text-ink-600 dark:text-ink-300">
          Gratis, tanpa kartu kredit. Verifikasi email hanya simulasi pada mode demo.
        </p>
      </header>

      <OAuthButtons onProvider={onProvider} disabled={submitting} />

      <div className="flex items-center gap-3" aria-hidden="true">
        <span className="h-px flex-1 bg-ink-200 dark:bg-ink-800" />
        <span className="text-xs font-medium uppercase tracking-wide text-ink-400">atau</span>
        <span className="h-px flex-1 bg-ink-200 dark:bg-ink-800" />
      </div>

      <form className="space-y-4" onSubmit={onSubmit} noValidate>
        <div aria-live="polite" className="empty:hidden">
          {error ? (
            <Banner tone="danger" role="alert">
              {error}
            </Banner>
          ) : null}
        </div>

        <Input
          label="Email"
          type="email"
          name="email"
          autoComplete="email"
          inputMode="email"
          value={email}
          onChange={(event) => setEmail(event.target.value)}
          error={fieldErrors.email}
          disabled={submitting}
          placeholder="nama@contoh.com"
        />

        <div className="space-y-2">
          <PasswordInput
            label="Password"
            name="password"
            autoComplete="new-password"
            value={password}
            onChange={(event) => setPassword(event.target.value)}
            error={fieldErrors.password}
            disabled={submitting}
            hint={`Minimal ${MIN_PASSWORD_LENGTH} karakter.`}
          />
          <PasswordStrength password={password} />
        </div>

        <div className="space-y-1">
          <div className="flex items-start gap-2.5">
            <input
              ref={agreedRef}
              id="setuju-syarat"
              name="setuju"
              type="checkbox"
              checked={agreed}
              onChange={(event) => setAgreed(event.target.checked)}
              disabled={submitting}
              aria-invalid={fieldErrors.agreed ? true : undefined}
              aria-describedby={fieldErrors.agreed ? 'setuju-error' : undefined}
              className="mt-1 h-4 w-4 rounded border-ink-300 text-accent-500 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent-400 dark:border-ink-600 dark:bg-ink-800"
            />
            <label htmlFor="setuju-syarat" className="text-sm leading-relaxed text-ink-700 dark:text-ink-300">
              Saya setuju dengan{' '}
              <a
                href="/tos"
                target="_blank"
                rel="noopener noreferrer"
                className="font-medium text-accent-700 underline underline-offset-2 dark:text-accent-300"
              >
                Syarat
              </a>{' '}
              dan{' '}
              <a
                href="/privasi"
                target="_blank"
                rel="noopener noreferrer"
                className="font-medium text-accent-700 underline underline-offset-2 dark:text-accent-300"
              >
                Kebijakan Privasi
              </a>
              .
            </label>
          </div>
          {fieldErrors.agreed ? (
            <p id="setuju-error" className="text-xs font-medium text-red-600 dark:text-red-400">
              {fieldErrors.agreed}
            </p>
          ) : null}
        </div>

        <Button type="submit" fullWidth disabled={submitting}>
          {submitting ? 'Mendaftarkan…' : 'Daftar'}
        </Button>
      </form>

      <p className="text-center text-sm text-ink-600 dark:text-ink-300">
        Sudah punya akun?{' '}
        <Link
          to="/login"
          className="font-medium text-accent-700 underline underline-offset-2 hover:text-accent-800 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent-400 dark:text-accent-300"
        >
          Masuk
        </Link>
      </p>
    </div>
  );
}
