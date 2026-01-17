#!/bin/bash
# ============================================================
# SURGE-AI Trading Dashboard - Startup Script (Linux/Mac)
# ============================================================

echo ""
echo "========================================"
echo "  SURGE-AI Trading Dashboard"
echo "  Starting services..."
echo "========================================"
echo ""

# Get the script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check if backend venv exists
if [ ! -d "$PROJECT_DIR/backend/venv" ]; then
    echo -e "${YELLOW}[!] Python virtual environment not found.${NC}"
    echo "[>] Creating virtual environment..."
    cd "$PROJECT_DIR/backend"
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    echo -e "${GREEN}[OK] Virtual environment created and dependencies installed.${NC}"
else
    echo -e "${GREEN}[OK] Virtual environment found.${NC}"
fi

# Check if frontend node_modules exists
if [ ! -d "$PROJECT_DIR/frontend/node_modules" ]; then
    echo -e "${YELLOW}[!] Node modules not found.${NC}"
    echo "[>] Installing frontend dependencies..."
    cd "$PROJECT_DIR/frontend"
    npm install
    echo -e "${GREEN}[OK] Frontend dependencies installed.${NC}"
else
    echo -e "${GREEN}[OK] Frontend dependencies found.${NC}"
fi

# Function to cleanup on exit
cleanup() {
    echo ""
    echo "Stopping services..."
    kill $BACKEND_PID 2>/dev/null
    kill $FRONTEND_PID 2>/dev/null
    echo "Services stopped."
    exit 0
}

# Set trap for cleanup
trap cleanup SIGINT SIGTERM

echo ""
echo "========================================"
echo "  Starting Backend (FastAPI)..."
echo "========================================"
echo ""

# Start backend
cd "$PROJECT_DIR/backend"
source venv/bin/activate
python main.py &
BACKEND_PID=$!

# Wait for backend to start
echo "[>] Waiting for backend to start..."
sleep 5

echo ""
echo "========================================"
echo "  Starting Frontend (Next.js)..."
echo "========================================"
echo ""

# Start frontend
cd "$PROJECT_DIR/frontend"
npm run dev &
FRONTEND_PID=$!

# Wait for frontend to start
echo "[>] Waiting for frontend to start..."
sleep 5

echo ""
echo "========================================"
echo "  SURGE-AI Trading Dashboard Ready!"
echo "========================================"
echo ""
echo "  Dashboard:  http://localhost:3000"
echo "  API Docs:   http://localhost:8000/docs"
echo "  WebSocket:  ws://localhost:8000/ws"
echo ""
echo -e "${GREEN}[OK] Services are running.${NC}"
echo "[!] Press Ctrl+C to stop all services."
echo ""

# Open dashboard in default browser (if available)
if command -v xdg-open &> /dev/null; then
    xdg-open http://localhost:3000 2>/dev/null
elif command -v open &> /dev/null; then
    open http://localhost:3000
fi

# Wait for both processes
wait $BACKEND_PID $FRONTEND_PID
