/// <reference types="vite/client" />

interface ImportMetaEnv {
  readonly VITE_AUTH_MODE?: string;
  readonly VITE_ALLOW_DUMMY_AUTH?: string;
  readonly VITE_CHAT_MODE?: string;
  readonly VITE_CHAT_REQUIRES_LOGIN?: string;
}

interface ImportMeta {
  readonly env: ImportMetaEnv;
}
