@echo off
cd /d "%~dp0"
py -3 -m ozcod.desktop
if errorlevel 1 (
  echo.
  echo Uygulama acilamadi. Python 3 kurulu mu kontrol edin.
  pause
)
