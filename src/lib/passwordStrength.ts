/** Skor kekuatan password sederhana, tanpa library. */
export function scorePassword(password: string): { score: 0 | 1 | 2 | 3; label: string } {
  if (!password) return { score: 0, label: 'Belum diisi' };
  let points = 0;
  if (password.length >= 8) points += 1;
  if (password.length >= 12) points += 1;
  if (/[a-z]/.test(password) && /[A-Z]/.test(password)) points += 1;
  if (/\d/.test(password)) points += 1;
  if (/[^A-Za-z0-9]/.test(password)) points += 1;

  if (password.length < 8) return { score: 1, label: 'Lemah' };
  if (points <= 2) return { score: 1, label: 'Lemah' };
  if (points <= 3) return { score: 2, label: 'Sedang' };
  return { score: 3, label: 'Kuat' };
}
