import { describe, expect, it } from 'vitest';
import { screen, waitFor, within } from '@testing-library/react';
import { renderApp } from './utils';
import { expectSidebarUser, makeUser } from './helpers';
import { dummyAuthApi } from '../lib/auth/dummyAuthApi';
import { readRaw } from '../lib/storage';

async function seedSession(email = 'profil@example.com') {
  await dummyAuthApi.register(email, 'rahasia123');
  await dummyAuthApi.verify(email, '123456');
  return dummyAuthApi.me();
}

describe('/profile', () => {
  it('edit nama langsung berubah di sidebar', async () => {
    const user = makeUser();
    const account = await seedSession('edit@example.com');
    expect(account).not.toBeNull();

    renderApp('/profile');
    await screen.findByRole('heading', { name: /Profil dan pengaturan/i });
    await expectSidebarUser(account?.displayName ?? '');

    const input = screen.getByLabelText(/Nama tampilan/i);
    await user.clear(input);
    await user.type(input, 'Dewi Lestari');
    await user.click(screen.getByRole('button', { name: /^Simpan$/i }));

    // Sidebar dan ringkasan akun ikut berubah tanpa reload.
    await expectSidebarUser('Dewi Lestari');
    expect(screen.getByTestId('profile-display-name')).toHaveTextContent('Dewi Lestari');
    expect(screen.getByRole('status', { name: '' })).toBeInTheDocument();
  });

  it('hapus akun: tombol nonaktif sampai email diketik benar, lalu kembali ke "/"', async () => {
    const user = makeUser();
    await seedSession('hapus@example.com');

    renderApp('/profile');
    await screen.findByRole('heading', { name: /Profil dan pengaturan/i });

    await user.click(screen.getByRole('button', { name: /^Hapus akun$/i }));
    const dialog = await screen.findByRole('dialog');

    const confirmButton = within(dialog).getByRole('button', { name: /^Hapus akun$/i });
    expect(confirmButton).toBeDisabled();

    const confirmInput = within(dialog).getByLabelText(/Email konfirmasi/i);
    await user.type(confirmInput, 'salah@example.com');
    expect(confirmButton).toBeDisabled();

    await user.clear(confirmInput);
    await user.type(confirmInput, 'hapus@example.com');
    await waitFor(() => expect(confirmButton).toBeEnabled());

    await user.click(confirmButton);

    // Kembali ke beranda publik, sesi & data terhapus, dan toast muncul
    // setelah proses hapus (delay simulasi) selesai.
    expect(
      await screen.findByRole(
        'heading',
        { name: /Tempat tenang untuk bertanya.*dan berpikir/i },
        { timeout: 5000 },
      ),
    ).toBeInTheDocument();
    expect(await screen.findByText('Akun dihapus.', undefined, { timeout: 5000 })).toBeInTheDocument();
    await waitFor(() => expect(readRaw('nara_dummy_session')).toBeNull());
  });

  it('akun OAuth menonaktifkan ganti password', async () => {
    await dummyAuthApi.loginWithProvider('github');
    renderApp('/profile');

    await screen.findByRole('heading', { name: /Profil dan pengaturan/i });
    expect(screen.getByRole('button', { name: /Ganti password/i })).toBeDisabled();
    expect(screen.getByText(/Akun dikelola oleh GitHub/i)).toBeInTheDocument();
  });
});
