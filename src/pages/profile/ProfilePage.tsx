import { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { Avatar } from '../../components/ui/Avatar';
import { Card, CardBody, CardHeader } from '../../components/ui/Card';
import { Modal } from '../../components/ui/Modal';
import { Banner } from '../../components/ui/Banner';
import { Button } from '../../components/ui/Button';
import { Input } from '../../components/ui/Input';
import { useToast } from '../../components/ui/Toast';
import { useAuth } from '../../lib/auth/AuthContext';
import { AuthError } from '../../lib/auth/types';
import { authApi } from '../../lib/auth';
import { formatTanggalIndonesia, providerLabel } from '../../lib/format';
import { usePageTitle } from '../../lib/usePageTitle';
import { AccountSummary } from './AccountSummary';
import { SecuritySection } from './SecuritySection';
import { ConnectedAccounts } from './ConnectedAccounts';
import { PreferencesSection } from './PreferencesSection';
import { DataPrivacySection } from './DataPrivacySection';

const SECTIONS = [
  { id: 'ringkasan', label: 'Ringkasan' },
  { id: 'nama', label: 'Nama' },
  { id: 'keamanan', label: 'Keamanan' },
  { id: 'terhubung', label: 'Akun terhubung' },
  { id: 'preferensi', label: 'Preferensi' },
  { id: 'data', label: 'Data' },
  { id: 'bahaya', label: 'Zona bahaya' },
];

export function ProfilePage() {
  usePageTitle('Profil');
  const { user, updateProfile, deleteAccount, logout, changePassword } = useAuth();
  const { showToast } = useToast();
  const navigate = useNavigate();

  const [displayName, setDisplayName] = useState(user?.displayName ?? '');
  const [nameError, setNameError] = useState<string | null>(null);
  const [savingName, setSavingName] = useState(false);

  const [deleteOpen, setDeleteOpen] = useState(false);
  const [deleteConfirm, setDeleteConfirm] = useState('');
  const [deleting, setDeleting] = useState(false);
  const [deleteError, setDeleteError] = useState<string | null>(null);

  if (!user) return null;

  const nameChanged = displayName.trim() !== user.displayName;

  const saveName = async () => {
    setNameError(null);
    const trimmed = displayName.trim();
    if (trimmed.length < 2 || trimmed.length > 40) {
      setNameError('Nama tampilan harus 2-40 karakter.');
      return;
    }
    setSavingName(true);
    try {
      await updateProfile({ displayName: trimmed });
      setDisplayName(trimmed);
      showToast('Nama tampilan diperbarui.', 'success');
    } catch (caught) {
      const message = caught instanceof AuthError ? caught.message : 'Gagal menyimpan nama.';
      setNameError(message);
      showToast(message, 'error');
    } finally {
      setSavingName(false);
    }
  };

  // Navigasi dilakukan SEBELUM sesi dihapus agar <RequireAuth> di /profile
  // tidak berlomba mengarahkan ke halaman login.
  const handleLogout = async () => {
    navigate('/', { replace: true });
    await logout();
  };

  const handleDelete = async () => {
    setDeleteError(null);
    setDeleting(true);
    navigate('/', { replace: true });
    try {
      await deleteAccount();
      setDeleteOpen(false);
      showToast('Akun dihapus.', 'success');
    } catch (caught) {
      const message = caught instanceof AuthError ? caught.message : 'Gagal menghapus akun.';
      showToast(message, 'error');
      navigate('/profile', { replace: true });
    } finally {
      setDeleting(false);
    }
  };

  const emailMatches = deleteConfirm.trim().toLowerCase() === user.email.toLowerCase();

  const downloadData = async () => {
    try {
      const data = await authApi.exportData();
      const blob = new Blob([JSON.stringify(data, null, 2)], { type: 'application/json' });
      const url = URL.createObjectURL(blob);
      const anchor = document.createElement('a');
      anchor.href = url;
      anchor.download = 'nara-data.json';
      document.body.appendChild(anchor);
      anchor.click();
      anchor.remove();
      URL.revokeObjectURL(url);
      showToast('Data akun diunduh sebagai nara-data.json.', 'success');
    } catch (caught) {
      showToast(
        caught instanceof AuthError ? caught.message : 'Gagal mengunduh data akun.',
        'error',
      );
    }
  };

  return (
    <div className="h-full overflow-y-auto bg-canvas">
      <div className="mx-auto w-full max-w-[880px] px-4 py-6 sm:px-6 sm:py-8">
        <div className="mb-5 flex flex-wrap items-center justify-between gap-3">
          <Link
            to="/chat"
            className="focus-ring inline-flex items-center gap-1.5 rounded-lg px-2 py-1 text-sm font-medium text-ink-600 hover:text-ink-900 dark:text-ink-300 dark:hover:text-ink-50"
          >
            <svg aria-hidden="true" viewBox="0 0 20 20" className="h-4 w-4" fill="none" stroke="currentColor" strokeWidth="1.8">
              <path d="M11 5 6 10l5 5" strokeLinecap="round" strokeLinejoin="round" />
            </svg>
            Kembali ke chat
          </Link>
          <p className="text-xs text-ink-500 dark:text-ink-400">
            Akun {providerLabel(user.provider)} · sejak {formatTanggalIndonesia(user.createdAt)}
          </p>
        </div>

        <header className="mb-5">
          <h1 className="text-2xl font-semibold tracking-tight text-ink-900 sm:text-[1.7rem] dark:text-ink-50">
            Profil dan pengaturan
          </h1>
          <p className="mt-1 text-sm text-ink-600 dark:text-ink-300">
            Kelola identitas, keamanan, dan data akun Anda dari satu tempat.
          </p>
        </header>

        {/* Navigasi bagian (jangkar) */}
        <nav aria-label="Bagian profil" className="sticky top-0 z-10 -mx-1 mb-5 px-1 py-2">
          <ul className="no-scrollbar flex gap-1 overflow-x-auto rounded-xl border border-ink-200/80 bg-white/80 p-1 backdrop-blur dark:border-ink-800/80 dark:bg-ink-900/80">
            {SECTIONS.map((section) => (
              <li key={section.id}>
                <a
                  href={`#${section.id}`}
                  className="focus-ring block whitespace-nowrap rounded-lg px-2.5 py-1.5 text-xs font-medium text-ink-600 transition-colors hover:bg-ink-100 hover:text-ink-900 dark:text-ink-300 dark:hover:bg-ink-800 dark:hover:text-ink-50"
                >
                  {section.label}
                </a>
              </li>
            ))}
          </ul>
        </nav>

        <div className="space-y-4">
          <div id="ringkasan" className="scroll-mt-24">
            <AccountSummary
              user={user}
              joinedLabel={formatTanggalIndonesia(user.createdAt)}
              providerText={providerLabel(user.provider)}
            />
          </div>

          <Card as="section" className="scroll-mt-24" >
            <span id="nama" className="block scroll-mt-24" />
            <CardHeader
              title="Nama tampilan"
              description="Nama ini tampil di sidebar, navbar, dan sapaan chat."
            />
            <CardBody className="space-y-3">
              <div className="flex flex-col gap-3 sm:flex-row sm:items-start">
                <Avatar name={displayName || user.displayName} email={user.email} size="lg" />
                <div className="min-w-0 flex-1">
                  <Input
                    label="Nama tampilan"
                    name="displayName"
                    value={displayName}
                    maxLength={40}
                    onChange={(event) => setDisplayName(event.target.value)}
                    error={nameError ?? undefined}
                    hint={`2-40 karakter · ${displayName.trim().length} dipakai`}
                    disabled={savingName}
                  />
                </div>
              </div>
              <div className="flex flex-wrap items-center justify-between gap-2">
                <p className="text-xs text-ink-500 dark:text-ink-400">
                  {nameChanged ? 'Ada perubahan yang belum disimpan.' : 'Tidak ada perubahan.'}
                </p>
                <div className="flex gap-2">
                  <Button
                    variant="ghost"
                    size="sm"
                    onClick={() => setDisplayName(user.displayName)}
                    disabled={!nameChanged || savingName}
                  >
                    Urungkan
                  </Button>
                  <Button onClick={() => void saveName()} disabled={savingName || !nameChanged} size="sm">
                    {savingName ? 'Menyimpan…' : 'Simpan'}
                  </Button>
                </div>
              </div>
            </CardBody>
          </Card>

          <div id="keamanan" className="scroll-mt-24">
            <SecuritySection
              provider={user.provider}
              providerText={providerLabel(user.provider)}
              onChangePassword={changePassword}
              onLogout={handleLogout}
              onLogoutAll={handleLogout}
            />
          </div>

          <div id="terhubung" className="scroll-mt-24">
            <ConnectedAccounts provider={user.provider} />
          </div>

          <div id="preferensi" className="scroll-mt-24">
            <PreferencesSection />
          </div>

          <div id="data" className="scroll-mt-24">
            <DataPrivacySection onDownload={downloadData} />
          </div>

          <div id="bahaya" className="scroll-mt-24">
            <Card as="section" className="border-red-300/80 dark:border-red-900/70">
              <CardHeader title="Zona bahaya" description="Tindakan berikut tidak dapat dibatalkan." />
              <CardBody className="flex flex-wrap items-center justify-between gap-3">
                <p className="max-w-md text-sm text-ink-600 dark:text-ink-300">
                  Menghapus akun akan menghapus data profil di perangkat ini. Percakapan tidak
                  tersimpan, jadi tidak ada riwayat yang perlu dihapus.
                </p>
                <Button variant="danger" size="sm" onClick={() => setDeleteOpen(true)}>
                  Hapus akun
                </Button>
              </CardBody>
            </Card>
          </div>

          <p className="pb-8 pt-2 text-center text-xs text-ink-500 dark:text-ink-500">
            Bergabung sejak {formatTanggalIndonesia(user.createdAt)} · Akun{' '}
            {providerLabel(user.provider)}
          </p>
        </div>
      </div>

      <Modal
        open={deleteOpen}
        onClose={() => {
          if (deleting) return;
          setDeleteOpen(false);
          setDeleteConfirm('');
          setDeleteError(null);
        }}
        title="Hapus akun?"
        description="Semua data akun di perangkat ini akan dihapus permanen. Tindakan ini tidak dapat dibatalkan."
        footer={
          <>
            <Button
              variant="secondary"
              size="sm"
              onClick={() => {
                setDeleteOpen(false);
                setDeleteConfirm('');
              }}
              disabled={deleting}
            >
              Batal
            </Button>
            <Button
              variant="danger"
              size="sm"
              onClick={() => void handleDelete()}
              disabled={!emailMatches || deleting}
            >
              {deleting ? 'Menghapus…' : 'Hapus akun'}
            </Button>
          </>
        }
      >
        <div className="space-y-3">
          <p className="text-sm text-ink-700 dark:text-ink-300">
            Ketik email Anda{' '}
            <strong className="font-semibold text-ink-900 dark:text-ink-50">{user.email}</strong>{' '}
            untuk mengonfirmasi.
          </p>
          <Input
            label="Email konfirmasi"
            name="confirmEmail"
            value={deleteConfirm}
            onChange={(event) => setDeleteConfirm(event.target.value)}
            autoComplete="off"
            disabled={deleting}
            error={
              deleteConfirm.length > 0 && !emailMatches ? 'Email belum cocok.' : undefined
            }
          />
          {deleteError ? (
            <Banner tone="danger" role="alert">
              {deleteError}
            </Banner>
          ) : null}
          {user.provider !== 'email' ? (
            <p className="text-xs text-ink-500 dark:text-ink-400">
              Akun ini dikelola oleh {providerLabel(user.provider)}.
            </p>
          ) : null}
        </div>
      </Modal>
    </div>
  );
}
