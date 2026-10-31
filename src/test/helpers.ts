import { screen, waitFor, within } from '@testing-library/react';
import { act } from 'react';
import userEvent from '@testing-library/user-event';
import { TEST_CODE, TEST_PASSWORD } from './utils';

export function makeUser() {
  return userEvent.setup({ advanceTimers: (ms) => void ms });
}

/** Isi form daftar dan kirim. */
export async function registerUser(
  user: ReturnType<typeof userEvent.setup>,
  email: string,
  password = TEST_PASSWORD,
) {
  await user.type(await screen.findByLabelText(/^Email$/i), email);
  await user.type(screen.getByLabelText(/^Password$/i), password);
  await user.click(screen.getByRole('checkbox', { name: /Saya setuju/i }));
  await user.click(screen.getByRole('button', { name: /^Daftar$/i }));
}

/**
 * Isi kode verifikasi (6 kotak terpisah) dan kirim.
 * Kotak pertama menerima seluruh kode lewat "paste" agar cepat dan stabil.
 */
export async function typeVerificationCode(rawCode: string) {
  const first = await screen.findByLabelText(/Digit 1 dari 6/i);
  await userEvent.clear(first);
  await userEvent.type(first, rawCode.slice(0, 1));
  for (let index = 1; index < rawCode.length; index += 1) {
    const box = screen.getByLabelText(new RegExp(`Digit ${index + 1} dari 6`, 'i'));
    await userEvent.type(box, rawCode[index]);
  }
}

/** Isi form verifikasi dan kirim. */
export async function submitCode(rawCode: string) {
  await typeVerificationCode(rawCode);
  const submit = await screen.findByRole('button', { name: /^Verifikasi$/i });
  await userEvent.click(submit);
}

/** Login lewat UI. */
export async function loginUser(
  user: ReturnType<typeof userEvent.setup>,
  email: string,
  password = TEST_PASSWORD,
) {
  await user.type(await screen.findByLabelText(/^Email$/i), email);
  await user.type(screen.getByLabelText(/^Password$/i), password);
  await user.click(screen.getByRole('button', { name: /^Masuk$/i }));
}

/** Tunggu halaman chat tampil (heading sapaan). */
export async function expectChatLanded() {
  // Judul sapaan bisa memuat nama pengguna ("Halo, Dewi. Ada yang bisa…"),
  // jadi cocokkan pola yang lebih longgar.
  await screen.findByRole('heading', { name: /Halo,.*ada yang bisa saya bantu\?/i }, { timeout: 5000 });
}

/**
 * Tunggu sampai teks tertentu muncul di body. Lebih tahan terhadap struktur
 * DOM (teks bisa terpecah antar elemen) dibanding getByText.
 */
export async function waitForBodyText(text: string | RegExp, timeout = 10_000): Promise<void> {
  const deadline = Date.now() + timeout;
  const matches = (value: string) =>
    typeof text === 'string' ? value.includes(text) : text.test(value);
  // Polling manual (bukan waitFor) agar tidak bercampur dengan act queue
  // Testing Library saat dipakai bersama fake timers.
  while (Date.now() < deadline) {
    await act(async () => {
      await new Promise((resolve) => setTimeout(resolve, 50));
    });
    if (matches(document.body.textContent ?? '')) return;
  }
  throw new Error(`Teks tidak muncul dalam ${timeout} ms: ${String(text)}`);
}

/**
 * Tunggu sampai tombol submit pada form aktif kembali. Ini menandakan
 * permintaan sebelumnya sudah selesai diproses.
 */
export async function waitForSubmitEnabled(timeout = 10_000): Promise<void> {
  const deadline = Date.now() + timeout;
  while (Date.now() < deadline) {
    await act(async () => {
      await new Promise((resolve) => setTimeout(resolve, 50));
    });
    const button = document.querySelector('form button[type="submit"]') as HTMLButtonElement | null;
    if (button && !button.disabled) return;
  }
  throw new Error('Tombol submit tidak aktif kembali dalam batas waktu.');
}

/** Tunggu sampai sidebar menampilkan pengguna tertentu. */
export async function expectSidebarUser(name: string) {
  await waitFor(
    () => {
      const nodes = screen.getAllByTestId('sidebar-display-name');
      expect(nodes.some((node) => node.textContent === name)).toBe(true);
    },
    { timeout: 5000 },
  );
}

export { within, TEST_CODE };
