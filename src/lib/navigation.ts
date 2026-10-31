/**
 * Aturan tujuan navigasi setelah login/daftar.
 *
 * Hanya "/chat" dan "/profile" yang boleh dipakai sebagai ?next=.
 * Nilai lain ("//evil.com", "https://x.com", "/tos", "/\\x") diabaikan
 * diam-diam dan diganti default /chat.
 */

export const DEFAULT_TARGET = '/chat';
export const LOGIN_PATH = '/login';
export const PROFILE_PATH = '/profile';

const NEXT_ALLOWLIST: readonly string[] = [DEFAULT_TARGET, PROFILE_PATH];

export function isAllowedNext(value: string | null | undefined): boolean {
  if (typeof value !== 'string') return false;
  return NEXT_ALLOWLIST.includes(value);
}

export function sanitizeNext(value: string | null | undefined): string {
  return isAllowedNext(value) ? (value as string) : DEFAULT_TARGET;
}

/** Bangun URL login beserta ?next= yang aman. */
export function loginPathFor(next: string): string {
  const safe = sanitizeNext(next);
  return `${LOGIN_PATH}?next=${encodeURIComponent(safe)}`;
}
