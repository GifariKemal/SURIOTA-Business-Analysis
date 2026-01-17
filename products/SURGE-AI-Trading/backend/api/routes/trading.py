"""
SURGE-AI Trading Dashboard - Trading API Routes
"""
from fastapi import APIRouter, HTTPException
from typing import List, Optional

from models.schemas import (
    TradeRequest, TradeResult, Position, Balance, TradeHistory
)
from services.trading_service import trading_service

router = APIRouter()


@router.get("/balance", response_model=Balance)
async def get_balance():
    """
    Get current account balance.

    Returns:
    - **total_usd/idr**: Total account value
    - **available_usd/idr**: Available for trading
    - **in_position_usd/idr**: Currently in positions
    """
    try:
        balance = await trading_service.get_balance()
        return balance
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/position", response_model=Optional[Position])
async def get_position():
    """
    Get current trading position.

    Returns position details including:
    - Entry price
    - Current price
    - Unrealized PnL
    - Stop loss / Take profit levels
    """
    try:
        position = await trading_service.get_position()
        return position
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/execute", response_model=TradeResult)
async def execute_trade(request: TradeRequest):
    """
    Execute a trade (1-click execution).

    Request body:
    - **action**: BUY or SELL
    - **symbol**: Trading pair (e.g., BTCUSDT)
    - **quantity**: Amount to trade
    - **stop_loss**: Optional stop loss price
    - **take_profit**: Optional take profit price

    Returns trade result with:
    - Success/failure status
    - Executed price
    - Trade value in USD and IDR
    """
    try:
        result = await trading_service.execute_trade(request)
        if not result.success:
            raise HTTPException(status_code=400, detail=result.error)
        return result
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/close", response_model=TradeResult)
async def close_position():
    """
    Close current position at market price.
    """
    try:
        result = await trading_service.close_position()
        if not result.success:
            raise HTTPException(status_code=400, detail=result.error)
        return result
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/history", response_model=List[TradeHistory])
async def get_trade_history(limit: int = 50):
    """
    Get trade history.

    - **limit**: Maximum number of trades to return
    """
    try:
        history = await trading_service.get_trade_history(limit)
        return history
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/status")
async def get_trading_status():
    """
    Get trading system status.
    """
    return {
        "trading_enabled": trading_service.is_trading_enabled(),
        "has_position": (await trading_service.get_position()) is not None
    }
