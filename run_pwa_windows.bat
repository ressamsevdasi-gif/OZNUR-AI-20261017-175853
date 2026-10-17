@echo off
setlocal EnableExtensions
cd /d "%~dp0"
title OZNUR AI - Windows PWA

echo ==========================================
echo       OZNUR AI - PWA / API BASLATMA
echo ==========================================
echo.

set "ROOT=%~dp0"
set "PY="

if exist "%ROOT%.venv\Scripts\python.exe" set "PY=%ROOT%.venv\Scripts\python.exe"
if not defined PY (
    where py.exe >nul 2>&1
    if not errorlevel 1 set "PY=py.exe"
)
if not defined PY (
    where python.exe >nul 2>&1
    if not errorlevel 1 set "PY=python.exe"
)
if not defined PY (
    echo HATA: Python bulunamadi.
    echo Python 3 kurun ve tekrar deneyin.
    pause
    exit /b 1
)

if not exist "%ROOT%api\server.py" (
    echo HATA: api\server.py bulunamadi.
    pause
    exit /b 2
)
if not exist "%ROOT%web\index.html" (
    echo HATA: web\index.html bulunamadi.
    pause
    exit /b 3
)

echo Python: %PY%
echo API: http://127.0.0.1:8788
echo.
echo Tarayici: http://127.0.0.1:8788/
echo Kapatmak icin bu pencereyi kapatin veya Ctrl+C basin.
echo.

if "%PY%"=="py.exe" (
    "%PY%" -3 "%ROOT%api\server.py"
) else (
    "%PY%" "%ROOT%api\server.py"
)

set "RC=%ERRORLEVEL%"
echo.
echo API cikis kodu: %RC%
pause
exit /b %RC%
