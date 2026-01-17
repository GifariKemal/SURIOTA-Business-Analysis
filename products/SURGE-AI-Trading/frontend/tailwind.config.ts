import type { Config } from 'tailwindcss'

const config: Config = {
  content: [
    './pages/**/*.{js,ts,jsx,tsx,mdx}',
    './components/**/*.{js,ts,jsx,tsx,mdx}',
    './app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        // Dark theme colors (nof1.ai inspired)
        background: '#0a0a0f',
        surface: '#121218',
        'surface-light': '#1a1a24',
        'surface-hover': '#22222e',
        border: '#2a2a3a',
        'border-light': '#3a3a4a',
        // Accent colors
        primary: '#6366f1',
        'primary-dark': '#4f46e5',
        accent: '#8b5cf6',
        // Semantic colors
        success: '#22c55e',
        'success-bg': '#22c55e20',
        warning: '#f59e0b',
        'warning-bg': '#f59e0b20',
        danger: '#ef4444',
        'danger-bg': '#ef444420',
        info: '#3b82f6',
        'info-bg': '#3b82f620',
        // Text colors
        'text-primary': '#ffffff',
        'text-secondary': '#a1a1aa',
        'text-muted': '#71717a',
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', 'sans-serif'],
        mono: ['JetBrains Mono', 'Fira Code', 'monospace'],
      },
      animation: {
        'pulse-slow': 'pulse 3s cubic-bezier(0.4, 0, 0.6, 1) infinite',
        'fade-in': 'fadeIn 0.3s ease-in-out',
        'slide-up': 'slideUp 0.3s ease-out',
      },
      keyframes: {
        fadeIn: {
          '0%': { opacity: '0' },
          '100%': { opacity: '1' },
        },
        slideUp: {
          '0%': { transform: 'translateY(10px)', opacity: '0' },
          '100%': { transform: 'translateY(0)', opacity: '1' },
        },
      },
    },
  },
  plugins: [],
}
export default config
