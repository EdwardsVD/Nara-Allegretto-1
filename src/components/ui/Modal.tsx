import { useCallback, useEffect, useId, useRef, type ReactNode } from 'react';
import { createPortal } from 'react-dom';
import { useFocusTrap } from '../../lib/useFocusTrap';

export function Modal({
  open,
  onClose,
  title,
  description,
  children,
  footer,
}: {
  open: boolean;
  onClose: () => void;
  title: string;
  description?: ReactNode;
  children: ReactNode;
  footer?: ReactNode;
}) {
  const containerRef = useRef<HTMLDivElement>(null);
  const titleId = useId();
  const descriptionId = useId();

  const close = useCallback(() => onClose(), [onClose]);
  useFocusTrap(open, containerRef, close);

  useEffect(() => {
    if (!open) return;
    const original = document.body.style.overflow;
    document.body.style.overflow = 'hidden';
    return () => {
      document.body.style.overflow = original;
    };
  }, [open]);

  if (!open) return null;

  return createPortal(
    <div className="fixed inset-0 z-50 flex items-end justify-center p-4 sm:items-center">
      <div
        className="absolute inset-0 bg-ink-950/60 backdrop-blur-sm animate-fade-in motion-reduce:animate-none"
        onClick={close}
        aria-hidden="true"
      />
      <div
        ref={containerRef}
        role="dialog"
        aria-modal="true"
        aria-labelledby={titleId}
        aria-describedby={description ? descriptionId : undefined}
        tabIndex={-1}
        className="relative w-full max-w-md rounded-2xl border border-ink-200 bg-white shadow-card animate-pop-in motion-reduce:animate-none dark:border-ink-800 dark:bg-ink-900"
      >
        <div className="border-b border-ink-200 px-5 py-4 dark:border-ink-800">
          <h2 id={titleId} className="text-base font-semibold text-ink-900 dark:text-ink-50">
            {title}
          </h2>
          {description ? (
            <p id={descriptionId} className="mt-1 text-sm text-ink-600 dark:text-ink-400">
              {description}
            </p>
          ) : null}
        </div>
        <div className="px-5 py-4">{children}</div>
        {footer ? (
          <div className="flex justify-end gap-2 border-t border-ink-200 px-5 py-4 dark:border-ink-800">
            {footer}
          </div>
        ) : null}
      </div>
    </div>,
    document.body,
  );
}
