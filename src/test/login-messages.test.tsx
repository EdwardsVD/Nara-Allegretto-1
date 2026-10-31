import { describe, expect, it } from 'vitest';
import { screen } from '@testing-library/react';
import { renderApp } from './utils';
import { loginUser, makeUser } from './helpers';
import { dummyAuthApi } from '../lib/auth/dummyAuthApi';

const INVALID = 'Email atau password salah';

describe('pesan login', () => {
  it('email tidak terdaftar dan password salah menghasilkan pesan identik', async () => {
    // Akun valid untuk kasus password salah.
    await dummyAuthApi.register('punya@example.com', 'rahasia123');
    await dummyAuthApi.verify('punya@example.com', '123456');
    await dummyAuthApi.logout();

    // Kasus 1: email tidak terdaftar.
    const first = renderApp('/login');
    const user1 = makeUser();
    await loginUser(user1, 'tidak-ada@example.com');
    const alert1 = await screen.findByRole('alert');
    expect(alert1).toHaveTextContent(INVALID);
    const message1 = alert1.textContent;
    first.unmount();

    // Kasus 2: password salah pada email terdaftar.
    // Mode dummy tidak menyimpan password: login hanya butuh password
    // minimal 8 karakter, jadi "salah" di sini berarti kurang dari 8.
    const second = renderApp('/login');
    await screen.findByRole('heading', { name: /Masuk ke Nara/i });
    const user2 = makeUser();
    await loginUser(user2, 'punya@example.com', 'salah');
    const alert2 = await screen.findByRole('alert');
    expect(alert2).toHaveTextContent(INVALID);
    const message2 = alert2.textContent;
    second.unmount();

    expect(message2).toBe(message1);
  });

  it('email terdaftar tapi belum terverifikasi diarahkan ke halaman verifikasi', async () => {
    await dummyAuthApi.register('belum@example.com', 'rahasia123');
    await dummyAuthApi.logout();

    const user = makeUser();
    renderApp('/login');
    await loginUser(user, 'belum@example.com');

    expect(await screen.findByRole('heading', { name: /Periksa email Anda/i })).toBeInTheDocument();
    expect(screen.getByTestId('masked-email')).toHaveTextContent('b****@example.com');
  });
});
