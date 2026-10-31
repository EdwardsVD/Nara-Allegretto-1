import { AUTH_MODE } from '../env';
import { dummyAuthApi } from './dummyAuthApi';
import { httpAuthApi } from './httpAuthApi';
import type { AuthApi } from './types';

/**
 * Titik tukar adapter. Halaman TIDAK pernah mengimpor dummyAuthApi /
 * httpAuthApi secara langsung, hanya `authApi` ini (lewat useAuth()).
 */
export const authApi: AuthApi = AUTH_MODE === 'http' ? httpAuthApi : dummyAuthApi;

export * from './types';
