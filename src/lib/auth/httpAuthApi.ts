import {
  AuthError,
  type AuthApi,
  type ExportedData,
  type OAuthProvider,
  type RegisterResult,
  type UpdateProfileInput,
  type User,
} from './types';

/**
 * STUB adapter untuk backend sungguhan (rencana: FastAPI).
 *
 * Setiap fungsi sengaja melempar NOT_IMPLEMENTED. Kontrak HTTP yang
 * diharapkan ada di komentar masing-masing fungsi dan di README.
 *
 * Catatan keamanan: token/sesi sebaiknya disimpan di cookie HttpOnly
 * yang di-set backend, jadi `credentials: 'include'` dipakai dan tidak ada
 * token di localStorage.
 */

const API_BASE = '/api';

interface RequestOptions {
  method: 'GET' | 'POST' | 'PATCH' | 'DELETE';
  path: string;
  body?: unknown;
}

async function request<T>(_options: RequestOptions): Promise<T> {
  // TODO: implementasikan fetch ke `${API_BASE}${path}` dengan credentials.
  throw new AuthError(
    'NOT_IMPLEMENTED',
    'Backend autentikasi belum tersedia. Gunakan mode demo.',
  );
}

export const httpAuthApi: AuthApi = {
  /** POST /api/auth/register { email, password } -> 202 RegisterResult */
  async register(_email: string, _password: string): Promise<RegisterResult> {
    throw new AuthError(
      'NOT_IMPLEMENTED',
      'Backend autentikasi belum tersedia. Gunakan mode demo.',
    );
  },

  /** POST /api/auth/verify { email, code } -> 200 User (set cookie sesi) */
  async verify(_email: string, _code: string): Promise<User> {
    return request<User>({ method: 'POST', path: '/auth/verify' });
  },

  /** POST /api/auth/resend { email } -> 204 */
  async resend(_email: string): Promise<void> {
    return request<void>({ method: 'POST', path: '/auth/resend' });
  },

  /** POST /api/auth/login { email, password } -> 200 User */
  async login(_email: string, _password: string): Promise<User> {
    return request<User>({ method: 'POST', path: '/auth/login' });
  },

  /** GET /api/auth/oauth/{provider}/start (redirect) -> 200 User */
  async loginWithProvider(_provider: OAuthProvider): Promise<User> {
    return request<User>({ method: 'POST', path: '/auth/oauth' });
  },

  /** POST /api/auth/logout -> 204 */
  async logout(): Promise<void> {
    return request<void>({ method: 'POST', path: '/auth/logout' });
  },

  /** GET /api/auth/me -> 200 User | 204 */
  async me(): Promise<User | null> {
    return request<User | null>({ method: 'GET', path: '/auth/me' });
  },

  /** PATCH /api/account/profile { displayName } -> 200 User */
  async updateProfile(_input: UpdateProfileInput): Promise<User> {
    return request<User>({ method: 'PATCH', path: '/account/profile' });
  },

  /** POST /api/account/password { currentPassword, nextPassword } -> 204 */
  async changePassword(_currentPassword: string, _nextPassword: string): Promise<void> {
    return request<void>({ method: 'POST', path: '/account/password' });
  },

  /** DELETE /api/account -> 204 */
  async deleteAccount(): Promise<void> {
    return request<void>({ method: 'DELETE', path: '/account' });
  },

  /** GET /api/account/export -> 200 ExportedData */
  async exportData(): Promise<ExportedData> {
    return request<ExportedData>({ method: 'GET', path: '/account/export' });
  },
};

export { API_BASE };
