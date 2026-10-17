@echo off
setlocal EnableExtensions DisableDelayedExpansion
chcp 65001 >nul 2>&1

title OZNUR AI - FULL PRO Kurulum

echo ==========================================
echo       OZNUR AI - FULL PRO KURULUM
echo ==========================================
echo.

set "SOURCE=%~dp0"
set "WORK=%LOCALAPPDATA%\OZNUR_AI_FULL_PRO"
set "ZIPFILE="

if exist "%SOURCE%api\server.py" if exist "%SOURCE%web\index.html" if exist "%SOURCE%ozcod\core.py" goto USE_SOURCE

echo Gecici/eksik ZIP klasoru tespit edildi.
echo Kaynak klasorunde tam proje dosyalari yok.
echo.
echo Tam ZIP dosyasi Windows kullanici klasorlerinde aranacak.
echo.

rem En yeni eslesen ZIP'i Downloads klasorunde ara.
if exist "%USERPROFILE%\Downloads" for /f "delims=" %%Z in ('dir /b /a-d /o-d "%USERPROFILE%\Downloads\OZNUR_AI_FULL_PRO*.zip" 2^>nul') do if not defined ZIPFILE set "ZIPFILE=%USERPROFILE%\Downloads\%%Z"

rem Bulunamazsa Desktop klasorunde ara.
if not defined ZIPFILE if exist "%USERPROFILE%\Desktop" for /f "delims=" %%Z in ('dir /b /a-d /o-d "%USERPROFILE%\Desktop\OZNUR_AI_FULL_PRO*.zip" 2^>nul') do if not defined ZIPFILE set "ZIPFILE=%USERPROFILE%\Desktop\%%Z"

rem Bulunamazsa Documents klasorunde ara.
if not defined ZIPFILE if exist "%USERPROFILE%\Documents" for /f "delims=" %%Z in ('dir /b /a-d /o-d "%USERPROFILE%\Documents\OZNUR_AI_FULL_PRO*.zip" 2^>nul') do if not defined ZIPFILE set "ZIPFILE=%USERPROFILE%\Documents\%%Z"

if not defined ZIPFILE goto NO_ZIP

if not exist "%ZIPFILE%" goto NO_ZIP

echo ZIP bulundu:
echo "%ZIPFILE%"
echo.

goto EXTRACT

:USE_SOURCE
echo Tam proje klasoru bulundu:
echo "%SOURCE%"
echo.
goto INSTALL

:EXTRACT
echo Temiz calisma klasoru hazirlaniyor...
if exist "%WORK%" rmdir /s /q "%WORK%" >nul 2>&1
mkdir "%WORK%" >nul 2>&1
if not exist "%WORK%" goto FAIL

echo ZIP cikartiliyor...
powershell.exe -NoProfile -ExecutionPolicy Bypass -Command "Expand-Archive -LiteralPath '%ZIPFILE%' -DestinationPath '%WORK%\_zip' -Force" 
if errorlevel 1 goto FAIL

rem ZIP'in icindeki OZcod_Offline_Sistem klasorunu bul.
if exist "%WORK%\_zip\OZcod_Offline_Sistem\api\server.py" set "SOURCE=%WORK%\_zip\OZcod_Offline_Sistem\"
if exist "%WORK%\_zip\OZcod_Offline_Sistem\web\index.html" set "SOURCE=%WORK%\_zip\OZcod_Offline_Sistem\"

if not exist "%SOURCE%api\server.py" goto FAIL
if not exist "%SOURCE%web\index.html" goto FAIL
if not exist "%SOURCE%ozcod\core.py" goto FAIL

echo Tam paket cikartildi.
echo.
goto INSTALL

:INSTALL
if not exist "%SOURCE%api\server.py" goto FAIL
if not exist "%SOURCE%web\index.html" goto FAIL
if not exist "%SOURCE%ozcod\core.py" goto FAIL

set "PY="
where py >nul 2>&1
if not errorlevel 1 set "PY=py -3"
if not defined PY (
    where python >nul 2>&1
    if not errorlevel 1 set "PY=python"
)
if not defined PY goto NO_PYTHON

echo Python bulundu.
echo.

echo Sanal ortam kontrol ediliyor...
if not exist "%WORK%\.venv\Scripts\python.exe" %PY% -m venv "%WORK%\.venv"
if errorlevel 1 goto FAIL

set "VENV=%WORK%\.venv\Scripts\python.exe"
if not exist "%VENV%" goto FAIL

rem Kaynak tam paket ise calisma kopyasini WORK altina al.
if /i not "%SOURCE:~0,%"=="%WORK%" goto COPY_SOURCE

goto TEST

:COPY_SOURCE
if not exist "%WORK%\app" mkdir "%WORK%\app" >nul 2>&1
xcopy "%SOURCE%*" "%WORK%\app\" /E /I /Y /Q >nul
if errorlevel 1 goto FAIL
set "SOURCE=%WORK%\app\"
if not exist "%SOURCE%api\server.py" goto FAIL
if not exist "%SOURCE%web\index.html" goto FAIL
if not exist "%SOURCE%ozcod\core.py" goto FAIL

goto TEST

:TEST
echo API syntax testi...
"%VENV%" -m py_compile "%SOURCE%api\server.py"
if errorlevel 1 goto FAIL

echo Dahili testler...
set "PYTHONPATH=%SOURCE%"
cd /d "%SOURCE%"
"%VENV%" -m unittest discover -s tests -p "test_*.py" -v
if errorlevel 1 goto FAIL

echo.
echo ==========================================
echo       KURULUM VE TESTLER BASARILI
echo ==========================================
echo.
echo PWA: http://127.0.0.1:8788/
echo.
echo PWA baslatilsin mi?
echo [E] Evet
 echo [H] Hayir
choice /c EH /n /m "Seciminiz: "
if errorlevel 2 goto SUCCESS
if errorlevel 1 start "OZNUR AI" "%SOURCE%run_pwa_windows.bat"

goto SUCCESS

:NO_ZIP
echo HATA: Tam OZNUR AI ZIP dosyasi bulunamadi.
echo.
echo ZIP'i once Windows'un Downloads klasorune kaydedin.
goto FAIL

:NO_PYTHON
echo HATA: Python bulunamadi.
echo Python 3 kurulu olmali ve PATH/py.exe kullanilabilir olmali.
goto FAIL

:FAIL
echo.
echo ==========================================
echo       KURULUM BASARISIZ
echo ==========================================
echo.
pause
exit /b 1

:SUCCESS
echo.
echo Kurulum tamamlandi.
echo Bu pencereyi kapatmak icin bir tusa basin.
pause
exit /b 0
