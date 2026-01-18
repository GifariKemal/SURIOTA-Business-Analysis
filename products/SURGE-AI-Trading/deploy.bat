@echo off
REM ============================================================
REM SURGE-AI Trading - Single Command Deployment Script (Windows)
REM ============================================================
REM
REM Usage:
REM   deploy.bat              - Full deployment
REM   deploy.bat --build      - Force rebuild images
REM   deploy.bat --admin      - Include admin tools (pgAdmin, Attu)
REM   deploy.bat --down       - Stop all services
REM   deploy.bat --logs       - View logs
REM   deploy.bat --status     - Check service status
REM
REM ============================================================

setlocal EnableDelayedExpansion

REM Configuration
set COMPOSE_FILE=docker-compose.full.yml
set ENV_FILE=.env
set ENV_EXAMPLE=.env.example

REM Change to script directory
cd /d "%~dp0"

REM Parse arguments
set BUILD_FLAG=
set PROFILES=
set COMMAND=deploy

:parse_args
if "%~1"=="" goto :main
if "%~1"=="--build" (
    set BUILD_FLAG=--build
    shift
    goto :parse_args
)
if "%~1"=="--admin" (
    set PROFILES=--profile admin
    shift
    goto :parse_args
)
if "%~1"=="--down" (
    set COMMAND=down
    shift
    goto :parse_args
)
if "%~1"=="--logs" (
    set COMMAND=logs
    shift
    goto :parse_args
)
if "%~1"=="--status" (
    set COMMAND=status
    shift
    goto :parse_args
)
if "%~1"=="--help" (
    set COMMAND=help
    shift
    goto :parse_args
)
if "%~1"=="-h" (
    set COMMAND=help
    shift
    goto :parse_args
)
shift
goto :parse_args

:main
echo.
echo ============================================================
echo   SURGE-AI Trading - Deployment Script
echo ============================================================
echo.

if "%COMMAND%"=="help" goto :show_help
if "%COMMAND%"=="down" goto :stop_services
if "%COMMAND%"=="logs" goto :show_logs
if "%COMMAND%"=="status" goto :show_status
goto :deploy

:check_prerequisites
echo [STEP] Checking prerequisites...

REM Check Docker
docker --version >nul 2>&1
if %ERRORLEVEL% neq 0 (
    echo [ERROR] Docker is not installed. Please install Docker Desktop first.
    exit /b 1
)

REM Check if Docker is running
docker info >nul 2>&1
if %ERRORLEVEL% neq 0 (
    echo [ERROR] Docker is not running. Please start Docker Desktop first.
    exit /b 1
)

echo [SUCCESS] Prerequisites check passed
goto :eof

:setup_env
echo [STEP] Setting up environment...

if not exist "%ENV_FILE%" (
    if exist "%ENV_EXAMPLE%" (
        copy "%ENV_EXAMPLE%" "%ENV_FILE%" >nul
        echo [WARNING] Created .env from .env.example
        echo [WARNING] Please edit .env with your API keys before proceeding
        echo.
        pause
    ) else (
        echo [WARNING] No .env file found. Using default values.
    )
) else (
    echo [SUCCESS] Using existing .env file
)
goto :eof

:deploy
call :check_prerequisites
if %ERRORLEVEL% neq 0 exit /b 1

call :setup_env

echo [STEP] Starting deployment...

REM Pull images first
echo   Pulling base images...
docker-compose -f "%COMPOSE_FILE%" pull --ignore-pull-failures 2>nul

REM Build and start
echo   Building and starting services...
if defined PROFILES (
    docker-compose -f "%COMPOSE_FILE%" %PROFILES% up -d %BUILD_FLAG%
) else (
    docker-compose -f "%COMPOSE_FILE%" up -d %BUILD_FLAG%
)

echo [STEP] Waiting for services to be healthy...
echo   Please wait while services start up (this may take a few minutes)...

REM Wait for services
timeout /t 30 /nobreak >nul

echo [SUCCESS] Deployment complete!
echo.
call :show_status
goto :end

:stop_services
echo [STEP] Stopping all services...
docker-compose -f "%COMPOSE_FILE%" --profile admin down
echo [SUCCESS] All services stopped
goto :end

:show_logs
echo [STEP] Showing logs (Press Ctrl+C to exit)...
docker-compose -f "%COMPOSE_FILE%" logs -f
goto :end

:show_status
echo ============================================================
echo   SURGE-AI Trading Dashboard - Service Status
echo ============================================================
echo.

REM Show service status
docker-compose -f "%COMPOSE_FILE%" ps

echo.
echo ============================================================
echo   Access URLs
echo ============================================================
echo.
echo   Dashboard:  http://localhost:3000
echo   API Docs:   http://localhost:8000/docs
echo   WebSocket:  ws://localhost:8000/ws
echo   MinIO:      http://localhost:9001 (minioadmin/minioadmin)
echo.

REM Check if admin tools are running
docker ps --format "{{.Names}}" | findstr /C:"surge-attu" >nul 2>&1
if %ERRORLEVEL% equ 0 (
    echo   Attu (Milvus):  http://localhost:8080
)
docker ps --format "{{.Names}}" | findstr /C:"surge-pgadmin" >nul 2>&1
if %ERRORLEVEL% equ 0 (
    echo   pgAdmin:        http://localhost:8081
)

echo.
echo ============================================================
goto :end

:show_help
echo SURGE-AI Trading - Deployment Script
echo.
echo Usage: %~nx0 [command] [options]
echo.
echo Commands:
echo   (default)    Deploy all services
echo   --down       Stop all services
echo   --logs       Show service logs
echo   --status     Show service status
echo   --help       Show this help message
echo.
echo Options:
echo   --build      Force rebuild Docker images
echo   --admin      Include admin tools (pgAdmin, Attu)
echo.
echo Examples:
echo   %~nx0                  Deploy all services
echo   %~nx0 --build          Rebuild and deploy
echo   %~nx0 --admin          Deploy with admin tools
echo   %~nx0 --down           Stop all services
echo   %~nx0 --logs           View logs
echo.
goto :end

:end
endlocal
