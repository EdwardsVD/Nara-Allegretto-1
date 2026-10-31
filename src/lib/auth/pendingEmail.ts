import { isString, readJSON, removeKey, writeJSON } from '../storage';

/**
 * Email pendaftaran yang menunggu verifikasi.
 *
 * Disimpan di sessionStorage (bukan query string) agar halaman
 * /register/verifikasi tetap bekerja setelah refresh, dan dibersihkan
 * setelah verifikasi/akun dihapus.
 */
export const PENDING_EMAIL_KEY = 'nara_pending_email';

export function savePendingEmail(email: string): void {
  writeJSON(PENDING_EMAIL_KEY, email, 'session');
}

export function readPendingEmail(): string | null {
  const value = readJSON(PENDING_EMAIL_KEY, isString, 'session');
  if (!value || !value.includes('@')) return null;
  return value;
}

export function clearPendingEmail(): void {
  removeKey(PENDING_EMAIL_KEY, 'session');
}
