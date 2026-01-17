"""
SURGE-AI Trading Dashboard - Pydantic Schemas
"""
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
from enum import Enum


# ============================================================
# Enums
# ============================================================

class SignalDirection(str, Enum):
    LONG = "LONG"
    SHORT = "SHORT"
    NEUTRAL = "NEUTRAL"


class TradeAction(str, Enum):
    BUY = "BUY"
    SELL = "SELL"
    HOLD = "HOLD"


class ActivityType(str, Enum):
    SIGNAL = "signal"
    TRADE = "trade"
    BLOCKED = "blocked"
    ALERT = "alert"
    RISK = "risk"


# ============================================================
# Market Data Schemas
# ============================================================

class PriceData(BaseModel):
    """Real-time price data with IDR conversion"""
    symbol: str
    price_usd: float
    price_idr: float
    idr_rate: float
    change_24h_percent: float = 0.0
    high_24h: float = 0.0
    low_24h: float = 0.0
    volume_24h: float = 0.0
    timestamp: datetime = Field(default_factory=datetime.now)


class ExchangeRate(BaseModel):
    """USD to IDR exchange rate"""
    usd_idr: float
    last_updated: datetime
    source: str = "api"


class TickerData(BaseModel):
    """Multiple price ticker data"""
    prices: List[PriceData]
    timestamp: datetime = Field(default_factory=datetime.now)


# ============================================================
# Signal Schemas
# ============================================================

class KalmanBreakdown(BaseModel):
    """Kalman filter component breakdown"""
    ml_signal: float = Field(description="ML-based signal (XGBoost + LSTM)")
    db_signal: float = Field(description="Database pattern matching signal")
    sentiment_signal: float = Field(description="Sentiment analysis signal")
    enhanced_signal: float = Field(description="Enhanced fusion signal")
    ml_weight: float = 0.50
    db_weight: float = 0.30
    sentiment_weight: float = 0.20


class SignalReasoning(BaseModel):
    """AI reasoning for signal generation"""
    ml_reason: str = ""
    db_reason: str = ""
    sentiment_reason: str = ""
    risk_note: str = ""


class Signal(BaseModel):
    """Trading signal with confidence and reasoning"""
    direction: SignalDirection
    confidence: float = Field(ge=0, le=100, description="Signal confidence 0-100%")
    kalman_breakdown: KalmanBreakdown
    reasoning: SignalReasoning
    timestamp: datetime = Field(default_factory=datetime.now)
    is_actionable: bool = True


class SignalHistory(BaseModel):
    """Historical signal data"""
    signals: List[Signal]
    total_count: int


# ============================================================
# Trading Schemas
# ============================================================

class TradeRecommendation(BaseModel):
    """Trade recommendation with exact amounts"""
    action: TradeAction
    symbol: str
    price_usd: float
    price_idr: float
    quantity_btc: float
    quantity_usd: float
    quantity_idr: float
    stop_loss_usd: float
    stop_loss_idr: float
    take_profit_usd: float
    take_profit_idr: float
    confidence: float
    signal: Signal
    reasoning: List[str]
    is_executable: bool = True
    blocked_reason: Optional[str] = None


class TradeRequest(BaseModel):
    """Request to execute a trade"""
    action: TradeAction
    symbol: str
    quantity: float
    stop_loss: Optional[float] = None
    take_profit: Optional[float] = None


class TradeResult(BaseModel):
    """Result of trade execution"""
    success: bool
    trade_id: Optional[str] = None
    action: TradeAction
    symbol: str
    quantity: float
    price: float
    price_idr: float
    total_value_usd: float
    total_value_idr: float
    timestamp: datetime = Field(default_factory=datetime.now)
    error: Optional[str] = None


class Position(BaseModel):
    """Current trading position"""
    symbol: str
    side: str  # LONG or SHORT
    quantity: float
    entry_price: float
    entry_price_idr: float
    current_price: float
    current_price_idr: float
    unrealized_pnl_usd: float
    unrealized_pnl_idr: float
    unrealized_pnl_percent: float
    stop_loss: Optional[float] = None
    take_profit: Optional[float] = None
    timestamp: datetime = Field(default_factory=datetime.now)


class Balance(BaseModel):
    """Account balance"""
    total_usd: float
    total_idr: float
    available_usd: float
    available_idr: float
    in_position_usd: float
    in_position_idr: float
    timestamp: datetime = Field(default_factory=datetime.now)


class TradeHistory(BaseModel):
    """Trade history item"""
    trade_id: str
    action: TradeAction
    symbol: str
    quantity: float
    entry_price: float
    exit_price: Optional[float] = None
    pnl_usd: float = 0.0
    pnl_percent: float = 0.0
    timestamp: datetime
    closed_at: Optional[datetime] = None
    status: str = "open"  # open, closed, cancelled


# ============================================================
# Risk Management Schemas
# ============================================================

class RiskMetrics(BaseModel):
    """Current risk metrics"""
    current_drawdown_percent: float
    max_drawdown_percent: float
    daily_loss_percent: float
    daily_loss_limit_percent: float
    current_exposure_percent: float
    max_exposure_percent: float
    position_size_percent: float
    max_position_size_percent: float
    kill_switch_active: bool = False
    kill_switch_reason: Optional[str] = None
    timestamp: datetime = Field(default_factory=datetime.now)


class RiskAlert(BaseModel):
    """Risk management alert"""
    alert_type: str  # warning, critical, kill_switch
    message: str
    metric: str
    current_value: float
    threshold: float
    timestamp: datetime = Field(default_factory=datetime.now)


# ============================================================
# Activity Feed Schemas
# ============================================================

class ActivityItem(BaseModel):
    """Activity feed item"""
    id: str
    type: ActivityType
    timestamp: datetime
    title: str
    description: str
    signal: Optional[Signal] = None
    trade: Optional[TradeResult] = None
    recommendation: Optional[TradeRecommendation] = None
    details: List[str] = []
    is_expanded: bool = False


class ActivityFeed(BaseModel):
    """Activity feed with multiple items"""
    activities: List[ActivityItem]
    total_count: int


# ============================================================
# Performance Schemas
# ============================================================

class PerformanceMetrics(BaseModel):
    """Trading performance metrics"""
    total_trades: int
    winning_trades: int
    losing_trades: int
    win_rate: float
    total_pnl_usd: float
    total_pnl_idr: float
    total_pnl_percent: float
    daily_pnl_usd: float
    daily_pnl_idr: float
    daily_pnl_percent: float
    best_trade_pnl_percent: float
    worst_trade_pnl_percent: float
    avg_trade_pnl_percent: float
    sharpe_ratio: float = 0.0
    timestamp: datetime = Field(default_factory=datetime.now)


class EquityPoint(BaseModel):
    """Point on equity curve"""
    timestamp: datetime
    equity_usd: float
    equity_idr: float
    pnl_percent: float


class EquityCurve(BaseModel):
    """Equity curve data"""
    points: List[EquityPoint]
    period: str = "30d"


# ============================================================
# WebSocket Schemas
# ============================================================

class WSMessage(BaseModel):
    """WebSocket message format"""
    event: str
    data: dict
    timestamp: datetime = Field(default_factory=datetime.now)


class WSSubscription(BaseModel):
    """WebSocket subscription request"""
    channel: str
    symbol: Optional[str] = None


# ============================================================
# System Schemas
# ============================================================

class HealthCheck(BaseModel):
    """System health check"""
    status: str  # healthy, degraded, unhealthy
    version: str
    uptime_seconds: float
    binance_connected: bool
    websocket_clients: int
    timestamp: datetime = Field(default_factory=datetime.now)


class SystemConfig(BaseModel):
    """System configuration (safe to expose)"""
    trading_symbol: str
    trading_enabled: bool
    testnet_mode: bool
    max_position_size_percent: float
    max_drawdown_percent: float
    daily_loss_limit_percent: float
    min_confidence_threshold: float
    kalman_weights: KalmanBreakdown


# ============================================================
# Dashboard Summary Schemas
# ============================================================

class DashboardSummary(BaseModel):
    """Complete dashboard summary"""
    price: PriceData
    signal: Signal
    recommendation: Optional[TradeRecommendation]
    position: Optional[Position]
    balance: Balance
    risk: RiskMetrics
    performance: PerformanceMetrics
    recent_activities: List[ActivityItem]
    timestamp: datetime = Field(default_factory=datetime.now)
