import { describe, expect, it } from 'vitest';
import { renderApp } from './utils';

const ROUTES: Array<[string, RegExp]> = [
  ['/', /Tempat tenang/i],
  ['/download', /Nara berjalan di peramban/i],
  ['/tos', /Syarat dan Ketentuan/i],
  ['/privasi', /Kebijakan Privasi/i],
  ['/login', /Masuk ke Nara/i],
  ['/register', /Buat akun Nara/i],
  ['/chat', /Halo,.*ada yang bisa saya bantu/i],
  ['/tidak-ada', /Halaman tidak ditemukan/i],
];

describe('audit markup per rute', () => {
  it.each(ROUTES)('%s punya landmark & judul halaman', async (path, heading) => {
    const view = renderApp(path);
    expect(await screenFind(heading)).toBe(true);
    const html = document.body.innerHTML;
    // Landmark dasar
    expect(html).toContain('<main');
    expect(html).toContain('Lewati ke konten');
    // Tidak ada gambar tanpa alt (tidak ada <img> sama sekali saat ini)
    const imgs = Array.from(document.querySelectorAll('img'));
    expect(imgs.every((img) => img.hasAttribute('alt'))).toBe(true);
    // Semua input punya label/aria-label
    const inputs = Array.from(document.querySelectorAll('input, textarea, select'));
    const unlabeled = inputs.filter((element) => {
      const id = element.getAttribute('id');
      const hasLabel = id ? Boolean(document.querySelector(`label[for="${CSS.escape(id)}"]`)) : false;
      const hasAria = element.hasAttribute('aria-label') || element.hasAttribute('aria-labelledby');
      const wrapped = element.closest('label') !== null;
      return !hasLabel && !hasAria && !wrapped;
    });
    expect(unlabeled.map((element) => element.outerHTML.slice(0, 80))).toEqual([]);
    view.unmount();
  });
});

describe('audit halaman profil', () => {
  it('semua kontrol berlabel dan judul dokumen berubah', async () => {
    const { dummyAuthApi } = await import('../lib/auth/dummyAuthApi');
    await dummyAuthApi.register('audit@example.com', 'rahasia123');
    await dummyAuthApi.verify('audit@example.com', '123456');

    const view = renderApp('/profile');
    const { screen } = await import('@testing-library/react');
    await screen.findByRole('heading', { name: /Profil dan pengaturan/i }, { timeout: 5000 });

    expect(document.title).toMatch(/Profil/);

    const inputs = Array.from(document.querySelectorAll('input, textarea, select'));
    const unlabeled = inputs.filter((element) => {
      const id = element.getAttribute('id');
      const hasLabel = id ? Boolean(document.querySelector(`label[for="${CSS.escape(id)}"]`)) : false;
      const hasAria = element.hasAttribute('aria-label') || element.hasAttribute('aria-labelledby');
      const wrapped = element.closest('label') !== null;
      return !hasLabel && !hasAria && !wrapped;
    });
    expect(unlabeled.map((element) => element.outerHTML.slice(0, 80))).toEqual([]);
    view.unmount();
  });
});

async function screenFind(regex: RegExp): Promise<boolean> {
  const { screen } = await import('@testing-library/react');
  const element = await screen.findByText(regex, undefined, { timeout: 5000 }).catch(() => null);
  return Boolean(element);
}
