import { Button } from '../../components/ui/Button';
import { Card, CardBody, CardHeader } from '../../components/ui/Card';

export function DataPrivacySection({ onDownload }: { onDownload(): void | Promise<void> }) {
  return (
    <Card as="section">
      <CardHeader title="Data dan privasi" description="Ekspor data Anda dalam format JSON." />
      <CardBody className="space-y-3">
        <Button variant="secondary" size="sm" onClick={() => void onDownload()}>
          <svg aria-hidden="true" viewBox="0 0 24 24" className="h-4 w-4" fill="none" stroke="currentColor" strokeWidth="1.8">
            <path d="M12 4v10m0 0 4-4m-4 4-4-4M5 19h14" strokeLinecap="round" strokeLinejoin="round" />
          </svg>
          Unduh data saya
        </Button>
        <p className="text-xs leading-relaxed text-ink-500 dark:text-ink-400">
          File <code className="font-mono">nara-data.json</code> berisi profil dan tanggal
          pendaftaran. Riwayat chat tidak disimpan.
        </p>
      </CardBody>
    </Card>
  );
}
