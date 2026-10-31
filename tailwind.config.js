/** @type {import('tailwindcss').Config} */
export default {
  darkMode: 'class',
  content: ['./index.html', './src/**/*.{ts,tsx}'],
  theme: {
    extend: {
      colors: {
        // Satu warna aksen: amber/emas hangat. Nilai kontras dicek untuk
        // teks di atas latar gelap maupun terang.
        accent: {
          50: '#fff8e6',
          100: '#fdefc6',
          200: '#fadf8e',
          300: '#f6c94f',
          400: '#f0b429',
          500: '#d99a12',
          600: '#b3780a',
          700: '#8c5a08',
          800: '#6b4408',
          900: '#4d3106',
        },
        ink: {
          50: '#f7f7f6',
          100: '#eceae7',
          200: '#d7d4ce',
          300: '#b4afa6',
          400: '#8b857a',
          500: '#6b655b',
          600: '#514c44',
          700: '#3b3731',
          800: '#272420',
          900: '#181613',
          950: '#0f0e0c',
        },
      },
      fontFamily: {
        sans: [
          'Inter',
          'ui-sans-serif',
          'system-ui',
          '-apple-system',
          'Segoe UI',
          'Roboto',
          'Helvetica Neue',
          'Arial',
          'sans-serif',
        ],
      },
      borderRadius: {
        xl: '0.875rem',
        '2xl': '1.25rem',
        '3xl': '1.75rem',
      },
      boxShadow: {
        card: '0 1px 2px rgba(0,0,0,0.04), 0 8px 24px -12px rgba(0,0,0,0.25)',
        lift: '0 2px 4px rgba(0,0,0,0.04), 0 18px 40px -20px rgba(0,0,0,0.35)',
      },
      keyframes: {
        'fade-in': {
          from: { opacity: '0', transform: 'translateY(4px)' },
          to: { opacity: '1', transform: 'translateY(0)' },
        },
        'pop-in': {
          from: { opacity: '0', transform: 'scale(0.97)' },
          to: { opacity: '1', transform: 'scale(1)' },
        },
        blink: {
          '0%, 80%, 100%': { opacity: '0.25', transform: 'translateY(0)' },
          '40%': { opacity: '1', transform: 'translateY(-2px)' },
        },
        'bubble-in': {
          from: { opacity: '0', transform: 'translateY(6px) scale(0.98)' },
          to: { opacity: '1', transform: 'translateY(0) scale(1)' },
        },
        shimmer: {
          '0%': { backgroundPosition: '200% 0' },
          '100%': { backgroundPosition: '-200% 0' },
        },
      },
      animation: {
        'fade-in': 'fade-in 180ms ease-out both',
        'pop-in': 'pop-in 160ms ease-out both',
        blink: 'blink 1.2s infinite ease-in-out',
        'bubble-in': 'bubble-in 220ms ease-out both',
      },
    },
  },
  plugins: [],
};
