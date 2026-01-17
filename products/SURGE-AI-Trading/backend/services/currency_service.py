"""
SURGE-AI Trading Dashboard - Currency Service
Handles USD to IDR conversion with caching
"""
import asyncio
from datetime import datetime, timedelta
from typing import Optional
import httpx
import logging

from config import settings

logger = logging.getLogger(__name__)


class CurrencyService:
    """Service for currency conversion with caching"""

    def __init__(self):
        self._cached_rate: Optional[float] = None
        self._cache_time: Optional[datetime] = None
        self._cache_ttl = timedelta(seconds=settings.EXCHANGE_RATE_CACHE_TTL)
        self._lock = asyncio.Lock()

    async def get_usd_idr_rate(self) -> float:
        """
        Get current USD to IDR exchange rate.
        Uses caching to reduce API calls.
        """
        async with self._lock:
            # Check cache validity
            if self._cached_rate and self._cache_time:
                if datetime.now() - self._cache_time < self._cache_ttl:
                    return self._cached_rate

            # Fetch new rate
            rate = await self._fetch_exchange_rate()
            self._cached_rate = rate
            self._cache_time = datetime.now()
            return rate

    async def _fetch_exchange_rate(self) -> float:
        """Fetch exchange rate from API"""
        try:
            # Try exchangerate-api.com (free tier)
            async with httpx.AsyncClient(timeout=10.0) as client:
                response = await client.get(
                    "https://api.exchangerate-api.com/v4/latest/USD"
                )
                if response.status_code == 200:
                    data = response.json()
                    rate = data.get("rates", {}).get("IDR", settings.DEFAULT_IDR_RATE)
                    logger.info(f"Fetched exchange rate: 1 USD = {rate:,.0f} IDR")
                    return rate

        except Exception as e:
            logger.warning(f"Failed to fetch exchange rate from primary API: {e}")

        try:
            # Fallback to alternative API
            async with httpx.AsyncClient(timeout=10.0) as client:
                response = await client.get(
                    "https://open.er-api.com/v6/latest/USD"
                )
                if response.status_code == 200:
                    data = response.json()
                    rate = data.get("rates", {}).get("IDR", settings.DEFAULT_IDR_RATE)
                    logger.info(f"Fetched exchange rate (fallback): 1 USD = {rate:,.0f} IDR")
                    return rate

        except Exception as e:
            logger.warning(f"Failed to fetch exchange rate from fallback API: {e}")

        # Return default rate
        logger.warning(f"Using default exchange rate: 1 USD = {settings.DEFAULT_IDR_RATE:,.0f} IDR")
        return settings.DEFAULT_IDR_RATE

    def convert_usd_to_idr(self, usd_amount: float, rate: float) -> float:
        """Convert USD amount to IDR"""
        return usd_amount * rate

    def convert_idr_to_usd(self, idr_amount: float, rate: float) -> float:
        """Convert IDR amount to USD"""
        if rate == 0:
            return 0
        return idr_amount / rate

    def format_idr(self, amount: float) -> str:
        """Format IDR amount with thousand separators"""
        return f"Rp {amount:,.0f}"

    def format_usd(self, amount: float) -> str:
        """Format USD amount"""
        return f"${amount:,.2f}"

    async def get_rate_info(self) -> dict:
        """Get exchange rate with metadata"""
        rate = await self.get_usd_idr_rate()
        return {
            "usd_idr": rate,
            "last_updated": self._cache_time.isoformat() if self._cache_time else None,
            "source": "exchangerate-api.com",
            "formatted": f"1 USD = Rp {rate:,.0f}"
        }


# Global instance
currency_service = CurrencyService()
