"""
SURGE-AI Trading Dashboard - WebSocket Handlers
Real-time data streaming to connected clients
"""
import asyncio
from datetime import datetime
from typing import Dict, Set, Optional
import logging
import json

from fastapi import WebSocket, WebSocketDisconnect

from config import settings
from services.price_service import price_service
from services.signal_service import signal_service
from services.risk_service import risk_service
from services.trading_service import trading_service

logger = logging.getLogger(__name__)


class WebSocketManager:
    """
    Manages WebSocket connections and broadcasts.
    Handles real-time price updates, signals, and trade notifications.
    """

    def __init__(self):
        # Active connections
        self._connections: Set[WebSocket] = set()
        # Subscription tracking
        self._subscriptions: Dict[WebSocket, Set[str]] = {}
        # Background tasks
        self._price_task: Optional[asyncio.Task] = None
        self._signal_task: Optional[asyncio.Task] = None
        # Running state
        self._running = False

    async def connect(self, websocket: WebSocket):
        """Accept new WebSocket connection"""
        logger.info("WebSocket connection request received, accepting...")
        await websocket.accept()
        logger.info("WebSocket accepted!")
        self._connections.add(websocket)
        self._subscriptions[websocket] = {"price", "signal", "risk", "trade"}  # Default subscriptions

        logger.info(f"WebSocket connected. Total clients: {len(self._connections)}")

        # Send initial data
        logger.info("Calling _send_initial_data...")
        await self._send_initial_data(websocket)
        logger.info("_send_initial_data completed!")

    async def disconnect(self, websocket: WebSocket):
        """Handle WebSocket disconnection"""
        self._connections.discard(websocket)
        self._subscriptions.pop(websocket, None)
        logger.info(f"WebSocket disconnected. Total clients: {len(self._connections)}")

    async def _send_initial_data(self, websocket: WebSocket):
        """Send initial data to newly connected client"""
        try:
            logger.info("Sending initial data to client...")

            # Send current price
            logger.debug("Getting price...")
            price = await price_service.get_price(settings.TRADING_SYMBOL)
            logger.debug(f"Sending price_update...")
            await self._send_to_client(websocket, "price_update", price.model_dump(mode='json'))
            logger.info("Sent price_update")

            # Send current signal
            logger.debug("Getting signal...")
            signal = await signal_service.get_current_signal(settings.TRADING_SYMBOL)
            await self._send_to_client(websocket, "signal_update", signal.model_dump(mode='json'))
            logger.info("Sent signal_update")

            # Send recommendation
            logger.debug("Getting recommendation...")
            recommendation = await signal_service.get_trade_recommendation(settings.TRADING_SYMBOL)
            await self._send_to_client(websocket, "recommendation_update", recommendation.model_dump(mode='json'))
            logger.info("Sent recommendation_update")

            # Send risk metrics
            logger.debug("Getting risk metrics...")
            risk = await risk_service.get_risk_metrics()
            await self._send_to_client(websocket, "risk_update", risk.model_dump(mode='json'))
            logger.info("Sent risk_update")

            # Send position if exists
            position = await trading_service.get_position()
            if position:
                await self._send_to_client(websocket, "position_update", position.model_dump(mode='json'))
                logger.info("Sent position_update")

            # Send balance
            logger.debug("Getting balance...")
            balance = await trading_service.get_balance()
            await self._send_to_client(websocket, "balance_update", balance.model_dump(mode='json'))
            logger.info("Sent balance_update")

            logger.info("All initial data sent successfully!")

        except Exception as e:
            logger.error(f"Error sending initial data: {e}")
            import traceback
            logger.error(traceback.format_exc())

    async def _send_to_client(self, websocket: WebSocket, event: str, data: dict):
        """Send message to a specific client"""
        # Check if websocket is still connected
        if websocket not in self._connections:
            return

        try:
            message = {
                "event": event,
                "data": data,
                "timestamp": datetime.now().isoformat()
            }
            await websocket.send_json(message)
        except Exception as e:
            logger.error(f"Error sending to client: {e}")
            # Only disconnect if still in connections
            if websocket in self._connections:
                self._connections.discard(websocket)
                self._subscriptions.pop(websocket, None)

    async def broadcast(self, event: str, data: dict, channel: Optional[str] = None):
        """Broadcast message to all connected clients"""
        if not self._connections:
            return

        message = {
            "event": event,
            "data": data,
            "timestamp": datetime.now().isoformat()
        }

        dead_connections = set()

        for websocket in self._connections:
            try:
                # Check subscription if channel specified
                if channel:
                    subscriptions = self._subscriptions.get(websocket, set())
                    if channel not in subscriptions:
                        continue

                await websocket.send_json(message)
            except Exception as e:
                logger.error(f"Error broadcasting to client: {e}")
                dead_connections.add(websocket)

        # Clean up dead connections
        for ws in dead_connections:
            await self.disconnect(ws)

    async def handle_client_message(self, websocket: WebSocket, message: dict):
        """Handle incoming message from client"""
        try:
            event = message.get("event")
            data = message.get("data", {})

            if event == "subscribe":
                channels = data.get("channels", [])
                self._subscriptions[websocket] = set(channels)
                await self._send_to_client(websocket, "subscribed", {"channels": channels})

            elif event == "unsubscribe":
                channels = data.get("channels", [])
                current = self._subscriptions.get(websocket, set())
                for channel in channels:
                    current.discard(channel)
                self._subscriptions[websocket] = current

            elif event == "ping":
                await self._send_to_client(websocket, "pong", {"timestamp": datetime.now().isoformat()})

            elif event == "execute_trade":
                # Handle trade execution via WebSocket
                from models.schemas import TradeRequest, TradeAction
                request = TradeRequest(
                    action=TradeAction(data.get("action", "BUY")),
                    symbol=data.get("symbol", settings.TRADING_SYMBOL),
                    quantity=float(data.get("quantity", 0)),
                    stop_loss=data.get("stop_loss"),
                    take_profit=data.get("take_profit")
                )
                result = await trading_service.execute_trade(request)
                await self._send_to_client(websocket, "trade_executed", result.model_dump(mode='json'))
                # Broadcast to all clients
                await self.broadcast("trade_executed", result.model_dump(mode='json'), "trade")

            elif event == "refresh_signal":
                signal_service.force_new_signal()
                signal = await signal_service.get_current_signal(settings.TRADING_SYMBOL)
                await self.broadcast("signal_update", signal.model_dump(mode='json'), "signal")

        except Exception as e:
            logger.error(f"Error handling client message: {e}")
            await self._send_to_client(websocket, "error", {"message": str(e)})

    async def start_background_tasks(self):
        """Start background streaming tasks"""
        if self._running:
            return

        self._running = True
        self._price_task = asyncio.create_task(self._price_stream())
        self._signal_task = asyncio.create_task(self._signal_stream())
        logger.info("Background streaming tasks started")

    async def stop_background_tasks(self):
        """Stop background streaming tasks"""
        self._running = False

        if self._price_task:
            self._price_task.cancel()
            try:
                await self._price_task
            except asyncio.CancelledError:
                pass

        if self._signal_task:
            self._signal_task.cancel()
            try:
                await self._signal_task
            except asyncio.CancelledError:
                pass

        logger.info("Background streaming tasks stopped")

    async def _price_stream(self):
        """Stream price updates to clients"""
        while self._running:
            try:
                if self._connections:
                    # Get current price
                    price = await price_service.get_price(settings.TRADING_SYMBOL)
                    await self.broadcast("price_update", price.model_dump(mode='json'), "price")

                    # Also update position PnL if exists
                    position = await trading_service.get_position()
                    if position:
                        await self.broadcast("position_update", position.model_dump(mode='json'), "trade")

                await asyncio.sleep(settings.PRICE_UPDATE_INTERVAL)

            except asyncio.CancelledError:
                break
            except Exception as e:
                logger.error(f"Error in price stream: {e}")
                await asyncio.sleep(5)

    async def _signal_stream(self):
        """Stream signal updates to clients"""
        last_signal_time = None

        while self._running:
            try:
                if self._connections:
                    # Get current signal
                    signal = await signal_service.get_current_signal(settings.TRADING_SYMBOL)

                    # Check if signal changed
                    if last_signal_time != signal.timestamp:
                        last_signal_time = signal.timestamp
                        await self.broadcast("signal_update", signal.model_dump(mode='json'), "signal")

                        # Also send recommendation
                        recommendation = await signal_service.get_trade_recommendation(settings.TRADING_SYMBOL)
                        await self.broadcast("recommendation_update", recommendation.model_dump(mode='json'), "signal")

                    # Send risk metrics periodically
                    risk = await risk_service.get_risk_metrics()
                    await self.broadcast("risk_update", risk.model_dump(mode='json'), "risk")

                # Check every 10 seconds
                await asyncio.sleep(10)

            except asyncio.CancelledError:
                break
            except Exception as e:
                logger.error(f"Error in signal stream: {e}")
                await asyncio.sleep(10)

    @property
    def client_count(self) -> int:
        """Get number of connected clients"""
        return len(self._connections)


# Global WebSocket manager instance
websocket_manager = WebSocketManager()


# Custom JSON encoder for datetime
class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)
