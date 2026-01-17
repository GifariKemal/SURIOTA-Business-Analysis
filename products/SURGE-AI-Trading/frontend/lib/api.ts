/**
 * SURGE-AI Trading Dashboard - API Client
 */
import type {
  PriceData,
  Signal,
  TradeRecommendation,
  TradeRequest,
  TradeResult,
  Position,
  Balance,
  RiskMetrics,
  TradeHistory,
  ExchangeRate,
} from '@/types';

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

/**
 * API error class
 */
export class ApiError extends Error {
  constructor(
    public status: number,
    message: string,
    public details?: unknown
  ) {
    super(message);
    this.name = 'ApiError';
  }
}

/**
 * Fetch wrapper with error handling
 */
async function fetchApi<T>(
  endpoint: string,
  options: RequestInit = {}
): Promise<T> {
  const url = `${API_BASE_URL}${endpoint}`;

  const response = await fetch(url, {
    ...options,
    headers: {
      'Content-Type': 'application/json',
      ...options.headers,
    },
  });

  if (!response.ok) {
    const error = await response.json().catch(() => ({ detail: 'Unknown error' }));
    throw new ApiError(response.status, error.detail || 'Request failed', error);
  }

  return response.json();
}

// ============================================================
// Market API
// ============================================================

export const marketApi = {
  /**
   * Get current price for a symbol
   */
  getPrice: (symbol: string = 'BTCUSDT') =>
    fetchApi<PriceData>(`/api/v1/market/price/${symbol}`),

  /**
   * Get all supported symbol prices
   */
  getTicker: () =>
    fetchApi<{ prices: PriceData[]; timestamp: string }>('/api/v1/market/ticker'),

  /**
   * Get USD to IDR exchange rate
   */
  getExchangeRate: () =>
    fetchApi<ExchangeRate>('/api/v1/market/exchange-rate'),

  /**
   * Get supported symbols
   */
  getSymbols: () =>
    fetchApi<string[]>('/api/v1/market/symbols'),
};

// ============================================================
// Signals API
// ============================================================

export const signalsApi = {
  /**
   * Get current trading signal
   */
  getCurrent: (symbol: string = 'BTCUSDT') =>
    fetchApi<Signal>(`/api/v1/signals/current?symbol=${symbol}`),

  /**
   * Get trade recommendation
   */
  getRecommendation: (symbol: string = 'BTCUSDT') =>
    fetchApi<TradeRecommendation>(`/api/v1/signals/recommendation?symbol=${symbol}`),

  /**
   * Get signal history
   */
  getHistory: (limit: number = 50) =>
    fetchApi<{ signals: Signal[]; total_count: number }>(
      `/api/v1/signals/history?limit=${limit}`
    ),

  /**
   * Get Kalman component breakdown
   */
  getComponents: (symbol: string = 'BTCUSDT') =>
    fetchApi<Signal['kalman_breakdown']>(`/api/v1/signals/components?symbol=${symbol}`),

  /**
   * Force refresh signal (for testing)
   */
  refresh: (symbol: string = 'BTCUSDT') =>
    fetchApi<{ message: string; signal: Signal }>(
      `/api/v1/signals/refresh?symbol=${symbol}`,
      { method: 'POST' }
    ),
};

// ============================================================
// Trading API
// ============================================================

export const tradingApi = {
  /**
   * Get account balance
   */
  getBalance: () =>
    fetchApi<Balance>('/api/v1/trading/balance'),

  /**
   * Get current position
   */
  getPosition: () =>
    fetchApi<Position | null>('/api/v1/trading/position'),

  /**
   * Execute a trade
   */
  executeTrade: (request: TradeRequest) =>
    fetchApi<TradeResult>('/api/v1/trading/execute', {
      method: 'POST',
      body: JSON.stringify(request),
    }),

  /**
   * Close current position
   */
  closePosition: () =>
    fetchApi<TradeResult>('/api/v1/trading/close', { method: 'POST' }),

  /**
   * Get trade history
   */
  getHistory: (limit: number = 50) =>
    fetchApi<TradeHistory[]>(`/api/v1/trading/history?limit=${limit}`),

  /**
   * Get trading status
   */
  getStatus: () =>
    fetchApi<{ trading_enabled: boolean; has_position: boolean }>(
      '/api/v1/trading/status'
    ),
};

// ============================================================
// Risk API
// ============================================================

export const riskApi = {
  /**
   * Get risk metrics
   */
  getStatus: () =>
    fetchApi<RiskMetrics>('/api/v1/risk/status'),

  /**
   * Get kill switch status
   */
  getKillSwitch: () =>
    fetchApi<{ active: boolean; reason: string | null }>('/api/v1/risk/kill-switch'),

  /**
   * Reset kill switch
   */
  resetKillSwitch: () =>
    fetchApi<{ message: string; reset: boolean }>(
      '/api/v1/risk/kill-switch/reset',
      { method: 'POST' }
    ),

  /**
   * Get risk alerts
   */
  getAlerts: (limit: number = 10) =>
    fetchApi<Array<{ alert_type: string; message: string; timestamp: string }>>(
      `/api/v1/risk/alerts?limit=${limit}`
    ),

  /**
   * Get portfolio summary
   */
  getPortfolio: () =>
    fetchApi<{
      initial_capital: number;
      current_capital: number;
      peak_capital: number;
      total_pnl: number;
      total_pnl_percent: number;
      current_drawdown: number;
      daily_loss: number;
      position_value: number;
      available_capital: number;
    }>('/api/v1/risk/portfolio'),

  /**
   * Get risk limits configuration
   */
  getLimits: () =>
    fetchApi<{
      max_position_size_percent: number;
      max_total_exposure_percent: number;
      max_drawdown_percent: number;
      daily_loss_limit_percent: number;
      min_confidence_threshold: number;
    }>('/api/v1/risk/limits'),
};

// ============================================================
// System API
// ============================================================

export const systemApi = {
  /**
   * Health check
   */
  healthCheck: () =>
    fetchApi<{
      status: string;
      version: string;
      uptime_seconds: number;
      websocket_clients: number;
      trading_enabled: boolean;
      testnet_mode: boolean;
      timestamp: string;
    }>('/health'),
};

// Export all APIs
export const api = {
  market: marketApi,
  signals: signalsApi,
  trading: tradingApi,
  risk: riskApi,
  system: systemApi,
};

export default api;
