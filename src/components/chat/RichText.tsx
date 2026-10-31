import type { ReactNode } from 'react';

/**
 * Render teks pesan dengan penekanan ringan TANPA HTML mentah:
 * - **tebal**
 * - `kode`
 * - daftar berbutir / bernomor sederhana di awal baris
 * - baris baru
 *
 * Tidak memakai dangerouslySetInnerHTML, sehingga aman dari injeksi.
 */

const INLINE_RE = /(\*\*[^*]+\*\*|`[^`]+`)/g;

function renderInline(text: string, keyPrefix: string): ReactNode[] {
  const parts = text.split(INLINE_RE).filter((part) => part !== '');
  return parts.map((part, index) => {
    const key = `${keyPrefix}-${index}`;
    if (part.startsWith('**') && part.endsWith('**') && part.length > 4) {
      return <strong key={key}>{part.slice(2, -2)}</strong>;
    }
    if (part.startsWith('`') && part.endsWith('`') && part.length > 2) {
      return <code key={key}>{part.slice(1, -1)}</code>;
    }
    return <span key={key}>{part}</span>;
  });
}

type Block =
  | { type: 'paragraph'; lines: string[] }
  | { type: 'ul'; items: string[] }
  | { type: 'ol'; items: string[] };

function toBlocks(text: string): Block[] {
  const lines = text.replace(/\r\n/g, '\n').split('\n');
  const blocks: Block[] = [];

  for (const line of lines) {
    const trimmed = line.trim();
    const bullet = /^[-*•]\s+(.*)$/.exec(trimmed);
    const numbered = /^(\d{1,2})[.)]\s+(.*)$/.exec(trimmed);

    if (bullet) {
      const last = blocks[blocks.length - 1];
      if (last?.type === 'ul') last.items.push(bullet[1]);
      else blocks.push({ type: 'ul', items: [bullet[1]] });
      continue;
    }
    if (numbered) {
      const last = blocks[blocks.length - 1];
      if (last?.type === 'ol') last.items.push(numbered[2]);
      else blocks.push({ type: 'ol', items: [numbered[2]] });
      continue;
    }
    if (trimmed === '') {
      blocks.push({ type: 'paragraph', lines: [] });
      continue;
    }
    const last = blocks[blocks.length - 1];
    if (last?.type === 'paragraph') last.lines.push(trimmed);
    else blocks.push({ type: 'paragraph', lines: [trimmed] });
  }

  return blocks.filter((block) => block.type !== 'paragraph' || block.lines.length > 0);
}

export function RichText({ text }: { text: string }) {
  const blocks = toBlocks(text);

  return (
    <div className="chat-prose space-y-2 [&>*:first-child]:mt-0 [&>*:last-child]:mb-0">
      {blocks.map((block, index) => {
        if (block.type === 'ul') {
          return (
            <ul key={`b-${index}`}>
              {block.items.map((item, itemIndex) => (
                <li key={`b-${index}-${itemIndex}`}>{renderInline(item, `b-${index}-${itemIndex}`)}</li>
              ))}
            </ul>
          );
        }
        if (block.type === 'ol') {
          return (
            <ol key={`b-${index}`}>
              {block.items.map((item, itemIndex) => (
                <li key={`b-${index}-${itemIndex}`}>{renderInline(item, `b-${index}-${itemIndex}`)}</li>
              ))}
            </ol>
          );
        }
        return (
          <p key={`b-${index}`} className="whitespace-pre-wrap break-words">
            {block.lines.map((line, lineIndex) => (
              <span key={`b-${index}-${lineIndex}`}>
                {lineIndex > 0 ? '\n' : null}
                {renderInline(line, `b-${index}-${lineIndex}`)}
              </span>
            ))}
          </p>
        );
      })}
    </div>
  );
}
