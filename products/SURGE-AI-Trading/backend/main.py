"""
SURGE-AI Trading Dashboard - FastAPI Backend
Main application entry point
"""
import asyncio
import logging
from contextlib import asynccontextmanager
from datetime import datetime

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from config import settings
from api import api_router
from api.websocket.handlers import websocket_manager
from services.price_service import price_service
from services.trading_service import trading_service

# Configure logging
logging.basicConfig(
    level=logging.INFO if settings.DEBUG else logging.WARNING,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Track startup time
startup_time = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan manager - handles startup and shutdown"""
    global startup_time
    startup_time = datetime.now()

    logger.info("=" * 60)
    logger.info("SURGE-AI Trading Dashboard Starting...")
    logger.info("=" * 60)

    # Initialize services
    try:
        await price_service.initialize()
        await trading_service.initialize()
        logger.info("Services initialized successfully")
    except Exception as e:
        logger.error(f"Failed to initialize services: {e}")

    # Start WebSocket background tasks
    await websocket_manager.start_background_tasks()
    logger.info("WebSocket streaming started")

    logger.info(f"Server running on http://{settings.API_HOST}:{settings.API_PORT}")
    logger.info(f"API Documentation: http://localhost:{settings.API_PORT}/docs")
    logger.info("=" * 60)

    yield

    # Shutdown
    logger.info("Shutting down...")
    await websocket_manager.stop_background_tasks()
    await price_service.close()
    logger.info("Server shutdown complete")


# Create FastAPI application
app = FastAPI(
    title=settings.APP_NAME,
    description="""
## SURGE-AI Trading Dashboard API

Real-time cryptocurrency trading dashboard with AI-powered signals.

### Features:
- **Live Price Data** with IDR conversion
- **AI Trading Signals** using Kalman filter fusion
- **Risk Management** with kill switch
- **Semi-Autonomous Trading** with 1-click execution

### WebSocket Endpoint:
Connect to `ws://localhost:8000/ws` for real-time updates.

### Events:
- `price_update`: Real-time price changes
- `signal_update`: New trading signals
- `recommendation_update`: Trade recommendations
- `risk_update`: Risk metrics changes
- `trade_executed`: Trade confirmations
    """,
    version=settings.APP_VERSION,
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(api_router)


# Root endpoint
@app.get("/", tags=["Root"])
async def root():
    """Root endpoint - returns API information"""
    return {
        "name": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "status": "running",
        "docs": "/docs",
        "api": "/api/v1"
    }


# Health check endpoint
@app.get("/health", tags=["System"])
async def health_check():
    """Health check endpoint"""
    uptime = (datetime.now() - startup_time).total_seconds() if startup_time else 0

    return {
        "status": "healthy",
        "version": settings.APP_VERSION,
        "uptime_seconds": uptime,
        "websocket_clients": websocket_manager.client_count,
        "trading_enabled": settings.TRADING_ENABLED,
        "testnet_mode": settings.BINANCE_TESTNET,
        "timestamp": datetime.now().isoformat()
    }


# WebSocket endpoint
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    """
    WebSocket endpoint for real-time updates.

    Connect to receive:
    - price_update: Real-time price changes
    - signal_update: New trading signals
    - recommendation_update: Trade recommendations
    - risk_update: Risk metrics
    - position_update: Position changes
    - trade_executed: Trade confirmations
    """
    await websocket_manager.connect(websocket)

    try:
        while True:
            # Receive messages from client
            data = await websocket.receive_json()
            await websocket_manager.handle_client_message(websocket, data)

    except WebSocketDisconnect:
        await websocket_manager.disconnect(websocket)
    except Exception as e:
        logger.error(f"WebSocket error: {e}")
        await websocket_manager.disconnect(websocket)


# Error handlers
@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    """Global exception handler"""
    logger.error(f"Unhandled exception: {exc}")
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error", "error": str(exc)}
    )


# Run server
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host=settings.API_HOST,
        port=settings.API_PORT,
        reload=settings.DEBUG,
        log_level="info"
    )
