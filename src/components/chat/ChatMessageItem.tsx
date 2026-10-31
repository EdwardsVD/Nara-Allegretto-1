import { useState } from 'react';
import { Avatar } from '../ui/Avatar';
import { RichText } from './RichText';
import type { ChatMessage } from '../../lib/chat/types';

function timeLabel(iso: string): string {
  const date = new Date(iso);
  if (Number.isNaN(date.getTime())) return '';
  try {
    return new Intl.DateTimeFormat('id-ID', { hour: '2-digit', minute: '2-digit' }).format(date);
  } catch {
    return '';
  }
}

function CopyButton({ text }: { text: string }) {
  const [state, setState] = useState<'idle' | 'copied' | 'failed'>('idle');

  const copy = async () => {
    try {
      if (!navigator.clipboard?.writeText) throw new Error('clipboard tidak tersedia');
      await navigator.clipboard.writeText(text);
      setState('copied');
    } catch {
      setState('failed');
    }
    setTimeout(() => setState('idle'), 1800);
  };

  return (
    <button
      type="button"
      onClick={() => void copy()}
      className="inline-flex items-center gap-1 rounded-md px-1.5 py-0.5 text-[11px] font-medium text-ink-500 opacity-0 transition-opacity hover:text-ink-800 focus-visible:opacity-100 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent-400 group-hover:opacity-100 group-focus-within:opacity-100 dark:text-ink-400 dark:hover:text-ink-100 sm:opacity-60"
      aria-label="Salin pesan"
    >
      <svg aria-hidden="true" viewBox="0 0 20 20" className="h-3 w-3" fill="none" stroke="currentColor" strokeWidth="1.6">
        <rect x="7" y="7" width="9" height="9" rx="2" />
        <path d="M13 5.5A1.5 1.5 0 0 0 11.5 4h-6A1.5 1.5 0 0 0 4 5.5v6A1.5 1.5 0 0 0 5.5 13" strokeLinecap="round" />
      </svg>
      <span aria-live="polite">
        {state === 'copied' ? 'Tersalin' : state === 'failed' ? 'Gagal' : 'Salin'}
      </span>
    </button>
  );
}

export function ChatMessageItem({
  message,
  userName,
  userEmail,
}: {
  message: ChatMessage;
  userName: string;
  userEmail: string;
}) {
  const isUser = message.role === 'user';

  return (
    <li
      data-testid="chat-message"
      className={`group flex gap-2.5 animate-bubble-in motion-reduce:animate-none ${
        isUser ? 'flex-row-reverse' : 'flex-row'
      }`}
    >
      {isUser ? (
        <Avatar name={userName} email={userEmail} size="sm" className="mt-0.5" />
      ) : (
        <span
          aria-hidden="true"
          className="mt-0.5 grid h-8 w-8 shrink-0 place-items-center rounded-full border border-accent-400/40 bg-accent-50 text-accent-800 dark:bg-accent-400/10 dark:text-accent-200"
        >
          <svg viewBox="0 0 24 24" className="h-4 w-4" fill="none" stroke="currentColor" strokeWidth="2.2">
            <path d="M6 18V6l12 12V6" strokeLinecap="round" strokeLinejoin="round" />
          </svg>
        </span>
      )}

      <div className={`flex min-w-0 max-w-[88%] flex-col gap-1 sm:max-w-[78%] ${isUser ? 'items-end' : 'items-start'}`}>
        <div
          className={`rounded-2xl px-3.5 py-2.5 text-sm leading-relaxed ${
            isUser
              ? 'rounded-br-md bg-accent-400 text-ink-950 shadow-sm'
              : 'rounded-bl-md border border-ink-200/80 bg-white text-ink-800 shadow-sm dark:border-ink-800 dark:bg-ink-900 dark:text-ink-100'
          }`}
        >
          <span className="sr-only">{isUser ? 'Anda:' : 'Nara:'} </span>
          <RichText text={message.content} />
        </div>
        <div className={`flex items-center gap-2 px-1 text-[11px] text-ink-400 dark:text-ink-500 ${isUser ? 'flex-row-reverse' : ''}`}>
          <span>{timeLabel(message.createdAt)}</span>
          <CopyButton text={message.content} />
        </div>
      </div>
    </li>
  );
}
