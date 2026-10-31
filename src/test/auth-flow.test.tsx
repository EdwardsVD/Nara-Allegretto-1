import { describe, expect, it, vi } from 'vitest';
import { act, fireEvent, screen } from '@testing-library/react';
import { renderApp, TEST_CODE, TEST_EMAIL, TEST_PASSWORD } from './utils';
import {
  expectChatLanded,
  loginUser,
  makeUser,
  registerUser,
  typeVerificationCode,
  waitForBodyText,
  waitForSubmitEnabled,
} from './helpers';

describe('alur akun', () => {
  it('daftar -> verifikasi kode benar -> mendarat di /chat dengan chat kosong', async () => {
    const user = makeUser();
    renderApp('/register');

    await screen.findByRole('heading', { name: /Buat akun Nara/i });
    await registerUser(user, TEST_EMAIL);

    // Halaman verifikasi dengan email tersamarkan
    expect(await screen.findByTestId('masked-email')).toHaveTextContent('d***@example.com');

    await typeVerificationCode(TEST_CODE);
    await user.click(screen.getByRole('button', { name: /^Verifikasi$/i }));

    await expectChatLanded();
    // Percakapan kosong: belum ada bubble pesan sama sekali
    expect(screen.queryAllByTestId('chat-message')).toHaveLength(0);
    // Tombol Back tidak kembali ke halaman auth (navigasi replace)
    expect(screen.queryByRole('heading', { name: /Periksa email Anda/i })).not.toBeInTheDocument();
    // Sesi tersimpan
    expect(window.localStorage.getItem('nara_dummy_session')).toBeTruthy();
  });

  it('kode salah 5 kali mengunci input (hitung mundur 30 detik)', async () => {
    const user = makeUser();
    renderApp('/register');

    await registerUser(user, 'kunci@example.com');
    expect(await screen.findByLabelText(/Digit 1 dari 6/i)).toBeEnabled();

    for (let attempt = 1; attempt <= 5; attempt += 1) {
      // Tunggu sampai permintaan sebelumnya benar-benar selesai: tombol submit
      // aktif kembali hanya setelah respons diterima dan state diperbarui.
      // (Lebih andal daripada menunggu teks "sisa percobaan".)
      if (attempt > 1) {
        await waitForSubmitEnabled();
      }
      await typeVerificationCode('000000');
      await user.click(screen.getByRole('button', { name: /^Verifikasi$/i }));
    }

    await waitForBodyText('Terlalu banyak percobaan', 15_000);
    expect(screen.getByLabelText(/Digit 1 dari 6/i)).toBeDisabled();
    expect(screen.getByText(/Input dikunci sementara/i)).toBeInTheDocument();
  });

  it('kunci input verifikasi berakhir setelah 30 detik (fake timers)', async () => {
    // Persiapan memakai timer asli (me() merangkai beberapa timer 120 ms).
    const { dummyAuthApi } = await import('../lib/auth/dummyAuthApi');
    await dummyAuthApi.register('kunci-timer@example.com', 'rahasia123');
    await dummyAuthApi.logout();
    window.sessionStorage.setItem('nara_pending_email', JSON.stringify('kunci-timer@example.com'));

    const view = renderApp('/register/verifikasi');
    expect(await screen.findByTestId('masked-email')).toHaveTextContent(/k\*\*\*/);

    // Mulai di sini semua delay simulasi memakai fake timers.
    vi.useFakeTimers();

    const clickSubmit = async () => {
      const boxes = screen.getAllByLabelText(/Digit \d dari 6/i) as HTMLInputElement[];
      boxes.forEach((box, index) => {
        fireEvent.change(box, { target: { value: '0' } });
        void index;
      });
      const submit = document.querySelector('form button[type="submit"]') as HTMLButtonElement;
      fireEvent.click(submit);
      await act(async () => {
        await vi.advanceTimersByTimeAsync(1500);
      });
    };

    for (let attempt = 0; attempt < 5; attempt += 1) {
      await clickSubmit();
    }

    expect(screen.getByText(/Terlalu banyak percobaan/i)).toBeInTheDocument();
    expect(screen.getByLabelText(/Digit 1 dari 6/i)).toBeDisabled();

    await act(async () => {
      await vi.advanceTimersByTimeAsync(15_000);
    });
    expect(screen.getByLabelText(/Digit 1 dari 6/i)).toBeDisabled();

    await act(async () => {
      await vi.advanceTimersByTimeAsync(16_000);
    });
    expect(screen.getByLabelText(/Digit 1 dari 6/i)).toBeEnabled();
    expect(screen.queryByText(/Terlalu banyak percobaan/i)).not.toBeInTheDocument();
    view.unmount();
  });

  it('/register/verifikasi tanpa pendaftaran menunggu -> /register', async () => {
    renderApp('/register/verifikasi');
    expect(await screen.findByRole('heading', { name: /Buat akun Nara/i })).toBeInTheDocument();
  });

  it('pengguna login yang membuka /login atau /register diarahkan ke /chat', async () => {
    // Siapkan sesi lewat alur nyata
    const setupUser = makeUser();
    const first = renderApp('/register');
    await registerUser(setupUser, 'sudah@example.com');
    await typeVerificationCode(TEST_CODE);
    await setupUser.click(screen.getByRole('button', { name: /^Verifikasi$/i }));
    await expectChatLanded();
    first.unmount();

    const second = renderApp('/login');
    await expectChatLanded();
    second.unmount();

    renderApp('/register');
    await expectChatLanded();
  });

  it('tamu membuka /profile -> /login?next=/profile, lalu mendarat di /profile', async () => {
    const user = makeUser();
    renderApp('/profile');

    // Form login tampil (redirect membawa next=/profile)
    await screen.findByRole('heading', { name: /Masuk ke Nara/i });
    expect(window.location.search).not.toContain('next'); // MemoryRouter: cek lewat UI

    // Daftar akun dulu lewat alur, lalu login
    const registerUser1 = makeUser();
    void registerUser1;
    // Buat akun langsung via adapter agar tes tetap fokus pada guard
    const { dummyAuthApi } = await import('../lib/auth/dummyAuthApi');
    await dummyAuthApi.register('tamu@example.com', TEST_PASSWORD);
    await dummyAuthApi.verify('tamu@example.com', TEST_CODE);
    await dummyAuthApi.logout();

    await loginUser(user, 'tamu@example.com');
    expect(
      await screen.findByRole('heading', { name: /Profil dan pengaturan/i }, { timeout: 5000 }),
    ).toBeInTheDocument();
  });

  it.each(['//evil.com', 'https://x.com', '/tos'])(
    '?next=%s diabaikan -> mendarat di /chat',
    async (nextValue) => {
      const { dummyAuthApi } = await import('../lib/auth/dummyAuthApi');
      await dummyAuthApi.register('allowlist@example.com', TEST_PASSWORD);
      await dummyAuthApi.verify('allowlist@example.com', TEST_CODE);
      await dummyAuthApi.logout();

      const user = makeUser();
      renderApp(`/login?next=${encodeURIComponent(nextValue)}`);
      await loginUser(user, 'allowlist@example.com');
      await expectChatLanded();
    },
  );
});
