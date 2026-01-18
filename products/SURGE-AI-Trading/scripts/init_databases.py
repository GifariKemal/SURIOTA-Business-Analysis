#!/usr/bin/env python3
"""
SURGE-AI Trading - Database Initialization Script
Creates tables, indexes, and initial data for all databases

Usage:
    python init_databases.py
    python init_databases.py --skip-milvus
    python init_databases.py --reset  # WARNING: Drops all data
"""

import argparse
import os
import sys
from datetime import datetime
from pathlib import Path

# Configuration
TIMESCALE_HOST = os.getenv("TIMESCALE_HOST", "localhost")
TIMESCALE_PORT = int(os.getenv("TIMESCALE_PORT", "5432"))
POSTGRES_DB = os.getenv("POSTGRES_DB", "surge_trading")
POSTGRES_USER = os.getenv("POSTGRES_USER", "postgres")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "surge_secret_2024")

MILVUS_HOST = os.getenv("MILVUS_HOST", "localhost")
MILVUS_PORT = os.getenv("MILVUS_PORT", "19530")

DB_CONFIG = {
    "host": TIMESCALE_HOST,
    "port": TIMESCALE_PORT,
    "database": POSTGRES_DB,
    "user": POSTGRES_USER,
    "password": POSTGRES_PASSWORD
}


def print_step(msg):
    print(f"\033[92m[STEP]\033[0m {msg}")


def print_warning(msg):
    print(f"\033[93m[WARNING]\033[0m {msg}")


def print_error(msg):
    print(f"\033[91m[ERROR]\033[0m {msg}")


def print_success(msg):
    print(f"\033[92m[SUCCESS]\033[0m {msg}")


def init_timescaledb(reset: bool = False):
    """Initialize TimescaleDB tables and hypertables"""
    print_step("Initializing TimescaleDB...")

    try:
        import psycopg2
        from psycopg2 import sql
    except ImportError:
        print_error("psycopg2 not installed. Run: pip install psycopg2-binary")
        return False

    try:
        conn = psycopg2.connect(**DB_CONFIG)
        conn.autocommit = True
        cur = conn.cursor()

        # Enable TimescaleDB extension
        print("  Enabling TimescaleDB extension...")
        cur.execute("CREATE EXTENSION IF NOT EXISTS timescaledb CASCADE;")

        if reset:
            print_warning("Dropping existing tables...")
            cur.execute("DROP TABLE IF EXISTS trade_signals CASCADE;")
            cur.execute("DROP TABLE IF EXISTS features_1h CASCADE;")
            cur.execute("DROP TABLE IF EXISTS ohlcv_1h CASCADE;")
            cur.execute("DROP TABLE IF EXISTS trades CASCADE;")
            cur.execute("DROP TABLE IF EXISTS portfolio CASCADE;")

        # Create OHLCV table
        print("  Creating ohlcv_1h table...")
        cur.execute("""
            CREATE TABLE IF NOT EXISTS ohlcv_1h (
                time TIMESTAMPTZ NOT NULL,
                symbol TEXT NOT NULL,
                open DOUBLE PRECISION,
                high DOUBLE PRECISION,
                low DOUBLE PRECISION,
                close DOUBLE PRECISION,
                volume DOUBLE PRECISION,
                quote_volume DOUBLE PRECISION,
                trades INTEGER,
                PRIMARY KEY (time, symbol)
            );
        """)

        # Create hypertable
        try:
            cur.execute("""
                SELECT create_hypertable('ohlcv_1h', 'time',
                    chunk_time_interval => INTERVAL '7 days',
                    if_not_exists => TRUE
                );
            """)
        except Exception as e:
            if "already a hypertable" not in str(e):
                raise

        # Create Features table
        print("  Creating features_1h table...")
        cur.execute("""
            CREATE TABLE IF NOT EXISTS features_1h (
                time TIMESTAMPTZ NOT NULL,
                symbol TEXT NOT NULL,
                -- EMA
                ema_9 DOUBLE PRECISION,
                ema_21 DOUBLE PRECISION,
                ema_50 DOUBLE PRECISION,
                dist_ema_9 DOUBLE PRECISION,
                dist_ema_21 DOUBLE PRECISION,
                dist_ema_50 DOUBLE PRECISION,
                -- MACD
                macd_line DOUBLE PRECISION,
                macd_signal DOUBLE PRECISION,
                macd_histogram DOUBLE PRECISION,
                -- RSI
                rsi_14 DOUBLE PRECISION,
                -- Bollinger Bands
                bb_upper DOUBLE PRECISION,
                bb_lower DOUBLE PRECISION,
                bb_middle DOUBLE PRECISION,
                bb_percent DOUBLE PRECISION,
                bb_bandwidth DOUBLE PRECISION,
                -- ATR
                atr_14 DOUBLE PRECISION,
                atr_percent DOUBLE PRECISION,
                -- Volume
                volume_ratio DOUBLE PRECISION,
                -- Returns
                returns_1h DOUBLE PRECISION,
                returns_4h DOUBLE PRECISION,
                returns_24h DOUBLE PRECISION,
                -- ROC
                roc_10 DOUBLE PRECISION,
                roc_20 DOUBLE PRECISION,
                -- Stochastic
                stoch_k DOUBLE PRECISION,
                stoch_d DOUBLE PRECISION,
                -- Other
                williams_r DOUBLE PRECISION,
                cci_20 DOUBLE PRECISION,
                range_percent DOUBLE PRECISION,
                -- Target (for training)
                target_direction INTEGER,
                target_return_24h DOUBLE PRECISION,
                PRIMARY KEY (time, symbol)
            );
        """)

        try:
            cur.execute("""
                SELECT create_hypertable('features_1h', 'time',
                    chunk_time_interval => INTERVAL '7 days',
                    if_not_exists => TRUE
                );
            """)
        except Exception as e:
            if "already a hypertable" not in str(e):
                raise

        # Create Trade Signals table
        print("  Creating trade_signals table...")
        cur.execute("""
            CREATE TABLE IF NOT EXISTS trade_signals (
                id SERIAL,
                time TIMESTAMPTZ NOT NULL,
                symbol TEXT NOT NULL,
                signal_type TEXT NOT NULL,
                confidence DOUBLE PRECISION,
                price DOUBLE PRECISION,
                model_version TEXT,
                executed BOOLEAN DEFAULT FALSE,
                created_at TIMESTAMPTZ DEFAULT NOW()
            );
        """)

        try:
            cur.execute("""
                SELECT create_hypertable('trade_signals', 'time',
                    chunk_time_interval => INTERVAL '7 days',
                    if_not_exists => TRUE
                );
            """)
        except Exception as e:
            if "already a hypertable" not in str(e):
                raise

        # Create Trades table
        print("  Creating trades table...")
        cur.execute("""
            CREATE TABLE IF NOT EXISTS trades (
                id SERIAL PRIMARY KEY,
                time TIMESTAMPTZ NOT NULL DEFAULT NOW(),
                symbol TEXT NOT NULL,
                side TEXT NOT NULL,
                quantity DOUBLE PRECISION,
                price DOUBLE PRECISION,
                value_usd DOUBLE PRECISION,
                fee DOUBLE PRECISION,
                signal_id INTEGER,
                status TEXT DEFAULT 'pending',
                binance_order_id TEXT,
                created_at TIMESTAMPTZ DEFAULT NOW()
            );
        """)

        # Create Portfolio table
        print("  Creating portfolio table...")
        cur.execute("""
            CREATE TABLE IF NOT EXISTS portfolio (
                id SERIAL PRIMARY KEY,
                time TIMESTAMPTZ NOT NULL DEFAULT NOW(),
                total_value_usd DOUBLE PRECISION,
                cash_usd DOUBLE PRECISION,
                btc_quantity DOUBLE PRECISION,
                btc_value_usd DOUBLE PRECISION,
                pnl_usd DOUBLE PRECISION,
                pnl_percent DOUBLE PRECISION,
                drawdown_percent DOUBLE PRECISION,
                created_at TIMESTAMPTZ DEFAULT NOW()
            );
        """)

        # Create indexes
        print("  Creating indexes...")
        cur.execute("CREATE INDEX IF NOT EXISTS idx_ohlcv_symbol ON ohlcv_1h (symbol, time DESC);")
        cur.execute("CREATE INDEX IF NOT EXISTS idx_features_symbol ON features_1h (symbol, time DESC);")
        cur.execute("CREATE INDEX IF NOT EXISTS idx_signals_symbol ON trade_signals (symbol, time DESC);")

        cur.close()
        conn.close()

        print_success("TimescaleDB initialized successfully")
        return True

    except Exception as e:
        print_error(f"TimescaleDB initialization failed: {e}")
        return False


def init_milvus(reset: bool = False):
    """Initialize Milvus collections for pattern matching and RAG"""
    print_step("Initializing Milvus...")

    try:
        from pymilvus import connections, Collection, FieldSchema, CollectionSchema, DataType, utility
    except ImportError:
        print_error("pymilvus not installed. Run: pip install pymilvus")
        return False

    try:
        connections.connect("default", host=MILVUS_HOST, port=MILVUS_PORT)

        # Pattern Embeddings Collection
        collection_name = "pattern_embeddings"

        if reset and utility.has_collection(collection_name):
            print_warning(f"Dropping collection: {collection_name}")
            utility.drop_collection(collection_name)

        if not utility.has_collection(collection_name):
            print(f"  Creating collection: {collection_name}...")

            fields = [
                FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=True),
                FieldSchema(name="symbol", dtype=DataType.VARCHAR, max_length=20),
                FieldSchema(name="timestamp", dtype=DataType.VARCHAR, max_length=30),
                FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=128),
                FieldSchema(name="target_direction", dtype=DataType.INT64),
                FieldSchema(name="target_return_24h", dtype=DataType.FLOAT)
            ]

            schema = CollectionSchema(fields, description="OHLCV pattern embeddings for similarity search")
            collection = Collection(collection_name, schema)

            # Create index
            print(f"  Creating index for {collection_name}...")
            index_params = {
                "index_type": "IVF_FLAT",
                "metric_type": "L2",
                "params": {"nlist": 128}
            }
            collection.create_index("embedding", index_params)
        else:
            print(f"  Collection {collection_name} already exists")

        # RAG Knowledge Collection
        rag_collection_name = "rag_knowledge"

        if reset and utility.has_collection(rag_collection_name):
            print_warning(f"Dropping collection: {rag_collection_name}")
            utility.drop_collection(rag_collection_name)

        if not utility.has_collection(rag_collection_name):
            print(f"  Creating collection: {rag_collection_name}...")

            fields = [
                FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=True),
                FieldSchema(name="book_title", dtype=DataType.VARCHAR, max_length=200),
                FieldSchema(name="chapter", dtype=DataType.VARCHAR, max_length=200),
                FieldSchema(name="content", dtype=DataType.VARCHAR, max_length=65535),
                FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=384),  # sentence-transformers
                FieldSchema(name="category", dtype=DataType.VARCHAR, max_length=50)
            ]

            schema = CollectionSchema(fields, description="Trading e-book knowledge for RAG")
            collection = Collection(rag_collection_name, schema)

            # Create index
            print(f"  Creating index for {rag_collection_name}...")
            index_params = {
                "index_type": "IVF_FLAT",
                "metric_type": "L2",
                "params": {"nlist": 128}
            }
            collection.create_index("embedding", index_params)
        else:
            print(f"  Collection {rag_collection_name} already exists")

        connections.disconnect("default")
        print_success("Milvus initialized successfully")
        return True

    except Exception as e:
        print_error(f"Milvus initialization failed: {e}")
        return False


def init_redis():
    """Initialize Redis with default keys"""
    print_step("Initializing Redis...")

    try:
        import redis
    except ImportError:
        print_error("redis not installed. Run: pip install redis")
        return False

    try:
        r = redis.Redis(host=os.getenv("REDIS_HOST", "localhost"),
                        port=int(os.getenv("REDIS_PORT", "6379")))
        r.ping()

        # Set initial keys
        r.set("surge:version", "1.0.0")
        r.set("surge:initialized", datetime.now().isoformat())

        print_success("Redis initialized successfully")
        return True

    except Exception as e:
        print_error(f"Redis initialization failed: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(description='SURGE-AI Trading Database Initialization')
    parser.add_argument('--reset', action='store_true',
                        help='Reset databases (WARNING: Drops all data)')
    parser.add_argument('--skip-milvus', action='store_true',
                        help='Skip Milvus initialization')
    parser.add_argument('--skip-timescale', action='store_true',
                        help='Skip TimescaleDB initialization')
    args = parser.parse_args()

    print("=" * 60)
    print("SURGE-AI Trading - Database Initialization")
    print("=" * 60)
    print(f"Timestamp: {datetime.now().isoformat()}")
    print(f"Reset Mode: {args.reset}")
    print("=" * 60)
    print()

    if args.reset:
        print_warning("RESET MODE ENABLED - All existing data will be deleted!")
        response = input("Are you sure? Type 'yes' to continue: ")
        if response.lower() != 'yes':
            print("Aborted.")
            return

    success = True

    # Initialize TimescaleDB
    if not args.skip_timescale:
        if not init_timescaledb(reset=args.reset):
            success = False
    else:
        print_warning("Skipping TimescaleDB initialization")

    print()

    # Initialize Milvus
    if not args.skip_milvus:
        if not init_milvus(reset=args.reset):
            success = False
    else:
        print_warning("Skipping Milvus initialization")

    print()

    # Initialize Redis
    if not init_redis():
        success = False

    print()
    print("=" * 60)

    if success:
        print_success("All databases initialized successfully!")
    else:
        print_error("Some initializations failed. Check the errors above.")
        sys.exit(1)


if __name__ == "__main__":
    main()
