"""
SURGE-AI Trading Dashboard - Trading Service
Handles trade execution and position management
"""
import asyncio
from datetime import datetime
from typing import Optional, List
import logging
import uuid

from config import settings
from models.schemas import (
    TradeRequest, TradeResult, Position, Balance,
    TradeHistory, TradeAction
)
from services.price_service import price_service
from services.currency_service import currency_service
from services.risk_service import risk_service

logger = logging.getLogger(__name__)


class TradingService:
    """
    Service for trade execution.
    Supports both simulation mode and live trading (via Binance API).
    """

    def __init__(self):
        # Simulated portfolio
        self._balance_usd = 10000.0
        self._position: Optional[Position] = None
        self._trade_history: List[TradeHistory] = []

        # Trading state
        self._is_trading_enabled = False
        self._lock = asyncio.Lock()

    async def initialize(self):
        """Initialize trading service"""
        # Sync capital with risk service
        await risk_service.set_capital(self._balance_usd)
        logger.info(f"Trading service initialized with ${self._balance_usd:,.2f}")

    async def get_balance(self) -> Balance:
        """Get current account balance"""
        idr_rate = await currency_service.get_usd_idr_rate()

        async with self._lock:
            position_value = 0.0
            if self._position:
                position_value = self._position.quantity * self._position.current_price

            available = self._balance_usd - position_value

            return Balance(
                total_usd=self._balance_usd,
                total_idr=self._balance_usd * idr_rate,
                available_usd=available,
                available_idr=available * idr_rate,
                in_position_usd=position_value,
                in_position_idr=position_value * idr_rate,
                timestamp=datetime.now()
            )

    async def get_position(self) -> Optional[Position]:
        """Get current trading position"""
        async with self._lock:
            if not self._position:
                return None

            # Update with current price
            price_data = await price_service.get_price(self._position.symbol)
            idr_rate = await currency_service.get_usd_idr_rate()

            # Calculate unrealized PnL
            if self._position.side == "LONG":
                pnl_usd = (price_data.price_usd - self._position.entry_price) * self._position.quantity
            else:
                pnl_usd = (self._position.entry_price - price_data.price_usd) * self._position.quantity

            pnl_percent = (pnl_usd / (self._position.entry_price * self._position.quantity)) * 100

            self._position.current_price = price_data.price_usd
            self._position.current_price_idr = price_data.price_idr
            self._position.unrealized_pnl_usd = pnl_usd
            self._position.unrealized_pnl_idr = pnl_usd * idr_rate
            self._position.unrealized_pnl_percent = pnl_percent
            self._position.timestamp = datetime.now()

            return self._position

    async def execute_trade(self, request: TradeRequest) -> TradeResult:
        """
        Execute a trade.
        For MVP, this simulates the trade. In production, uses Binance API.
        """
        async with self._lock:
            # Get current price
            price_data = await price_service.get_price(request.symbol)
            idr_rate = await currency_service.get_usd_idr_rate()

            # Calculate trade value
            trade_value = request.quantity * price_data.price_usd

            # Check risk limits
            allowed, reason = await risk_service.check_trade_allowed(trade_value)
            if not allowed:
                return TradeResult(
                    success=False,
                    action=request.action,
                    symbol=request.symbol,
                    quantity=request.quantity,
                    price=price_data.price_usd,
                    price_idr=price_data.price_idr,
                    total_value_usd=trade_value,
                    total_value_idr=trade_value * idr_rate,
                    error=reason
                )

            # Check if we have an existing position
            if self._position:
                # Close existing position first if different direction
                if (request.action == TradeAction.BUY and self._position.side == "SHORT") or \
                   (request.action == TradeAction.SELL and self._position.side == "LONG"):
                    await self._close_position_internal(price_data.price_usd)

            # Execute the trade
            trade_id = str(uuid.uuid4())[:8]

            if request.action == TradeAction.BUY:
                # Check available balance
                if trade_value > self._balance_usd:
                    return TradeResult(
                        success=False,
                        action=request.action,
                        symbol=request.symbol,
                        quantity=request.quantity,
                        price=price_data.price_usd,
                        price_idr=price_data.price_idr,
                        total_value_usd=trade_value,
                        total_value_idr=trade_value * idr_rate,
                        error=f"Insufficient balance: ${self._balance_usd:,.2f} < ${trade_value:,.2f}"
                    )

                # Create long position
                self._position = Position(
                    symbol=request.symbol,
                    side="LONG",
                    quantity=request.quantity,
                    entry_price=price_data.price_usd,
                    entry_price_idr=price_data.price_idr,
                    current_price=price_data.price_usd,
                    current_price_idr=price_data.price_idr,
                    unrealized_pnl_usd=0,
                    unrealized_pnl_idr=0,
                    unrealized_pnl_percent=0,
                    stop_loss=request.stop_loss,
                    take_profit=request.take_profit
                )

                logger.info(f"Opened LONG position: {request.quantity} {request.symbol} @ ${price_data.price_usd:,.2f}")

            elif request.action == TradeAction.SELL:
                if self._position and self._position.side == "LONG":
                    # Close long position
                    result = await self._close_position_internal(price_data.price_usd)
                    return result
                else:
                    # Open short position (if enabled)
                    self._position = Position(
                        symbol=request.symbol,
                        side="SHORT",
                        quantity=request.quantity,
                        entry_price=price_data.price_usd,
                        entry_price_idr=price_data.price_idr,
                        current_price=price_data.price_usd,
                        current_price_idr=price_data.price_idr,
                        unrealized_pnl_usd=0,
                        unrealized_pnl_idr=0,
                        unrealized_pnl_percent=0,
                        stop_loss=request.stop_loss,
                        take_profit=request.take_profit
                    )
                    logger.info(f"Opened SHORT position: {request.quantity} {request.symbol} @ ${price_data.price_usd:,.2f}")

            # Update risk service
            await risk_service.update_position(self._position)

            # Record trade in history
            self._trade_history.append(TradeHistory(
                trade_id=trade_id,
                action=request.action,
                symbol=request.symbol,
                quantity=request.quantity,
                entry_price=price_data.price_usd,
                timestamp=datetime.now(),
                status="open"
            ))

            return TradeResult(
                success=True,
                trade_id=trade_id,
                action=request.action,
                symbol=request.symbol,
                quantity=request.quantity,
                price=price_data.price_usd,
                price_idr=price_data.price_idr,
                total_value_usd=trade_value,
                total_value_idr=trade_value * idr_rate
            )

    async def _close_position_internal(self, exit_price: float) -> TradeResult:
        """Internal method to close position"""
        if not self._position:
            return TradeResult(
                success=False,
                action=TradeAction.SELL,
                symbol="BTCUSDT",
                quantity=0,
                price=exit_price,
                price_idr=0,
                total_value_usd=0,
                total_value_idr=0,
                error="No position to close"
            )

        idr_rate = await currency_service.get_usd_idr_rate()

        # Calculate PnL
        if self._position.side == "LONG":
            pnl = (exit_price - self._position.entry_price) * self._position.quantity
        else:
            pnl = (self._position.entry_price - exit_price) * self._position.quantity

        pnl_percent = (pnl / (self._position.entry_price * self._position.quantity)) * 100

        # Update balance
        self._balance_usd += pnl

        # Record PnL with risk service
        await risk_service.record_trade_result(pnl, pnl_percent)

        # Update trade history
        for trade in reversed(self._trade_history):
            if trade.status == "open" and trade.symbol == self._position.symbol:
                trade.exit_price = exit_price
                trade.pnl_usd = pnl
                trade.pnl_percent = pnl_percent
                trade.closed_at = datetime.now()
                trade.status = "closed"
                break

        trade_value = self._position.quantity * exit_price
        symbol = self._position.symbol
        quantity = self._position.quantity

        logger.info(f"Closed position: {quantity} {symbol} @ ${exit_price:,.2f}, PnL: ${pnl:,.2f} ({pnl_percent:+.1f}%)")

        # Clear position
        self._position = None
        await risk_service.update_position(None)

        return TradeResult(
            success=True,
            trade_id=str(uuid.uuid4())[:8],
            action=TradeAction.SELL,
            symbol=symbol,
            quantity=quantity,
            price=exit_price,
            price_idr=exit_price * idr_rate,
            total_value_usd=trade_value,
            total_value_idr=trade_value * idr_rate
        )

    async def close_position(self) -> TradeResult:
        """Close current position at market price"""
        async with self._lock:
            if not self._position:
                idr_rate = await currency_service.get_usd_idr_rate()
                return TradeResult(
                    success=False,
                    action=TradeAction.SELL,
                    symbol="BTCUSDT",
                    quantity=0,
                    price=0,
                    price_idr=0,
                    total_value_usd=0,
                    total_value_idr=0,
                    error="No position to close"
                )

            price_data = await price_service.get_price(self._position.symbol)
            return await self._close_position_internal(price_data.price_usd)

    async def get_trade_history(self, limit: int = 50) -> List[TradeHistory]:
        """Get trade history"""
        return list(reversed(self._trade_history[-limit:]))

    def enable_trading(self, enabled: bool = True):
        """Enable or disable trading"""
        self._is_trading_enabled = enabled
        logger.info(f"Trading {'enabled' if enabled else 'disabled'}")

    def is_trading_enabled(self) -> bool:
        """Check if trading is enabled"""
        return self._is_trading_enabled


# Global instance
trading_service = TradingService()
