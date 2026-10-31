import { describe, expect, it } from 'vitest';
import { screen, waitFor } from '@testing-library/react';
import { renderApp } from './utils';
import { makeUser, waitForBodyText } from './helpers';

describe('/chat', () => {
  it('tamu bisa mengirim pesan dan menerima balasan contoh', async () => {
    const user = makeUser();
    renderApp('/chat');

    const input = await screen.findByLabelText(/Tulis pesan untuk Nara/i);
    await user.type(input, 'Siapa kamu?');
    await user.click(screen.getByRole('button', { name: /Kirim pesan/i }));

    // Pesan pengguna tampil, indikator mengetik muncul, lalu balasan mock
    // (jawaban sampel memuat "Nara Ai").
    expect(await screen.findByText('Siapa kamu?')).toBeInTheDocument();
    await waitForBodyText(/Nara Ai/i, 5000);
    await waitFor(() => expect(screen.getAllByTestId('chat-message').length).toBeGreaterThanOrEqual(2));
  });

  it('saran pertanyaan mengisi & mengirim pesan otomatis', async () => {
    const user = makeUser();
    renderApp('/chat');

    await screen.findByRole('heading', { name: /Halo,.*ada yang bisa saya bantu/i });
    await user.click(screen.getByRole('button', { name: /Apa rumus kimia air/i }));

    await waitFor(() => expect(screen.getAllByTestId('chat-message').length).toBeGreaterThan(0));
    await waitForBodyText(/H2O/i, 5000);
  });

  it('Chat baru mengosongkan percakapan', async () => {
    const user = makeUser();
    renderApp('/chat');

    await screen.findByRole('heading', { name: /Halo,.*ada yang bisa saya bantu/i });
    await user.click(screen.getByRole('button', { name: /Apa itu uang rupiah/i }));
    await waitFor(() => expect(screen.getAllByTestId('chat-message').length).toBeGreaterThan(0));

    // Tombol "Chat baru" ada di sidebar (desktop) — klik yang pertama.
    await user.click(screen.getAllByRole('button', { name: /Chat baru/i })[0]);

    await waitFor(() => expect(screen.queryAllByTestId('chat-message')).toHaveLength(0));
    expect(
      await screen.findByRole('heading', { name: /Halo,.*ada yang bisa saya bantu/i }),
    ).toBeInTheDocument();
  });
});
