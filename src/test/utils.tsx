import { render } from '@testing-library/react';
import { MemoryRouter, useLocation } from 'react-router-dom';
import type { ReactElement } from 'react';
import { AuthProvider } from '../lib/auth/AuthContext';
import { ToastProvider } from '../components/ui/Toast';
import { ThemeProvider } from '../lib/useTheme';
import { AppRoutes } from '../routes';

/* eslint-disable react-refresh/only-export-components -- berkas utilitas tes */

interface TestGlobals {
  __naraTestPaths?: string[];
}

function testGlobals(): TestGlobals {
  return globalThis as unknown as TestGlobals;
}

/** Mencatat setiap perubahan lokasi (khusus tes). */
function RouteProbe() {
  const location = useLocation();
  const globals = testGlobals();
  const list = (globals.__naraTestPaths ??= []);
  const entry = location.pathname + location.search;
  if (list[list.length - 1] !== entry) list.push(entry);
  return null;
}

export function renderApp(initialPath = '/') {
  testGlobals().__naraTestPaths = [initialPath];
  return render(
    <ThemeProvider>
      <AuthProvider>
        <ToastProvider>
          <MemoryRouter initialEntries={[initialPath]}>
            <RouteProbe />
            <AppRoutes />
          </MemoryRouter>
        </ToastProvider>
      </AuthProvider>
    </ThemeProvider>,
  );
}

export function visitedPaths(): string[] {
  return testGlobals().__naraTestPaths ?? [];
}

export function renderWithProviders(ui: ReactElement, initialPath = '/') {
  return render(
    <ThemeProvider>
      <AuthProvider>
        <ToastProvider>
          <MemoryRouter initialEntries={[initialPath]}>{ui}</MemoryRouter>
        </ToastProvider>
      </AuthProvider>
    </ThemeProvider>,
  );
}

export const TEST_EMAIL = 'dewi@example.com';
export const TEST_PASSWORD = 'rahasia123';
export const TEST_CODE = '123456';
