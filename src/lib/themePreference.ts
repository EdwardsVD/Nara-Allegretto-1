import { isString, readRaw, removeKey, writeRaw } from './storage';

export type ThemePreference = 'system' | 'light' | 'dark';

export const THEME_KEY = 'nara_theme';

const THEME_VALUES: ThemePreference[] = ['system', 'light', 'dark'];

export function isThemePreference(value: unknown): value is ThemePreference {
  return isString(value) && (THEME_VALUES as string[]).includes(value);
}

export function readThemePreference(): ThemePreference {
  const raw = readRaw(THEME_KEY, 'local');
  return isThemePreference(raw) ? raw : 'system';
}

export function saveThemePreference(preference: ThemePreference): void {
  if (preference === 'system') {
    removeKey(THEME_KEY, 'local');
    return;
  }
  writeRaw(THEME_KEY, preference, 'local');
}

export function prefersDark(): boolean {
  try {
    return window.matchMedia('(prefers-color-scheme: dark)').matches;
  } catch {
    return true;
  }
}

export function resolveDark(preference: ThemePreference): boolean {
  if (preference === 'dark') return true;
  if (preference === 'light') return false;
  return prefersDark();
}
