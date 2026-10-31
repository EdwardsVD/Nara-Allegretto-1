import { isValidEmail, normalizeEmail } from '../email';
import {
  isArrayOf,
  isRecord,
  isString,
  readJSON,
  removeKey,
  writeJSON,
} from '../storage';
import { clearPendingEmail, savePendingEmail } from './pendingEmail';
import { DEMO_CODE } from '../env';
import {
  AuthError,
  type AuthApi,
  type ExportedData,
  type OAuthProvider,
  type Provider,
  type RegisterResult,
  type Session,
  type UpdateProfileInput,
  type User,
} from './types';

/**
 * Implementasi DUMMY dari AuthApi.
 *
 * Aturan penting:
 * - Tidak ada backend, email, atau OAuth sungguhan.
 * - Password TIDAK PERNAH disimpan. Password hanya divalidasi (min 8 karakter).
 * - Semua panggilan punya delay 500-900 ms yang deterministik (bukan acak),
 *   dan tidak ada kegagalan acak.
 */

export const USERS_KEY = 'nara_dummy_users';
export const SESSION_KEY = 'nara_dummy_session';
export const SESSION_TTL_MS = 24 * 60 * 60 * 1000;
export const MIN_PASSWORD_LENGTH = 8;

/** Delay deterministik: bergantian 500-900 ms mengikuti hitungan panggilan. */
const DELAY_STEPS = [650, 500, 900, 750, 600, 850, 550, 800];
let delayCursor = 0;

function nextDelay(): number {
  const value = DELAY_STEPS[delayCursor % DELAY_STEPS.length];
  delayCursor += 1;
  return value;
}

export function wait(ms: number): Promise<void> {
  return new Promise((resolve) => {
    setTimeout(resolve, ms);
  });
}

async function simulate<T>(fn: () => T | Promise<T>): Promise<T> {
  await wait(nextDelay());
  return fn();
}

/** Khusus tes: kembalikan penjadwalan delay ke kondisi awal. */
export function __resetDummyDelay(): void {
  delayCursor = 0;
}

const PROVIDER_VALUES: Provider[] = ['email', 'github', 'google'];

function isUser(value: unknown): value is User {
  if (!isRecord(value)) return false;
  return (
    isString(value.id) &&
    isString(value.email) &&
    isString(value.displayName) &&
    isString(value.provider) &&
    PROVIDER_VALUES.includes(value.provider as Provider) &&
    typeof value.verified === 'boolean' &&
    isString(value.createdAt)
  );
}

function isSession(value: unknown): value is Session {
  return isRecord(value) && isString(value.userId) && isString(value.expiresAt);
}

function readUsers(): User[] {
  return readJSON(USERS_KEY, isArrayOf(isUser), 'local') ?? [];
}

function writeUsers(users: User[]): void {
  writeJSON(USERS_KEY, users, 'local');
}

function readSession(): Session | null {
  return readJSON(SESSION_KEY, isSession, 'local');
}

function clearSession(): void {
  removeKey(SESSION_KEY, 'local');
}

function startSession(userId: string): void {
  const session: Session = {
    userId,
    expiresAt: new Date(Date.now() + SESSION_TTL_MS).toISOString(),
  };
  writeJSON(SESSION_KEY, session, 'local');
}

function isExpired(session: Session): boolean {
  const expiry = new Date(session.expiresAt).getTime();
  return Number.isNaN(expiry) || expiry <= Date.now();
}

function assertPassword(password: string): void {
  if (password.length < MIN_PASSWORD_LENGTH) {
    throw new AuthError(
      'VALIDATION',
      `Password minimal ${MIN_PASSWORD_LENGTH} karakter.`,
    );
  }
}

function assertEmail(email: string): string {
  const normalized = normalizeEmail(email);
  if (!isValidEmail(normalized)) {
    throw new AuthError('VALIDATION', 'Format email tidak valid.');
  }
  return normalized;
}

function createId(): string {
  return `usr_${Date.now().toString(36)}${Math.random().toString(36).slice(2, 8)}`;
}

function displayNameFromEmail(email: string): string {
  const local = email.split('@')[0] ?? 'Pengguna';
  const cleaned = local.replace(/[._-]+/g, ' ').trim();
  if (!cleaned) return 'Pengguna';
  return cleaned
    .split(' ')
    .map((part) => part.charAt(0).toUpperCase() + part.slice(1))
    .join(' ');
}

function requireCurrentUser(): User {
  const session = readSession();
  if (!session || isExpired(session)) {
    clearSession();
    throw new AuthError('INVALID_CREDENTIALS', 'Sesi berakhir. Silakan masuk kembali.');
  }
  const users = readUsers();
  const user = users.find((item) => item.id === session.userId);
  if (!user) {
    clearSession();
    throw new AuthError('INVALID_CREDENTIALS', 'Sesi tidak ditemukan. Silakan masuk kembali.');
  }
  return user;
}

/** Pesan register selalu identik agar tidak membocorkan email terdaftar. */
const REGISTER_MESSAGE_SUCCESS =
  'Pendaftaran diterima. Kami mengirim kode 6 digit ke email Anda.';

export const dummyAuthApi: AuthApi = {
  async register(rawEmail: string, password: string): Promise<RegisterResult> {
    const email = assertEmail(rawEmail);
    assertPassword(password);

    return simulate<RegisterResult>(() => {
      const users = readUsers();
      const existing = users.find((user) => user.email === email);

      savePendingEmail(email);

      if (existing) {
        // Email sudah terdaftar: balasan sama persis, status verifikasi tidak diubah
        // bila akun sudah terverifikasi.
        return {
          email,
          existingAccount: existing.verified,
          demoCode: DEMO_CODE,
          message: REGISTER_MESSAGE_SUCCESS,
        };
      }

      const newUser: User = {
        id: createId(),
        email,
        displayName: displayNameFromEmail(email),
        provider: 'email',
        verified: false,
        createdAt: new Date().toISOString(),
      };
      writeUsers([...users, newUser]);
      return {
        email,
        existingAccount: false,
        demoCode: DEMO_CODE,
        message: REGISTER_MESSAGE_SUCCESS,
      };
    });
  },

  async verify(rawEmail: string, code: string): Promise<User> {
    const email = assertEmail(rawEmail);
    return simulate(() => {
      if (code.trim() !== DEMO_CODE) {
        throw new AuthError('VALIDATION', 'Kode verifikasi salah. Periksa kembali kode Anda.');
      }
      const users = readUsers();
      const index = users.findIndex((user) => user.email === email);
      if (index === -1) {
        throw new AuthError(
          'VALIDATION',
          'Data pendaftaran tidak ditemukan. Silakan daftar ulang.',
        );
      }
      const updated: User = { ...users[index], verified: true };
      const nextUsers = [...users];
      nextUsers[index] = updated;
      writeUsers(nextUsers);
      startSession(updated.id);
      clearPendingEmail();
      return updated;
    });
  },

  async resend(rawEmail: string): Promise<void> {
    const email = assertEmail(rawEmail);
    await simulate(() => {
      savePendingEmail(email);
    });
  },

  async login(rawEmail: string, password: string): Promise<User> {
    const email = normalizeEmail(rawEmail);
    return simulate(() => {
      const users = readUsers();
      const user = users.find((item) => item.email === email);

      if (!user) {
        // Pesan sama persis dengan kasus password salah.
        throw new AuthError('INVALID_CREDENTIALS', 'Email atau password salah');
      }
      if (password.length < MIN_PASSWORD_LENGTH) {
        throw new AuthError('INVALID_CREDENTIALS', 'Email atau password salah');
      }
      if (!user.verified) {
        throw new AuthError(
          'NOT_VERIFIED',
          'Email belum diverifikasi. Masukkan kode verifikasi yang kami kirim.',
          email,
        );
      }
      startSession(user.id);
      return user;
    });
  },

  async loginWithProvider(provider: OAuthProvider): Promise<User> {
    return simulate(() => {
      const email = `demo-${provider}@example.com`;
      const users = readUsers();
      const existing = users.find((user) => user.email === email);
      if (existing) {
        const updated: User = { ...existing, provider, verified: true };
        writeUsers(users.map((item) => (item.id === existing.id ? updated : item)));
        startSession(updated.id);
        return updated;
      }
      const created: User = {
        id: createId(),
        email,
        displayName: provider === 'github' ? 'Demo GitHub' : 'Demo Google',
        provider,
        verified: true,
        createdAt: new Date().toISOString(),
      };
      writeUsers([...users, created]);
      startSession(created.id);
      return created;
    });
  },

  async logout(): Promise<void> {
    await simulate(() => {
      clearSession();
    });
  },

  async me(): Promise<User | null> {
    // Tidak memakai delay panjang saat startup agar UI tidak berkedip lama.
    await wait(120);
    const session = readSession();
    if (!session || isExpired(session)) {
      clearSession();
      return null;
    }
    const user = readUsers().find((item) => item.id === session.userId);
    if (!user) {
      clearSession();
      return null;
    }
    return user;
  },

  async updateProfile(input: UpdateProfileInput): Promise<User> {
    return simulate(() => {
      const name = input.displayName.trim();
      if (name.length < 2 || name.length > 40) {
        throw new AuthError('VALIDATION', 'Nama tampilan harus 2-40 karakter.');
      }
      const current = requireCurrentUser();
      const updated: User = { ...current, displayName: name };
      writeUsers(readUsers().map((item) => (item.id === current.id ? updated : item)));
      return updated;
    });
  },

  async changePassword(currentPassword: string, nextPassword: string): Promise<void> {
    return simulate(() => {
      const current = requireCurrentUser();
      if (current.provider !== 'email') {
        throw new AuthError(
          'VALIDATION',
          `Akun dikelola oleh ${current.provider === 'github' ? 'GitHub' : 'Google'}.`,
        );
      }
      if (currentPassword.length < MIN_PASSWORD_LENGTH) {
        throw new AuthError('VALIDATION', 'Password lama tidak sesuai.');
      }
      assertPassword(nextPassword);
      if (currentPassword === nextPassword) {
        throw new AuthError('VALIDATION', 'Password baru harus berbeda dari password lama.');
      }
      // Simulasi: tidak ada password yang disimpan.
    });
  },

  async deleteAccount(): Promise<void> {
    await simulate(() => {
      const current = requireCurrentUser();
      writeUsers(readUsers().filter((item) => item.id !== current.id));
      clearSession();
      clearPendingEmail();
    });
  },

  async exportData(): Promise<ExportedData> {
    return simulate(() => {
      const current = requireCurrentUser();
      return {
        profile: current,
        exportedAt: new Date().toISOString(),
        chatHistory: null,
      };
    });
  },
};
