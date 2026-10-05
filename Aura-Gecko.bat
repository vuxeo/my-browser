@echo off
setlocal
title Aura Browser (Gecko Edition)

set "APP_DIR=%~dp0Aura-Gecko"

if not exist "%APP_DIR%\Aura.exe" (
    echo [ERROR] Could not find Aura.exe in %APP_DIR%
    pause
    exit /b 1
)

start "" "%APP_DIR%\Aura.exe" -profile "%APP_DIR%\profile" -no-remote %*
