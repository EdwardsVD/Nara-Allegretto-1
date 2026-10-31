import { describe, expect, it } from 'vitest';
import { screen } from '@testing-library/react';
import { renderApp } from './utils';

/** Data localStorage yang rusak tidak boleh membuat aplikasi crash. */
describe('render dengan data rusak', () => {
  it('halaman tetap tampil saat nara_dummy_users/session/theme rusak', async () => {
    window.localStorage.setItem('nara_dummy_users', 'bukan-json-sama-sekali');
    window.localStorage.setItem('nara_dummy_session', '{bad session');
    window.localStorage.setItem('nara_theme', '"ungu"');

    renderApp('/login');

    expect(await screen.findByRole('heading', { name: /Masuk ke Nara/i })).toBeInTheDocument();
    // Sesi rusak dibersihkan saat pembacaan (users hanya dibaca saat butuh data akun).
    expect(window.localStorage.getItem('nara_dummy_session')).toBeNull();
  });

  it('halaman chat tetap bisa dibuka dengan data rusak', async () => {
    window.localStorage.setItem('nara_dummy_session', 'rusak');
    renderApp('/chat');

    expect(
      await screen.findByRole('heading', { name: /Halo,.*ada yang bisa saya bantu\?/i }),
    ).toBeInTheDocument();
  });
});
