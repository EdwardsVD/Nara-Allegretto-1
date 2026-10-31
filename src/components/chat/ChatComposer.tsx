import { useEffect, useRef, useState, type ChangeEvent, type KeyboardEvent } from 'react';
import { Button } from '../ui/Button';
import { MAX_MESSAGE_LENGTH } from '../../lib/chat/chatApi';

const MAX_ROWS = 6;
const LINE_HEIGHT = 24;
const PADDING = 20;

export function ChatComposer({
  onSend,
  disabled,
  focusSignal,
}: {
  onSend(text: string): void | Promise<void>;
  disabled?: boolean;
  focusSignal?: number;
}) {
  const [value, setValue] = useState('');
  const textareaRef = useRef<HTMLTextAreaElement>(null);
  const [isFocused, setIsFocused] = useState(false);

  // Auto-resize sampai 6 baris.
  useEffect(() => {
    const element = textareaRef.current;
    if (!element) return;
    element.style.height = 'auto';
    const maxHeight = MAX_ROWS * LINE_HEIGHT + PADDING;
    element.style.height = `${Math.min(element.scrollHeight + 2, maxHeight)}px`;
    element.style.overflowY = element.scrollHeight + 2 > maxHeight ? 'auto' : 'hidden';
  }, [value]);

  useEffect(() => {
    if (focusSignal === undefined) return;
    textareaRef.current?.focus();
  }, [focusSignal]);

  const submit = async () => {
    const trimmed = value.trim();
    if (!trimmed || disabled) return;
    setValue('');
    await onSend(trimmed.slice(0, MAX_MESSAGE_LENGTH));
    textareaRef.current?.focus();
  };

  const onChange = (event: ChangeEvent<HTMLTextAreaElement>) => {
    setValue(event.target.value.slice(0, MAX_MESSAGE_LENGTH));
  };

  const onKeyDown = (event: KeyboardEvent<HTMLTextAreaElement>) => {
    if (event.key === 'Enter' && !event.shiftKey && !event.nativeEvent.isComposing) {
      event.preventDefault();
      void submit();
    }
  };

  const remaining = MAX_MESSAGE_LENGTH - value.length;
  const nearLimit = remaining <= 50;
  const overSoftLimit = value.length > 0 && remaining <= 0;
  const canSend = value.trim().length > 0 && !disabled;

  return (
    <form
      className={`rounded-2xl border bg-white p-2 transition-shadow dark:bg-ink-900 ${
        isFocused
          ? 'border-accent-400 shadow-lift ring-2 ring-accent-400/25'
          : 'border-ink-200 shadow-card dark:border-ink-800'
      }`}
      onSubmit={(event) => {
        event.preventDefault();
        void submit();
      }}
    >
      <label htmlFor="chat-input" className="sr-only">
        Tulis pesan untuk Nara
      </label>
      <textarea
        ref={textareaRef}
        id="chat-input"
        name="pesan"
        rows={1}
        value={value}
        onChange={onChange}
        onKeyDown={onKeyDown}
        onFocus={() => setIsFocused(true)}
        onBlur={() => setIsFocused(false)}
        disabled={disabled}
        maxLength={MAX_MESSAGE_LENGTH}
        aria-describedby="chat-input-help"
        placeholder="Tulis pesan…"
        className="block w-full resize-none rounded-xl bg-transparent px-3 py-2.5 text-sm leading-6 text-ink-900 placeholder:text-ink-400 focus:outline-none disabled:opacity-60 dark:text-ink-50 dark:placeholder:text-ink-500"
        style={{ maxHeight: MAX_ROWS * LINE_HEIGHT + PADDING }}
      />
      <div className="flex items-center justify-between gap-3 px-1 pb-1 pt-1">
        <p
          id="chat-input-help"
          className="flex items-center gap-2 text-[11px] text-ink-400 dark:text-ink-500"
        >
          <kbd className="hidden rounded border border-ink-200 bg-ink-50 px-1.5 py-0.5 font-sans text-[10px] font-medium text-ink-600 sm:inline dark:border-ink-700 dark:bg-ink-800 dark:text-ink-300">
            Enter
          </kbd>
          <span className="hidden sm:inline">kirim ·</span>
          <kbd className="hidden rounded border border-ink-200 bg-ink-50 px-1.5 py-0.5 font-sans text-[10px] font-medium text-ink-600 sm:inline dark:border-ink-700 dark:bg-ink-800 dark:text-ink-300">
            Shift + Enter
          </kbd>
          <span className="hidden sm:inline">baris baru</span>
          <span className="sm:hidden">Enter kirim · Shift+Enter baris baru</span>
        </p>
        <div className="flex items-center gap-2">
          <span
            aria-live="polite"
            className={`text-[11px] tabular-nums ${
              overSoftLimit
                ? 'font-semibold text-red-600 dark:text-red-400'
                : nearLimit
                  ? 'font-medium text-amber-600 dark:text-amber-400'
                  : 'text-ink-400 dark:text-ink-500'
            }`}
          >
            {value.length}/{MAX_MESSAGE_LENGTH}
          </span>
          <Button type="submit" size="sm" disabled={!canSend} aria-label="Kirim pesan">
            <svg aria-hidden="true" viewBox="0 0 20 20" className="h-4 w-4" fill="none" stroke="currentColor" strokeWidth="1.8">
              <path d="M3.5 10 16 4l-3.5 6L16 16 3.5 10Z" strokeLinecap="round" strokeLinejoin="round" />
            </svg>
            Kirim
          </Button>
        </div>
      </div>
    </form>
  );
}
