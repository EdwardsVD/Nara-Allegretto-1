/**
 * Konfigurasi lingkungan. Semua nilai berasal dari variabel VITE_* (.env),
 * tidak ada secret di sisi frontend.
 */

export type AuthMode = 'dummy' | 'http';
export type ChatMode = 'mock' | 'http';

const rawAuthMode = import.meta.env.VITE_AUTH_MODE;
const rawAllowDummy = import.meta.env.VITE_ALLOW_DUMMY_AUTH;
const rawChatMode = import.meta.env.VITE_CHAT_MODE;
const rawChatRequiresLogin = import.meta.env.VITE_CHAT_REQUIRES_LOGIN;

/** `import.meta.env.DEV` bernilai true saat `vite dev` dan saat tes. */
export const IS_DEV = Boolean(import.meta.env.DEV);

export const AUTH_MODE: AuthMode = rawAuthMode === 'http' ? 'http' : 'dummy';

/**
 * Mode dummy hanya boleh di build production jika VITE_ALLOW_DUMMY_AUTH=true.
 * Di dev selalu boleh agar pengembangan tidak terhambat.
 */
export const DUMMY_AUTH_ENABLED = AUTH_MODE === 'dummy' && (IS_DEV || rawAllowDummy === 'true');

/** Apakah alur /login dan /register bisa dipakai sama sekali. */
export const AUTH_AVAILABLE = AUTH_MODE === 'http' || DUMMY_AUTH_ENABLED;

/** Banner demo permanen hanya saat akun simulasi benar-benar aktif. */
export const SHOW_DEMO_BANNER = AUTH_MODE === 'dummy' && DUMMY_AUTH_ENABLED;

export const CHAT_MODE: ChatMode = rawChatMode === 'http' ? 'http' : 'mock';

export const CHAT_REQUIRES_LOGIN = rawChatRequiresLogin === 'true';

/** Pesan kode verifikasi demo (dipakai UI dan dummy API). */
export const DEMO_CODE = '123456';
