"""
SURGE-AI Trading Dashboard - Risk Service
Handles risk management, drawdown tracking, and kill switch
"""
import asyncio
from datetime import datetime, date
from typing import Optional, List
import logging

from config import settings
from models.schemas import RiskMetrics, RiskAlert, Position

logger = logging.getLogger(__name__)


class RiskService:
    """
    Service for risk management.
    Tracks drawdown, daily losses, and manages kill switch.
    """

    def __init__(self):
        # Portfolio tracking
        self._initial_capital = 10000.0  # Starting capital
        self._current_capital = 10000.0
        self._peak_capital = 10000.0  # Highest capital reached
        self._daily_starting_capital = 10000.0

        # Position tracking
        self._current_position: Optional[Position] = None
        self._position_value = 0.0

        # Risk metrics
        self._current_drawdown = 0.0
        self._daily_loss = 0.0
        self._current_date = date.today()

        # Kill switch
        self._kill_switch_active = False
        self._kill_switch_reason: Optional[str] = None
        self._alerts: List[RiskAlert] = []

        # Lock for thread safety
        self._lock = asyncio.Lock()

    async def get_risk_metrics(self) -> RiskMetrics:
        """Get current risk metrics"""
        async with self._lock:
            # Check for day rollover
            self._check_day_rollover()

            # Calculate metrics
            exposure_percent = (self._position_value / self._current_capital * 100) if self._current_capital > 0 else 0

            return RiskMetrics(
                current_drawdown_percent=self._current_drawdown,
                max_drawdown_percent=settings.MAX_DRAWDOWN_PERCENT,
                daily_loss_percent=self._daily_loss,
                daily_loss_limit_percent=settings.DAILY_LOSS_LIMIT_PERCENT,
                current_exposure_percent=exposure_percent,
                max_exposure_percent=settings.MAX_TOTAL_EXPOSURE_PERCENT,
                position_size_percent=settings.MAX_POSITION_SIZE_PERCENT,
                max_position_size_percent=settings.MAX_POSITION_SIZE_PERCENT,
                kill_switch_active=self._kill_switch_active,
                kill_switch_reason=self._kill_switch_reason,
                timestamp=datetime.now()
            )

    def _check_day_rollover(self):
        """Check if we've rolled over to a new day"""
        today = date.today()
        if today != self._current_date:
            self._current_date = today
            self._daily_starting_capital = self._current_capital
            self._daily_loss = 0.0
            logger.info(f"Day rollover: {today}, starting capital: ${self._current_capital:,.2f}")

    async def check_trade_allowed(self, trade_value: float) -> tuple[bool, Optional[str]]:
        """
        Check if a trade is allowed based on risk rules.
        Returns (allowed, reason_if_blocked)
        """
        async with self._lock:
            # Check kill switch
            if self._kill_switch_active:
                return False, f"Kill switch active: {self._kill_switch_reason}"

            # Check daily loss limit
            if self._daily_loss >= settings.DAILY_LOSS_LIMIT_PERCENT:
                return False, f"Daily loss limit reached: {self._daily_loss:.1f}%"

            # Check max drawdown
            if self._current_drawdown >= settings.MAX_DRAWDOWN_PERCENT:
                self._activate_kill_switch(f"Max drawdown reached: {self._current_drawdown:.1f}%")
                return False, f"Max drawdown reached: {self._current_drawdown:.1f}%"

            # Check position size
            position_percent = (trade_value / self._current_capital * 100) if self._current_capital > 0 else 100
            if position_percent > settings.MAX_POSITION_SIZE_PERCENT:
                return False, f"Position size {position_percent:.1f}% exceeds max {settings.MAX_POSITION_SIZE_PERCENT}%"

            # Check total exposure
            new_exposure = self._position_value + trade_value
            exposure_percent = (new_exposure / self._current_capital * 100) if self._current_capital > 0 else 100
            if exposure_percent > settings.MAX_TOTAL_EXPOSURE_PERCENT:
                return False, f"Total exposure {exposure_percent:.1f}% exceeds max {settings.MAX_TOTAL_EXPOSURE_PERCENT}%"

            return True, None

    async def update_position(self, position: Optional[Position]):
        """Update current position"""
        async with self._lock:
            self._current_position = position
            if position:
                self._position_value = position.quantity * position.current_price
            else:
                self._position_value = 0.0

    async def record_trade_result(self, pnl: float, pnl_percent: float):
        """Record the result of a closed trade"""
        async with self._lock:
            # Update capital
            self._current_capital += pnl

            # Update peak
            if self._current_capital > self._peak_capital:
                self._peak_capital = self._current_capital

            # Calculate drawdown from peak
            if self._peak_capital > 0:
                self._current_drawdown = ((self._peak_capital - self._current_capital) / self._peak_capital) * 100
            else:
                self._current_drawdown = 0

            # Update daily loss if negative
            if pnl < 0:
                daily_change = ((self._current_capital - self._daily_starting_capital) / self._daily_starting_capital) * 100
                self._daily_loss = abs(min(0, daily_change))

            # Check risk thresholds
            await self._check_risk_thresholds()

            logger.info(f"Trade recorded: PnL ${pnl:,.2f} ({pnl_percent:+.1f}%), "
                       f"Drawdown: {self._current_drawdown:.1f}%, Daily loss: {self._daily_loss:.1f}%")

    async def _check_risk_thresholds(self):
        """Check and alert on risk thresholds"""
        alerts = []

        # Check drawdown
        if self._current_drawdown >= settings.MAX_DRAWDOWN_PERCENT:
            self._activate_kill_switch(f"Max drawdown exceeded: {self._current_drawdown:.1f}%")
            alerts.append(RiskAlert(
                alert_type="kill_switch",
                message="KILL SWITCH ACTIVATED - Max drawdown exceeded",
                metric="drawdown",
                current_value=self._current_drawdown,
                threshold=settings.MAX_DRAWDOWN_PERCENT,
                timestamp=datetime.now()
            ))
        elif self._current_drawdown >= settings.MAX_DRAWDOWN_PERCENT * 0.8:
            alerts.append(RiskAlert(
                alert_type="critical",
                message="CRITICAL: Approaching max drawdown",
                metric="drawdown",
                current_value=self._current_drawdown,
                threshold=settings.MAX_DRAWDOWN_PERCENT,
                timestamp=datetime.now()
            ))
        elif self._current_drawdown >= settings.MAX_DRAWDOWN_PERCENT * 0.5:
            alerts.append(RiskAlert(
                alert_type="warning",
                message="Warning: Drawdown at 50% of limit",
                metric="drawdown",
                current_value=self._current_drawdown,
                threshold=settings.MAX_DRAWDOWN_PERCENT,
                timestamp=datetime.now()
            ))

        # Check daily loss
        if self._daily_loss >= settings.DAILY_LOSS_LIMIT_PERCENT:
            alerts.append(RiskAlert(
                alert_type="critical",
                message="Daily loss limit reached - Trading halted for today",
                metric="daily_loss",
                current_value=self._daily_loss,
                threshold=settings.DAILY_LOSS_LIMIT_PERCENT,
                timestamp=datetime.now()
            ))
        elif self._daily_loss >= settings.DAILY_LOSS_LIMIT_PERCENT * 0.7:
            alerts.append(RiskAlert(
                alert_type="warning",
                message="Warning: Daily loss approaching limit",
                metric="daily_loss",
                current_value=self._daily_loss,
                threshold=settings.DAILY_LOSS_LIMIT_PERCENT,
                timestamp=datetime.now()
            ))

        self._alerts.extend(alerts)
        return alerts

    def _activate_kill_switch(self, reason: str):
        """Activate the kill switch"""
        self._kill_switch_active = True
        self._kill_switch_reason = reason
        logger.critical(f"KILL SWITCH ACTIVATED: {reason}")

    async def reset_kill_switch(self) -> bool:
        """Reset the kill switch (manual override)"""
        async with self._lock:
            if not self._kill_switch_active:
                return False

            self._kill_switch_active = False
            self._kill_switch_reason = None
            logger.warning("Kill switch reset by manual override")
            return True

    async def get_alerts(self, limit: int = 10) -> List[RiskAlert]:
        """Get recent alerts"""
        return self._alerts[-limit:] if self._alerts else []

    async def get_portfolio_summary(self) -> dict:
        """Get portfolio summary"""
        async with self._lock:
            return {
                "initial_capital": self._initial_capital,
                "current_capital": self._current_capital,
                "peak_capital": self._peak_capital,
                "total_pnl": self._current_capital - self._initial_capital,
                "total_pnl_percent": ((self._current_capital - self._initial_capital) / self._initial_capital) * 100,
                "current_drawdown": self._current_drawdown,
                "daily_loss": self._daily_loss,
                "position_value": self._position_value,
                "available_capital": self._current_capital - self._position_value
            }

    async def set_capital(self, amount: float):
        """Set initial capital (for configuration)"""
        async with self._lock:
            self._initial_capital = amount
            self._current_capital = amount
            self._peak_capital = amount
            self._daily_starting_capital = amount
            logger.info(f"Capital set to ${amount:,.2f}")


# Global instance
risk_service = RiskService()
