$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest

$Root = Split-Path -Parent $PSCommandPath
Set-Location -LiteralPath $Root

Write-Host 'OZNUR AI Windows kurulumu'
Write-Host "Klasor: $Root"
Write-Host ''

$Python = Get-Command py -ErrorAction SilentlyContinue
if (-not $Python) {
    $Python = Get-Command python -ErrorAction SilentlyContinue
}

if (-not $Python) {
    Write-Host 'HATA: Python bulunamadi.' -ForegroundColor Red
    exit 1
}

$venv = Join-Path $Root '.venv'

if (-not (Test-Path -LiteralPath (Join-Path $venv 'Scripts\python.exe'))) {
    if ($Python.Name -eq 'py.exe') {
        & $Python.Source -3 -m venv $venv
    } else {
        & $Python.Source -m venv $venv
    }
    if ($LASTEXITCODE -ne 0) {
        throw "venv olusturulamadi. Kod: $LASTEXITCODE"
    }
}

Write-Host 'Kurulum tamamlandi.' -ForegroundColor Green
Write-Host 'PWA: run_pwa_windows.bat'
Write-Host 'API: http://127.0.0.1:8788'
