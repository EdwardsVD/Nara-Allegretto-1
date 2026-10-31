import { Card, CardBody, CardHeader } from '../../components/ui/Card';
import { useTheme } from '../../lib/useTheme';
import type { ThemePreference } from '../../lib/themePreference';

const OPTIONS: Array<{ value: ThemePreference; label: string; description: string }> = [
  { value: 'system', label: 'Sistem', description: 'Ikuti pengaturan perangkat.' },
  { value: 'light', label: 'Terang', description: 'Latar terang sepanjang waktu.' },
  { value: 'dark', label: 'Gelap', description: 'Latar gelap sepanjang waktu.' },
];

export function PreferencesSection() {
  const { preference, setPreference } = useTheme();

  return (
    <Card as="section">
      <CardHeader title="Preferensi" description="Tampilan disimpan di perangkat ini (nara_theme)." />
      <CardBody>
        <fieldset>
          <legend className="mb-2 text-sm font-medium text-ink-800 dark:text-ink-100">Tema</legend>
          <div className="grid gap-2 sm:grid-cols-3">
            {OPTIONS.map((option) => (
              <label
                key={option.value}
                className={`flex cursor-pointer flex-col gap-0.5 rounded-xl border px-3 py-2.5 text-sm transition-colors focus-within:ring-2 focus-within:ring-accent-400 ${
                  preference === option.value
                    ? 'border-accent-400 bg-accent-50 text-accent-900 dark:bg-accent-400/10 dark:text-accent-100'
                    : 'border-ink-200 text-ink-700 hover:bg-ink-100 dark:border-ink-800 dark:text-ink-300 dark:hover:bg-ink-800'
                }`}
              >
                <span className="flex items-center gap-2 font-medium">
                  <input
                    type="radio"
                    name="tema"
                    value={option.value}
                    checked={preference === option.value}
                    onChange={() => setPreference(option.value)}
                    className="h-3.5 w-3.5 accent-accent-500"
                  />
                  {option.label}
                </span>
                <span className="pl-5 text-xs text-ink-500 dark:text-ink-400">
                  {option.description}
                </span>
              </label>
            ))}
          </div>
        </fieldset>
      </CardBody>
    </Card>
  );
}
