export type ChatRole = 'user' | 'assistant';

export interface ChatMessage {
  id: string;
  role: ChatRole;
  content: string;
  createdAt: string;
}

export interface ChatRequest {
  message: string;
  /** Riwayat percakapan untuk konteks; tidak dipersistensi di mana pun. */
  history: Array<{ role: ChatRole; content: string }>;
}

export interface ChatReply {
  content: string;
}

export class ChatError extends Error {
  readonly code: 'NETWORK' | 'VALIDATION' | 'RATE_LIMITED';

  constructor(code: ChatError['code'], message: string) {
    super(message);
    this.name = 'ChatError';
    this.code = code;
  }
}

export interface ChatApi {
  send(request: ChatRequest): Promise<ChatReply>;
}
