import type { ReactNode } from 'react';

export function Card({
  children,
  className = '',
  as: Tag = 'section',
}: {
  children: ReactNode;
  className?: string;
  as?: 'section' | 'div' | 'article' | 'aside';
}) {
  return (
    <Tag
      className={`rounded-2xl border border-ink-200 bg-white shadow-card dark:border-ink-800 dark:bg-ink-900 ${className}`}
    >
      {children}
    </Tag>
  );
}

export function CardHeader({
  title,
  description,
  id,
  action,
}: {
  title: string;
  description?: ReactNode;
  id?: string;
  action?: ReactNode;
}) {
  return (
    <div className="flex flex-wrap items-start justify-between gap-3 border-b border-ink-200 px-5 py-4 dark:border-ink-800">
      <div className="space-y-1">
        <h2 id={id} className="text-base font-semibold text-ink-900 dark:text-ink-50">
          {title}
        </h2>
        {description ? (
          <p className="text-sm text-ink-600 dark:text-ink-400">{description}</p>
        ) : null}
      </div>
      {action}
    </div>
  );
}

export function CardBody({
  children,
  className = '',
}: {
  children: ReactNode;
  className?: string;
}) {
  return <div className={`px-5 py-4 ${className}`}>{children}</div>;
}
