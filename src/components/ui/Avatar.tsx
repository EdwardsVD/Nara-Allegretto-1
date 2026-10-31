import { avatarHue, initials } from '../../lib/format';

export function Avatar({
  name,
  email,
  size = 'md',
  className = '',
}: {
  name: string;
  email: string;
  size?: 'sm' | 'md' | 'lg';
  className?: string;
}) {
  const hue = avatarHue(email || name);
  const dimension =
    size === 'sm' ? 'h-8 w-8 text-xs' : size === 'lg' ? 'h-16 w-16 text-xl' : 'h-10 w-10 text-sm';

  return (
    <span
      aria-hidden="true"
      title={name}
      className={`inline-grid shrink-0 place-items-center rounded-full font-semibold ${dimension} ${className}`}
      style={{
        backgroundColor: `hsl(${hue} 65% 42%)`,
        color: '#fff',
        letterSpacing: '0.02em',
      }}
    >
      {initials(name || email)}
    </span>
  );
}
