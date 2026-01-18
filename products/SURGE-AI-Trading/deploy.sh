#!/bin/bash
# ============================================================
# SURGE-AI Trading - Single Command Deployment Script (Linux/Mac)
# ============================================================
#
# Usage:
#   ./deploy.sh              # Full deployment
#   ./deploy.sh --build      # Force rebuild images
#   ./deploy.sh --admin      # Include admin tools (pgAdmin, Attu)
#   ./deploy.sh --down       # Stop all services
#   ./deploy.sh --logs       # View logs
#   ./deploy.sh --status     # Check service status
#
# ============================================================

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Configuration
COMPOSE_FILE="docker-compose.full.yml"
ENV_FILE=".env"
ENV_EXAMPLE=".env.example"

# ============================================================
# Functions
# ============================================================

print_banner() {
    echo -e "${BLUE}"
    echo "============================================================"
    echo "  SURGE-AI Trading - Deployment Script"
    echo "============================================================"
    echo -e "${NC}"
}

print_step() {
    echo -e "${GREEN}[STEP]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

check_prerequisites() {
    print_step "Checking prerequisites..."

    # Check Docker
    if ! command -v docker &> /dev/null; then
        print_error "Docker is not installed. Please install Docker first."
        exit 1
    fi

    # Check Docker Compose
    if ! command -v docker-compose &> /dev/null && ! docker compose version &> /dev/null; then
        print_error "Docker Compose is not installed. Please install Docker Compose first."
        exit 1
    fi

    # Check if Docker is running
    if ! docker info &> /dev/null; then
        print_error "Docker is not running. Please start Docker first."
        exit 1
    fi

    print_success "Prerequisites check passed"
}

setup_env() {
    print_step "Setting up environment..."

    if [ ! -f "$ENV_FILE" ]; then
        if [ -f "$ENV_EXAMPLE" ]; then
            cp "$ENV_EXAMPLE" "$ENV_FILE"
            print_warning "Created .env from .env.example"
            print_warning "Please edit .env with your API keys before proceeding"
            echo ""
            read -p "Press Enter to continue after editing .env, or Ctrl+C to abort..."
        else
            print_warning "No .env file found. Using default values."
        fi
    else
        print_success "Using existing .env file"
    fi
}

wait_for_service() {
    local service=$1
    local url=$2
    local max_attempts=${3:-30}
    local attempt=1

    echo -n "  Waiting for $service"
    while [ $attempt -le $max_attempts ]; do
        if curl -s "$url" > /dev/null 2>&1; then
            echo -e " ${GREEN}OK${NC}"
            return 0
        fi
        echo -n "."
        sleep 2
        ((attempt++))
    done
    echo -e " ${RED}TIMEOUT${NC}"
    return 1
}

deploy() {
    local build_flag=""
    local profiles=""

    # Parse arguments
    for arg in "$@"; do
        case $arg in
            --build)
                build_flag="--build"
                ;;
            --admin)
                profiles="--profile admin"
                ;;
        esac
    done

    print_step "Starting deployment..."

    # Pull images first
    echo "  Pulling base images..."
    docker-compose -f "$COMPOSE_FILE" pull --ignore-pull-failures 2>/dev/null || true

    # Build and start
    echo "  Building and starting services..."
    if [ -n "$profiles" ]; then
        docker-compose -f "$COMPOSE_FILE" $profiles up -d $build_flag
    else
        docker-compose -f "$COMPOSE_FILE" up -d $build_flag
    fi

    print_step "Waiting for services to be healthy..."

    # Wait for databases
    wait_for_service "TimescaleDB" "http://localhost:5432" 60 || true
    wait_for_service "Redis" "http://localhost:6379" 30 || true
    wait_for_service "Milvus" "http://localhost:9091/healthz" 60 || true

    # Wait for application services
    wait_for_service "Backend" "http://localhost:8000/health" 60 || true
    wait_for_service "Frontend" "http://localhost:3000" 60 || true

    print_success "Deployment complete!"
    echo ""
    print_status
}

stop_services() {
    print_step "Stopping all services..."
    docker-compose -f "$COMPOSE_FILE" --profile admin down
    print_success "All services stopped"
}

show_logs() {
    print_step "Showing logs (Ctrl+C to exit)..."
    docker-compose -f "$COMPOSE_FILE" logs -f
}

print_status() {
    echo -e "${BLUE}============================================================${NC}"
    echo -e "${BLUE}  SURGE-AI Trading Dashboard - Service Status${NC}"
    echo -e "${BLUE}============================================================${NC}"
    echo ""

    # Check each service
    echo "Services:"
    docker-compose -f "$COMPOSE_FILE" ps --format "table {{.Name}}\t{{.Status}}\t{{.Ports}}" 2>/dev/null || \
        docker-compose -f "$COMPOSE_FILE" ps

    echo ""
    echo -e "${BLUE}============================================================${NC}"
    echo -e "${BLUE}  Access URLs${NC}"
    echo -e "${BLUE}============================================================${NC}"
    echo ""
    echo -e "  ${GREEN}Dashboard:${NC}  http://localhost:3000"
    echo -e "  ${GREEN}API Docs:${NC}   http://localhost:8000/docs"
    echo -e "  ${GREEN}WebSocket:${NC}  ws://localhost:8000/ws"
    echo -e "  ${GREEN}MinIO:${NC}      http://localhost:9001 (minioadmin/minioadmin)"

    # Check if admin tools are running
    if docker ps --format '{{.Names}}' | grep -q "surge-attu"; then
        echo -e "  ${GREEN}Attu (Milvus):${NC}  http://localhost:8080"
    fi
    if docker ps --format '{{.Names}}' | grep -q "surge-pgadmin"; then
        echo -e "  ${GREEN}pgAdmin:${NC}        http://localhost:8081"
    fi

    echo ""
    echo -e "${BLUE}============================================================${NC}"
}

show_help() {
    echo "SURGE-AI Trading - Deployment Script"
    echo ""
    echo "Usage: $0 [command] [options]"
    echo ""
    echo "Commands:"
    echo "  (default)    Deploy all services"
    echo "  --down       Stop all services"
    echo "  --logs       Show service logs"
    echo "  --status     Show service status"
    echo "  --help       Show this help message"
    echo ""
    echo "Options:"
    echo "  --build      Force rebuild Docker images"
    echo "  --admin      Include admin tools (pgAdmin, Attu)"
    echo ""
    echo "Examples:"
    echo "  $0                  # Deploy all services"
    echo "  $0 --build          # Rebuild and deploy"
    echo "  $0 --admin          # Deploy with admin tools"
    echo "  $0 --down           # Stop all services"
    echo "  $0 --logs           # View logs"
    echo ""
}

# ============================================================
# Main
# ============================================================

print_banner

# Parse command
case "${1:-}" in
    --down)
        stop_services
        ;;
    --logs)
        show_logs
        ;;
    --status)
        print_status
        ;;
    --help|-h)
        show_help
        ;;
    *)
        check_prerequisites
        setup_env
        deploy "$@"
        ;;
esac
