import { forwardRef, useState, type InputHTMLAttributes } from 'react';
import { Input, type InputProps } from './Input';

type Props = Omit<InputProps, 'type' | 'trailing'> &
  Pick<InputHTMLAttributes<HTMLInputElement>, 'autoComplete'>;

/** Input password dengan tombol tampil/sembunyikan yang bisa diakses keyboard. */
export const PasswordInput = forwardRef<HTMLInputElement, Props>(function PasswordInput(
  { label, ...props },
  ref,
) {
  const [visible, setVisible] = useState(false);

  return (
    <Input
      ref={ref}
      label={label}
      type={visible ? 'text' : 'password'}
      trailing={
        <button
          type="button"
          onClick={() => setVisible((value) => !value)}
          aria-pressed={visible}
          aria-label={visible ? 'Sembunyikan password' : 'Tampilkan password'}
          className="mr-1 rounded-lg px-2 py-1 text-xs font-medium text-ink-600 transition-colors hover:bg-ink-200/70 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent-400 dark:text-ink-300 dark:hover:bg-ink-800"
        >
          {visible ? 'Sembunyi' : 'Tampil'}
        </button>
      }
      {...props}
    />
  );
});
