import { useCallback, useEffect, useLayoutEffect, useRef, useState } from 'react';
import { Link, Navigate } from 'react-router-dom';
import { ChatComposer } from '../components/chat/ChatComposer';
import { ChatMessageItem } from '../components/chat/ChatMessageItem';
import { Banner } from '../components/ui/Banner';
import { Button } from '../components/ui/Button';
import { useAuth } from '../lib/auth/AuthContext';
import { useChatSession } from '../lib/chat/ChatSessionContext';
import { CHAT_REQUIRES_LOGIN } from '../lib/env';
import { usePageTitle } from '../lib/usePageTitle';

const SUGGESTIONS = [
  { icon: '👋', text: 'Siapa kamu, Nara?' },
  { icon: '🧪', text: 'Apa rumus kimia air?' },
  { icon: '💵', text: 'Apa itu uang rupiah?' },
  { icon: '🐛', text: 'Hewan apa yang bernapas lewat kulit?' },
];

const STICK_THRESHOLD = 96;

export function Chat() {
  usePageTitle('Chat');
  const { status, user } = useAuth();
  const { messages, isThinking, error, focusSignal, send, retry, startNew, clearError } =
    useChatSession();

  const scrollRef = useRef<HTMLDivElement>(null);
  const shouldStickToBottom = useRef(true);
  const [showJumpButton, setShowJumpButton] = useState(false);
  const [showNewChatHint, setShowNewChatHint] = useState(false);

  const scrollToBottom = useCallback((smooth = false) => {
    const container = scrollRef.current;
    if (!container) return;
    container.scrollTo({
      top: container.scrollHeight,
      behavior: smooth ? 'smooth' : 'auto',
    });
    shouldStickToBottom.current = true;
    setShowJumpButton(false);
  }, []);

  // Gulung otomatis ke bawah kecuali pengguna sedang membaca ke atas.
  useLayoutEffect(() => {
    if (!shouldStickToBottom.current) return;
    const container = scrollRef.current;
    if (!container) return;
    container.scrollTop = container.scrollHeight;
  }, [messages, isThinking]);

  // "Chat baru" dari sidebar: percakapan kosong + fokus input.
  // Petunjuk singkat ditampilkan lewat timer (state diperbarui dari callback
  // timer, bukan sinkron di badan efek).
  const previousSignal = useRef(focusSignal);

  useEffect(() => {
    if (focusSignal === previousSignal.current) return;
    previousSignal.current = focusSignal;
    shouldStickToBottom.current = true;
    const showTimer = setTimeout(() => setShowNewChatHint(true), 0);
    const hideTimer = setTimeout(() => setShowNewChatHint(false), 2600);
    return () => {
      clearTimeout(showTimer);
      clearTimeout(hideTimer);
    };
  }, [focusSignal]);

  if (CHAT_REQUIRES_LOGIN && status === 'anonymous') {
    return <Navigate to="/login?next=%2Fchat" replace />;
  }

  const isEmpty = messages.length === 0;

  const handleScroll = () => {
    const container = scrollRef.current;
    if (!container) return;
    const distanceFromBottom =
      container.scrollHeight - container.scrollTop - container.clientHeight;
    const atBottom = distanceFromBottom < STICK_THRESHOLD;
    shouldStickToBottom.current = atBottom;
    setShowJumpButton(!atBottom && (messages.length > 0 || isThinking));
  };

  const handleSend = async (text: string) => {
    shouldStickToBottom.current = true;
    await send(text);
  };

  const displayName = user?.displayName ?? 'Tamu';
  const displayEmail = user?.email ?? 'tamu@nara';

  return (
    <div className="flex h-full min-h-0 flex-col">
      <div
        ref={scrollRef}
        onScroll={handleScroll}
        className="scroll-smooth relative min-h-0 flex-1 overflow-y-auto px-4 py-6 sm:px-6"
        aria-label="Percakapan"
        role="log"
        aria-live="polite"
        aria-relevant="additions text"
      >
        <div className="mx-auto w-full max-w-3xl">
          {isEmpty ? (
            <div className="space-y-8 py-6 sm:py-10 animate-fade-in motion-reduce:animate-none">
              <div className="space-y-3">
                <span className="inline-grid h-12 w-12 place-items-center rounded-2xl border border-accent-400/40 bg-accent-50 text-accent-800 dark:bg-accent-400/10 dark:text-accent-200">
                  <svg aria-hidden="true" viewBox="0 0 24 24" className="h-6 w-6" fill="none" stroke="currentColor" strokeWidth="2">
                    <path d="M12 3v3m0 12v3M4.2 7.5l2.6 1.5m10.4 6 2.6 1.5M4.2 16.5l2.6-1.5m10.4-6 2.6-1.5" strokeLinecap="round" />
                    <circle cx="12" cy="12" r="3.2" />
                  </svg>
                </span>
                <h1 className="text-2xl font-semibold tracking-tight text-ink-900 sm:text-[1.75rem] dark:text-ink-50">
                  {status === 'authenticated'
                    ? `Halo, ${displayName.split(' ')[0]}. Ada yang bisa saya bantu?`
                    : 'Halo, ada yang bisa saya bantu?'}
                </h1>
                <p className="max-w-xl text-sm leading-relaxed text-ink-600 dark:text-ink-300">
                  Percakapan ini dimulai kosong dan tidak disimpan di mana pun. Pilih satu
                  contoh di bawah atau ketik pertanyaan Anda sendiri.
                </p>
              </div>

              <ul className="grid gap-2 sm:grid-cols-2">
                {SUGGESTIONS.map((suggestion) => (
                  <li key={suggestion.text}>
                    <button
                      type="button"
                      onClick={() => void handleSend(suggestion.text)}
                      disabled={isThinking}
                      className="group flex h-full w-full items-start gap-3 rounded-xl border border-ink-200 bg-white/80 px-4 py-3 text-left text-sm text-ink-800 transition-all hover:-translate-y-0.5 hover:border-accent-400 hover:shadow-card focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent-400 disabled:opacity-60 disabled:hover:translate-y-0 motion-reduce:hover:translate-y-0 dark:border-ink-800 dark:bg-ink-900/70 dark:text-ink-100 dark:hover:border-accent-500/60"
                    >
                      <span aria-hidden="true" className="text-base leading-6">
                        {suggestion.icon}
                      </span>
                      <span className="flex-1 leading-6">{suggestion.text}</span>
                      <span
                        aria-hidden="true"
                        className="mt-0.5 text-ink-400 opacity-0 transition-opacity group-hover:opacity-100"
                      >
                        →
                      </span>
                    </button>
                  </li>
                ))}
              </ul>

              <div className="flex flex-wrap items-center gap-x-3 gap-y-2 text-xs text-ink-500 dark:text-ink-400">
                <button
                  type="button"
                  onClick={startNew}
                  className="rounded underline underline-offset-2 transition-colors hover:text-ink-800 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent-400 dark:hover:text-ink-100"
                >
                  Mulai percakapan kosong
                </button>
                <span aria-hidden="true">·</span>
                <Link
                  to={status === 'authenticated' ? '/profile' : '/login?next=%2Fchat'}
                  className="rounded underline underline-offset-2 transition-colors hover:text-ink-800 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent-400 dark:hover:text-ink-100"
                >
                  {status === 'authenticated' ? 'Pengaturan akun' : 'Masuk untuk menyimpan preferensi'}
                </Link>
              </div>
            </div>
          ) : (
            <ul className="space-y-4">
              {messages.map((message) => (
                <ChatMessageItem
                  key={message.id}
                  message={message}
                  userName={displayName}
                  userEmail={displayEmail}
                />
              ))}
            </ul>
          )}

          {isThinking ? (
            <div className="mt-4 flex items-start gap-2.5" aria-live="polite">
              <span
                aria-hidden="true"
                className="mt-0.5 grid h-8 w-8 shrink-0 place-items-center rounded-full border border-accent-400/40 bg-accent-50 text-accent-800 dark:bg-accent-400/10 dark:text-accent-200"
              >
                <svg viewBox="0 0 24 24" className="h-4 w-4" fill="none" stroke="currentColor" strokeWidth="2.2">
                  <path d="M6 18V6l12 12V6" strokeLinecap="round" strokeLinejoin="round" />
                </svg>
              </span>
              <div className="rounded-2xl rounded-bl-md border border-ink-200/80 bg-white px-4 py-3 shadow-sm dark:border-ink-800 dark:bg-ink-900">
                <span className="sr-only">Nara sedang mengetik…</span>
                <span className="flex items-center gap-1.5" aria-hidden="true">
                  {[0, 1, 2].map((dot) => (
                    <span
                      key={dot}
                      className="h-1.5 w-1.5 rounded-full bg-ink-400 animate-blink motion-reduce:animate-none dark:bg-ink-500"
                      style={{ animationDelay: `${dot * 0.15}s` }}
                    />
                  ))}
                </span>
              </div>
            </div>
          ) : null}

          {error ? (
            <Banner
              tone="danger"
              role="alert"
              className="mt-4 flex flex-wrap items-center justify-between gap-3"
            >
              <span>{error}</span>
              <span className="flex gap-2">
                <Button size="sm" variant="secondary" onClick={() => void retry()}>
                  Coba lagi
                </Button>
                <Button size="sm" variant="ghost" onClick={clearError}>
                  Tutup
                </Button>
              </span>
            </Banner>
          ) : null}
        </div>

        {showJumpButton ? (
          <div className="pointer-events-none sticky bottom-2 flex justify-center">
            <button
              type="button"
              onClick={() => scrollToBottom(true)}
              className="pointer-events-auto inline-flex items-center gap-1.5 rounded-full border border-ink-200 bg-white/95 px-3 py-1.5 text-xs font-medium text-ink-700 shadow-card backdrop-blur transition-colors hover:bg-white focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent-400 dark:border-ink-700 dark:bg-ink-900/95 dark:text-ink-200 dark:hover:bg-ink-800"
            >
              <svg aria-hidden="true" viewBox="0 0 20 20" className="h-3.5 w-3.5" fill="none" stroke="currentColor" strokeWidth="1.8">
                <path d="M10 4v11m0 0 4-4m-4 4-4-4" strokeLinecap="round" strokeLinejoin="round" />
              </svg>
              Pesan terbaru
            </button>
          </div>
        ) : null}
      </div>

      <div className="border-t border-ink-200/80 bg-ink-50/85 px-4 py-3 backdrop-blur sm:px-6 dark:border-ink-800/80 dark:bg-ink-950/85">
        <div className="mx-auto w-full max-w-3xl space-y-2">
          {showNewChatHint ? (
            <p
              role="status"
              className="text-center text-xs font-medium text-accent-700 animate-fade-in motion-reduce:animate-none dark:text-accent-300"
            >
              Percakapan baru dimulai — riwayat sebelumnya tidak disimpan.
            </p>
          ) : null}
          <ChatComposer onSend={handleSend} disabled={isThinking} focusSignal={focusSignal} />
          <p className="text-center text-xs text-ink-500 dark:text-ink-500">
            Nara bisa salah. Jangan jadikan rujukan utama.
          </p>
        </div>
      </div>
    </div>
  );
}
