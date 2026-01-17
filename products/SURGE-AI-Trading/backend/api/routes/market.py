"""
SURGE-AI Trading Dashboard - Market Data API Routes
"""
from fastapi import APIRouter, HTTPException
from typing import List

from config import SUPPORTED_SYMBOLS
from models.schemas import PriceData, ExchangeRate, TickerData
from services.price_service import price_service
from services.currency_service import currency_service

router = APIRouter()


@router.get("/price/{symbol}", response_model=PriceData)
async def get_price(symbol: str = "BTCUSDT"):
    """
    Get current price for a symbol with IDR conversion.

    - **symbol**: Trading pair symbol (e.g., BTCUSDT, ETHUSDT)
    """
    symbol = symbol.upper()
    if symbol not in SUPPORTED_SYMBOLS:
        raise HTTPException(
            status_code=400,
            detail=f"Symbol {symbol} not supported. Supported: {SUPPORTED_SYMBOLS}"
        )

    try:
        price_data = await price_service.get_price(symbol)
        return price_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/ticker", response_model=TickerData)
async def get_ticker():
    """
    Get current prices for all supported symbols.
    """
    try:
        prices = await price_service.get_all_prices()
        return TickerData(prices=list(prices.values()))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/exchange-rate", response_model=dict)
async def get_exchange_rate():
    """
    Get current USD to IDR exchange rate.
    """
    try:
        rate_info = await currency_service.get_rate_info()
        return rate_info
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/symbols", response_model=List[str])
async def get_supported_symbols():
    """
    Get list of supported trading symbols.
    """
    return SUPPORTED_SYMBOLS
