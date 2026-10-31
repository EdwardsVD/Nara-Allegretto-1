import { usePageTitle } from '../lib/usePageTitle';

const SECTIONS = [
  {
    title: 'Penggunaan layanan',
    body: [
      'Nara adalah asisten percakapan eksperimental. Anda setuju menggunakan layanan ini untuk keperluan yang sah dan tidak merugikan pihak lain.',
      'Layanan disediakan apa adanya, tanpa jaminan ketersediaan atau ketepatan. Kami dapat mengubah atau menghentikan fitur kapan saja.',
    ],
  },
  {
    title: 'Batasan jawaban',
    body: [
      'Jawaban Nara dapat mengandung kesalahan atau informasi yang sudah usang. Jangan jadikan jawaban Nara sebagai rujukan utama untuk keputusan medis, hukum, atau keuangan.',
      'Selalu verifikasi informasi penting pada sumber resmi sebelum mengambil tindakan.',
    ],
  },
  {
    title: 'Akun',
    body: [
      'Dalam mode demo, akun hanya tersimpan di peramban Anda dan tidak diautentikasi oleh server mana pun. Jangan gunakan password asli pada mode demo.',
      'Anda bertanggung jawab menjaga akses ke perangkat tempat akun demo tersimpan.',
    ],
  },
  {
    title: 'Konten yang tidak diperbolehkan',
    body: [
      'Pengguna tidak boleh menggunakan layanan untuk menyebarkan konten ilegal, menyesatkan, atau melanggar hak pihak lain.',
    ],
  },
  {
    title: 'Perubahan ketentuan',
    body: [
      'Ketentuan ini dapat berubah sewaktu-waktu. Versi terbaru selalu tersedia di halaman ini beserta tanggal pembaruannya.',
    ],
  },
];

export function Tos() {
  usePageTitle('Syarat dan Ketentuan');

  return (
    <div className="bg-canvas">
      <article className="mx-auto w-full max-w-3xl px-4 py-12 sm:px-6 sm:py-16">
        <header className="mb-8 space-y-2 border-b border-ink-200 pb-5 dark:border-ink-800">
          <p className="text-[11px] font-semibold uppercase tracking-[0.16em] text-accent-700 dark:text-accent-300">
            Legal
          </p>
          <h1 className="text-3xl font-semibold tracking-tight text-ink-900 sm:text-4xl dark:text-ink-50">
            Syarat dan Ketentuan
          </h1>
          <p className="text-sm text-ink-500 dark:text-ink-400">
            Terakhir diperbarui: 1 Januari 2026 · Berlaku untuk versi demo
          </p>
        </header>

        <nav aria-label="Daftar isi" className="mb-8 rounded-xl border border-ink-200 bg-white/70 p-4 dark:border-ink-800 dark:bg-ink-900/70">
          <p className="mb-2 text-xs font-semibold uppercase tracking-wide text-ink-500 dark:text-ink-400">
            Daftar isi
          </p>
          <ol className="grid gap-1 text-sm sm:grid-cols-2">
            {SECTIONS.map((section, index) => (
              <li key={section.title}>
                <a
                  href={`#bagian-${index + 1}`}
                  className="focus-ring rounded text-ink-700 underline-offset-2 hover:underline dark:text-ink-300"
                >
                  {index + 1}. {section.title}
                </a>
              </li>
            ))}
          </ol>
        </nav>

        <div className="space-y-8">
          {SECTIONS.map((section, index) => (
            <section key={section.title} id={`bagian-${index + 1}`} className="scroll-mt-24 space-y-2">
              <h2 className="text-lg font-semibold text-ink-900 dark:text-ink-50">
                {index + 1}. {section.title}
              </h2>
              {section.body.map((paragraph) => (
                <p key={paragraph} className="text-sm leading-relaxed text-ink-700 dark:text-ink-300">
                  {paragraph}
                </p>
              ))}
            </section>
          ))}
        </div>
      </article>
    </div>
  );
}
