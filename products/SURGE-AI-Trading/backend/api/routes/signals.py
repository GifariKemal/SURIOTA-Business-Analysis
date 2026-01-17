"""
SURGE-AI Trading Dashboard - Signals API Routes
"""
from fastapi import APIRouter, HTTPException, Query

from config import SUPPORTED_SYMBOLS
from models.schemas import Signal, TradeRecommendation, SignalHistory, KalmanBreakdown
from services.signal_service import signal_service

router = APIRouter()


@router.get("/current", response_model=Signal)
async def get_current_signal(symbol: str = Query("BTCUSDT", description="Trading symbol")):
    """
    Get current trading signal with Kalman breakdown.

    Returns:
    - **direction**: LONG, SHORT, or NEUTRAL
    - **confidence**: Signal confidence (0-100%)
    - **kalman_breakdown**: Individual Kalman component values
    - **reasoning**: AI reasoning for the signal
    """
    symbol = symbol.upper()
    if symbol not in SUPPORTED_SYMBOLS:
        raise HTTPException(
            status_code=400,
            detail=f"Symbol {symbol} not supported"
        )

    try:
        signal = await signal_service.get_current_signal(symbol)
        return signal
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/recommendation", response_model=TradeRecommendation)
async def get_trade_recommendation(symbol: str = Query("BTCUSDT", description="Trading symbol")):
    """
    Get full trade recommendation with exact amounts.

    Returns complete recommendation including:
    - **action**: BUY, SELL, or HOLD
    - **price_usd**: Current price in USD
    - **price_idr**: Current price in IDR
    - **quantity_btc**: Recommended quantity to trade
    - **quantity_usd/idr**: Trade value in both currencies
    - **stop_loss**: Recommended stop loss price
    - **take_profit**: Recommended take profit price
    - **reasoning**: List of AI reasoning points
    """
    symbol = symbol.upper()
    if symbol not in SUPPORTED_SYMBOLS:
        raise HTTPException(
            status_code=400,
            detail=f"Symbol {symbol} not supported"
        )

    try:
        recommendation = await signal_service.get_trade_recommendation(symbol)
        return recommendation
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/history", response_model=SignalHistory)
async def get_signal_history(limit: int = Query(50, ge=1, le=100, description="Max signals to return")):
    """
    Get signal history.

    - **limit**: Maximum number of signals to return (1-100)
    """
    try:
        history = await signal_service.get_signal_history(limit)
        return history
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/components", response_model=KalmanBreakdown)
async def get_signal_components(symbol: str = Query("BTCUSDT", description="Trading symbol")):
    """
    Get Kalman filter component breakdown.

    Returns individual signal values from:
    - **ml_signal**: Machine Learning model (XGBoost + LSTM)
    - **db_signal**: Database pattern matching (Milvus)
    - **sentiment_signal**: Sentiment analysis (FinGPT-mini)
    - **enhanced_signal**: Enhanced fusion signal
    """
    symbol = symbol.upper()
    if symbol not in SUPPORTED_SYMBOLS:
        raise HTTPException(
            status_code=400,
            detail=f"Symbol {symbol} not supported"
        )

    try:
        signal = await signal_service.get_current_signal(symbol)
        return signal.kalman_breakdown
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/refresh")
async def refresh_signal(symbol: str = Query("BTCUSDT", description="Trading symbol")):
    """
    Force generation of a new signal (for testing).
    """
    symbol = symbol.upper()
    if symbol not in SUPPORTED_SYMBOLS:
        raise HTTPException(
            status_code=400,
            detail=f"Symbol {symbol} not supported"
        )

    try:
        signal_service.force_new_signal()
        signal = await signal_service.get_current_signal(symbol)
        return {"message": "Signal refreshed", "signal": signal}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
