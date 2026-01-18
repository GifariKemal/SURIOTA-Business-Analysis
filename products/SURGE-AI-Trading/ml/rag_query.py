"""
SURGE-AI Trading - RAG Query Service
Retrieves relevant knowledge from e-books for trading decisions

This module implements the RAG (Retrieval Augmented Generation) system
for incorporating e-book trading knowledge into signal generation.

Usage:
    python rag_query.py --query "RSI divergence in uptrend"
    python rag_query.py --market-context '{"rsi": 75, "trend": "up"}'
    python rag_query.py --generate-signal --symbol BTCUSDT
"""

import argparse
import json
import os
import time
from typing import List, Dict, Optional
from datetime import datetime

import numpy as np
import psycopg2
from pymilvus import connections, Collection, utility
from filterpy.kalman import KalmanFilter

# Configuration
DB_CONFIG = {
    "host": os.environ.get("POSTGRES_HOST", "localhost"),
    "port": int(os.environ.get("POSTGRES_PORT", 5432)),
    "database": os.environ.get("POSTGRES_DB", "surge_trading"),
    "user": os.environ.get("POSTGRES_USER", "postgres"),
    "password": os.environ.get("POSTGRES_PASSWORD", "surge_secret_2024")
}

MILVUS_HOST = os.environ.get("MILVUS_HOST", "localhost")
MILVUS_PORT = os.environ.get("MILVUS_PORT", "19530")
COLLECTION_NAME = "ebook_knowledge"
EMBEDDING_DIM = 384

# Query settings
DEFAULT_TOP_K = 5
MIN_SIMILARITY = 0.3
CATEGORY_WEIGHTS = {
    'technical': 1.2,      # Boost technical analysis
    'risk': 1.1,           # Boost risk management
    'psychology': 1.0,
    'fundamental': 0.9,
    'general': 0.8
}


class RAGQueryService:
    """Service for querying e-book knowledge base"""

    def __init__(self):
        self.embedding_model = None
        self.kalman_filter = None
        self._setup_kalman()
        self._load_embedding_model()

    def _load_embedding_model(self):
        """Load sentence transformer for query embeddings"""
        try:
            from sentence_transformers import SentenceTransformer
            self.embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
            print("RAG embedding model loaded: all-MiniLM-L6-v2")
        except ImportError:
            print("WARNING: sentence-transformers not installed")
            self.embedding_model = None

    def _setup_kalman(self):
        """Initialize Kalman filter for RAG signal smoothing"""
        self.kalman_filter = KalmanFilter(dim_x=2, dim_z=1)

        # State transition matrix
        self.kalman_filter.F = np.array([[1., 1.],
                                          [0., 1.]])

        # Measurement matrix
        self.kalman_filter.H = np.array([[1., 0.]])

        # Measurement noise (adjusted by confidence)
        self.kalman_filter.R = np.array([[0.1]])

        # Process noise
        self.kalman_filter.Q = np.array([[0.01, 0.01],
                                          [0.01, 0.02]])

        # Initial state
        self.kalman_filter.x = np.array([[0.],
                                          [0.]])

        # Initial covariance
        self.kalman_filter.P = np.eye(2) * 0.1

    def build_query_from_context(self, market_context: Dict) -> str:
        """Build search query from market context"""
        parts = []

        # Price action
        if market_context.get('trend'):
            trend = market_context['trend']
            parts.append(f"{trend} trend trading strategy")

        # RSI conditions
        if market_context.get('rsi'):
            rsi = market_context['rsi']
            if rsi > 70:
                parts.append("overbought RSI divergence reversal")
            elif rsi < 30:
                parts.append("oversold RSI reversal buy signal")
            elif rsi > 60:
                parts.append("RSI momentum continuation")
            elif rsi < 40:
                parts.append("RSI weakness bearish")

        # MACD
        if market_context.get('macd_signal'):
            macd = market_context['macd_signal']
            if macd == 'bullish_crossover':
                parts.append("MACD bullish crossover buy")
            elif macd == 'bearish_crossover':
                parts.append("MACD bearish crossover sell")
            elif macd == 'bullish_divergence':
                parts.append("MACD bullish divergence reversal")
            elif macd == 'bearish_divergence':
                parts.append("MACD bearish divergence top")

        # Patterns
        if market_context.get('pattern'):
            pattern = market_context['pattern']
            parts.append(f"{pattern} chart pattern breakout")

        # Volume
        if market_context.get('volume_spike'):
            parts.append("high volume breakout confirmation")

        # Support/Resistance
        if market_context.get('near_support'):
            parts.append("support level bounce buy")
        if market_context.get('near_resistance'):
            parts.append("resistance level rejection sell")

        # Volatility
        if market_context.get('high_volatility'):
            parts.append("high volatility position sizing risk")

        # Sentiment
        if market_context.get('sentiment'):
            sentiment = market_context['sentiment']
            if sentiment > 0.3:
                parts.append("bullish sentiment momentum")
            elif sentiment < -0.3:
                parts.append("bearish sentiment fear")

        return " ".join(parts) if parts else "crypto trading strategy market analysis"

    def query_knowledge(
        self,
        query: str,
        category: Optional[str] = None,
        top_k: int = DEFAULT_TOP_K,
        min_similarity: float = MIN_SIMILARITY
    ) -> List[Dict]:
        """
        Query knowledge base for relevant chunks

        Args:
            query: Search query string
            category: Filter by category (optional)
            top_k: Number of results to return
            min_similarity: Minimum cosine similarity threshold

        Returns:
            List of relevant knowledge chunks with metadata
        """
        if self.embedding_model is None:
            raise RuntimeError("Embedding model not loaded")

        # Connect to Milvus
        connections.connect("default", host=MILVUS_HOST, port=MILVUS_PORT)

        if not utility.has_collection(COLLECTION_NAME):
            print(f"Collection '{COLLECTION_NAME}' not found")
            return []

        collection = Collection(COLLECTION_NAME)
        collection.load()

        # Generate query embedding
        query_embedding = self.embedding_model.encode(query).tolist()

        # Search parameters
        search_params = {
            "metric_type": "COSINE",
            "params": {"nprobe": 16}
        }

        # Category filter
        expr = f'category == "{category}"' if category else None

        # Search
        results = collection.search(
            data=[query_embedding],
            anns_field="embedding",
            param=search_params,
            limit=top_k * 2,  # Get extra for filtering
            expr=expr,
            output_fields=['content', 'book_title', 'chapter', 'category', 'keywords', 'relevance_score']
        )

        # Process results
        knowledge_chunks = []
        for hit in results[0]:
            similarity = hit.score  # Cosine similarity (higher is better)

            if similarity < min_similarity:
                continue

            # Apply category weight
            cat = hit.entity.get('category', 'general')
            weighted_score = similarity * CATEGORY_WEIGHTS.get(cat, 1.0)

            knowledge_chunks.append({
                'content': hit.entity.get('content'),
                'book_title': hit.entity.get('book_title'),
                'chapter': hit.entity.get('chapter'),
                'category': cat,
                'keywords': hit.entity.get('keywords'),
                'relevance_score': hit.entity.get('relevance_score', 0),
                'similarity': similarity,
                'weighted_score': weighted_score
            })

        # Sort by weighted score and return top_k
        knowledge_chunks.sort(key=lambda x: x['weighted_score'], reverse=True)
        return knowledge_chunks[:top_k]

    def extract_signal_from_knowledge(self, chunks: List[Dict]) -> Dict:
        """
        Extract trading signal from knowledge chunks

        Args:
            chunks: List of knowledge chunks from query

        Returns:
            Signal dictionary with direction and reasoning
        """
        if not chunks:
            return {
                'signal': 0.0,
                'direction': 'neutral',
                'confidence': 0.0,
                'reasoning': 'No relevant knowledge found'
            }

        # Keyword-based signal extraction
        bullish_keywords = [
            'buy', 'long', 'bullish', 'support', 'accumulation', 'breakout',
            'uptrend', 'reversal from bottom', 'oversold bounce', 'momentum up',
            'higher high', 'higher low', 'golden cross', 'bull flag'
        ]

        bearish_keywords = [
            'sell', 'short', 'bearish', 'resistance', 'distribution', 'breakdown',
            'downtrend', 'reversal from top', 'overbought', 'momentum down',
            'lower high', 'lower low', 'death cross', 'bear flag'
        ]

        neutral_keywords = [
            'hold', 'wait', 'consolidation', 'range', 'sideways',
            'uncertainty', 'mixed signals', 'no clear direction'
        ]

        # Analyze each chunk
        signal_scores = []
        reasoning_parts = []

        for chunk in chunks:
            content = chunk['content'].lower()
            weight = chunk['weighted_score']

            # Count keyword occurrences
            bullish_count = sum(1 for kw in bullish_keywords if kw in content)
            bearish_count = sum(1 for kw in bearish_keywords if kw in content)
            neutral_count = sum(1 for kw in neutral_keywords if kw in content)

            total_signals = bullish_count + bearish_count + neutral_count
            if total_signals == 0:
                continue

            # Calculate chunk signal (-1 to 1)
            chunk_signal = (bullish_count - bearish_count) / (total_signals + 1)
            chunk_signal = chunk_signal * weight  # Weight by similarity

            signal_scores.append(chunk_signal)

            # Build reasoning
            if bullish_count > bearish_count:
                reasoning_parts.append(f"'{chunk['book_title']}' suggests bullish bias")
            elif bearish_count > bullish_count:
                reasoning_parts.append(f"'{chunk['book_title']}' suggests bearish bias")

        # Aggregate signals
        if signal_scores:
            raw_signal = np.mean(signal_scores)
            confidence = np.mean([c['similarity'] for c in chunks])
        else:
            raw_signal = 0.0
            confidence = 0.0

        # Clamp signal to [-1, 1]
        raw_signal = max(-1.0, min(1.0, raw_signal))

        # Determine direction
        if raw_signal > 0.1:
            direction = 'bullish'
        elif raw_signal < -0.1:
            direction = 'bearish'
        else:
            direction = 'neutral'

        return {
            'signal': raw_signal,
            'direction': direction,
            'confidence': confidence,
            'reasoning': '; '.join(reasoning_parts[:3]) if reasoning_parts else 'Based on general knowledge'
        }

    def apply_kalman_filter(self, raw_signal: float, confidence: float) -> float:
        """Apply Kalman filter to smooth RAG signal"""
        # Adjust measurement noise based on confidence
        self.kalman_filter.R = np.array([[0.5 - (confidence * 0.4)]])

        # Predict and update
        self.kalman_filter.predict()
        self.kalman_filter.update(np.array([[raw_signal]]))

        return float(self.kalman_filter.x[0, 0])

    def generate_rag_signal(
        self,
        market_context: Dict,
        symbol: str = "BTCUSDT"
    ) -> Dict:
        """
        Generate RAG-based trading signal

        Args:
            market_context: Current market conditions
            symbol: Trading symbol

        Returns:
            Complete RAG signal with sources and reasoning
        """
        print("=" * 60)
        print("SURGE-AI Trading - RAG Knowledge Signal")
        print("=" * 60)
        print(f"Symbol: {symbol}")
        print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

        # Build query from context
        query = self.build_query_from_context(market_context)
        print(f"\nGenerated Query: {query[:100]}...")

        # Query knowledge base
        print("\nQuerying knowledge base...")
        chunks = self.query_knowledge(query, top_k=5)
        print(f"Found {len(chunks)} relevant chunks")

        if chunks:
            print("\nTop Sources:")
            for i, chunk in enumerate(chunks[:3], 1):
                print(f"   {i}. {chunk['book_title']} ({chunk['category']})")
                print(f"      Similarity: {chunk['similarity']:.3f}")

        # Extract signal
        print("\nExtracting signal...")
        signal_data = self.extract_signal_from_knowledge(chunks)

        # Apply Kalman filter
        filtered_signal = self.apply_kalman_filter(
            signal_data['signal'],
            signal_data['confidence']
        )

        # Convert to probability (0-1 scale for UP direction)
        prob_up = (filtered_signal + 1) / 2  # Map [-1,1] to [0,1]

        # Log query
        self._log_query(
            query=query,
            market_context=market_context,
            results_count=len(chunks),
            confidence=signal_data['confidence'],
            signal=prob_up
        )

        # Build result
        result = {
            'prob_up': prob_up,
            'raw_signal': signal_data['signal'],
            'filtered_signal': filtered_signal,
            'direction': signal_data['direction'],
            'confidence': signal_data['confidence'],
            'reasoning': signal_data['reasoning'],
            'knowledge_sources': [
                {
                    'book': c['book_title'],
                    'chapter': c['chapter'],
                    'category': c['category'],
                    'similarity': c['similarity']
                }
                for c in chunks[:3]
            ],
            'query': query,
            'source': 'kalman_rag',
            'status': 'active' if chunks else 'no_knowledge'
        }

        print("\n" + "=" * 60)
        print("RAG SIGNAL RESULT")
        print("=" * 60)
        print(f"Direction: {result['direction'].upper()}")
        print(f"Probability UP: {result['prob_up']*100:.1f}%")
        print(f"Confidence: {result['confidence']*100:.1f}%")
        print(f"Reasoning: {result['reasoning'][:100]}...")

        return result

    def _log_query(
        self,
        query: str,
        market_context: Dict,
        results_count: int,
        confidence: float,
        signal: float
    ):
        """Log query to database for analytics"""
        try:
            conn = psycopg2.connect(**DB_CONFIG)
            cur = conn.cursor()

            cur.execute("""
                INSERT INTO ebook_query_log (query_text, market_context, results_count, confidence_score, signal_contribution)
                VALUES (%s, %s, %s, %s, %s)
            """, (
                query[:1000],
                json.dumps(market_context),
                results_count,
                confidence,
                signal
            ))

            conn.commit()
            cur.close()
            conn.close()
        except Exception as e:
            print(f"Warning: Could not log query: {e}")


def predict_kalman_rag(symbol: str, market_context: Optional[Dict] = None) -> Dict:
    """
    Kalman Filter RAG: E-book knowledge prediction

    This is the main interface for the Kalman fusion system.

    Args:
        symbol: Trading symbol
        market_context: Optional market context (if None, uses default query)

    Returns:
        RAG signal dictionary compatible with kalman_fusion.py
    """
    service = RAGQueryService()

    if market_context is None:
        market_context = {}

    try:
        result = service.generate_rag_signal(market_context, symbol)
        return result
    except Exception as e:
        print(f"RAG error: {e}")
        return {
            'prob_up': 0.5,
            'confidence': 0.0,
            'source': 'kalman_rag',
            'status': 'error',
            'error': str(e)
        }


def interactive_query():
    """Interactive query mode"""
    service = RAGQueryService()

    print("\nSURGE-AI RAG Query (type 'exit' to quit)")
    print("-" * 40)

    while True:
        query = input("\nQuery: ").strip()
        if query.lower() == 'exit':
            break

        if not query:
            continue

        results = service.query_knowledge(query, top_k=5)

        if not results:
            print("No results found.")
            continue

        print(f"\nFound {len(results)} results:")
        for i, r in enumerate(results, 1):
            print(f"\n{i}. {r['book_title']} ({r['category']})")
            print(f"   Similarity: {r['similarity']:.3f}")
            print(f"   Keywords: {r['keywords']}")
            print(f"   Content: {r['content'][:200]}...")


def main():
    parser = argparse.ArgumentParser(description='SURGE-AI RAG Query Service')
    parser.add_argument('--query', type=str, help='Direct query string')
    parser.add_argument('--market-context', type=str, help='Market context as JSON')
    parser.add_argument('--generate-signal', action='store_true', help='Generate trading signal')
    parser.add_argument('--symbol', type=str, default='BTCUSDT', help='Trading symbol')
    parser.add_argument('--category', type=str, help='Filter by category')
    parser.add_argument('--top-k', type=int, default=5, help='Number of results')
    parser.add_argument('--interactive', action='store_true', help='Interactive query mode')

    args = parser.parse_args()

    if args.interactive:
        interactive_query()

    elif args.generate_signal:
        market_context = {}
        if args.market_context:
            market_context = json.loads(args.market_context)

        result = predict_kalman_rag(args.symbol, market_context)
        print(f"\nResult: {json.dumps(result, indent=2, default=str)}")

    elif args.query:
        service = RAGQueryService()
        results = service.query_knowledge(
            query=args.query,
            category=args.category,
            top_k=args.top_k
        )

        print(f"\nFound {len(results)} results:")
        for i, r in enumerate(results, 1):
            print(f"\n{i}. {r['book_title']} ({r['category']})")
            print(f"   Similarity: {r['similarity']:.3f}")
            print(f"   Keywords: {r['keywords']}")
            print(f"   Content: {r['content'][:300]}...")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
