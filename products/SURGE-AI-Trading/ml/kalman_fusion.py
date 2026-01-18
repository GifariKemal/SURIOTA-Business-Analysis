"""
SURGE-AI Trading - Kalman Filter Signal Fusion v4
Combines ML, Pattern Matching, Sentiment, Enhanced Market Data, and RAG Knowledge

Final Signal = 0.45 * Kalman_ML + 0.15 * Kalman_DB + 0.15 * Kalman_Sentiment + 0.10 * Kalman_Enhanced + 0.15 * Kalman_RAG

Components:
- Kalman Filter 1 (ML):       XGBoost + LSTM ensemble (45% weight)
- Kalman Filter 2 (DB):       Milvus pattern matching (15% weight)
- Kalman Filter 3 (Sentiment): FinBERT news sentiment analysis (15% weight)
- Kalman Filter 4 (Enhanced): Market structure data (10% weight)
  - Fear & Greed Index
  - CoinGecko market momentum
  - Multi-timeframe trend alignment
  - Order book imbalance (when available)
  - Futures metrics (when available)
- Kalman Filter 5 (RAG):      E-book knowledge retrieval (15% weight)
  - Trading e-books knowledge base
  - Contextual pattern retrieval
  - Expert strategy extraction

Note: v4 adds RAG for incorporating trading e-book knowledge

Usage:
    python kalman_fusion.py --symbol BTCUSDT
    python kalman_fusion.py --symbol BTCUSDT --threshold 0.55
    python kalman_fusion.py --symbol BTCUSDT --no-rag  # Skip RAG
"""

import argparse
import os
import pickle
from datetime import datetime
from pathlib import Path

import numpy as np
import pandas as pd
import psycopg2
import torch
from sklearn.preprocessing import StandardScaler
from pymilvus import connections, Collection

# ============================================================
# Configuration
# ============================================================

DB_CONFIG = {
    "host": os.environ.get("POSTGRES_HOST", "localhost"),
    "port": int(os.environ.get("POSTGRES_PORT", 5432)),
    "database": os.environ.get("POSTGRES_DB", "surge_trading"),
    "user": os.environ.get("POSTGRES_USER", "postgres"),
    "password": os.environ.get("POSTGRES_PASSWORD", "surge_secret_2024")
}

MILVUS_HOST = os.environ.get("MILVUS_HOST", "localhost")
MILVUS_PORT = os.environ.get("MILVUS_PORT", "19530")
COLLECTION_NAME = "pattern_embeddings"

MODEL_DIR = Path(__file__).parent / "models"

# Feature columns
FEATURE_COLUMNS = [
    'dist_ema_9', 'dist_ema_21', 'dist_ema_50',
    'macd_line', 'macd_signal', 'macd_histogram',
    'rsi_14',
    'bb_percent', 'bb_bandwidth',
    'atr_percent',
    'volume_ratio',
    'returns_1h', 'returns_4h', 'returns_24h',
    'roc_10', 'roc_20',
    'stoch_k', 'stoch_d',
    'williams_r', 'cci_20', 'range_percent'
]

# Kalman Filter weights (optimized with enhanced data + RAG)
# v1: ML=50%, DB=30%, Sent=20% - caused SHORT bias from Milvus (~33% UP)
# v2: ML=60%, DB=20%, Sent=20% - reduced SHORT bias
# v3: Added enhanced market data filter for better context
# v4: Added RAG e-book knowledge for expert trading strategies
KALMAN_ML_WEIGHT = 0.45         # ML models (XGBoost + LSTM)
KALMAN_DB_WEIGHT = 0.15         # Milvus pattern matching
KALMAN_SENTIMENT_WEIGHT = 0.15  # Sentiment analysis
KALMAN_ENHANCED_WEIGHT = 0.10   # Enhanced market data (Fear&Greed, CoinGecko, etc.)
KALMAN_RAG_WEIGHT = 0.15        # RAG e-book knowledge

# ML ensemble weights (within Kalman Filter 1)
XGBOOST_WEIGHT = 0.6
LSTM_WEIGHT = 0.4

# Parameters
SEQUENCE_LENGTH = 24
HIDDEN_SIZE = 64
NUM_LAYERS = 2
DROPOUT = 0.2
EMBEDDING_DIM = 128
TOP_K_PATTERNS = 100


# ============================================================
# LSTM Model Definition (must match train_lstm.py)
# ============================================================

class LSTMClassifier(torch.nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, dropout):
        super(LSTMClassifier, self).__init__()
        self.lstm = torch.nn.LSTM(
            input_size=input_size,
            hidden_size=hidden_size,
            num_layers=num_layers,
            batch_first=True,
            dropout=dropout if num_layers > 1 else 0,
            bidirectional=False
        )
        self.fc = torch.nn.Sequential(
            torch.nn.Linear(hidden_size, 32),
            torch.nn.ReLU(),
            torch.nn.Dropout(dropout),
            torch.nn.Linear(32, 1),
            torch.nn.Sigmoid()
        )

    def forward(self, x):
        lstm_out, _ = self.lstm(x)
        last_hidden = lstm_out[:, -1, :]
        return self.fc(last_hidden)


# ============================================================
# Data Loading
# ============================================================

def get_latest_features(symbol: str, n_rows: int = 50) -> pd.DataFrame:
    """Get latest features from TimescaleDB"""
    conn = psycopg2.connect(**DB_CONFIG)

    query = f"""
    SELECT
        f.time as timestamp,
        o.open,
        o.high,
        o.low,
        o.close,
        o.volume,
        f.ema_9,
        f.ema_21,
        f.ema_50,
        f.dist_ema_9,
        f.dist_ema_21,
        f.dist_ema_50,
        f.macd_line,
        f.macd_signal,
        f.macd_histogram,
        f.rsi_14,
        f.bb_upper,
        f.bb_lower,
        f.bb_middle,
        f.bb_percent,
        f.bb_bandwidth,
        f.atr_14,
        f.atr_percent,
        f.volume_ratio,
        f.returns_1h,
        f.returns_4h,
        f.returns_24h,
        f.roc_10,
        f.roc_20,
        f.stoch_k,
        f.stoch_d,
        f.williams_r,
        f.cci_20,
        f.range_percent
    FROM features_1h f
    JOIN ohlcv_1h o ON f.time = o.time AND f.symbol = o.symbol
    WHERE f.symbol = '{symbol}'
    ORDER BY f.time DESC
    LIMIT {n_rows}
    """

    df = pd.read_sql(query, conn)
    conn.close()

    # Reverse to chronological order
    df = df.iloc[::-1].reset_index(drop=True)
    return df


# ============================================================
# Kalman Filter 1: ML (XGBoost + LSTM)
# ============================================================

def load_xgboost_model(symbol: str):
    model_path = MODEL_DIR / f"xgboost_{symbol}_latest.pkl"
    with open(model_path, 'rb') as f:
        return pickle.load(f)


def load_lstm_model(symbol: str):
    model_path = MODEL_DIR / f"lstm_{symbol}_latest.pth"
    scaler_path = MODEL_DIR / f"lstm_{symbol}_scaler.pkl"

    with open(scaler_path, 'rb') as f:
        scaler = pickle.load(f)

    checkpoint = torch.load(model_path, map_location='cpu', weights_only=False)
    model = LSTMClassifier(
        input_size=checkpoint['input_size'],
        hidden_size=checkpoint['hidden_size'],
        num_layers=checkpoint['num_layers'],
        dropout=checkpoint['dropout']
    )
    model.load_state_dict(checkpoint['model_state_dict'])
    model.eval()
    return model, scaler


def predict_kalman_ml(symbol: str, df: pd.DataFrame) -> dict:
    """Kalman Filter 1: ML prediction (XGBoost + LSTM)"""
    # Load models
    xgb_model = load_xgboost_model(symbol)
    lstm_model, lstm_scaler = load_lstm_model(symbol)

    # XGBoost prediction
    X_xgb = df[FEATURE_COLUMNS].iloc[[-1]].fillna(0)
    xgb_prob = xgb_model.predict_proba(X_xgb)[0, 1]

    # LSTM prediction
    X_lstm = df[FEATURE_COLUMNS].ffill().fillna(0).values[-SEQUENCE_LENGTH:]
    X_lstm_scaled = lstm_scaler.transform(X_lstm)
    X_lstm_tensor = torch.FloatTensor(X_lstm_scaled).unsqueeze(0)

    with torch.no_grad():
        lstm_prob = lstm_model(X_lstm_tensor).item()

    # Ensemble
    ensemble_prob = XGBOOST_WEIGHT * xgb_prob + LSTM_WEIGHT * lstm_prob

    return {
        'prob_up': ensemble_prob,
        'xgb_prob': xgb_prob,
        'lstm_prob': lstm_prob,
        'source': 'kalman_ml'
    }


# ============================================================
# Kalman Filter 2: DB (Milvus Pattern Matching)
# ============================================================

def build_embedding(window: pd.DataFrame) -> np.ndarray:
    """Build 128-dim embedding (matching embedding_generator.py)"""
    embedding = []

    # 1. Price Pattern (24 dims)
    close_pattern = window["close"].values[-24:]
    if len(close_pattern) < 24:
        close_pattern = np.pad(close_pattern, (24 - len(close_pattern), 0), mode="edge")
    embedding.extend(close_pattern)

    # 2. Technical Indicators (48 dims)
    for col in ["rsi_14"]:
        if col in window.columns:
            vals = window[col].values[-6:]
            if len(vals) < 6:
                vals = np.pad(vals, (6 - len(vals), 0), mode="edge")
            embedding.extend(vals)
        else:
            embedding.extend([0] * 6)

    for col in ["macd_line", "macd_signal", "macd_histogram"]:
        if col in window.columns:
            vals = window[col].values[-4:]
            if len(vals) < 4:
                vals = np.pad(vals, (4 - len(vals), 0), mode="edge")
            embedding.extend(vals)
        else:
            embedding.extend([0] * 4)

    for col in ["bb_percent", "bb_bandwidth"]:
        if col in window.columns:
            vals = window[col].values[-6:]
            if len(vals) < 6:
                vals = np.pad(vals, (6 - len(vals), 0), mode="edge")
            embedding.extend(vals)
        else:
            embedding.extend([0] * 6)

    for col in ["stoch_k", "stoch_d"]:
        if col in window.columns:
            vals = window[col].values[-3:]
            if len(vals) < 3:
                vals = np.pad(vals, (3 - len(vals), 0), mode="edge")
            embedding.extend(vals)
        else:
            embedding.extend([0] * 3)

    for col in ["dist_ema_9", "dist_ema_21", "dist_ema_50"]:
        if col in window.columns:
            vals = window[col].values[-4:]
            if len(vals) < 4:
                vals = np.pad(vals, (4 - len(vals), 0), mode="edge")
            embedding.extend(vals)
        else:
            embedding.extend([0] * 4)

    # 3. Volume Pattern (16 dims)
    if "volume_ratio" in window.columns:
        vol_pattern = window["volume_ratio"].values[-8:]
        if len(vol_pattern) < 8:
            vol_pattern = np.pad(vol_pattern, (8 - len(vol_pattern), 0), mode="edge")
        embedding.extend(vol_pattern)
    else:
        embedding.extend([0] * 8)

    if "volume" in window.columns:
        vol_norm = window["volume"].values[-8:]
        if len(vol_norm) < 8:
            vol_norm = np.pad(vol_norm, (8 - len(vol_norm), 0), mode="edge")
        embedding.extend(vol_norm)
    else:
        embedding.extend([0] * 8)

    # 4. Momentum Features (24 dims)
    for col in ["returns_1h", "returns_4h", "returns_24h"]:
        if col in window.columns:
            vals = window[col].values[-4:]
            if len(vals) < 4:
                vals = np.pad(vals, (4 - len(vals), 0), mode="edge")
            embedding.extend(vals)
        else:
            embedding.extend([0] * 4)

    for col in ["roc_10", "roc_20"]:
        if col in window.columns:
            vals = window[col].values[-4:]
            if len(vals) < 4:
                vals = np.pad(vals, (4 - len(vals), 0), mode="edge")
            embedding.extend(vals)
        else:
            embedding.extend([0] * 4)

    for col in ["williams_r", "cci_20"]:
        if col in window.columns:
            vals = window[col].values[-2:]
            if len(vals) < 2:
                vals = np.pad(vals, (2 - len(vals), 0), mode="edge")
            embedding.extend(vals)
        else:
            embedding.extend([0] * 2)

    # 5. Context Features (16 dims)
    if "timestamp" in window.columns:
        ts = pd.to_datetime(window["timestamp"].iloc[-1])
        embedding.extend([
            np.sin(2 * np.pi * ts.hour / 24),
            np.cos(2 * np.pi * ts.hour / 24),
            np.sin(2 * np.pi * ts.dayofweek / 7),
            np.cos(2 * np.pi * ts.dayofweek / 7),
            np.sin(2 * np.pi * ts.month / 12),
            np.cos(2 * np.pi * ts.month / 12)
        ])
    else:
        embedding.extend([0] * 6)

    if "atr_percent" in window.columns:
        atr_vals = window["atr_percent"].values[-4:]
        if len(atr_vals) < 4:
            atr_vals = np.pad(atr_vals, (4 - len(atr_vals), 0), mode="edge")
        embedding.extend(atr_vals)
    else:
        embedding.extend([0] * 4)

    if "range_percent" in window.columns:
        range_vals = window["range_percent"].values[-6:]
        if len(range_vals) < 6:
            range_vals = np.pad(range_vals, (6 - len(range_vals), 0), mode="edge")
        embedding.extend(range_vals)
    else:
        embedding.extend([0] * 6)

    embedding = np.array(embedding, dtype=np.float32)

    # Ensure correct dimension
    if len(embedding) < EMBEDDING_DIM:
        embedding = np.pad(embedding, (0, EMBEDDING_DIM - len(embedding)), mode="constant")
    elif len(embedding) > EMBEDDING_DIM:
        embedding = embedding[:EMBEDDING_DIM]

    return np.nan_to_num(embedding, nan=0.0, posinf=1.0, neginf=-1.0)


def predict_kalman_db(symbol: str, df: pd.DataFrame) -> dict:
    """Kalman Filter 2: Milvus pattern matching prediction"""
    # Connect to Milvus
    connections.connect("default", host=MILVUS_HOST, port=MILVUS_PORT)
    collection = Collection(COLLECTION_NAME)
    collection.load()

    # Normalize features for embedding
    df_norm = df.copy()
    normalize_cols = ["open", "high", "low", "close", "volume", "ema_9", "ema_21", "ema_50",
                      "macd_line", "macd_signal", "macd_histogram", "rsi_14"]
    available = [c for c in normalize_cols if c in df_norm.columns]
    if available:
        scaler = StandardScaler()
        df_norm[available] = scaler.fit_transform(df_norm[available].fillna(0))

    # Build embedding
    window = df_norm.iloc[-SEQUENCE_LENGTH:]
    embedding = build_embedding(window)

    # Search Milvus
    results = collection.search(
        data=[embedding.tolist()],
        anns_field="embedding",
        param={"metric_type": "L2", "params": {"nprobe": 16}},
        limit=TOP_K_PATTERNS,
        expr=f'symbol == "{symbol}"',
        output_fields=["target_direction", "target_return_24h"]
    )

    if not results or len(results[0]) == 0:
        return {'prob_up': 0.5, 'patterns_found': 0, 'source': 'kalman_db'}

    # Aggregate results
    total_weight = 0.0
    weighted_up = 0.0

    for hit in results[0]:
        similarity = 1.0 / (1.0 + hit.distance)
        direction = hit.entity.get("target_direction")

        total_weight += similarity
        if direction == 1:
            weighted_up += similarity

    prob_up = weighted_up / total_weight if total_weight > 0 else 0.5

    return {
        'prob_up': prob_up,
        'patterns_found': len(results[0]),
        'source': 'kalman_db'
    }


# ============================================================
# Kalman Filter 3: Sentiment (Placeholder)
# ============================================================

def predict_kalman_sentiment(symbol: str) -> dict:
    """
    Kalman Filter 3: Sentiment analysis prediction using FinBERT
    Analyzes recent news headlines and returns bullish/bearish probability
    """
    try:
        # Import sentiment module
        from sentiment_predict import (
            fetch_cryptopanic_news,
            fetch_rss_news,
            fetch_sample_news,
            analyze_sentiment_finbert,
            aggregate_sentiment
        )

        # Fetch news from multiple sources
        all_news = []

        # Try CryptoPanic
        cryptopanic_news = fetch_cryptopanic_news(symbol, 24)
        all_news.extend(cryptopanic_news)

        # Try RSS feeds
        rss_news = fetch_rss_news(symbol)
        all_news.extend(rss_news)

        # Fallback to sample if no news
        if not all_news:
            all_news = fetch_sample_news(symbol)

        # Remove duplicates
        seen = set()
        unique_news = []
        for item in all_news:
            title = item.get("title", "")
            if title and title not in seen:
                seen.add(title)
                unique_news.append(item)

        # Analyze sentiment
        titles = [item["title"] for item in unique_news if item.get("title")]
        sentiment_results = analyze_sentiment_finbert(titles)

        # Aggregate
        aggregated = aggregate_sentiment(sentiment_results)

        return {
            'prob_up': aggregated['prob_up'],
            'sentiment_score': aggregated['sentiment_score'],
            'news_count': aggregated['total_news'],
            'positive_count': aggregated['positive_count'],
            'negative_count': aggregated['negative_count'],
            'neutral_count': aggregated['neutral_count'],
            'source': 'kalman_sentiment',
            'status': 'active',
            'model': 'finbert'
        }

    except Exception as e:
        print(f"   Sentiment error: {e}")
        # Fallback to neutral
        return {
            'prob_up': 0.5,
            'sentiment_score': 0.0,
            'news_count': 0,
            'source': 'kalman_sentiment',
            'status': 'error',
            'error': str(e)
        }


# ============================================================
# Kalman Filter 4: Enhanced Market Data
# ============================================================

def predict_kalman_enhanced(symbol: str) -> dict:
    """
    Kalman Filter 4: Enhanced market data analysis
    Uses Fear & Greed, CoinGecko, multi-timeframe trends, and order book data
    """
    try:
        from enhanced_data_fetcher import EnhancedDataFetcher

        fetcher = EnhancedDataFetcher(verify_ssl=False)
        data = fetcher.get_all_enhanced_data(symbol)
        features = fetcher.calculate_enhanced_features(data)

        # Calculate probability based on multiple signals
        signals = []
        weights = []

        # 1. Fear & Greed Index (contrarian)
        fg_value = features.get("fear_greed_value", 50)
        if fg_value < 25:  # Extreme fear = bullish
            fg_signal = 0.7
        elif fg_value > 75:  # Extreme greed = bearish
            fg_signal = 0.3
        elif fg_value < 40:  # Fear
            fg_signal = 0.6
        elif fg_value > 60:  # Greed
            fg_signal = 0.4
        else:  # Neutral
            fg_signal = 0.5
        signals.append(fg_signal)
        weights.append(0.25)

        # 2. CoinGecko momentum
        if "coingecko" in data:
            cg = data["coingecko"]
            change_7d = cg.get("price_change_7d", 0)
            change_30d = cg.get("price_change_30d", 0)

            # 7-day momentum
            if change_7d > 10:
                mom_7d = 0.7
            elif change_7d < -10:
                mom_7d = 0.3
            elif change_7d > 5:
                mom_7d = 0.6
            elif change_7d < -5:
                mom_7d = 0.4
            else:
                mom_7d = 0.5

            # 30-day momentum
            if change_30d > 20:
                mom_30d = 0.65
            elif change_30d < -20:
                mom_30d = 0.35
            else:
                mom_30d = 0.5

            momentum_signal = 0.6 * mom_7d + 0.4 * mom_30d
            signals.append(momentum_signal)
            weights.append(0.25)
        else:
            signals.append(0.5)
            weights.append(0.25)

        # 3. Trend alignment
        trend_align = features.get("trend_alignment", 0)
        trend_signal = 0.5 + trend_align * 0.3  # Scale to 0.2-0.8
        trend_signal = max(0.2, min(0.8, trend_signal))
        signals.append(trend_signal)
        weights.append(0.25)

        # 4. Order book / Futures data (if available)
        ob_signal = 0.5
        if data.get("order_book", {}).get("basic", {}):
            imbalance = data["order_book"]["basic"].get("imbalance", 0)
            ob_signal = 0.5 + imbalance * 0.3  # Scale imbalance
            ob_signal = max(0.3, min(0.7, ob_signal))
        elif data.get("futures", {}).get("long_short_ratio", {}):
            ls_ratio = data["futures"]["long_short_ratio"].get("long_short_ratio", 1.0)
            # High long/short = potentially overbought (contrarian)
            if ls_ratio > 1.5:
                ob_signal = 0.4
            elif ls_ratio < 0.7:
                ob_signal = 0.6
            else:
                ob_signal = 0.5
        signals.append(ob_signal)
        weights.append(0.25)

        # Weighted average
        prob_up = sum(s * w for s, w in zip(signals, weights)) / sum(weights)

        return {
            'prob_up': prob_up,
            'fear_greed_value': fg_value,
            'fear_greed_signal': fg_signal,
            'momentum_signal': signals[1] if len(signals) > 1 else 0.5,
            'trend_signal': trend_signal,
            'order_book_signal': ob_signal,
            'composite_signal': features.get("composite_signal", 0),
            'source': 'kalman_enhanced',
            'status': 'active',
            'data_sources': list(data.keys())
        }

    except Exception as e:
        print(f"   Enhanced data error: {e}")
        return {
            'prob_up': 0.5,
            'source': 'kalman_enhanced',
            'status': 'error',
            'error': str(e)
        }


# ============================================================
# Kalman Filter 5: RAG (E-book Knowledge)
# ============================================================

def predict_kalman_rag(symbol: str, df: pd.DataFrame) -> dict:
    """
    Kalman Filter 5: RAG e-book knowledge prediction
    Retrieves relevant trading knowledge from e-books
    """
    try:
        from rag_query import predict_kalman_rag as rag_predict

        # Build market context from current data
        latest = df.iloc[-1]

        market_context = {}

        # RSI
        if 'rsi_14' in latest:
            market_context['rsi'] = float(latest['rsi_14'])

        # MACD
        if 'macd_histogram' in latest:
            macd = float(latest['macd_histogram'])
            if macd > 0 and latest.get('macd_histogram', 0) > df.iloc[-2].get('macd_histogram', 0):
                market_context['macd_signal'] = 'bullish_crossover'
            elif macd < 0 and latest.get('macd_histogram', 0) < df.iloc[-2].get('macd_histogram', 0):
                market_context['macd_signal'] = 'bearish_crossover'

        # Trend
        if 'dist_ema_50' in latest:
            dist_50 = float(latest['dist_ema_50'])
            if dist_50 > 2:
                market_context['trend'] = 'up'
            elif dist_50 < -2:
                market_context['trend'] = 'down'
            else:
                market_context['trend'] = 'sideways'

        # Volatility
        if 'atr_percent' in latest:
            atr = float(latest['atr_percent'])
            market_context['high_volatility'] = atr > 3

        # Volume
        if 'volume_ratio' in latest:
            vol_ratio = float(latest['volume_ratio'])
            market_context['volume_spike'] = vol_ratio > 1.5

        # Call RAG service
        result = rag_predict(symbol, market_context)

        return {
            'prob_up': result.get('prob_up', 0.5),
            'confidence': result.get('confidence', 0.0),
            'direction': result.get('direction', 'neutral'),
            'reasoning': result.get('reasoning', ''),
            'knowledge_sources': result.get('knowledge_sources', []),
            'source': 'kalman_rag',
            'status': result.get('status', 'unknown')
        }

    except ImportError:
        print("   RAG module not available (rag_query.py not found)")
        return {
            'prob_up': 0.5,
            'confidence': 0.0,
            'source': 'kalman_rag',
            'status': 'not_available',
            'error': 'RAG module not installed'
        }
    except Exception as e:
        print(f"   RAG error: {e}")
        return {
            'prob_up': 0.5,
            'confidence': 0.0,
            'source': 'kalman_rag',
            'status': 'error',
            'error': str(e)
        }


# ============================================================
# Kalman Fusion
# ============================================================

def kalman_fusion(symbol: str, threshold: float = 0.5, use_rag: bool = True):
    """
    Combine all Kalman Filters into final signal

    Final Signal = ML + DB + Sentiment + Enhanced + RAG (weighted)
    """
    print("=" * 70)
    print("SURGE-AI Trading - Kalman Filter Signal Fusion v4")
    print("=" * 70)
    print(f"Symbol: {symbol}")
    print(f"Threshold: {threshold}")
    print(f"RAG Enabled: {use_rag}")
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    if use_rag:
        print(f"\nKalman Weights: ML={KALMAN_ML_WEIGHT:.0%}, DB={KALMAN_DB_WEIGHT:.0%}, "
              f"Sentiment={KALMAN_SENTIMENT_WEIGHT:.0%}, Enhanced={KALMAN_ENHANCED_WEIGHT:.0%}, "
              f"RAG={KALMAN_RAG_WEIGHT:.0%}")
    else:
        # Redistribute RAG weight when disabled
        adj_ml = KALMAN_ML_WEIGHT + (KALMAN_RAG_WEIGHT * 0.6)
        adj_sent = KALMAN_SENTIMENT_WEIGHT + (KALMAN_RAG_WEIGHT * 0.2)
        adj_enh = KALMAN_ENHANCED_WEIGHT + (KALMAN_RAG_WEIGHT * 0.2)
        print(f"\nKalman Weights (RAG disabled): ML={adj_ml:.0%}, DB={KALMAN_DB_WEIGHT:.0%}, "
              f"Sentiment={adj_sent:.0%}, Enhanced={adj_enh:.0%}")

    # Get latest data
    step_count = 6 if use_rag else 5
    print(f"\n[1/{step_count}] Fetching market data...")
    df = get_latest_features(symbol, n_rows=50)
    latest = df.iloc[-1]
    print(f"      Latest: {latest['timestamp']} | Price: ${latest['close']:,.2f}")

    # Kalman Filter 1: ML
    print(f"\n[2/{step_count}] Kalman Filter 1 (ML: XGBoost + LSTM)...")
    try:
        kf1 = predict_kalman_ml(symbol, df)
        print(f"      XGBoost: {kf1['xgb_prob']*100:.1f}% UP")
        print(f"      LSTM:    {kf1['lstm_prob']*100:.1f}% UP")
        print(f"      ML Ensemble: {kf1['prob_up']*100:.1f}% UP")
    except Exception as e:
        print(f"      ERROR: {e}")
        kf1 = {'prob_up': 0.5}

    # Kalman Filter 2: DB
    print(f"\n[3/{step_count}] Kalman Filter 2 (DB: Milvus Pattern Matching)...")
    try:
        kf2 = predict_kalman_db(symbol, df)
        print(f"      Patterns: {kf2['patterns_found']}")
        print(f"      Historical: {kf2['prob_up']*100:.1f}% UP")
    except Exception as e:
        print(f"      ERROR: {e}")
        kf2 = {'prob_up': 0.5, 'patterns_found': 0}

    # Kalman Filter 3: Sentiment
    print(f"\n[4/{step_count}] Kalman Filter 3 (Sentiment: FinBERT)...")
    kf3 = predict_kalman_sentiment(symbol)
    print(f"      Status: {kf3['status']}")
    print(f"      News Articles: {kf3.get('news_count', 0)}")
    if kf3.get('news_count', 0) > 0:
        print(f"      Positive/Negative/Neutral: {kf3.get('positive_count', 0)}/{kf3.get('negative_count', 0)}/{kf3.get('neutral_count', 0)}")
        print(f"      Sentiment Score: {kf3.get('sentiment_score', 0):+.2f}")
    print(f"      Probability UP: {kf3['prob_up']*100:.1f}%")

    # Kalman Filter 4: Enhanced Market Data
    print(f"\n[5/{step_count}] Kalman Filter 4 (Enhanced: Market Structure)...")
    kf4 = predict_kalman_enhanced(symbol)
    print(f"      Status: {kf4.get('status', 'unknown')}")
    if kf4.get('status') == 'active':
        print(f"      Data Sources: {', '.join(kf4.get('data_sources', []))}")
        print(f"      Fear & Greed: {kf4.get('fear_greed_value', 50)} ({kf4.get('fear_greed_signal', 0.5)*100:.0f}% UP)")
        print(f"      Momentum Signal: {kf4.get('momentum_signal', 0.5)*100:.0f}% UP")
        print(f"      Trend Alignment: {kf4.get('trend_signal', 0.5)*100:.0f}% UP")
    print(f"      Probability UP: {kf4['prob_up']*100:.1f}%")

    # Kalman Filter 5: RAG (E-book Knowledge)
    kf5 = {'prob_up': 0.5, 'status': 'disabled'}
    if use_rag:
        print(f"\n[6/{step_count}] Kalman Filter 5 (RAG: E-book Knowledge)...")
        kf5 = predict_kalman_rag(symbol, df)
        print(f"      Status: {kf5.get('status', 'unknown')}")
        if kf5.get('status') == 'active':
            print(f"      Direction: {kf5.get('direction', 'neutral')}")
            print(f"      Confidence: {kf5.get('confidence', 0)*100:.1f}%")
            if kf5.get('knowledge_sources'):
                print(f"      Sources: {len(kf5['knowledge_sources'])} books")
                for src in kf5['knowledge_sources'][:2]:
                    print(f"         - {src['book']} ({src['category']})")
            if kf5.get('reasoning'):
                print(f"      Reasoning: {kf5['reasoning'][:80]}...")
        print(f"      Probability UP: {kf5['prob_up']*100:.1f}%")

    # Kalman Fusion
    if use_rag:
        final_prob_up = (
            KALMAN_ML_WEIGHT * kf1['prob_up'] +
            KALMAN_DB_WEIGHT * kf2['prob_up'] +
            KALMAN_SENTIMENT_WEIGHT * kf3['prob_up'] +
            KALMAN_ENHANCED_WEIGHT * kf4['prob_up'] +
            KALMAN_RAG_WEIGHT * kf5['prob_up']
        )
    else:
        # Redistribute RAG weight when disabled
        adj_ml = KALMAN_ML_WEIGHT + (KALMAN_RAG_WEIGHT * 0.6)
        adj_sent = KALMAN_SENTIMENT_WEIGHT + (KALMAN_RAG_WEIGHT * 0.2)
        adj_enh = KALMAN_ENHANCED_WEIGHT + (KALMAN_RAG_WEIGHT * 0.2)
        final_prob_up = (
            adj_ml * kf1['prob_up'] +
            KALMAN_DB_WEIGHT * kf2['prob_up'] +
            adj_sent * kf3['prob_up'] +
            adj_enh * kf4['prob_up']
        )

    # Determine signal
    if final_prob_up >= threshold:
        signal = "LONG"
        confidence = final_prob_up
    elif final_prob_up <= (1 - threshold):
        signal = "SHORT"
        confidence = 1 - final_prob_up
    else:
        signal = "HOLD"
        confidence = max(final_prob_up, 1 - final_prob_up)

    # Display results
    print("\n" + "=" * 70)
    print("KALMAN FILTER FUSION RESULT")
    print("=" * 70)

    print(f"\n>>> SIGNAL BREAKDOWN <<<")
    print(f"   Kalman 1 (ML):        {kf1['prob_up']*100:5.1f}% UP  x {KALMAN_ML_WEIGHT:.0%} = {kf1['prob_up']*KALMAN_ML_WEIGHT*100:5.1f}%")
    print(f"   Kalman 2 (DB):        {kf2['prob_up']*100:5.1f}% UP  x {KALMAN_DB_WEIGHT:.0%} = {kf2['prob_up']*KALMAN_DB_WEIGHT*100:5.1f}%")
    print(f"   Kalman 3 (Sentiment): {kf3['prob_up']*100:5.1f}% UP  x {KALMAN_SENTIMENT_WEIGHT:.0%} = {kf3['prob_up']*KALMAN_SENTIMENT_WEIGHT*100:5.1f}%")
    print(f"   Kalman 4 (Enhanced):  {kf4['prob_up']*100:5.1f}% UP  x {KALMAN_ENHANCED_WEIGHT:.0%} = {kf4['prob_up']*KALMAN_ENHANCED_WEIGHT*100:5.1f}%")
    if use_rag:
        print(f"   Kalman 5 (RAG):       {kf5['prob_up']*100:5.1f}% UP  x {KALMAN_RAG_WEIGHT:.0%} = {kf5['prob_up']*KALMAN_RAG_WEIGHT*100:5.1f}%")
    print(f"   " + "-" * 60)
    print(f"   FINAL PROBABILITY:    {final_prob_up*100:5.1f}% UP")

    # Color coding
    if signal == "LONG":
        signal_str = f"\033[92m{signal}\033[0m"
    elif signal == "SHORT":
        signal_str = f"\033[91m{signal}\033[0m"
    else:
        signal_str = f"\033[93m{signal}\033[0m"

    print(f"\n>>> FINAL SIGNAL: {signal_str} <<<")
    print(f"   Confidence: {confidence*100:.1f}%")
    print(f"   Price: ${latest['close']:,.2f}")
    print(f"   Time: {latest['timestamp']}")

    # Return result
    result = {
        'time': latest['timestamp'],
        'symbol': symbol,
        'price': latest['close'],
        'signal': signal,
        'confidence': confidence,
        'final_prob_up': final_prob_up,
        'final_prob_down': 1 - final_prob_up,
        'kalman_ml_prob': kf1['prob_up'],
        'kalman_db_prob': kf2['prob_up'],
        'kalman_sentiment_prob': kf3['prob_up'],
        'kalman_enhanced_prob': kf4['prob_up'],
        'kalman_rag_prob': kf5['prob_up'] if use_rag else None,
        'kalman_ml_weight': KALMAN_ML_WEIGHT,
        'kalman_db_weight': KALMAN_DB_WEIGHT,
        'kalman_sentiment_weight': KALMAN_SENTIMENT_WEIGHT,
        'kalman_enhanced_weight': KALMAN_ENHANCED_WEIGHT,
        'kalman_rag_weight': KALMAN_RAG_WEIGHT if use_rag else None,
        'patterns_found': kf2.get('patterns_found', 0),
        'fear_greed_value': kf4.get('fear_greed_value', 50),
        'rag_enabled': use_rag,
        'rag_status': kf5.get('status', 'disabled'),
        'rag_direction': kf5.get('direction', None) if use_rag else None,
        'rag_confidence': kf5.get('confidence', 0) if use_rag else None,
        'rag_reasoning': kf5.get('reasoning', '') if use_rag else None,
        'rag_sources': kf5.get('knowledge_sources', []) if use_rag else [],
        'model': 'kalman_fusion_v4'
    }

    return result


def save_signal_to_db(signal: dict):
    """Save fused signal to trade_signals table"""
    import json as json_lib
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()

    # Convert numpy types to native Python types for PostgreSQL
    confidence = float(signal['confidence']) if signal['confidence'] is not None else None
    k1_signal = float(signal.get('kalman_ml_prob', 0.5))
    k2_signal = float(signal.get('kalman_db_prob', 0.5))
    k3_signal = float(signal.get('kalman_sentiment_prob', 0.5))
    final_signal = confidence / 100.0 if confidence else 0.5

    # Store additional data in metadata
    metadata = {
        'price': float(signal['price']) if signal.get('price') else None,
        'model': 'kalman_fusion_v4',
        'k4_probability': float(signal.get('kalman_enhanced_prob', 0.5)),
        'k5_probability': float(signal.get('kalman_rag_prob', 0.5)),
        'rag_enabled': signal.get('rag_enabled', False)
    }

    cur.execute("""
        INSERT INTO trade_signals (time, symbol, signal_type, confidence, kalman_1_signal, kalman_2_signal, kalman_3_signal, final_signal, metadata)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        signal['time'],
        signal['symbol'],
        signal['signal'],
        confidence,
        k1_signal,
        k2_signal,
        k3_signal,
        final_signal,
        json_lib.dumps(metadata)
    ))

    conn.commit()
    cur.close()
    conn.close()

    print(f"\nSignal saved to database!")


def main():
    parser = argparse.ArgumentParser(description='SURGE-AI Kalman Filter Signal Fusion v4')
    parser.add_argument('--symbol', type=str, default='BTCUSDT', help='Symbol to predict')
    parser.add_argument('--threshold', type=float, default=0.5, help='Confidence threshold')
    parser.add_argument('--save', action='store_true', help='Save signal to database')
    parser.add_argument('--no-rag', action='store_true', help='Disable RAG knowledge (faster)')
    args = parser.parse_args()

    use_rag = not args.no_rag
    signal = kalman_fusion(args.symbol, args.threshold, use_rag=use_rag)

    if signal and args.save:
        save_signal_to_db(signal)

    print("\n" + "=" * 70)


if __name__ == "__main__":
    main()
