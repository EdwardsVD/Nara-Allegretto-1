import {
  createContext,
  useCallback,
  useContext,
  useMemo,
  useRef,
  useState,
  type ReactNode,
} from 'react';
import { ChatError, type ChatMessage } from './types';
import { chatApi, MAX_MESSAGE_LENGTH } from './chatApi';

/**
 * State percakapan HANYA di memori React:
 * - tidak ditulis ke localStorage
 * - tidak dikirim ke server untuk disimpan
 * - hilang saat refresh
 *
 * Provider diletakkan di AppLayout agar percakapan bertahan saat berpindah
 * antara /chat dan /profile tanpa reload, tetapi tetap hilang saat refresh.
 */

export interface ChatSessionValue {
  messages: ChatMessage[];
  isThinking: boolean;
  error: string | null;
  /** Naik setiap kali "Chat baru" ditekan; dipakai untuk memfokuskan input. */
  focusSignal: number;
  send(text: string): Promise<void>;
  retry(): Promise<void>;
  startNew(): void;
  clearError(): void;
}

const ChatSessionContext = createContext<ChatSessionValue | null>(null);

let sequence = 0;
function nextId(prefix: string): string {
  sequence += 1;
  return `${prefix}_${Date.now().toString(36)}_${sequence}`;
}

export function ChatSessionProvider({ children }: { children: ReactNode }) {
  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [isThinking, setIsThinking] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [focusSignal, setFocusSignal] = useState(0);
  const lastRequest = useRef<string | null>(null);

  const run = useCallback(async (text: string, appendUserMessage: boolean) => {
    const trimmed = text.trim();
    if (!trimmed) return;

    lastRequest.current = trimmed;
    setError(null);

    let historyForApi: Array<{ role: 'user' | 'assistant'; content: string }> = [];
    setMessages((current) => {
      historyForApi = current.map((message) => ({
        role: message.role,
        content: message.content,
      }));
      if (!appendUserMessage) return current;
      const userMessage: ChatMessage = {
        id: nextId('user'),
        role: 'user',
        content: trimmed.slice(0, MAX_MESSAGE_LENGTH),
        createdAt: new Date().toISOString(),
      };
      return [...current, userMessage];
    });

    setIsThinking(true);
    try {
      const reply = await chatApi.send({
        message: trimmed.slice(0, MAX_MESSAGE_LENGTH),
        history: historyForApi,
      });
      setMessages((current) => [
        ...current,
        {
          id: nextId('nara'),
          role: 'assistant',
          content: reply.content,
          createdAt: new Date().toISOString(),
        },
      ]);
    } catch (caught) {
      const message =
        caught instanceof ChatError
          ? caught.message
          : 'Gagal mengirim pesan. Periksa koneksi Anda lalu coba lagi.';
      setError(message);
    } finally {
      setIsThinking(false);
    }
  }, []);

  const send = useCallback((text: string) => run(text, true), [run]);

  const retry = useCallback(async () => {
    if (!lastRequest.current) return;
    await run(lastRequest.current, false);
  }, [run]);

  const startNew = useCallback(() => {
    setMessages([]);
    setError(null);
    setIsThinking(false);
    lastRequest.current = null;
    setFocusSignal((value) => value + 1);
  }, []);

  const clearError = useCallback(() => setError(null), []);

  const value = useMemo<ChatSessionValue>(
    () => ({ messages, isThinking, error, focusSignal, send, retry, startNew, clearError }),
    [messages, isThinking, error, focusSignal, send, retry, startNew, clearError],
  );

  return <ChatSessionContext.Provider value={value}>{children}</ChatSessionContext.Provider>;
}

// eslint-disable-next-line react-refresh/only-export-components
export function useChatSession(): ChatSessionValue {
  const context = useContext(ChatSessionContext);
  if (!context) throw new Error('useChatSession harus dipakai di dalam <ChatSessionProvider>.');
  return context;
}
