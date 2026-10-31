import {
  createContext,
  useCallback,
  useContext,
  useEffect,
  useMemo,
  useRef,
  useState,
  type ReactNode,
} from 'react';

type ToastTone = 'success' | 'error' | 'info';

interface ToastItem {
  id: number;
  message: string;
  tone: ToastTone;
}

interface ToastContextValue {
  showToast(message: string, tone?: ToastTone): void;
}

const ToastContext = createContext<ToastContextValue | null>(null);

const toneStyles: Record<ToastTone, string> = {
  success:
    'border-emerald-300 bg-emerald-50 text-emerald-900 dark:border-emerald-700 dark:bg-emerald-950 dark:text-emerald-100',
  error:
    'border-red-300 bg-red-50 text-red-900 dark:border-red-700 dark:bg-red-950 dark:text-red-100',
  info: 'border-ink-300 bg-white text-ink-900 dark:border-ink-700 dark:bg-ink-900 dark:text-ink-50',
};

const toneIcons: Record<ToastTone, ReactNode> = {
  success: (
    <svg aria-hidden="true" viewBox="0 0 20 20" className="h-4 w-4" fill="none" stroke="currentColor" strokeWidth="2">
      <path d="m4 10.5 4 4 8-9" strokeLinecap="round" strokeLinejoin="round" />
    </svg>
  ),
  error: (
    <svg aria-hidden="true" viewBox="0 0 20 20" className="h-4 w-4" fill="none" stroke="currentColor" strokeWidth="2">
      <path d="M10 5v6m0 3.5v.2" strokeLinecap="round" />
      <circle cx="10" cy="10" r="7.5" />
    </svg>
  ),
  info: (
    <svg aria-hidden="true" viewBox="0 0 20 20" className="h-4 w-4" fill="none" stroke="currentColor" strokeWidth="2">
      <path d="M10 9v6m0-9.5V6" strokeLinecap="round" />
      <circle cx="10" cy="10" r="7.5" />
    </svg>
  ),
};

export function ToastProvider({ children }: { children: ReactNode }) {
  const [toasts, setToasts] = useState<ToastItem[]>([]);
  const counter = useRef(0);
  const timers = useRef<Map<number, ReturnType<typeof setTimeout>>>(new Map());

  const dismiss = useCallback((id: number) => {
    setToasts((current) => current.filter((toast) => toast.id !== id));
    const timer = timers.current.get(id);
    if (timer) {
      clearTimeout(timer);
      timers.current.delete(id);
    }
  }, []);

  const showToast = useCallback(
    (message: string, tone: ToastTone = 'success') => {
      counter.current += 1;
      const id = counter.current;
      setToasts((current) => [...current.slice(-2), { id, message, tone }]);
      const timer = setTimeout(() => dismiss(id), 4200);
      timers.current.set(id, timer);
    },
    [dismiss],
  );

  useEffect(() => {
    const map = timers.current;
    return () => {
      map.forEach((timer) => clearTimeout(timer));
      map.clear();
    };
  }, []);

  const value = useMemo(() => ({ showToast }), [showToast]);

  return (
    <ToastContext.Provider value={value}>
      {children}
      <div
        aria-live="polite"
        aria-atomic="false"
        className="pointer-events-none fixed inset-x-0 bottom-4 z-[60] flex flex-col items-center gap-2 px-4"
      >
        {toasts.map((toast) => (
          <div
            key={toast.id}
            role={toast.tone === 'error' ? 'alert' : 'status'}
            className={`pointer-events-auto flex w-full max-w-sm items-start gap-2.5 rounded-xl border px-4 py-3 text-sm shadow-lift animate-pop-in motion-reduce:animate-none ${toneStyles[toast.tone]}`}
          >
            <span className="mt-0.5 shrink-0">{toneIcons[toast.tone]}</span>
            <span className="flex-1 leading-snug">{toast.message}</span>
            <button
              type="button"
              onClick={() => dismiss(toast.id)}
              className="focus-ring -mr-1 shrink-0 rounded-md p-1 text-xs font-semibold opacity-60 hover:opacity-100"
              aria-label="Tutup notifikasi"
            >
              <svg aria-hidden="true" viewBox="0 0 16 16" className="h-3 w-3" fill="none" stroke="currentColor" strokeWidth="2">
                <path d="m4 4 8 8M12 4l-8 8" strokeLinecap="round" />
              </svg>
            </button>
          </div>
        ))}
      </div>
    </ToastContext.Provider>
  );
}

// eslint-disable-next-line react-refresh/only-export-components
export function useToast(): ToastContextValue {
  const context = useContext(ToastContext);
  if (!context) throw new Error('useToast harus dipakai di dalam <ToastProvider>.');
  return context;
}
