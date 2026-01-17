@echo off
REM ============================================================
REM SURGE-AI Trading Dashboard - Startup Script (Windows)
REM ============================================================

echo.
echo ========================================
echo   SURGE-AI Trading Dashboard
echo   Starting services...
echo ========================================
echo.

REM Get the script directory
set "SCRIPT_DIR=%~dp0"
set "PROJECT_DIR=%SCRIPT_DIR%.."

REM Check if backend venv exists
if not exist "%PROJECT_DIR%\backend\venv" (
    echo [!] Python virtual environment not found.
    echo [>] Creating virtual environment...
    cd /d "%PROJECT_DIR%\backend"
    python -m venv venv
    call venv\Scripts\activate
    pip install -r requirements.txt
    echo [OK] Virtual environment created and dependencies installed.
) else (
    echo [OK] Virtual environment found.
)

REM Check if frontend node_modules exists
if not exist "%PROJECT_DIR%\frontend\node_modules" (
    echo [!] Node modules not found.
    echo [>] Installing frontend dependencies...
    cd /d "%PROJECT_DIR%\frontend"
    call npm install
    echo [OK] Frontend dependencies installed.
) else (
    echo [OK] Frontend dependencies found.
)

echo.
echo ========================================
echo   Starting Backend (FastAPI)...
echo ========================================
echo.

REM Start backend in new window
start "SURGE-AI Backend" cmd /k "cd /d %PROJECT_DIR%\backend && call venv\Scripts\activate && python main.py"

REM Wait for backend to start
echo [>] Waiting for backend to start...
timeout /t 5 /nobreak > nul

echo.
echo ========================================
echo   Starting Frontend (Next.js)...
echo ========================================
echo.

REM Start frontend in new window
start "SURGE-AI Frontend" cmd /k "cd /d %PROJECT_DIR%\frontend && npm run dev"

REM Wait for frontend to start
echo [>] Waiting for frontend to start...
timeout /t 5 /nobreak > nul

echo.
echo ========================================
echo   SURGE-AI Trading Dashboard Ready!
echo ========================================
echo.
echo   Dashboard:  http://localhost:3000
echo   API Docs:   http://localhost:8000/docs
echo   WebSocket:  ws://localhost:8000/ws
echo.
echo   Press any key to open dashboard in browser...
pause > nul

REM Open dashboard in default browser
start http://localhost:3000

echo.
echo [OK] Dashboard opened in browser.
echo [!] Keep this window open. Close to stop all services.
echo.
pause
