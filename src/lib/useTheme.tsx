import {
  createContext,
  useCallback,
  useContext,
  useEffect,
  useMemo,
  useState,
  useSyncExternalStore,
  type ReactNode,
} from 'react';
import {
  prefersDark,
  readThemePreference,
  resolveDark,
  saveThemePreference,
  type ThemePreference,
} from './themePreference';

interface ThemeContextValue {
  preference: ThemePreference;
  isDark: boolean;
  setPreference(next: ThemePreference): void;
  toggle(): void;
}

const ThemeContext = createContext<ThemeContextValue | null>(null);

function applyDom(isDark: boolean) {
  try {
    document.documentElement.classList.toggle('dark', isDark);
  } catch {
    /* diabaikan */
  }
}

/** Langganan ke media query prefers-color-scheme (dibaca lewat useSyncExternalStore). */
function subscribeSystemTheme(onChange: () => void): () => void {
  let media: MediaQueryList | null = null;
  try {
    media = window.matchMedia('(prefers-color-scheme: dark)');
  } catch {
    return () => {};
  }
  if (typeof media.addEventListener === 'function') {
    media.addEventListener('change', onChange);
    return () => media.removeEventListener('change', onChange);
  }
  return () => {};
}

export function ThemeProvider({ children }: { children: ReactNode }) {
  const [preference, setPreferenceState] = useState<ThemePreference>(() => readThemePreference());
  const systemDark = useSyncExternalStore(
    subscribeSystemTheme,
    () => prefersDark(),
    () => true,
  );
  const isDark =
    preference === 'dark' || (preference === 'system' && systemDark);

  // Sinkronkan kelas di <html> dengan preferensi (efek ke sistem eksternal).
  useEffect(() => {
    applyDom(isDark);
  }, [isDark]);

  const setPreference = useCallback((next: ThemePreference) => {
    saveThemePreference(next);
    setPreferenceState(next);
  }, []);

  const toggle = useCallback(() => {
    setPreferenceState((current) => {
      const next: ThemePreference = resolveDark(current) ? 'light' : 'dark';
      saveThemePreference(next);
      return next;
    });
  }, []);

  const value = useMemo(
    () => ({ preference, isDark, setPreference, toggle }),
    [preference, isDark, setPreference, toggle],
  );

  return <ThemeContext.Provider value={value}>{children}</ThemeContext.Provider>;
}

// eslint-disable-next-line react-refresh/only-export-components
export function useTheme(): ThemeContextValue {
  const context = useContext(ThemeContext);
  if (!context) throw new Error('useTheme harus dipakai di dalam <ThemeProvider>.');
  return context;
}
