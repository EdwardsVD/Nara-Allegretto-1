/**
 * Kontrak adapter autentikasi.
 *
 * Halaman hanya berbicara dengan `AuthApi`. Implementasi saat ini:
 *  - dummyAuthApi.ts : data simulasi di localStorage
 *  - httpAuthApi.ts  : stub untuk backend FastAPI (belum diimplementasikan)
 * Mengganti backend cukup dengan mengisi stub http, halaman tidak berubah.
 */

export type Provider = 'email' | 'github' | 'google';

export type OAuthProvider = Exclude<Provider, 'email'>;

export interface User {
  id: string;
  email: string;
  displayName: string;
  provider: Provider;
  verified: boolean;
  /** Tanggal ISO 8601. */
  createdAt: string;
}

export interface Session {
  userId: string;
  /** Tanggal ISO 8601, berlaku 24 jam. */
  expiresAt: string;
}

export interface RegisterResult {
  /** Email tujuan verifikasi. */
  email: string;
  /**
   * true bila email sudah terdaftar & terverifikasi. UI tetap menampilkan
   * pesan yang sama agar keberadaan akun tidak bocor.
   */
  existingAccount: boolean;
  /** Pesan sukses netral (sama untuk email baru maupun yang sudah terdaftar). */
  message: string;
  /** Hanya ada di mode dummy; tidak pernah dikirim backend sungguhan. */
  demoCode?: string;
}

export interface UpdateProfileInput {
  displayName: string;
}

export interface ExportedData {
  profile: Omit<User, 'id'> & { id: string };
  exportedAt: string;
  /** Chat sengaja tidak disertakan karena tidak disimpan. */
  chatHistory: null;
}

export type AuthErrorCode =
  | 'INVALID_CREDENTIALS'
  | 'NOT_VERIFIED'
  | 'RATE_LIMITED'
  | 'VALIDATION'
  | 'NETWORK'
  | 'NOT_IMPLEMENTED';

export interface AuthErrorShape {
  code: AuthErrorCode;
  message: string;
  /** Khusus NOT_VERIFIED: email yang perlu diverifikasi. */
  email?: string;
}

export class AuthError extends Error implements AuthErrorShape {
  readonly code: AuthErrorCode;
  readonly email?: string;

  constructor(code: AuthErrorCode, message: string, email?: string) {
    super(message);
    this.name = 'AuthError';
    this.code = code;
    if (email !== undefined) this.email = email;
  }
}

export interface AuthApi {
  register(email: string, password: string): Promise<RegisterResult>;
  verify(email: string, code: string): Promise<User>;
  resend(email: string): Promise<void>;
  login(email: string, password: string): Promise<User>;
  loginWithProvider(provider: OAuthProvider): Promise<User>;
  logout(): Promise<void>;
  me(): Promise<User | null>;
  updateProfile(input: UpdateProfileInput): Promise<User>;
  changePassword(currentPassword: string, nextPassword: string): Promise<void>;
  deleteAccount(): Promise<void>;
  exportData(): Promise<ExportedData>;
}

export function isAuthError(value: unknown): value is AuthError {
  return value instanceof AuthError;
}

/** Ubah error tak dikenal menjadi AuthError berbahasa Indonesia. */
export function toAuthError(value: unknown): AuthError {
  if (value instanceof AuthError) return value;
  if (value instanceof TypeError) {
    return new AuthError('NETWORK', 'Tidak dapat terhubung ke server. Periksa koneksi Anda.');
  }
  return new AuthError('NETWORK', 'Terjadi kesalahan. Coba lagi sebentar lagi.');
}
