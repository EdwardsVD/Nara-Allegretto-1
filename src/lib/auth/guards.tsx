import { useEffect, type ReactNode } from 'react';
import { Navigate, useLocation, useNavigate, useSearchParams } from 'react-router-dom';
import { Spinner } from '../../components/ui/Spinner';
import { readPendingEmail } from './pendingEmail';
import { useAuth } from './AuthContext';
import { loginPathFor, DEFAULT_TARGET, sanitizeNext } from '../navigation';

/** Spinner layar penuh selama status sesi 'loading'. */
export function FullScreenLoader({ label = 'Memuat…' }: { label?: string }) {
  return (
    <div className="grid min-h-dvh place-items-center bg-ink-50 dark:bg-ink-950">
      <Spinner label={label} />
    </div>
  );
}

/**
 * Wajib login. Tamu diarahkan ke /login?next=<path saat ini>.
 *
 * Perpindahan dilakukan lewat efek (navigate), bukan <Navigate> saat render.
 * Alasannya: saat sesi berakhir karena aksi pengguna (mis. "Hapus akun"),
 * <Navigate> dari guard ini bisa ditimpa oleh guard tamu di /login sehingga
 * tujuan akhir (mis. beranda) tidak tercapai. Navigasi eksplisit di efek
 * berjalan sesudah navigasi halaman dan tetap mempertahankan tujuan tamu
 * (login?next=...) karena GuestOnly menghormati ?next= yang lolos allowlist.
 */
export function RequireAuth({ children }: { children: ReactNode }) {
  const { status } = useAuth();
  const location = useLocation();
  const navigate = useNavigate();
  const target = loginPathFor(location.pathname + location.search);

  useEffect(() => {
    if (status === 'anonymous') {
      navigate(target, { replace: true });
    }
  }, [status, target, navigate]);

  if (status === 'loading') return <FullScreenLoader label="Memeriksa sesi…" />;
  if (status === 'anonymous') return null;
  return <>{children}</>;
}

/**
 * Hanya tamu. Pengguna yang sudah login langsung diarahkan ke /chat.
 * Bila datang dari guard dengan ?next=/profile (lolos allowlist), tujuan itu
 * dipakai agar tidak bertabrakan dengan navigasi halaman.
 */
export function GuestOnly({ children }: { children: ReactNode }) {
  const { status } = useAuth();
  const [searchParams] = useSearchParams();

  if (status === 'loading') return <FullScreenLoader label="Memeriksa sesi…" />;
  if (status === 'authenticated') {
    return <Navigate to={sanitizeNext(searchParams.get('next'))} replace />;
  }
  return <>{children}</>;
}

/**
 * Hanya untuk alur verifikasi: harus ada pendaftaran menunggu di
 * sessionStorage. Refresh tetap bekerja karena email dicadangkan.
 */
export function PendingOnly({ children }: { children: ReactNode }) {
  const { status } = useAuth();

  if (status === 'loading') return <FullScreenLoader label="Memeriksa sesi…" />;
  if (status === 'authenticated') return <Navigate to={DEFAULT_TARGET} replace />;
  if (!readPendingEmail()) return <Navigate to="/register" replace />;
  return <>{children}</>;
}
