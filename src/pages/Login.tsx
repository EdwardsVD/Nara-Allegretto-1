import { useRef, useState, type FormEvent } from 'react';
import { Link, useNavigate, useSearchParams } from 'react-router-dom';
import { OAuthButtons } from '../components/auth/OAuthButtons';
import { Banner } from '../components/ui/Banner';
import { Button } from '../components/ui/Button';
import { Input } from '../components/ui/Input';
import { PasswordInput } from '../components/ui/PasswordInput';
import { useAuth } from '../lib/auth/AuthContext';
import { AuthError, type OAuthProvider } from '../lib/auth/types';
import { isValidEmail, normalizeEmail } from '../lib/email';
import { AUTH_AVAILABLE } from '../lib/env';
import { sanitizeNext } from '../lib/navigation';
import { usePageTitle } from '../lib/usePageTitle';
import { AuthDisabled } from './AuthDisabled';

export function Login() {
  usePageTitle('Masuk');
  const { login, loginWithProvider } = useAuth();
  const navigate = useNavigate();
  const [searchParams] = useSearchParams();
  const nextTarget = sanitizeNext(searchParams.get('next'));
  const verified = searchParams.get('verified') === '1';

  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState<string | null>(null);
  const [fieldErrors, setFieldErrors] = useState<{ email?: string; password?: string }>({});
  const [submitting, setSubmitting] = useState(false);
  const errorRef = useRef<HTMLDivElement>(null);

  if (!AUTH_AVAILABLE) return <AuthDisabled action="login" />;

  const goToTarget = () => {
    navigate(nextTarget, { replace: true });
  };

  const onSubmit = async (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    setError(null);
    const nextFieldErrors: { email?: string; password?: string } = {};
    if (!email.trim()) nextFieldErrors.email = 'Email wajib diisi.';
    else if (!isValidEmail(email)) nextFieldErrors.email = 'Format email tidak valid.';
    if (!password) nextFieldErrors.password = 'Password wajib diisi.';
    setFieldErrors(nextFieldErrors);
    if (Object.keys(nextFieldErrors).length > 0) return;

    setSubmitting(true);
    try {
      await login(normalizeEmail(email), password);
      goToTarget();
    } catch (caught) {
      if (caught instanceof AuthError && caught.code === 'NOT_VERIFIED') {
        // Arahkan ke verifikasi dengan email lewat router state.
        navigate('/register/verifikasi', {
          replace: true,
          state: { email: caught.email ?? normalizeEmail(email) },
        });
        return;
      }
      setError(caught instanceof AuthError ? caught.message : 'Gagal masuk. Coba lagi.');
      requestAnimationFrame(() => errorRef.current?.focus());
    } finally {
      setSubmitting(false);
    }
  };

  const onProvider = async (provider: OAuthProvider) => {
    setError(null);
    setSubmitting(true);
    try {
      await loginWithProvider(provider);
      goToTarget();
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
          Masuk ke Nara
        </h1>
        <p className="text-sm text-ink-600 dark:text-ink-300">
          Lanjutkan percakapan dan kelola profil Anda.
        </p>
      </header>

      {verified ? (
        <Banner tone="success" role="status">
          Email berhasil diverifikasi. Silakan masuk.
        </Banner>
      ) : null}

      <OAuthButtons onProvider={onProvider} disabled={submitting} />

      <div className="flex items-center gap-3" aria-hidden="true">
        <span className="h-px flex-1 bg-ink-200 dark:bg-ink-800" />
        <span className="text-xs font-medium uppercase tracking-wide text-ink-400">atau</span>
        <span className="h-px flex-1 bg-ink-200 dark:bg-ink-800" />
      </div>

      <form className="space-y-4" onSubmit={onSubmit} noValidate>
        <div ref={errorRef} tabIndex={-1} aria-live="polite" className="focus:outline-none">
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

        <PasswordInput
          label="Password"
          name="password"
          autoComplete="current-password"
          value={password}
          onChange={(event) => setPassword(event.target.value)}
          error={fieldErrors.password}
          disabled={submitting}
        />

        <Button type="submit" fullWidth disabled={submitting}>
          {submitting ? 'Memproses…' : 'Masuk'}
        </Button>
      </form>

      <p className="text-center text-sm text-ink-600 dark:text-ink-300">
        Belum punya akun?{' '}
        <Link
          to="/register"
          className="font-medium text-accent-700 underline underline-offset-2 hover:text-accent-800 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent-400 dark:text-accent-300"
        >
          Daftar
        </Link>
      </p>
    </div>
  );
}
