/**
 * SURGE-AI Trading Dashboard - TypeScript Types
 */

// ============================================================
// Enums
// ============================================================

export type SignalDirection = 'LONG' | 'SHORT' | 'NEUTRAL';
export type TradeAction = 'BUY' | 'SELL' | 'HOLD';
export type ActivityType = 'signal' | 'trade' | 'blocked' | 'alert' | 'risk';

// ============================================================
// Market Data Types
// ============================================================

export interface PriceData {
  symbol: string;
  price_usd: number;
  price_idr: number;
  idr_rate: number;
  change_24h_percent: number;
  high_24h: number;
  low_24h: number;
  volume_24h: number;
  timestamp: string;
}

export interface ExchangeRate {
  usd_idr: number;
  last_updated: string;
  source: string;
  formatted: string;
}

// ============================================================
// Signal Types
// ============================================================

export interface KalmanBreakdown {
  ml_signal: number;
  db_signal: number;
  sentiment_signal: number;
  enhanced_signal: number;
  ml_weight: number;
  db_weight: number;
  sentiment_weight: number;
}

export interface SignalReasoning {
  ml_reason: string;
  db_reason: string;
  sentiment_reason: string;
  risk_note: string;
}

export interface Signal {
  direction: SignalDirection;
  confidence: number;
  kalman_breakdown: KalmanBreakdown;
  reasoning: SignalReasoning;
  timestamp: string;
  is_actionable: boolean;
}

// ============================================================
// Trading Types
// ============================================================

export interface TradeRecommendation {
  action: TradeAction;
  symbol: string;
  price_usd: number;
  price_idr: number;
  quantity_btc: number;
  quantity_usd: number;
  quantity_idr: number;
  stop_loss_usd: number;
  stop_loss_idr: number;
  take_profit_usd: number;
  take_profit_idr: number;
  confidence: number;
  signal: Signal;
  reasoning: string[];
  is_executable: boolean;
  blocked_reason?: string;
}

export interface TradeRequest {
  action: TradeAction;
  symbol: string;
  quantity: number;
  stop_loss?: number;
  take_profit?: number;
}

export interface TradeResult {
  success: boolean;
  trade_id?: string;
  action: TradeAction;
  symbol: string;
  quantity: number;
  price: number;
  price_idr: number;
  total_value_usd: number;
  total_value_idr: number;
  timestamp: string;
  error?: string;
}

export interface Position {
  symbol: string;
  side: 'LONG' | 'SHORT';
  quantity: number;
  entry_price: number;
  entry_price_idr: number;
  current_price: number;
  current_price_idr: number;
  unrealized_pnl_usd: number;
  unrealized_pnl_idr: number;
  unrealized_pnl_percent: number;
  stop_loss?: number;
  take_profit?: number;
  timestamp: string;
}

export interface Balance {
  total_usd: number;
  total_idr: number;
  available_usd: number;
  available_idr: number;
  in_position_usd: number;
  in_position_idr: number;
  timestamp: string;
}

export interface TradeHistory {
  trade_id: string;
  action: TradeAction;
  symbol: string;
  quantity: number;
  entry_price: number;
  exit_price?: number;
  pnl_usd: number;
  pnl_percent: number;
  timestamp: string;
  closed_at?: string;
  status: 'open' | 'closed' | 'cancelled';
}

// ============================================================
// Risk Types
// ============================================================

export interface RiskMetrics {
  current_drawdown_percent: number;
  max_drawdown_percent: number;
  daily_loss_percent: number;
  daily_loss_limit_percent: number;
  current_exposure_percent: number;
  max_exposure_percent: number;
  position_size_percent: number;
  max_position_size_percent: number;
  kill_switch_active: boolean;
  kill_switch_reason?: string;
  timestamp: string;
}

export interface RiskAlert {
  alert_type: 'warning' | 'critical' | 'kill_switch';
  message: string;
  metric: string;
  current_value: number;
  threshold: number;
  timestamp: string;
}

// ============================================================
// Activity Feed Types
// ============================================================

export interface ActivityItem {
  id: string;
  type: ActivityType;
  timestamp: string;
  title: string;
  description: string;
  signal?: Signal;
  trade?: TradeResult;
  recommendation?: TradeRecommendation;
  details: string[];
  is_expanded: boolean;
}

// ============================================================
// Performance Types
// ============================================================

export interface PerformanceMetrics {
  total_trades: number;
  winning_trades: number;
  losing_trades: number;
  win_rate: number;
  total_pnl_usd: number;
  total_pnl_idr: number;
  total_pnl_percent: number;
  daily_pnl_usd: number;
  daily_pnl_idr: number;
  daily_pnl_percent: number;
  best_trade_pnl_percent: number;
  worst_trade_pnl_percent: number;
  avg_trade_pnl_percent: number;
  sharpe_ratio: number;
  timestamp: string;
}

export interface EquityPoint {
  timestamp: string;
  equity_usd: number;
  equity_idr: number;
  pnl_percent: number;
}

// ============================================================
// WebSocket Types
// ============================================================

export interface WSMessage {
  event: string;
  data: unknown;
  timestamp: string;
}

export type WSEventType =
  | 'price_update'
  | 'signal_update'
  | 'recommendation_update'
  | 'risk_update'
  | 'position_update'
  | 'balance_update'
  | 'trade_executed'
  | 'error';

// ============================================================
// Dashboard State Types
// ============================================================

export interface DashboardState {
  // Connection status
  isConnected: boolean;
  lastUpdate: string | null;

  // Market data
  price: PriceData | null;
  idrRate: number;

  // Signals
  signal: Signal | null;
  recommendation: TradeRecommendation | null;

  // Trading
  position: Position | null;
  balance: Balance | null;

  // Risk
  risk: RiskMetrics | null;

  // Activity
  activities: ActivityItem[];

  // Performance
  performance: PerformanceMetrics | null;
  equityCurve: EquityPoint[];

  // UI State
  isLoading: boolean;
  error: string | null;
}
