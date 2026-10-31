import {
  createContext,
  useCallback,
  useContext,
  useEffect,
  useMemo,
  useRef,
  useState,
  type ReactNode,
} from 'react';
import { authApi } from './index';
import {
  toAuthError,
  type OAuthProvider,
  type RegisterResult,
  type User,
} from './types';

export type AuthStatus = 'loading' | 'authenticated' | 'anonymous';

export interface AuthContextValue {
  user: User | null;
  status: AuthStatus;
  register(email: string, password: string): Promise<RegisterResult>;
  verify(email: string, code: string): Promise<User>;
  resend(email: string): Promise<void>;
  login(email: string, password: string): Promise<User>;
  loginWithProvider(provider: OAuthProvider): Promise<User>;
  logout(): Promise<void>;
  updateProfile(input: { displayName: string }): Promise<User>;
  changePassword(currentPassword: string, nextPassword: string): Promise<void>;
  deleteAccount(): Promise<void>;
}

const AuthContext = createContext<AuthContextValue | null>(null);

export function AuthProvider({ children }: { children: ReactNode }) {
  const [user, setUser] = useState<User | null>(null);
  const [status, setStatus] = useState<AuthStatus>('loading');
  const mounted = useRef(true);

  useEffect(() => {
    mounted.current = true;
    let cancelled = false;
    authApi
      .me()
      .then((current) => {
        if (cancelled) return;
        setUser(current);
        setStatus(current ? 'authenticated' : 'anonymous');
      })
      .catch(() => {
        if (cancelled) return;
        // Sesi rusak / backend tidak terjangkau: anggap tamu, jangan crash.
        setUser(null);
        setStatus('anonymous');
      });
    return () => {
      cancelled = true;
      mounted.current = false;
    };
  }, []);

  const login = useCallback(async (email: string, password: string) => {
    try {
      const next = await authApi.login(email, password);
      setUser(next);
      setStatus('authenticated');
      return next;
    } catch (error) {
      throw toAuthError(error);
    }
  }, []);

  const loginWithProvider = useCallback(async (provider: OAuthProvider) => {
    try {
      const next = await authApi.loginWithProvider(provider);
      setUser(next);
      setStatus('authenticated');
      return next;
    } catch (error) {
      throw toAuthError(error);
    }
  }, []);

  const register = useCallback(async (email: string, password: string) => {
    try {
      return await authApi.register(email, password);
    } catch (error) {
      throw toAuthError(error);
    }
  }, []);

  const verify = useCallback(async (email: string, code: string) => {
    try {
      const next = await authApi.verify(email, code);
      setUser(next);
      setStatus('authenticated');
      return next;
    } catch (error) {
      throw toAuthError(error);
    }
  }, []);

  const resend = useCallback(async (email: string) => {
    try {
      await authApi.resend(email);
    } catch (error) {
      throw toAuthError(error);
    }
  }, []);

  const logout = useCallback(async () => {
    try {
      await authApi.logout();
    } finally {
      setUser(null);
      setStatus('anonymous');
    }
  }, []);

  const updateProfile = useCallback(async (input: { displayName: string }) => {
    try {
      const next = await authApi.updateProfile(input);
      setUser(next);
      setStatus('authenticated');
      return next;
    } catch (error) {
      throw toAuthError(error);
    }
  }, []);

  const changePassword = useCallback(
    async (currentPassword: string, nextPassword: string) => {
      try {
        await authApi.changePassword(currentPassword, nextPassword);
      } catch (error) {
        throw toAuthError(error);
      }
    },
    [],
  );

  const deleteAccount = useCallback(async () => {
    try {
      await authApi.deleteAccount();
    } finally {
      setUser(null);
      setStatus('anonymous');
    }
  }, []);

  const value = useMemo<AuthContextValue>(
    () => ({
      user,
      status,
      register,
      verify,
      resend,
      login,
      loginWithProvider,
      logout,
      updateProfile,
      changePassword,
      deleteAccount,
    }),
    [
      user,
      status,
      register,
      verify,
      resend,
      login,
      loginWithProvider,
      logout,
      updateProfile,
      changePassword,
      deleteAccount,
    ],
  );

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
}

// eslint-disable-next-line react-refresh/only-export-components
export function useAuth(): AuthContextValue {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth harus dipakai di dalam <AuthProvider>.');
  }
  return context;
}
