import { describe, expect, it } from 'vitest';
import { isArrayOf, isRecord, isString, readJSON, readRaw } from '../lib/storage';
import { dummyAuthApi } from '../lib/auth/dummyAuthApi';
import { readPendingEmail } from '../lib/auth/pendingEmail';

describe('lib/storage', () => {
  it('mengembalikan null dan membersihkan data JSON rusak', () => {
    window.localStorage.setItem('nara_dummy_users', '{bukan json');
    expect(readJSON('nara_dummy_users', isArrayOf(isRecord))).toBeNull();
    expect(readRaw('nara_dummy_users')).toBeNull();
  });

  it('menolak bentuk data yang tidak cocok', () => {
    window.localStorage.setItem('nara_dummy_users', JSON.stringify({ bukan: 'array' }));
    expect(readJSON('nara_dummy_users', isArrayOf(isRecord))).toBeNull();
    expect(readRaw('nara_dummy_users')).toBeNull();
  });

  it('menerima data valid', () => {
    window.localStorage.setItem('nara_theme', JSON.stringify('dark'));
    expect(readJSON('nara_theme', isString)).toBe('dark');
  });
});

describe('ketahanan aplikasi terhadap localStorage rusak', () => {
  it('data akun & sesi rusak tidak membuat me()/login crash', async () => {
    window.localStorage.setItem('nara_dummy_users', '[[[rusak');
    window.localStorage.setItem('nara_dummy_session', '{"userId": 123}');
    window.sessionStorage.setItem('nara_pending_email', 'bukan-json');

    await expect(dummyAuthApi.me()).resolves.toBeNull();
    expect(readPendingEmail()).toBeNull();

    // Pendaftaran baru tetap bisa berjalan setelah data rusak dibersihkan.
    const result = await dummyAuthApi.register('baru@example.com', 'rahasia123');
    expect(result.email).toBe('baru@example.com');
    expect(result.message).toMatch(/Pendaftaran diterima/i);
  });
});
