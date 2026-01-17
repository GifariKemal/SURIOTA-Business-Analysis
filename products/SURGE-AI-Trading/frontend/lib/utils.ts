/**
 * SURGE-AI Trading Dashboard - Utility Functions
 */
import { clsx, type ClassValue } from 'clsx';
import { twMerge } from 'tailwind-merge';

/**
 * Merge Tailwind CSS classes with clsx
 */
export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}

/**
 * Format currency with locale
 */
export function formatCurrency(
  value: number,
  currency: 'USD' | 'IDR' = 'USD',
  options: Intl.NumberFormatOptions = {}
): string {
  const defaults: Intl.NumberFormatOptions = {
    style: 'currency',
    currency,
    minimumFractionDigits: currency === 'IDR' ? 0 : 2,
    maximumFractionDigits: currency === 'IDR' ? 0 : 2,
    ...options,
  };

  return new Intl.NumberFormat(currency === 'IDR' ? 'id-ID' : 'en-US', defaults).format(value);
}

/**
 * Format USD price
 */
export function formatUSD(value: number): string {
  return formatCurrency(value, 'USD');
}

/**
 * Format IDR price
 */
export function formatIDR(value: number): string {
  return `Rp ${new Intl.NumberFormat('id-ID').format(Math.round(value))}`;
}

/**
 * Format percentage with sign
 */
export function formatPercent(value: number, decimals: number = 2): string {
  const sign = value >= 0 ? '+' : '';
  return `${sign}${value.toFixed(decimals)}%`;
}

/**
 * Format crypto quantity
 */
export function formatCrypto(value: number, decimals: number = 6): string {
  return value.toFixed(decimals);
}

/**
 * Format large numbers with abbreviations
 */
export function formatCompact(value: number): string {
  const formatter = new Intl.NumberFormat('en-US', {
    notation: 'compact',
    compactDisplay: 'short',
  });
  return formatter.format(value);
}

/**
 * Format timestamp to readable string
 */
export function formatTime(timestamp: string | Date): string {
  const date = typeof timestamp === 'string' ? new Date(timestamp) : timestamp;
  return date.toLocaleTimeString('en-US', {
    hour: '2-digit',
    minute: '2-digit',
    second: '2-digit',
    hour12: false,
  });
}

/**
 * Format date to readable string
 */
export function formatDate(timestamp: string | Date): string {
  const date = typeof timestamp === 'string' ? new Date(timestamp) : timestamp;
  return date.toLocaleDateString('en-US', {
    month: 'short',
    day: 'numeric',
    year: 'numeric',
  });
}

/**
 * Format datetime to readable string
 */
export function formatDateTime(timestamp: string | Date): string {
  return `${formatDate(timestamp)} ${formatTime(timestamp)}`;
}

/**
 * Get relative time (e.g., "2 minutes ago")
 */
export function getRelativeTime(timestamp: string | Date): string {
  const date = typeof timestamp === 'string' ? new Date(timestamp) : timestamp;
  const now = new Date();
  const diff = now.getTime() - date.getTime();
  const seconds = Math.floor(diff / 1000);
  const minutes = Math.floor(seconds / 60);
  const hours = Math.floor(minutes / 60);
  const days = Math.floor(hours / 24);

  if (seconds < 60) return 'just now';
  if (minutes < 60) return `${minutes}m ago`;
  if (hours < 24) return `${hours}h ago`;
  if (days < 7) return `${days}d ago`;
  return formatDate(timestamp);
}

/**
 * Get color class based on value (positive/negative)
 */
export function getValueColor(value: number): string {
  if (value > 0) return 'text-success';
  if (value < 0) return 'text-danger';
  return 'text-text-secondary';
}

/**
 * Get background color class based on value
 */
export function getValueBgColor(value: number): string {
  if (value > 0) return 'bg-success-bg';
  if (value < 0) return 'bg-danger-bg';
  return 'bg-surface-light';
}

/**
 * Get signal direction color
 */
export function getSignalColor(direction: string): string {
  switch (direction) {
    case 'LONG':
      return 'text-success';
    case 'SHORT':
      return 'text-danger';
    default:
      return 'text-warning';
  }
}

/**
 * Get signal direction badge color
 */
export function getSignalBadgeColor(direction: string): string {
  switch (direction) {
    case 'LONG':
      return 'badge-success';
    case 'SHORT':
      return 'badge-danger';
    default:
      return 'badge-warning';
  }
}

/**
 * Get confidence level label
 */
export function getConfidenceLevel(confidence: number): string {
  if (confidence >= 80) return 'Very High';
  if (confidence >= 70) return 'High';
  if (confidence >= 60) return 'Medium';
  if (confidence >= 50) return 'Low';
  return 'Very Low';
}

/**
 * Get confidence color
 */
export function getConfidenceColor(confidence: number): string {
  if (confidence >= 80) return 'text-success';
  if (confidence >= 70) return 'text-info';
  if (confidence >= 60) return 'text-warning';
  return 'text-danger';
}

/**
 * Calculate progress percentage (capped at 100)
 */
export function calcProgress(current: number, max: number): number {
  if (max === 0) return 0;
  return Math.min((current / max) * 100, 100);
}

/**
 * Debounce function
 */
export function debounce<T extends (...args: unknown[]) => unknown>(
  func: T,
  wait: number
): (...args: Parameters<T>) => void {
  let timeout: NodeJS.Timeout;
  return (...args: Parameters<T>) => {
    clearTimeout(timeout);
    timeout = setTimeout(() => func(...args), wait);
  };
}

/**
 * Generate unique ID
 */
export function generateId(): string {
  return Math.random().toString(36).substring(2, 10);
}

/**
 * Sleep function for async/await
 */
export function sleep(ms: number): Promise<void> {
  return new Promise((resolve) => setTimeout(resolve, ms));
}
