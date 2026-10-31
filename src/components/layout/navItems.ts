export interface NavItem {
  label: string;
  to: string;
  /** Hanya tampil untuk pengguna login. */
  authOnly?: boolean;
}

/** Navigasi publik (navbar + footer). */
export const PUBLIC_NAV: NavItem[] = [
  { label: 'Beranda', to: '/' },
  { label: 'Chat', to: '/chat' },
  { label: 'Download', to: '/download' },
  { label: 'Syarat', to: '/tos' },
  { label: 'Privasi', to: '/privasi' },
];

/** Navigasi di sidebar aplikasi (urutan wajib sesuai spesifikasi). */
export const SIDEBAR_NAV: NavItem[] = [
  { label: 'Beranda', to: '/' },
  { label: 'Chat', to: '/chat' },
  { label: 'Profil', to: '/profile', authOnly: true },
  { label: 'Download', to: '/download' },
  { label: 'Syarat', to: '/tos' },
  { label: 'Privasi', to: '/privasi' },
];
