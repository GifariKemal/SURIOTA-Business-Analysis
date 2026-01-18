# ============================================================
# SURGE-AI Trading - ML Service Dockerfile
# Signal generation, model training, and scheduling
# ============================================================

FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app

# Install system dependencies (minimal for pre-built wheels)
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/* \
    || echo "apt-get failed, continuing with base image"

# Copy requirements first (for caching)
COPY requirements.txt .

# Install Python dependencies
# Using CPU-only PyTorch to reduce image size
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir torch --index-url https://download.pytorch.org/whl/cpu && \
    pip install --no-cache-dir -r requirements.txt

# Pre-download HuggingFace models during build (avoids first-run delays)
# This caches FinBERT for sentiment analysis and sentence-transformers for RAG
RUN python -c "from transformers import AutoTokenizer, AutoModelForSequenceClassification; \
    AutoTokenizer.from_pretrained('ProsusAI/finbert'); \
    AutoModelForSequenceClassification.from_pretrained('ProsusAI/finbert'); \
    print('FinBERT model cached')"

RUN python -c "from sentence_transformers import SentenceTransformer; \
    SentenceTransformer('all-MiniLM-L6-v2'); \
    print('Sentence-transformers model cached')"

# Copy application code
COPY . .

# Create directories
RUN mkdir -p /app/models /app/outputs /app/cache /app/data

# Create non-root user for security
RUN useradd --create-home --shell /bin/bash mluser && \
    chown -R mluser:mluser /app
USER mluser

# Health check (check if scheduler is running via Redis)
HEALTHCHECK --interval=60s --timeout=10s --start-period=30s --retries=3 \
    CMD python -c "import redis; r=redis.Redis(host='${REDIS_HOST:-redis}'); print(r.ping())" || exit 1

# Default command: run the scheduler
CMD ["python", "scheduler.py"]
