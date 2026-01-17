"""
SURGE-AI Trading Dashboard - Risk Management API Routes
"""
from fastapi import APIRouter, HTTPException
from typing import List

from models.schemas import RiskMetrics, RiskAlert
from services.risk_service import risk_service

router = APIRouter()


@router.get("/status", response_model=RiskMetrics)
async def get_risk_status():
    """
    Get current risk metrics.

    Returns:
    - **current_drawdown_percent**: Current drawdown from peak
    - **daily_loss_percent**: Today's loss percentage
    - **current_exposure_percent**: Current market exposure
    - **kill_switch_active**: Whether kill switch is triggered
    """
    try:
        metrics = await risk_service.get_risk_metrics()
        return metrics
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/kill-switch")
async def get_kill_switch_status():
    """
    Get kill switch status.
    """
    try:
        metrics = await risk_service.get_risk_metrics()
        return {
            "active": metrics.kill_switch_active,
            "reason": metrics.kill_switch_reason
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/kill-switch/reset")
async def reset_kill_switch():
    """
    Reset the kill switch (manual override).

    WARNING: This allows trading to resume after hitting risk limits.
    Use with caution.
    """
    try:
        success = await risk_service.reset_kill_switch()
        if not success:
            return {"message": "Kill switch was not active", "reset": False}
        return {"message": "Kill switch reset successfully", "reset": True}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/alerts", response_model=List[RiskAlert])
async def get_risk_alerts(limit: int = 10):
    """
    Get recent risk alerts.

    - **limit**: Maximum number of alerts to return
    """
    try:
        alerts = await risk_service.get_alerts(limit)
        return alerts
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/portfolio")
async def get_portfolio_summary():
    """
    Get portfolio summary.
    """
    try:
        summary = await risk_service.get_portfolio_summary()
        return summary
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/limits")
async def get_risk_limits():
    """
    Get configured risk limits.
    """
    from config import settings
    return {
        "max_position_size_percent": settings.MAX_POSITION_SIZE_PERCENT,
        "max_total_exposure_percent": settings.MAX_TOTAL_EXPOSURE_PERCENT,
        "max_drawdown_percent": settings.MAX_DRAWDOWN_PERCENT,
        "daily_loss_limit_percent": settings.DAILY_LOSS_LIMIT_PERCENT,
        "min_confidence_threshold": settings.MIN_CONFIDENCE_THRESHOLD
    }
