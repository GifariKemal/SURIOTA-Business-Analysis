"""
SURGE-AI Trading Dashboard - Configuration
"""
import os
from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """Application settings loaded from environment variables"""

    # Application
    APP_NAME: str = "SURGE-AI Trading Dashboard"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True

    # API Server
    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8000

    # CORS - Allow multiple ports for development
    CORS_ORIGINS: list[str] = [
        "http://localhost:3000",
        "http://localhost:3001",
        "http://localhost:3002",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:3001",
        "http://127.0.0.1:3002",
    ]

    # Binance API
    BINANCE_API_KEY: Optional[str] = None
    BINANCE_API_SECRET: Optional[str] = None
    BINANCE_TESTNET: bool = True  # Use testnet by default for safety

    # Trading Configuration
    TRADING_SYMBOL: str = "BTCUSDT"
    TRADING_ENABLED: bool = False  # Must explicitly enable trading

    # Risk Management
    MAX_POSITION_SIZE_PERCENT: float = 12.5  # Half Kelly
    MAX_TOTAL_EXPOSURE_PERCENT: float = 50.0
    MAX_DRAWDOWN_PERCENT: float = 15.0
    DAILY_LOSS_LIMIT_PERCENT: float = 3.0
    MIN_CONFIDENCE_THRESHOLD: float = 70.0

    # Currency Conversion
    DEFAULT_IDR_RATE: float = 16000.0  # Fallback rate if API fails
    EXCHANGE_RATE_CACHE_TTL: int = 3600  # 1 hour cache

    # WebSocket
    WS_HEARTBEAT_INTERVAL: int = 30
    PRICE_UPDATE_INTERVAL: float = 1.0  # seconds

    # Signal Generation
    KALMAN_ML_WEIGHT: float = 0.50
    KALMAN_DB_WEIGHT: float = 0.30
    KALMAN_SENTIMENT_WEIGHT: float = 0.20

    # Redis (optional)
    REDIS_URL: Optional[str] = None

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"


# Create global settings instance
settings = Settings()


# Trading pairs configuration
SUPPORTED_SYMBOLS = [
    "BTCUSDT",
    "ETHUSDT",
    "BNBUSDT",
    "SOLUSDT",
    "XRPUSDT"
]

# Signal types
class SignalType:
    LONG = "LONG"
    SHORT = "SHORT"
    NEUTRAL = "NEUTRAL"

# Trade actions
class TradeAction:
    BUY = "BUY"
    SELL = "SELL"
    HOLD = "HOLD"

# Activity types
class ActivityType:
    SIGNAL = "signal"
    TRADE = "trade"
    BLOCKED = "blocked"
    ALERT = "alert"
    RISK = "risk"
