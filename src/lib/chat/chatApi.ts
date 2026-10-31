import knowledge from './knowledge.json';
import { CHAT_MODE } from '../env';
import { ChatError, type ChatApi, type ChatReply, type ChatRequest } from './types';

/**
 * API chat.
 * - mock (default di dev): balasan contoh lokal setelah 600 ms, tanpa jaringan.
 * - http: POST /api/chat { message, history } -> { reply }
 *
 * Percakapan TIDAK dikirim ke storage mana pun; hanya hidup di state React.
 */

interface KnowledgeEntry {
  question: string;
  answer: string;
}

const entries = knowledge as KnowledgeEntry[];

export const MOCK_LATENCY_MS = 600;

const FALLBACK_ANSWERS = [
  'Ini mode demo chat, jadi jawaban saya masih contoh. Coba tanyakan hal lain dengan kalimat yang lebih spesifik, ya.',
  'Saya belum punya jawaban contoh untuk pertanyaan itu di mode demo. Coba tanyakan tentang Nara, air, atau rupiah.',
  'Di mode demo ini saya hanya bisa membalas dengan contoh jawaban. Untuk jawaban sungguhan, sambungkan backend lewat VITE_CHAT_MODE=http.',
];

/** Cocokkan kata kunci sederhana: skor = jumlah kata yang sama. */
function scoreEntry(question: string, message: string): number {
  const words = new Set(
    message
      .toLowerCase()
      .replace(/[^\p{L}\p{N}\s]/gu, ' ')
      .split(/\s+/)
      .filter((word) => word.length > 3),
  );
  if (words.size === 0) return 0;
  return question
    .toLowerCase()
    .replace(/[^\p{L}\p{N}\s]/gu, ' ')
    .split(/\s+/)
    .reduce((score, word) => (words.has(word) ? score + 1 : score), 0);
}

export function pickMockAnswer(message: string): string {
  let best: { score: number; answer: string } | null = null;
  for (const entry of entries) {
    const score = scoreEntry(entry.question, message);
    if (score >= 2 && (!best || score > best.score)) {
      best = { score, answer: entry.answer };
    }
  }
  if (best) return best.answer;
  // Tanpa pemilihan acak agar deterministik untuk pengujian.
  const index = message.trim().length % FALLBACK_ANSWERS.length;
  return FALLBACK_ANSWERS[index];
}

export const mockChatApi: ChatApi = {
  async send(request: ChatRequest): Promise<ChatReply> {
    const message = request.message.trim();
    if (!message) {
      throw new ChatError('VALIDATION', 'Pesan tidak boleh kosong.');
    }
    await new Promise((resolve) => setTimeout(resolve, MOCK_LATENCY_MS));
    return { content: pickMockAnswer(message) };
  },
};

export const httpChatApi: ChatApi = {
  async send(request: ChatRequest): Promise<ChatReply> {
    let response: Response;
    try {
      response = await fetch('/api/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: request.message, history: request.history }),
      });
    } catch {
      throw new ChatError('NETWORK', 'Tidak dapat menghubungi server. Periksa koneksi Anda.');
    }
    if (!response.ok) {
      if (response.status === 429) {
        throw new ChatError('RATE_LIMITED', 'Terlalu banyak permintaan. Tunggu sebentar.');
      }
      throw new ChatError('NETWORK', 'Server sedang bermasalah. Coba lagi.');
    }
    const data: unknown = await response.json();
    if (
      typeof data !== 'object' ||
      data === null ||
      typeof (data as { reply?: unknown }).reply !== 'string'
    ) {
      throw new ChatError('NETWORK', 'Balasan server tidak dikenali.');
    }
    return { content: (data as { reply: string }).reply };
  },
};

export const chatApi: ChatApi = CHAT_MODE === 'http' ? httpChatApi : mockChatApi;

export const MAX_MESSAGE_LENGTH = 500;
