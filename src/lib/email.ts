/** Validasi email sederhana yang cukup ketat untuk form. */
const EMAIL_RE = /^[^\s@]+@[^\s@]+\.[a-zA-Z]{2,}$/;

export function isValidEmail(value: string): boolean {
  const trimmed = value.trim();
  return trimmed.length <= 254 && EMAIL_RE.test(trimmed);
}

export function normalizeEmail(value: string): string {
  return value.trim().toLowerCase();
}
