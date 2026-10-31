import '@testing-library/jest-dom/vitest';
import { afterEach, beforeEach, vi } from 'vitest';
import { cleanup } from '@testing-library/react';

// jsdom tidak menyediakan matchMedia; sediakan stub minimal.
if (!window.matchMedia) {
  Object.defineProperty(window, 'matchMedia', {
    writable: true,
    value: (query: string) => ({
      matches: query.includes('dark'),
      media: query,
      onchange: null,
      addEventListener: vi.fn(),
      removeEventListener: vi.fn(),
      addListener: vi.fn(),
      removeListener: vi.fn(),
      dispatchEvent: vi.fn(),
    }),
  });
}

// jsdom belum punya scrollTo/scrollIntoView pada elemen.
if (!Element.prototype.scrollIntoView) {
  Element.prototype.scrollIntoView = vi.fn();
}

beforeEach(() => {
  window.localStorage.clear();
  window.sessionStorage.clear();
  document.documentElement.classList.remove('dark');
});

afterEach(() => {
  cleanup();
  vi.useRealTimers();
});
