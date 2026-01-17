"""
SURGE-AI Trading Dashboard - Price Service
Handles Binance price data with real-time streaming
"""
import asyncio
from datetime import datetime
from typing import Dict, Optional, Callable, List
import logging
import httpx
from binance import AsyncClient

from config import settings, SUPPORTED_SYMBOLS
from models.schemas import PriceData
from services.currency_service import currency_service

logger = logging.getLogger(__name__)


class PriceService:
    """Service for real-time price data from Binance"""

    def __init__(self):
        self._client: Optional[AsyncClient] = None
        self._prices: Dict[str, PriceData] = {}
        self._subscribers: List[Callable] = []
        self._running = False
        self._price_lock = asyncio.Lock()

    async def initialize(self):
        """Initialize Binance client"""
        try:
            if settings.BINANCE_TESTNET:
                self._client = await AsyncClient.create(
                    api_key=settings.BINANCE_API_KEY,
                    api_secret=settings.BINANCE_API_SECRET,
                    testnet=True
                )
                logger.info("Connected to Binance Testnet")
            else:
                self._client = await AsyncClient.create(
                    api_key=settings.BINANCE_API_KEY,
                    api_secret=settings.BINANCE_API_SECRET
                )
                logger.info("Connected to Binance Mainnet")
        except Exception as e:
            logger.warning(f"Failed to connect to Binance with API: {e}")
            # Create client without API keys for public data
            self._client = await AsyncClient.create()
            logger.info("Connected to Binance (public data only)")

    async def close(self):
        """Close Binance client"""
        if self._client:
            await self._client.close_connection()
            self._client = None

    async def get_price(self, symbol: str = "BTCUSDT") -> PriceData:
        """
        Get current price for a symbol with IDR conversion
        """
        async with self._price_lock:
            # Check cache first
            if symbol in self._prices:
                cached = self._prices[symbol]
                # Return cached if less than 2 seconds old
                if (datetime.now() - cached.timestamp).total_seconds() < 2:
                    return cached

        # Fetch fresh price
        price_data = await self._fetch_price(symbol)

        async with self._price_lock:
            self._prices[symbol] = price_data

        return price_data

    async def _fetch_price(self, symbol: str) -> PriceData:
        """Fetch price from Binance API"""
        try:
            if self._client:
                # Get ticker data
                ticker = await self._client.get_ticker(symbol=symbol)

                price_usd = float(ticker["lastPrice"])
                idr_rate = await currency_service.get_usd_idr_rate()

                return PriceData(
                    symbol=symbol,
                    price_usd=price_usd,
                    price_idr=price_usd * idr_rate,
                    idr_rate=idr_rate,
                    change_24h_percent=float(ticker.get("priceChangePercent", 0)),
                    high_24h=float(ticker.get("highPrice", 0)),
                    low_24h=float(ticker.get("lowPrice", 0)),
                    volume_24h=float(ticker.get("volume", 0)),
                    timestamp=datetime.now()
                )
            else:
                # Fallback to HTTP API
                return await self._fetch_price_http(symbol)

        except Exception as e:
            logger.error(f"Error fetching price for {symbol}: {e}")
            # Return mock data for development
            return await self._get_mock_price(symbol)

    async def _fetch_price_http(self, symbol: str) -> PriceData:
        """Fetch price using HTTP API (fallback)"""
        try:
            base_url = "https://api.binance.com" if not settings.BINANCE_TESTNET else "https://testnet.binance.vision"

            async with httpx.AsyncClient(timeout=10.0) as client:
                response = await client.get(f"{base_url}/api/v3/ticker/24hr", params={"symbol": symbol})

                if response.status_code == 200:
                    ticker = response.json()
                    price_usd = float(ticker["lastPrice"])
                    idr_rate = await currency_service.get_usd_idr_rate()

                    return PriceData(
                        symbol=symbol,
                        price_usd=price_usd,
                        price_idr=price_usd * idr_rate,
                        idr_rate=idr_rate,
                        change_24h_percent=float(ticker.get("priceChangePercent", 0)),
                        high_24h=float(ticker.get("highPrice", 0)),
                        low_24h=float(ticker.get("lowPrice", 0)),
                        volume_24h=float(ticker.get("volume", 0)),
                        timestamp=datetime.now()
                    )
        except Exception as e:
            logger.error(f"HTTP API error for {symbol}: {e}")

        return await self._get_mock_price(symbol)

    async def _get_mock_price(self, symbol: str) -> PriceData:
        """Generate mock price data for development"""
        import random

        mock_prices = {
            "BTCUSDT": 87500.0,
            "ETHUSDT": 3200.0,
            "BNBUSDT": 580.0,
            "SOLUSDT": 185.0,
            "XRPUSDT": 2.5
        }

        base_price = mock_prices.get(symbol, 1000.0)
        # Add small random variation
        price_usd = base_price * (1 + random.uniform(-0.001, 0.001))
        idr_rate = await currency_service.get_usd_idr_rate()

        return PriceData(
            symbol=symbol,
            price_usd=price_usd,
            price_idr=price_usd * idr_rate,
            idr_rate=idr_rate,
            change_24h_percent=random.uniform(-3, 3),
            high_24h=base_price * 1.02,
            low_24h=base_price * 0.98,
            volume_24h=random.uniform(10000, 50000),
            timestamp=datetime.now()
        )

    async def get_all_prices(self) -> Dict[str, PriceData]:
        """Get prices for all supported symbols"""
        prices = {}
        for symbol in SUPPORTED_SYMBOLS:
            prices[symbol] = await self.get_price(symbol)
        return prices

    def subscribe(self, callback: Callable):
        """Subscribe to price updates"""
        self._subscribers.append(callback)

    def unsubscribe(self, callback: Callable):
        """Unsubscribe from price updates"""
        if callback in self._subscribers:
            self._subscribers.remove(callback)

    async def start_streaming(self, symbol: str = "BTCUSDT"):
        """Start streaming prices"""
        self._running = True
        logger.info(f"Starting price stream for {symbol}")

        while self._running:
            try:
                price = await self._fetch_price(symbol)
                async with self._price_lock:
                    self._prices[symbol] = price

                # Notify subscribers
                for callback in self._subscribers:
                    try:
                        if asyncio.iscoroutinefunction(callback):
                            await callback(price)
                        else:
                            callback(price)
                    except Exception as e:
                        logger.error(f"Error in price subscriber: {e}")

                await asyncio.sleep(settings.PRICE_UPDATE_INTERVAL)

            except Exception as e:
                logger.error(f"Error in price stream: {e}")
                await asyncio.sleep(5)  # Wait before retry

    def stop_streaming(self):
        """Stop streaming prices"""
        self._running = False
        logger.info("Stopping price stream")


# Global instance
price_service = PriceService()
