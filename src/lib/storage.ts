/**
 * Pembungkus aman untuk localStorage/sessionStorage.
 *
 * Semua pembacaan/penulisan data di aplikasi WAJIB lewat modul ini:
 * - try/catch untuk mode privat, kuota penuh, atau storage diblokir
 * - JSON.parse aman + validator bentuk data
 * - data rusak diabaikan (return null), tidak pernah membuat aplikasi crash
 */

export type StorageKind = 'local' | 'session';

function getArea(kind: StorageKind): Storage | null {
  try {
    const area = kind === 'local' ? window.localStorage : window.sessionStorage;
    // Beberapa browser melempar error saat properti diakses.
    if (!area) return null;
    return area;
  } catch {
    return null;
  }
}

export function readRaw(key: string, kind: StorageKind = 'local'): string | null {
  try {
    return getArea(kind)?.getItem(key) ?? null;
  } catch {
    return null;
  }
}

export function writeRaw(key: string, value: string, kind: StorageKind = 'local'): boolean {
  try {
    const area = getArea(kind);
    if (!area) return false;
    area.setItem(key, value);
    return true;
  } catch {
    return false;
  }
}

export function removeKey(key: string, kind: StorageKind = 'local'): void {
  try {
    getArea(kind)?.removeItem(key);
  } catch {
    /* diabaikan dengan sengaja */
  }
}

/**
 * Baca JSON dengan validator. Jika data rusak / bentuknya tidak cocok,
 * nilai dibuang (dan opsional dihapus) lalu return null.
 */
export function readJSON<T>(
  key: string,
  guard: (value: unknown) => value is T,
  kind: StorageKind = 'local',
): T | null {
  const raw = readRaw(key, kind);
  if (raw === null) return null;
  try {
    const parsed: unknown = JSON.parse(raw);
    if (!guard(parsed)) {
      removeKey(key, kind);
      return null;
    }
    return parsed;
  } catch {
    removeKey(key, kind);
    return null;
  }
}

export function writeJSON(key: string, value: unknown, kind: StorageKind = 'local'): boolean {
  try {
    return writeRaw(key, JSON.stringify(value), kind);
  } catch {
    return false;
  }
}

/** Validator umum yang bisa dipakai ulang. */
export const isRecord = (value: unknown): value is Record<string, unknown> =>
  typeof value === 'object' && value !== null && !Array.isArray(value);

export const isString = (value: unknown): value is string => typeof value === 'string';

export const isArrayOf =
  <T>(guard: (value: unknown) => value is T) =>
  (value: unknown): value is T[] =>
    Array.isArray(value) && value.every(guard);
