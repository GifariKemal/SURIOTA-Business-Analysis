"""
SURGE-AI Trading Dashboard - Signal Service
Generates trading signals using Kalman filter fusion
"""
import asyncio
from datetime import datetime, timedelta
from typing import Optional, List
import logging
import random
import math

from config import settings
from models.schemas import (
    Signal, SignalDirection, KalmanBreakdown, SignalReasoning,
    TradeRecommendation, TradeAction, SignalHistory
)
from services.price_service import price_service
from services.currency_service import currency_service

logger = logging.getLogger(__name__)


class SignalService:
    """
    Service for generating trading signals.
    In production, this would bridge to the ML engine (kalman_fusion.py).
    For the dashboard MVP, it generates simulated signals.
    """

    def __init__(self):
        self._current_signal: Optional[Signal] = None
        self._signal_history: List[Signal] = []
        self._last_signal_time: Optional[datetime] = None
        self._signal_interval = timedelta(minutes=5)  # Generate new signal every 5 min

    async def get_current_signal(self, symbol: str = "BTCUSDT") -> Signal:
        """
        Get current trading signal.
        In production, this calls kalman_fusion.generate_signal()
        """
        # Check if we need a new signal
        if self._should_generate_new_signal():
            self._current_signal = await self._generate_signal(symbol)
            self._signal_history.append(self._current_signal)
            self._last_signal_time = datetime.now()

        return self._current_signal or await self._generate_signal(symbol)

    def _should_generate_new_signal(self) -> bool:
        """Check if we should generate a new signal"""
        if not self._last_signal_time:
            return True
        return datetime.now() - self._last_signal_time > self._signal_interval

    async def _generate_signal(self, symbol: str) -> Signal:
        """
        Generate trading signal using Kalman filter fusion.

        In production, this would:
        1. Get ML predictions from XGBoost + LSTM
        2. Get pattern matches from Milvus vector DB
        3. Get sentiment from FinGPT-mini
        4. Fuse all signals using Kalman filter

        For MVP, we simulate this with realistic random values.
        """
        # Get current price for context
        price_data = await price_service.get_price(symbol)

        # Generate Kalman component signals (simulated)
        # In production: these come from actual ML models
        kalman_ml = self._simulate_ml_signal(price_data)
        kalman_db = self._simulate_db_signal(price_data)
        kalman_sentiment = self._simulate_sentiment_signal()

        # Enhanced signal (simulated adaptive Kalman)
        kalman_enhanced = self._calculate_enhanced_signal(
            kalman_ml, kalman_db, kalman_sentiment
        )

        # Calculate final fused signal
        final_signal = (
            settings.KALMAN_ML_WEIGHT * kalman_ml +
            settings.KALMAN_DB_WEIGHT * kalman_db +
            settings.KALMAN_SENTIMENT_WEIGHT * kalman_sentiment
        )

        # Determine direction
        if final_signal > 0.55:
            direction = SignalDirection.LONG
        elif final_signal < 0.45:
            direction = SignalDirection.SHORT
        else:
            direction = SignalDirection.NEUTRAL

        # Calculate confidence (0-100%)
        confidence = self._calculate_confidence(final_signal, kalman_enhanced)

        # Generate reasoning
        reasoning = self._generate_reasoning(
            kalman_ml, kalman_db, kalman_sentiment, direction, price_data
        )

        # Check if actionable
        is_actionable = (
            confidence >= settings.MIN_CONFIDENCE_THRESHOLD and
            direction != SignalDirection.NEUTRAL
        )

        return Signal(
            direction=direction,
            confidence=confidence,
            kalman_breakdown=KalmanBreakdown(
                ml_signal=kalman_ml * 100,  # Convert to percentage
                db_signal=kalman_db * 100,
                sentiment_signal=kalman_sentiment * 100,
                enhanced_signal=kalman_enhanced * 100,
                ml_weight=settings.KALMAN_ML_WEIGHT,
                db_weight=settings.KALMAN_DB_WEIGHT,
                sentiment_weight=settings.KALMAN_SENTIMENT_WEIGHT
            ),
            reasoning=reasoning,
            timestamp=datetime.now(),
            is_actionable=is_actionable
        )

    def _simulate_ml_signal(self, price_data) -> float:
        """
        Simulate ML signal from XGBoost + LSTM.
        Returns value between 0 (bearish) and 1 (bullish).
        """
        # Use price change as base indicator
        change = price_data.change_24h_percent / 100

        # Add some randomness to simulate model uncertainty
        noise = random.gauss(0, 0.1)

        # Normalize to 0-1 range with sigmoid-like function
        signal = 0.5 + (change * 2) + noise
        return max(0, min(1, signal))

    def _simulate_db_signal(self, price_data) -> float:
        """
        Simulate pattern matching signal from vector database.
        Returns value between 0 and 1.
        """
        # Simulate historical pattern matching
        base = 0.5 + random.gauss(0, 0.15)
        return max(0, min(1, base))

    def _simulate_sentiment_signal(self) -> float:
        """
        Simulate sentiment analysis signal from FinGPT-mini.
        Returns value between 0 (bearish) and 1 (bullish).
        """
        # Simulate sentiment with slight positive bias (crypto tends bullish)
        base = 0.52 + random.gauss(0, 0.12)
        return max(0, min(1, base))

    def _calculate_enhanced_signal(
        self, ml: float, db: float, sentiment: float
    ) -> float:
        """
        Calculate enhanced signal using adaptive Kalman filtering.
        This simulates the final Kalman filter that fuses all signals.
        """
        # Weighted combination with adaptive weights
        weights = [settings.KALMAN_ML_WEIGHT, settings.KALMAN_DB_WEIGHT, settings.KALMAN_SENTIMENT_WEIGHT]
        signals = [ml, db, sentiment]

        # Calculate agreement score
        mean = sum(signals) / len(signals)
        variance = sum((s - mean) ** 2 for s in signals) / len(signals)

        # Adjust weights based on agreement (lower variance = more confident)
        confidence_boost = max(0, 0.1 - variance * 2)

        # Enhanced signal with slight confidence adjustment
        enhanced = sum(w * s for w, s in zip(weights, signals)) + confidence_boost
        return max(0, min(1, enhanced))

    def _calculate_confidence(self, signal: float, enhanced: float) -> float:
        """
        Calculate confidence percentage (0-100%).
        Higher when signals agree and are strong.
        """
        # Distance from neutral (0.5)
        strength = abs(signal - 0.5) * 2

        # Agreement between signal and enhanced
        agreement = 1 - abs(signal - enhanced)

        # Base confidence
        confidence = (strength * 0.6 + agreement * 0.4) * 100

        # Add some noise
        confidence += random.gauss(0, 5)

        return max(50, min(95, confidence))

    def _generate_reasoning(
        self, ml: float, db: float, sentiment: float,
        direction: SignalDirection, price_data
    ) -> SignalReasoning:
        """Generate human-readable reasoning for the signal"""

        # ML reasoning
        if ml > 0.6:
            ml_reason = "RSI oversold bounce + MACD crossover bullish"
        elif ml < 0.4:
            ml_reason = "RSI overbought + MACD crossover bearish"
        else:
            ml_reason = "Mixed technical indicators, no clear direction"

        # DB reasoning
        similarity = int(db * 100)
        if db > 0.6:
            db_reason = f"{similarity}/100 similar patterns found → +{random.uniform(2, 5):.1f}% avg return"
        elif db < 0.4:
            db_reason = f"{similarity}/100 similar patterns found → -{random.uniform(2, 5):.1f}% avg return"
        else:
            db_reason = f"{similarity}/100 similar patterns → mixed outcomes"

        # Sentiment reasoning
        fear_greed = int(sentiment * 100)
        if sentiment > 0.6:
            sentiment_reason = f"Bullish sentiment (Fear & Greed: {fear_greed})"
        elif sentiment < 0.4:
            sentiment_reason = f"Bearish sentiment (Fear & Greed: {fear_greed})"
        else:
            sentiment_reason = f"Neutral sentiment (Fear & Greed: {fear_greed})"

        # Risk note
        if direction == SignalDirection.LONG:
            risk_note = "Position size: 12.5% (Half Kelly) | Stop Loss: 2%"
        elif direction == SignalDirection.SHORT:
            risk_note = "Position size: 12.5% (Half Kelly) | Stop Loss: 2%"
        else:
            risk_note = "No trade recommended - waiting for clearer signal"

        return SignalReasoning(
            ml_reason=ml_reason,
            db_reason=db_reason,
            sentiment_reason=sentiment_reason,
            risk_note=risk_note
        )

    async def get_trade_recommendation(self, symbol: str = "BTCUSDT") -> TradeRecommendation:
        """
        Get full trade recommendation with exact amounts.
        """
        signal = await self.get_current_signal(symbol)
        price_data = await price_service.get_price(symbol)
        idr_rate = await currency_service.get_usd_idr_rate()

        # Determine action
        if signal.direction == SignalDirection.LONG:
            action = TradeAction.BUY
        elif signal.direction == SignalDirection.SHORT:
            action = TradeAction.SELL
        else:
            action = TradeAction.HOLD

        # Calculate position size (simulated $10,000 portfolio)
        portfolio_value = 10000.0
        position_percent = settings.MAX_POSITION_SIZE_PERCENT / 100
        position_usd = portfolio_value * position_percent

        # Calculate quantities
        quantity_btc = position_usd / price_data.price_usd if price_data.price_usd > 0 else 0

        # Calculate stop loss and take profit
        if action == TradeAction.BUY:
            stop_loss = price_data.price_usd * 0.98  # 2% SL
            take_profit = price_data.price_usd * 1.03  # 3% TP
        elif action == TradeAction.SELL:
            stop_loss = price_data.price_usd * 1.02  # 2% SL
            take_profit = price_data.price_usd * 0.97  # 3% TP
        else:
            stop_loss = price_data.price_usd
            take_profit = price_data.price_usd

        # Generate reasoning list
        reasoning = [
            f"▸ ML: {signal.reasoning.ml_reason}",
            f"▸ DB: {signal.reasoning.db_reason}",
            f"▸ Sentiment: {signal.reasoning.sentiment_reason}",
            f"▸ Risk: {signal.reasoning.risk_note}"
        ]

        # Check if executable
        is_executable = (
            signal.is_actionable and
            action != TradeAction.HOLD and
            signal.confidence >= settings.MIN_CONFIDENCE_THRESHOLD
        )

        blocked_reason = None
        if not is_executable:
            if signal.confidence < settings.MIN_CONFIDENCE_THRESHOLD:
                blocked_reason = f"Confidence {signal.confidence:.1f}% below {settings.MIN_CONFIDENCE_THRESHOLD}% threshold"
            elif action == TradeAction.HOLD:
                blocked_reason = "No clear signal direction"

        return TradeRecommendation(
            action=action,
            symbol=symbol,
            price_usd=price_data.price_usd,
            price_idr=price_data.price_idr,
            quantity_btc=round(quantity_btc, 6),
            quantity_usd=position_usd,
            quantity_idr=position_usd * idr_rate,
            stop_loss_usd=stop_loss,
            stop_loss_idr=stop_loss * idr_rate,
            take_profit_usd=take_profit,
            take_profit_idr=take_profit * idr_rate,
            confidence=signal.confidence,
            signal=signal,
            reasoning=reasoning,
            is_executable=is_executable,
            blocked_reason=blocked_reason
        )

    async def get_signal_history(self, limit: int = 50) -> SignalHistory:
        """Get signal history"""
        signals = self._signal_history[-limit:] if self._signal_history else []
        return SignalHistory(
            signals=list(reversed(signals)),
            total_count=len(self._signal_history)
        )

    def force_new_signal(self):
        """Force generation of a new signal (for testing)"""
        self._last_signal_time = None


# Global instance
signal_service = SignalService()
