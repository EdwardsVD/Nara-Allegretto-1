import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    host: '0.0.0.0',
    port: 5173,
    strictPort: false,
    // Preview di-host pada domain lain (proxied), jadi semua host diizinkan.
    allowedHosts: true,
    // Proxy dev: aplikasi memanggil path relatif /api/* agar tidak ada
    // referensi localhost di browser. Ganti target saat backend FastAPI siap.
    proxy: {
      '/api': {
        target: 'http://127.0.0.1:8000',
        changeOrigin: true,
      },
    },
  },
  preview: {
    host: '0.0.0.0',
    allowedHosts: true,
  },
});
