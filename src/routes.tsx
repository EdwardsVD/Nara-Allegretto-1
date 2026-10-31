import { Navigate, Route, Routes } from 'react-router-dom';
import { AppLayout } from './components/layout/AppLayout';
import { AuthLayout } from './components/layout/AuthLayout';
import { PublicLayout } from './components/layout/PublicLayout';
import { GuestOnly, PendingOnly, RequireAuth } from './lib/auth/guards';
import { Chat } from './pages/Chat';
import { Download } from './pages/Download';
import { Landing } from './pages/Landing';
import { Login } from './pages/Login';
import { NotFound } from './pages/NotFound';
import { Privasi } from './pages/Privasi';
import { ProfilePage } from './pages/profile/ProfilePage';
import { Register } from './pages/Register';
import { Tos } from './pages/Tos';
import { Verifikasi } from './pages/Verifikasi';

export function AppRoutes() {
  return (
    <Routes>
      {/* Halaman publik dengan navbar + footer */}
      <Route element={<PublicLayout />}>
        <Route index element={<Landing />} />
        <Route path="download" element={<Download />} />
        <Route path="tos" element={<Tos />} />
        <Route path="privasi" element={<Privasi />} />
        <Route path="*" element={<NotFound />} />
      </Route>

      {/* Layout auth minimal */}
      <Route element={<AuthLayout />}>
        <Route
          path="login"
          element={
            <GuestOnly>
              <Login />
            </GuestOnly>
          }
        />
        <Route
          path="register"
          element={
            <GuestOnly>
              <Register />
            </GuestOnly>
          }
        />
        <Route
          path="register/verifikasi"
          element={
            <PendingOnly>
              <Verifikasi />
            </PendingOnly>
          }
        />
        {/* Rute lama yang tidak dipakai lagi: dialihkan ke halaman verifikasi. */}
        <Route path="register/send" element={<Navigate to="/register/verifikasi" replace />} />
      </Route>

      {/* Layout aplikasi (sidebar) */}
      <Route element={<AppLayout />}>
        <Route path="chat" element={<Chat />} />
        <Route
          path="profile"
          element={
            <RequireAuth>
              <ProfilePage />
            </RequireAuth>
          }
        />
      </Route>
    </Routes>
  );
}
