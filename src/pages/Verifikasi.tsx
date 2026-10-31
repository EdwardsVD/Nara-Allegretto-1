import { useEffect, useRef, useState, type ChangeEvent, type ClipboardEvent, type FormEvent } from 'react';
import { Link, useLocation, useNavigate } from 'react-router-dom';
import { Banner } from '../components/ui/Banner';
import { Button } from '../components/ui/Button';
import { useAuth } from '../lib/auth/AuthContext';
import { AuthError } from '../lib/auth/types';
import { clearPendingEmail, readPendingEmail, savePendingEmail } from '../lib/auth/pendingEmail';
import { maskEmail } from '../lib/format';
import { useCountdown } from '../lib/useCountdown';
import { usePageTitle } from '../lib/usePageTitle';

interface LocationState {
  email?: string;
}

const RESEND_SECONDS = 60;
const LOCK_SECONDS = 30;
const MAX_ATTEMPTS = 5;

export function Verifikasi() {
  usePageTitle('Verifikasi email');
  const { verify, resend } = useAuth();
  const navigate = useNavigate();
  const location = useLocation();
  const stateEmail = (location.state as LocationState | null)?.email;
  const pendingEmail = readPendingEmail();

  // Email dari router state; cadangan sessionStorage dipakai setelah refresh.
  const email = stateEmail ?? pendingEmail ?? '';

  const [code, setCode] = useState('');
  const [error, setError] = useState<string | null>(null);
  const [info, setInfo] = useState<string | null>(null);
  const [submitting, setSubmitting] = useState(false);
  const [resending, setResending] = useState(false);
  const attemptsRef = useRef(0);
  const inputRef = useRef<HTMLInputElement>(null);
  const errorRef = useRef<HTMLDivElement>(null);
  const resendTimer = useCountdown();
  const lockTimer = useCountdown();

  const locked = lockTimer.isRunning;

  useEffect(() => {
    // Pastikan cadangan sessionStorage selalu sinkron untuk refresh.
    if (stateEmail && stateEmail !== pendingEmail) {
      savePendingEmail(stateEmail);
    }
  }, [stateEmail, pendingEmail]);

  useEffect(() => {
    if (!locked) inputRef.current?.focus();
  }, [locked]);

  const onSubmit = async (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    if (locked || submitting) return;
    setError(null);
    setInfo(null);
    if (code.length !== 6) {
      setError('Kode verifikasi terdiri dari 6 digit.');
      return;
    }

    setSubmitting(true);
    try {
      await verify(email, code);
      clearPendingEmail();
      navigate('/chat', { replace: true });
    } catch (caught) {
      attemptsRef.current += 1;
      const nextAttempts = attemptsRef.current;
      setCode('');
      if (nextAttempts >= MAX_ATTEMPTS) {
        // Pesan kunci tampil dari banner hitung mundur (tidak ada error
        // menggantung setelah kunci berakhir).
        setError(null);
        lockTimer.start(LOCK_SECONDS);
      } else {
        const remainingAttempts = MAX_ATTEMPTS - nextAttempts;
        setError(
          caught instanceof AuthError
            ? `${caught.message} Sisa percobaan: ${remainingAttempts}.`
            : 'Kode verifikasi salah.',
        );
        requestAnimationFrame(() => inputRef.current?.focus());
      }
      requestAnimationFrame(() => errorRef.current?.focus());
    } finally {
      setSubmitting(false);
    }
  };

  const onResend = async () => {
    if (resendTimer.isRunning || resending) return;
    setResending(true);
    setError(null);
    try {
      await resend(email);
      setInfo('Kode verifikasi dikirim ulang. (Simulasi: kode tetap 123456.)');
      resendTimer.start(RESEND_SECONDS);
    } catch (caught) {
      setError(caught instanceof AuthError ? caught.message : 'Gagal mengirim ulang kode.');
    } finally {
      setResending(false);
    }
  };

  const onPaste = (event: ClipboardEvent<HTMLInputElement>) => {
    if (!locked && attemptsRef.current >= MAX_ATTEMPTS) {
      attemptsRef.current = 0;
    }
    const pasted = event.clipboardData.getData('text').replace(/\D/g, '').slice(0, 6);
    if (!pasted) return;
    event.preventDefault();
    setCode(pasted);
  };

  const onDigitChange = (index: number) => (event: ChangeEvent<HTMLInputElement>) => {
    // Kunci sudah berakhir: beri jatah percobaan baru saat pengguna mengetik lagi.
    if (!locked && attemptsRef.current >= MAX_ATTEMPTS) {
      attemptsRef.current = 0;
    }
    const digits = event.target.value.replace(/\D/g, '');
    if (!digits) return;
    const next = (code.slice(0, index) + digits + code.slice(index + digits.length)).slice(0, 6);
    setCode(next);
    // Fokuskan kotak berikutnya yang masih kosong.
    const nextEmpty = Math.min(next.length, 5);
    const boxes = document.querySelectorAll<HTMLInputElement>('[data-code-box]');
    boxes[nextEmpty]?.focus();
  };

  const digits = code.padEnd(6, ' ').split('');

  if (!email) return null;

  return (
    <div className="space-y-5">
      <header className="space-y-2">
        <span className="inline-grid h-11 w-11 place-items-center rounded-2xl border border-accent-400/40 bg-accent-50 text-accent-800 dark:bg-accent-400/10 dark:text-accent-200">
          <svg aria-hidden="true" viewBox="0 0 24 24" className="h-5 w-5" fill="none" stroke="currentColor" strokeWidth="1.7">
            <rect x="3.5" y="5.5" width="17" height="13" rx="2.2" />
            <path d="m4.5 7 7.5 6 7.5-6" strokeLinecap="round" strokeLinejoin="round" />
          </svg>
        </span>
        <h1 className="text-2xl font-semibold tracking-tight text-ink-900 dark:text-ink-50">
          Periksa email Anda
        </h1>
        <p className="text-sm text-ink-600 dark:text-ink-300">
          Kami mengirim kode 6 digit ke{' '}
          <span className="font-semibold text-ink-900 dark:text-ink-50" data-testid="masked-email">
            {maskEmail(email)}
          </span>
          .
        </p>
      </header>

      <div
        ref={errorRef}
        tabIndex={-1}
        aria-live="polite"
        className="space-y-2 focus:outline-none empty:hidden"
      >
        {error ? (
          <Banner tone="danger" role="alert">
            {error}
          </Banner>
        ) : null}
        {info && !error ? (
          <Banner tone="info" role="status">
            {info}
          </Banner>
        ) : null}
        {locked ? (
          <div>
            <Banner tone="warning" role="status">
              <strong className="font-semibold">Terlalu banyak percobaan.</strong> Input dikunci
              sementara, coba lagi dalam <strong>{lockTimer.remaining} detik</strong>.
            </Banner>
          </div>
        ) : null}
      </div>

      <form className="space-y-4" onSubmit={onSubmit} noValidate>
        <fieldset className="space-y-2" disabled={locked || submitting}>
          <legend className="mb-1 block text-sm font-medium text-ink-800 dark:text-ink-100">
            Kode verifikasi
          </legend>
          <div className="flex justify-between gap-2">
            {digits.map((digit, index) => (
              <input
                key={index}
                data-code-box
                ref={index === 0 ? inputRef : undefined}
                aria-label={`Digit ${index + 1} dari 6`}
                aria-describedby="kode-hint"
                aria-invalid={error ? true : undefined}
                id={index === 0 ? 'kode-verifikasi' : `kode-${index}`}
                name={index === 0 ? 'kode' : undefined}
                type="text"
                inputMode="numeric"
                autoComplete={index === 0 ? 'one-time-code' : 'off'}
                pattern="[0-9]*"
                maxLength={1}
                value={digit.trim()}
                onChange={onDigitChange(index)}
                onPaste={onPaste}
                disabled={locked || submitting}
                className="h-12 w-full rounded-xl border border-ink-300 bg-white text-center text-xl font-semibold tabular-nums text-ink-900 transition-colors focus-visible:border-accent-400 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent-400/60 disabled:cursor-not-allowed disabled:opacity-50 sm:h-14 sm:text-2xl dark:border-ink-700 dark:bg-ink-900 dark:text-ink-50"
              />
            ))}
          </div>
          <p id="kode-hint" className="text-xs text-ink-500 dark:text-ink-400">
            Mode demo: kode selalu <strong className="font-semibold">123456</strong>. Anda juga
            bisa menempel (paste) kode dari email.
          </p>
        </fieldset>

        <Button type="submit" fullWidth disabled={locked || submitting}>
          {submitting ? 'Memverifikasi…' : 'Verifikasi'}
        </Button>
      </form>

      <div className="flex flex-col items-center gap-2 border-t border-ink-200 pt-4 text-sm dark:border-ink-800">
        <Button
          type="button"
          variant="ghost"
          size="sm"
          onClick={() => void onResend()}
          disabled={resendTimer.isRunning || resending || submitting}
        >
          {resendTimer.isRunning
            ? `Kirim ulang dalam ${resendTimer.remaining} detik`
            : resending
              ? 'Mengirim…'
              : 'Kirim ulang kode'}
        </Button>
        <Link
          to="/register"
          state={{ email }}
          className="focus-ring rounded text-xs text-ink-600 underline underline-offset-2 hover:text-ink-900 dark:text-ink-300 dark:hover:text-ink-50"
        >
          Ganti email
        </Link>
      </div>
    </div>
  );
}
