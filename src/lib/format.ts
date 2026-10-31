/** Utilitas format tampilan berbahasa Indonesia. */

export function formatTanggalIndonesia(iso: string): string {
  const date = new Date(iso);
  if (Number.isNaN(date.getTime())) return '-';
  try {
    return new Intl.DateTimeFormat('id-ID', {
      day: 'numeric',
      month: 'long',
      year: 'numeric',
    }).format(date);
  } catch {
    return date.toISOString().slice(0, 10);
  }
}

/**
 * Samarkan email: "dewi@example.com" -> "d***@example.com".
 * Bagian lokal yang pendek tetap disamarkan tanpa membocorkan panjang aslinya.
 */
export function maskEmail(email: string): string {
  const at = email.indexOf('@');
  if (at <= 0) return '***';
  const local = email.slice(0, at);
  const domain = email.slice(at);
  const first = local.slice(0, 1);
  const maskLength = Math.min(Math.max(local.length - 1, 3), 6);
  return `${first}${'*'.repeat(maskLength)}${domain}`;
}

export function initials(nameOrEmail: string): string {
  const base = nameOrEmail.trim();
  if (!base) return '?';
  const words = base.split(/\s+/).filter(Boolean);
  if (words.length === 0) return '?';
  if (words.length === 1) {
    return words[0].slice(0, 2).toUpperCase();
  }
  return (words[0][0] + words[1][0]).toUpperCase();
}

/** Warna avatar deterministik dari email (bukan acak). */
const AVATAR_HUES = [12, 32, 48, 92, 142, 172, 198, 222, 262, 292, 322, 342];

export function avatarHue(seed: string): number {
  let hash = 0;
  for (let i = 0; i < seed.length; i += 1) {
    hash = (hash * 31 + seed.charCodeAt(i)) % 100000;
  }
  return AVATAR_HUES[hash % AVATAR_HUES.length];
}

export function providerLabel(provider: string): string {
  switch (provider) {
    case 'github':
      return 'GitHub';
    case 'google':
      return 'Google';
    default:
      return 'Email';
  }
}

export function countdownLabel(seconds: number): string {
  return `${seconds} detik`;
}
