import { useCallback, useEffect, useRef, useState } from 'react';

/**
 * Hitung mundur berbasis interval 1 detik.
 * Dipakai untuk tombol "Kirim ulang" (60 dtk) dan kunci input kode (30 dtk).
 */
export function useCountdown(): {
  remaining: number;
  isRunning: boolean;
  start(seconds: number): void;
  stop(): void;
} {
  const [remaining, setRemaining] = useState(0);
  const intervalRef = useRef<ReturnType<typeof setInterval> | null>(null);

  const stop = useCallback(() => {
    if (intervalRef.current !== null) {
      clearInterval(intervalRef.current);
      intervalRef.current = null;
    }
    setRemaining(0);
  }, []);

  const start = useCallback((seconds: number) => {
    if (intervalRef.current !== null) {
      clearInterval(intervalRef.current);
    }
    setRemaining(seconds);
    intervalRef.current = setInterval(() => {
      setRemaining((current) => {
        if (current <= 1) {
          if (intervalRef.current !== null) {
            clearInterval(intervalRef.current);
            intervalRef.current = null;
          }
          return 0;
        }
        return current - 1;
      });
    }, 1000);
  }, []);

  useEffect(() => {
    return () => {
      if (intervalRef.current !== null) clearInterval(intervalRef.current);
    };
  }, []);

  return { remaining, isRunning: remaining > 0, start, stop };
}
