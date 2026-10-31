import { useState } from 'react';
import { Button } from '../ui/Button';
import type { OAuthProvider } from '../../lib/auth/types';

function GithubIcon() {
  return (
    <svg aria-hidden="true" viewBox="0 0 24 24" className="h-4 w-4" fill="currentColor">
      <path d="M12 2a10 10 0 0 0-3.16 19.49c.5.09.68-.22.68-.48v-1.7c-2.78.6-3.37-1.34-3.37-1.34-.45-1.16-1.11-1.47-1.11-1.47-.91-.62.07-.6.07-.6 1 .07 1.53 1.03 1.53 1.03.9 1.53 2.36 1.09 2.94.83.09-.65.35-1.09.63-1.34-2.22-.25-4.55-1.11-4.55-4.94 0-1.09.39-1.98 1.03-2.68-.1-.25-.45-1.27.1-2.65 0 0 .84-.27 2.75 1.02a9.5 9.5 0 0 1 5 0c1.91-1.29 2.75-1.02 2.75-1.02.55 1.38.2 2.4.1 2.65.64.7 1.03 1.59 1.03 2.68 0 3.84-2.34 4.69-4.57 4.94.36.31.68.92.68 1.85v2.74c0 .27.18.58.69.48A10 10 0 0 0 12 2Z" />
    </svg>
  );
}

function GoogleIcon() {
  return (
    <svg aria-hidden="true" viewBox="0 0 24 24" className="h-4 w-4">
      <path fill="#4285F4" d="M21.6 12.2c0-.7-.06-1.35-.18-2H12v3.8h5.4a4.62 4.62 0 0 1-2 3.03v2.5h3.23c1.89-1.74 2.97-4.3 2.97-7.33Z" />
      <path fill="#34A853" d="M12 22c2.7 0 4.96-.9 6.63-2.43l-3.23-2.5c-.9.6-2.05.96-3.4.96a6 6 0 0 1-5.63-4.14H3.03v2.58A10 10 0 0 0 12 22Z" />
      <path fill="#FBBC05" d="M6.37 13.89a6 6 0 0 1 0-3.78V7.53H3.03a10 10 0 0 0 0 8.94l3.34-2.58Z" />
      <path fill="#EA4335" d="M12 5.97c1.47 0 2.79.5 3.83 1.5l2.86-2.86A9.97 9.97 0 0 0 12 2 10 10 0 0 0 3.03 7.53l3.34 2.58A6 6 0 0 1 12 5.97Z" />
    </svg>
  );
}

export function OAuthButtons({
  onProvider,
  disabled = false,
}: {
  onProvider(provider: OAuthProvider): Promise<void> | void;
  disabled?: boolean;
}) {
  const [pending, setPending] = useState<OAuthProvider | null>(null);

  const handle = async (provider: OAuthProvider) => {
    setPending(provider);
    try {
      await onProvider(provider);
    } finally {
      setPending(null);
    }
  };

  return (
    <div className="grid gap-2">
      <Button
        type="button"
        variant="secondary"
        onClick={() => void handle('github')}
        disabled={disabled || pending !== null}
        leftIcon={<GithubIcon />}
      >
        {pending === 'github' ? 'Menghubungkan…' : 'Lanjutkan dengan GitHub'}
      </Button>
      <Button
        type="button"
        variant="secondary"
        onClick={() => void handle('google')}
        disabled={disabled || pending !== null}
        leftIcon={<GoogleIcon />}
      >
        {pending === 'google' ? 'Menghubungkan…' : 'Lanjutkan dengan Google'}
      </Button>
    </div>
  );
}
