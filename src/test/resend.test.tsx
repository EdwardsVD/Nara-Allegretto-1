import { describe, expect, it, vi } from 'vitest';
import { act, fireEvent, screen } from '@testing-library/react';
import { renderApp } from './utils';

/**
 * Tombol "Kirim ulang" wajib nonaktif 60 detik dengan hitung mundur.
 * Memakai fake timers; interaksi memakai fireEvent (sinkron) agar tidak
 * menunggu timer internal userEvent.
 */
describe('tombol kirim ulang', () => {
  it('nonaktif selama 60 detik dan aktif lagi setelahnya', async () => {
    vi.useFakeTimers();

    // Pendaftaran menunggu disiapkan langsung di sessionStorage
    // (bukan lewat UI) agar tes fokus pada hitung mundur.
    window.sessionStorage.setItem('nara_pending_email', JSON.stringify('ulang@example.com'));

    renderApp('/register/verifikasi');
    await act(async () => {
      await vi.advanceTimersByTimeAsync(500);
    });

    expect(screen.getByTestId('masked-email')).toHaveTextContent('u****@example.com');

    const resendButton = screen.getByRole('button', { name: /^Kirim ulang kode$/i });
    expect(resendButton).toBeEnabled();

    await act(async () => {
      fireEvent.click(resendButton);
      // Selesaikan delay simulasi (500-900 ms) + pembaruan state.
      await vi.advanceTimersByTimeAsync(2000);
    });

    expect(screen.getByRole('button', { name: /Kirim ulang dalam \d+ detik/i })).toBeDisabled();

    await act(async () => {
      await vi.advanceTimersByTimeAsync(30_000);
    });
    expect(screen.getByRole('button', { name: /Kirim ulang dalam [23]\d detik/i })).toBeDisabled();

    // Total 60 detik: tombol kembali aktif.
    await act(async () => {
      await vi.advanceTimersByTimeAsync(31_000);
    });
    expect(screen.getByRole('button', { name: /^Kirim ulang kode$/i })).toBeEnabled();
  });
});
