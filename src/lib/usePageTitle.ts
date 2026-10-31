import { useEffect } from 'react';

export const APP_NAME = 'Nara';

/** Ubah document.title per rute. */
export function usePageTitle(title: string): void {
  useEffect(() => {
    document.title = title ? `${title} · ${APP_NAME}` : APP_NAME;
  }, [title]);
}
