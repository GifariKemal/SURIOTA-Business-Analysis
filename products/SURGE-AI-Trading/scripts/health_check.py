#!/usr/bin/env python3
"""
SURGE-AI Trading - Health Check Script
Comprehensive system health verification

Usage:
    python health_check.py
    python health_check.py --json    # JSON output
    python health_check.py --verbose # Detailed output
"""

import argparse
import json
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, Any

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

# Configuration
TIMESCALE_HOST = os.getenv("TIMESCALE_HOST", "localhost")
TIMESCALE_PORT = int(os.getenv("TIMESCALE_PORT", "5432"))
POSTGRES_DB = os.getenv("POSTGRES_DB", "surge_trading")
POSTGRES_USER = os.getenv("POSTGRES_USER", "postgres")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "surge_secret_2024")

MILVUS_HOST = os.getenv("MILVUS_HOST", "localhost")
MILVUS_PORT = os.getenv("MILVUS_PORT", "19530")

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))

BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")
FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:3000")

ML_DIR = Path(__file__).parent.parent / "ml"


def check_timescaledb() -> Dict[str, Any]:
    """Check TimescaleDB connection and data"""
    result = {
        "name": "TimescaleDB",
        "status": "unknown",
        "details": {}
    }

    try:
        import psycopg2

        conn = psycopg2.connect(
            host=TIMESCALE_HOST,
            port=TIMESCALE_PORT,
            database=POSTGRES_DB,
            user=POSTGRES_USER,
            password=POSTGRES_PASSWORD
        )
        cur = conn.cursor()

        # Check connection
        cur.execute("SELECT version()")
        version = cur.fetchone()[0]
        result["details"]["version"] = version.split(",")[0]

        # Check TimescaleDB extension
        cur.execute("SELECT extversion FROM pg_extension WHERE extname = 'timescaledb'")
        ts_version = cur.fetchone()
        result["details"]["timescaledb_version"] = ts_version[0] if ts_version else "Not installed"

        # Check data tables
        cur.execute("""
            SELECT
                (SELECT COUNT(*) FROM ohlcv_1h) as ohlcv_count,
                (SELECT COUNT(*) FROM features_1h) as features_count,
                (SELECT MAX(time) FROM ohlcv_1h) as latest_time
        """)
        data = cur.fetchone()
        result["details"]["ohlcv_rows"] = data[0]
        result["details"]["features_rows"] = data[1]
        result["details"]["latest_data"] = str(data[2]) if data[2] else None

        cur.close()
        conn.close()

        result["status"] = "healthy"
        if data[0] == 0:
            result["status"] = "warning"
            result["details"]["warning"] = "No OHLCV data found"

    except ImportError:
        result["status"] = "error"
        result["details"]["error"] = "psycopg2 not installed"
    except Exception as e:
        result["status"] = "error"
        result["details"]["error"] = str(e)

    return result


def check_milvus() -> Dict[str, Any]:
    """Check Milvus connection and collections"""
    result = {
        "name": "Milvus",
        "status": "unknown",
        "details": {}
    }

    try:
        from pymilvus import connections, utility, Collection

        connections.connect("default", host=MILVUS_HOST, port=MILVUS_PORT)

        # List collections
        collections = utility.list_collections()
        result["details"]["collections"] = collections

        # Check pattern_embeddings collection
        if "pattern_embeddings" in collections:
            col = Collection("pattern_embeddings")
            col.load()
            result["details"]["pattern_embeddings_count"] = col.num_entities

        # Check rag_knowledge collection
        if "rag_knowledge" in collections:
            col = Collection("rag_knowledge")
            col.load()
            result["details"]["rag_knowledge_count"] = col.num_entities

        connections.disconnect("default")
        result["status"] = "healthy"

        if "pattern_embeddings" not in collections:
            result["status"] = "warning"
            result["details"]["warning"] = "pattern_embeddings collection not found"

    except ImportError:
        result["status"] = "error"
        result["details"]["error"] = "pymilvus not installed"
    except Exception as e:
        result["status"] = "error"
        result["details"]["error"] = str(e)

    return result


def check_redis() -> Dict[str, Any]:
    """Check Redis connection"""
    result = {
        "name": "Redis",
        "status": "unknown",
        "details": {}
    }

    try:
        import redis

        r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)
        r.ping()

        # Get info
        info = r.info()
        result["details"]["version"] = info.get("redis_version", "unknown")
        result["details"]["used_memory"] = info.get("used_memory_human", "unknown")
        result["details"]["connected_clients"] = info.get("connected_clients", 0)

        # Check scheduler health key
        scheduler_health = r.get("scheduler:health")
        if scheduler_health:
            result["details"]["scheduler_status"] = "running"
        else:
            result["details"]["scheduler_status"] = "not reporting"

        result["status"] = "healthy"

    except ImportError:
        result["status"] = "error"
        result["details"]["error"] = "redis not installed"
    except Exception as e:
        result["status"] = "error"
        result["details"]["error"] = str(e)

    return result


def check_binance() -> Dict[str, Any]:
    """Check Binance API connectivity"""
    result = {
        "name": "Binance API",
        "status": "unknown",
        "details": {}
    }

    try:
        import requests

        # Check public API
        response = requests.get("https://api.binance.com/api/v3/ping", timeout=5)
        result["details"]["ping"] = response.status_code == 200

        # Get server time
        response = requests.get("https://api.binance.com/api/v3/time", timeout=5)
        if response.status_code == 200:
            server_time = response.json().get("serverTime", 0)
            result["details"]["server_time"] = datetime.fromtimestamp(server_time/1000).isoformat()

        # Get BTC price
        response = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT", timeout=5)
        if response.status_code == 200:
            result["details"]["btc_price"] = float(response.json().get("price", 0))

        result["status"] = "healthy"

    except ImportError:
        result["status"] = "error"
        result["details"]["error"] = "requests not installed"
    except Exception as e:
        result["status"] = "error"
        result["details"]["error"] = str(e)

    return result


def check_backend() -> Dict[str, Any]:
    """Check Backend API health"""
    result = {
        "name": "Backend API",
        "status": "unknown",
        "details": {}
    }

    try:
        import requests

        response = requests.get(f"{BACKEND_URL}/health", timeout=5)
        if response.status_code == 200:
            data = response.json()
            result["details"]["version"] = data.get("version", "unknown")
            result["details"]["uptime"] = data.get("uptime_seconds", 0)
            result["details"]["websocket_clients"] = data.get("websocket_clients", 0)
            result["details"]["trading_enabled"] = data.get("trading_enabled", False)
            result["status"] = "healthy"
        else:
            result["status"] = "error"
            result["details"]["error"] = f"HTTP {response.status_code}"

    except ImportError:
        result["status"] = "error"
        result["details"]["error"] = "requests not installed"
    except Exception as e:
        result["status"] = "error"
        result["details"]["error"] = str(e)

    return result


def check_frontend() -> Dict[str, Any]:
    """Check Frontend health"""
    result = {
        "name": "Frontend",
        "status": "unknown",
        "details": {}
    }

    try:
        import requests

        response = requests.get(FRONTEND_URL, timeout=5)
        if response.status_code == 200:
            result["status"] = "healthy"
            result["details"]["status_code"] = 200
        else:
            result["status"] = "error"
            result["details"]["error"] = f"HTTP {response.status_code}"

    except ImportError:
        result["status"] = "error"
        result["details"]["error"] = "requests not installed"
    except Exception as e:
        result["status"] = "error"
        result["details"]["error"] = str(e)

    return result


def check_ml_models() -> Dict[str, Any]:
    """Check ML model files"""
    result = {
        "name": "ML Models",
        "status": "unknown",
        "details": {}
    }

    models_dir = ML_DIR / "models"

    try:
        if not models_dir.exists():
            result["status"] = "error"
            result["details"]["error"] = "Models directory not found"
            return result

        # Check for required model files
        required_models = [
            "xgboost_BTCUSDT_latest.pkl",
            "lstm_BTCUSDT_latest.pth",
            "lstm_BTCUSDT_scaler.pkl"
        ]

        found_models = []
        missing_models = []

        for model_file in required_models:
            path = models_dir / model_file
            if path.exists():
                found_models.append(model_file)
                result["details"][model_file] = {
                    "exists": True,
                    "size_mb": round(path.stat().st_size / (1024 * 1024), 2),
                    "modified": datetime.fromtimestamp(path.stat().st_mtime).isoformat()
                }
            else:
                missing_models.append(model_file)
                result["details"][model_file] = {"exists": False}

        result["details"]["found_count"] = len(found_models)
        result["details"]["missing_count"] = len(missing_models)

        if len(missing_models) == 0:
            result["status"] = "healthy"
        elif len(found_models) > 0:
            result["status"] = "warning"
            result["details"]["warning"] = f"Missing models: {missing_models}"
        else:
            result["status"] = "error"
            result["details"]["error"] = "No models found"

    except Exception as e:
        result["status"] = "error"
        result["details"]["error"] = str(e)

    return result


def run_all_checks(verbose: bool = False) -> Dict[str, Any]:
    """Run all health checks"""
    results = {
        "timestamp": datetime.now().isoformat(),
        "overall_status": "unknown",
        "services": []
    }

    checks = [
        ("TimescaleDB", check_timescaledb),
        ("Milvus", check_milvus),
        ("Redis", check_redis),
        ("Binance API", check_binance),
        ("Backend API", check_backend),
        ("Frontend", check_frontend),
        ("ML Models", check_ml_models),
    ]

    healthy_count = 0
    warning_count = 0
    error_count = 0

    for name, check_func in checks:
        if verbose:
            print(f"Checking {name}...", end=" ", flush=True)

        result = check_func()
        results["services"].append(result)

        if result["status"] == "healthy":
            healthy_count += 1
            if verbose:
                print("\033[92mOK\033[0m")
        elif result["status"] == "warning":
            warning_count += 1
            if verbose:
                print(f"\033[93mWARNING\033[0m - {result['details'].get('warning', '')}")
        else:
            error_count += 1
            if verbose:
                print(f"\033[91mERROR\033[0m - {result['details'].get('error', '')}")

    # Determine overall status
    if error_count > 0:
        results["overall_status"] = "unhealthy"
    elif warning_count > 0:
        results["overall_status"] = "degraded"
    else:
        results["overall_status"] = "healthy"

    results["summary"] = {
        "healthy": healthy_count,
        "warning": warning_count,
        "error": error_count,
        "total": len(checks)
    }

    return results


def print_results(results: Dict[str, Any], verbose: bool = False):
    """Print health check results"""
    print("\n" + "=" * 60)
    print("SURGE-AI Trading - System Health Check")
    print("=" * 60)
    print(f"Timestamp: {results['timestamp']}")
    print(f"Overall Status: ", end="")

    status = results["overall_status"]
    if status == "healthy":
        print("\033[92mHEALTHY\033[0m")
    elif status == "degraded":
        print("\033[93mDEGRADED\033[0m")
    else:
        print("\033[91mUNHEALTHY\033[0m")

    print(f"\nSummary: {results['summary']['healthy']}/{results['summary']['total']} services healthy")
    print("-" * 60)

    for service in results["services"]:
        # Use ASCII-safe characters for Windows compatibility
        status_icon = {
            "healthy": "\033[92m[OK]\033[0m",
            "warning": "\033[93m[WARN]\033[0m",
            "error": "\033[91m[FAIL]\033[0m",
            "unknown": "\033[90m[?]\033[0m"
        }.get(service["status"], "[?]")

        print(f"{status_icon} {service['name']}: {service['status']}")

        if verbose and service["details"]:
            for key, value in service["details"].items():
                if key not in ["error", "warning"]:
                    print(f"    {key}: {value}")

    print("=" * 60)


def main():
    parser = argparse.ArgumentParser(description='SURGE-AI Trading Health Check')
    parser.add_argument('--json', action='store_true', help='Output as JSON')
    parser.add_argument('--verbose', '-v', action='store_true', help='Verbose output')
    args = parser.parse_args()

    results = run_all_checks(verbose=args.verbose)

    if args.json:
        print(json.dumps(results, indent=2))
    else:
        print_results(results, verbose=args.verbose)

    # Exit with appropriate code
    if results["overall_status"] == "unhealthy":
        sys.exit(1)
    elif results["overall_status"] == "degraded":
        sys.exit(2)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()
