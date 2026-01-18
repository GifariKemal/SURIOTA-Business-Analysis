"""
SURGE-AI Trading - ML Scheduler Service
Automated signal generation using APScheduler

Jobs:
- generate_signals: Every 5 minutes - Run kalman_fusion.py
- update_sentiment: Every 15 minutes - Fetch and analyze news
- update_enhanced_data: Every 30 minutes - Fear & Greed + CoinGecko
- health_check: Every 1 minute - Service status monitoring
- retrain_models: Daily at 00:00 UTC - Re-fit XGBoost/LSTM models

Usage:
    python scheduler.py
    python scheduler.py --symbol ETHUSDT
    python scheduler.py --dry-run  # Test without executing
"""

import argparse
import json
import logging
import os
import signal
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Optional

import psycopg2
import redis
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.executors.pool import ThreadPoolExecutor
from apscheduler.jobstores.memory import MemoryJobStore
from apscheduler.triggers.cron import CronTrigger
from apscheduler.triggers.interval import IntervalTrigger

# ============================================================
# Configuration
# ============================================================

# Database configuration
DB_CONFIG = {
    "host": os.getenv("TIMESCALE_HOST", "localhost"),
    "port": int(os.getenv("TIMESCALE_PORT", "5432")),
    "database": os.getenv("POSTGRES_DB", "surge_trading"),
    "user": os.getenv("POSTGRES_USER", "postgres"),
    "password": os.getenv("POSTGRES_PASSWORD", "surge_secret_2024")
}

# Redis configuration
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))

# Milvus configuration
MILVUS_HOST = os.getenv("MILVUS_HOST", "localhost")
MILVUS_PORT = os.getenv("MILVUS_PORT", "19530")

# Trading configuration
DEFAULT_SYMBOL = os.getenv("TRADING_SYMBOL", "BTCUSDT")
SIGNAL_THRESHOLD = float(os.getenv("SIGNAL_THRESHOLD", "0.55"))

# Paths
ML_DIR = Path(__file__).parent
PROJECT_DIR = ML_DIR.parent
OUTPUTS_DIR = ML_DIR / "outputs"

# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(OUTPUTS_DIR / "scheduler.log")
    ]
)
logger = logging.getLogger("scheduler")

# ============================================================
# Scheduler State
# ============================================================

class SchedulerState:
    """Track scheduler state and metrics"""

    def __init__(self):
        self.start_time = datetime.now()
        self.signal_count = 0
        self.error_count = 0
        self.last_signal_time = None
        self.last_signal_result = None
        self.services_healthy = {
            "timescaledb": False,
            "milvus": False,
            "redis": False,
            "binance": False
        }
        self.running = True

    def to_dict(self):
        return {
            "start_time": self.start_time.isoformat(),
            "uptime_seconds": (datetime.now() - self.start_time).total_seconds(),
            "signal_count": self.signal_count,
            "error_count": self.error_count,
            "last_signal_time": self.last_signal_time.isoformat() if self.last_signal_time else None,
            "last_signal": self.last_signal_result,
            "services_healthy": self.services_healthy,
            "running": self.running
        }

state = SchedulerState()

# ============================================================
# Health Check Functions
# ============================================================

def check_timescaledb() -> bool:
    """Check TimescaleDB connection"""
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()
        cur.execute("SELECT 1")
        cur.close()
        conn.close()
        return True
    except Exception as e:
        logger.warning(f"TimescaleDB health check failed: {e}")
        return False


def check_milvus() -> bool:
    """Check Milvus connection"""
    try:
        from pymilvus import connections, utility
        connections.connect("default", host=MILVUS_HOST, port=MILVUS_PORT)
        utility.list_collections()
        connections.disconnect("default")
        return True
    except Exception as e:
        logger.warning(f"Milvus health check failed: {e}")
        return False


def check_redis() -> bool:
    """Check Redis connection"""
    try:
        r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)
        r.ping()
        return True
    except Exception as e:
        logger.warning(f"Redis health check failed: {e}")
        return False


def check_binance() -> bool:
    """Check Binance API connectivity"""
    try:
        import requests
        response = requests.get("https://api.binance.com/api/v3/ping", timeout=5)
        return response.status_code == 200
    except Exception as e:
        logger.warning(f"Binance health check failed: {e}")
        return False


def job_health_check():
    """Run health checks for all services"""
    logger.debug("Running health checks...")

    state.services_healthy["timescaledb"] = check_timescaledb()
    state.services_healthy["milvus"] = check_milvus()
    state.services_healthy["redis"] = check_redis()
    state.services_healthy["binance"] = check_binance()

    # Count healthy services
    healthy = sum(state.services_healthy.values())
    total = len(state.services_healthy)

    if healthy < total:
        logger.warning(f"Health check: {healthy}/{total} services healthy")
        for service, is_healthy in state.services_healthy.items():
            if not is_healthy:
                logger.warning(f"  - {service}: UNHEALTHY")
    else:
        logger.debug(f"Health check: All {total} services healthy")

    # Publish health status to Redis if available
    if state.services_healthy["redis"]:
        try:
            r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)
            r.set("scheduler:health", json.dumps(state.to_dict()))
            r.expire("scheduler:health", 120)  # Expire in 2 minutes
        except Exception:
            pass


# ============================================================
# Signal Generation Jobs
# ============================================================

def job_generate_signals(symbol: str = DEFAULT_SYMBOL, dry_run: bool = False):
    """
    Generate trading signals using Kalman filter fusion
    Runs every 5 minutes
    """
    logger.info(f"[Signal] Starting signal generation for {symbol}...")

    if dry_run:
        logger.info("[Signal] DRY RUN - skipping actual signal generation")
        return

    # Check if services are healthy
    if not state.services_healthy["timescaledb"] or not state.services_healthy["milvus"]:
        logger.warning("[Signal] Skipping - required services not healthy")
        state.error_count += 1
        return

    try:
        # Run kalman_fusion.py as subprocess
        result = subprocess.run(
            [
                sys.executable,
                str(ML_DIR / "kalman_fusion.py"),
                "--symbol", symbol,
                "--threshold", str(SIGNAL_THRESHOLD),
                "--save"
            ],
            capture_output=True,
            text=True,
            timeout=300,  # 5 minute timeout (model loading takes time)
            cwd=str(ML_DIR)
        )

        if result.returncode == 0:
            state.signal_count += 1
            state.last_signal_time = datetime.now()

            # Parse signal from output
            output_lines = result.stdout.split("\n")
            for line in output_lines:
                if "FINAL SIGNAL:" in line:
                    signal = line.split("FINAL SIGNAL:")[-1].strip()
                    # Remove ANSI color codes
                    import re
                    signal = re.sub(r'\033\[[0-9;]*m', '', signal)
                    state.last_signal_result = signal.strip().replace("<<<", "").strip()
                    break

            logger.info(f"[Signal] Generated: {state.last_signal_result}")

            # Publish to Redis
            if state.services_healthy["redis"]:
                try:
                    r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)
                    r.publish("signals", json.dumps({
                        "symbol": symbol,
                        "signal": state.last_signal_result,
                        "time": datetime.now().isoformat()
                    }))
                except Exception:
                    pass
        else:
            logger.error(f"[Signal] Failed: {result.stderr[:500]}")
            state.error_count += 1

    except subprocess.TimeoutExpired:
        logger.error("[Signal] Timeout - signal generation took too long")
        state.error_count += 1
    except Exception as e:
        logger.error(f"[Signal] Error: {e}")
        state.error_count += 1


def job_update_sentiment(symbol: str = DEFAULT_SYMBOL, dry_run: bool = False):
    """
    Update sentiment analysis data
    Runs every 15 minutes
    """
    logger.info(f"[Sentiment] Updating sentiment for {symbol}...")

    if dry_run:
        logger.info("[Sentiment] DRY RUN - skipping actual update")
        return

    try:
        # Run sentiment_predict.py
        result = subprocess.run(
            [
                sys.executable,
                str(ML_DIR / "sentiment_predict.py"),
                "--symbol", symbol
            ],
            capture_output=True,
            text=True,
            timeout=60,
            cwd=str(ML_DIR)
        )

        if result.returncode == 0:
            logger.info("[Sentiment] Update complete")
        else:
            logger.warning(f"[Sentiment] Warning: {result.stderr[:200]}")

    except subprocess.TimeoutExpired:
        logger.error("[Sentiment] Timeout")
    except Exception as e:
        logger.error(f"[Sentiment] Error: {e}")


def job_update_enhanced_data(symbol: str = DEFAULT_SYMBOL, dry_run: bool = False):
    """
    Update enhanced market data (Fear & Greed, CoinGecko)
    Runs every 30 minutes
    """
    logger.info(f"[Enhanced] Updating enhanced data for {symbol}...")

    if dry_run:
        logger.info("[Enhanced] DRY RUN - skipping actual update")
        return

    try:
        # Import and run the fetcher
        from enhanced_data_fetcher import EnhancedDataFetcher

        fetcher = EnhancedDataFetcher(verify_ssl=False)
        data = fetcher.get_all_enhanced_data(symbol)

        # Cache to Redis if available
        if state.services_healthy["redis"]:
            try:
                r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)
                r.set(
                    f"enhanced_data:{symbol}",
                    json.dumps(data, default=str),
                    ex=3600  # Expire in 1 hour
                )
            except Exception:
                pass

        logger.info(f"[Enhanced] Updated - Sources: {list(data.keys())}")

    except Exception as e:
        logger.error(f"[Enhanced] Error: {e}")


def job_retrain_models(symbol: str = DEFAULT_SYMBOL, dry_run: bool = False):
    """
    Retrain ML models (XGBoost and LSTM)
    Runs daily at 00:00 UTC
    """
    logger.info(f"[Retrain] Starting model retraining for {symbol}...")

    if dry_run:
        logger.info("[Retrain] DRY RUN - skipping actual retraining")
        return

    if not state.services_healthy["timescaledb"]:
        logger.warning("[Retrain] Skipping - TimescaleDB not healthy")
        return

    try:
        # Retrain XGBoost
        logger.info("[Retrain] Training XGBoost model...")
        result = subprocess.run(
            [
                sys.executable,
                str(ML_DIR / "train_xgboost.py"),
                "--symbol", symbol
            ],
            capture_output=True,
            text=True,
            timeout=600,  # 10 minute timeout
            cwd=str(ML_DIR)
        )

        if result.returncode == 0:
            logger.info("[Retrain] XGBoost training complete")
        else:
            logger.error(f"[Retrain] XGBoost failed: {result.stderr[:300]}")

        # Retrain LSTM
        logger.info("[Retrain] Training LSTM model...")
        result = subprocess.run(
            [
                sys.executable,
                str(ML_DIR / "train_lstm.py"),
                "--symbol", symbol
            ],
            capture_output=True,
            text=True,
            timeout=1800,  # 30 minute timeout
            cwd=str(ML_DIR)
        )

        if result.returncode == 0:
            logger.info("[Retrain] LSTM training complete")
        else:
            logger.error(f"[Retrain] LSTM failed: {result.stderr[:300]}")

    except subprocess.TimeoutExpired:
        logger.error("[Retrain] Timeout during model training")
    except Exception as e:
        logger.error(f"[Retrain] Error: {e}")


def job_update_milvus_embeddings(symbol: str = DEFAULT_SYMBOL, dry_run: bool = False):
    """
    Update Milvus pattern embeddings
    Runs daily at 01:00 UTC
    """
    logger.info(f"[Milvus] Updating pattern embeddings for {symbol}...")

    if dry_run:
        logger.info("[Milvus] DRY RUN - skipping actual update")
        return

    if not state.services_healthy["timescaledb"] or not state.services_healthy["milvus"]:
        logger.warning("[Milvus] Skipping - required services not healthy")
        return

    try:
        result = subprocess.run(
            [
                sys.executable,
                str(ML_DIR / "retrain_milvus.py"),
                "--symbol", symbol
            ],
            capture_output=True,
            text=True,
            timeout=1200,  # 20 minute timeout
            cwd=str(ML_DIR)
        )

        if result.returncode == 0:
            logger.info("[Milvus] Embeddings update complete")
        else:
            logger.error(f"[Milvus] Failed: {result.stderr[:300]}")

    except subprocess.TimeoutExpired:
        logger.error("[Milvus] Timeout during embedding update")
    except Exception as e:
        logger.error(f"[Milvus] Error: {e}")


# ============================================================
# Scheduler Setup
# ============================================================

def create_scheduler(symbol: str, dry_run: bool = False) -> BackgroundScheduler:
    """Create and configure the APScheduler instance"""

    # Configure job stores and executors
    jobstores = {
        'default': MemoryJobStore()
    }
    executors = {
        'default': ThreadPoolExecutor(max_workers=4)
    }
    job_defaults = {
        'coalesce': True,  # Combine missed jobs
        'max_instances': 1,  # Only one instance per job
        'misfire_grace_time': 60  # Allow 60 seconds late
    }

    scheduler = BackgroundScheduler(
        jobstores=jobstores,
        executors=executors,
        job_defaults=job_defaults,
        timezone='UTC'
    )

    # Add jobs
    # Health check - every 1 minute
    scheduler.add_job(
        job_health_check,
        trigger=IntervalTrigger(minutes=1),
        id='health_check',
        name='Health Check',
        replace_existing=True
    )

    # Signal generation - every 5 minutes
    scheduler.add_job(
        job_generate_signals,
        trigger=IntervalTrigger(minutes=5),
        args=[symbol, dry_run],
        id='generate_signals',
        name='Generate Signals',
        replace_existing=True
    )

    # Sentiment update - every 15 minutes
    scheduler.add_job(
        job_update_sentiment,
        trigger=IntervalTrigger(minutes=15),
        args=[symbol, dry_run],
        id='update_sentiment',
        name='Update Sentiment',
        replace_existing=True
    )

    # Enhanced data update - every 30 minutes
    scheduler.add_job(
        job_update_enhanced_data,
        trigger=IntervalTrigger(minutes=30),
        args=[symbol, dry_run],
        id='update_enhanced_data',
        name='Update Enhanced Data',
        replace_existing=True
    )

    # Model retraining - daily at 00:00 UTC
    scheduler.add_job(
        job_retrain_models,
        trigger=CronTrigger(hour=0, minute=0),
        args=[symbol, dry_run],
        id='retrain_models',
        name='Retrain Models',
        replace_existing=True
    )

    # Milvus embeddings update - daily at 01:00 UTC
    scheduler.add_job(
        job_update_milvus_embeddings,
        trigger=CronTrigger(hour=1, minute=0),
        args=[symbol, dry_run],
        id='update_milvus',
        name='Update Milvus Embeddings',
        replace_existing=True
    )

    return scheduler


# ============================================================
# Main
# ============================================================

def shutdown_handler(signum, frame):
    """Handle shutdown signals gracefully"""
    logger.info("Shutdown signal received...")
    state.running = False


def main():
    parser = argparse.ArgumentParser(description='SURGE-AI Trading ML Scheduler')
    parser.add_argument('--symbol', type=str, default=DEFAULT_SYMBOL,
                        help='Trading symbol (default: BTCUSDT)')
    parser.add_argument('--dry-run', action='store_true',
                        help='Test mode - do not execute actual jobs')
    parser.add_argument('--run-once', action='store_true',
                        help='Run all jobs once and exit')
    args = parser.parse_args()

    # Ensure outputs directory exists
    OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)

    print("=" * 70)
    print("SURGE-AI Trading - ML Scheduler Service")
    print("=" * 70)
    print(f"Symbol: {args.symbol}")
    print(f"Dry Run: {args.dry_run}")
    print(f"Run Once: {args.run_once}")
    print(f"Started: {state.start_time.strftime('%Y-%m-%d %H:%M:%S')} UTC")
    print("=" * 70)

    # Register signal handlers
    signal.signal(signal.SIGINT, shutdown_handler)
    signal.signal(signal.SIGTERM, shutdown_handler)

    if args.run_once:
        # Run all jobs once for testing
        print("\n[Running all jobs once...]")
        job_health_check()
        job_generate_signals(args.symbol, args.dry_run)
        job_update_sentiment(args.symbol, args.dry_run)
        job_update_enhanced_data(args.symbol, args.dry_run)
        print("\n[All jobs completed]")
        return

    # Create and start scheduler
    scheduler = create_scheduler(args.symbol, args.dry_run)
    scheduler.start()

    print("\nScheduler started with the following jobs:")
    print("-" * 70)
    for job in scheduler.get_jobs():
        print(f"  - {job.name}: {job.trigger}")
    print("-" * 70)
    print("\nPress Ctrl+C to stop the scheduler.\n")

    # Run initial health check
    job_health_check()

    # Run initial signal generation
    print("\n[Running initial signal generation...]\n")
    job_generate_signals(args.symbol, args.dry_run)

    # Keep the main thread alive
    try:
        while state.running:
            time.sleep(1)
    except (KeyboardInterrupt, SystemExit):
        pass
    finally:
        print("\nShutting down scheduler...")
        scheduler.shutdown(wait=True)
        print("Scheduler stopped.")

        # Print summary
        print("\n" + "=" * 70)
        print("SCHEDULER SUMMARY")
        print("=" * 70)
        print(f"Total signals generated: {state.signal_count}")
        print(f"Total errors: {state.error_count}")
        print(f"Last signal: {state.last_signal_result}")
        print(f"Last signal time: {state.last_signal_time}")
        uptime = (datetime.now() - state.start_time).total_seconds()
        print(f"Uptime: {uptime:.1f} seconds ({uptime/3600:.2f} hours)")
        print("=" * 70)


if __name__ == "__main__":
    main()
