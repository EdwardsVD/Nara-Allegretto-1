import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import { BrowserRouter } from 'react-router-dom';
import { AuthProvider } from './lib/auth/AuthContext';
import { ThemeProvider } from './lib/useTheme';
import { ToastProvider } from './components/ui/Toast';
import { AppRoutes } from './routes';
import './index.css';

const container = document.getElementById('root');
if (!container) {
  throw new Error('Elemen #root tidak ditemukan.');
}

createRoot(container).render(
  <StrictMode>
    <ThemeProvider>
      <AuthProvider>
        <ToastProvider>
          <BrowserRouter>
            <AppRoutes />
          </BrowserRouter>
        </ToastProvider>
      </AuthProvider>
    </ThemeProvider>
  </StrictMode>,
);
