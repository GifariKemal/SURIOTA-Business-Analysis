"""
SURGE-AI Trading Dashboard - API
"""
from fastapi import APIRouter

from .routes import market, signals, trading, risk

# Create main API router
api_router = APIRouter(prefix="/api/v1")

# Include route modules
api_router.include_router(market.router, prefix="/market", tags=["Market"])
api_router.include_router(signals.router, prefix="/signals", tags=["Signals"])
api_router.include_router(trading.router, prefix="/trading", tags=["Trading"])
api_router.include_router(risk.router, prefix="/risk", tags=["Risk"])
