@echo off
setlocal

:: Aura Browser - Optimized Performance Launcher
:: Tailored for Intel Core i3 / RTX 3050 / 16GB RAM
:: Features: GPU Rasterization, Process Limit (RAM saver without tab discarding), Anti-Fingerprinting, Pre-bundled uBlock Origin

set "SCRIPT_DIR=%~dp0"
set "CHROME_EXE="

:: 1. Search for Aura / Chromium executable
if exist "%SCRIPT_DIR%build\src\out\Default\chrome.exe" (
    set "CHROME_EXE=%SCRIPT_DIR%build\src\out\Default\chrome.exe"
) else if exist "%SCRIPT_DIR%out\Default\chrome.exe" (
    set "CHROME_EXE=%SCRIPT_DIR%out\Default\chrome.exe"
) else if exist "%SCRIPT_DIR%chrome.exe" (
    set "CHROME_EXE=%SCRIPT_DIR%chrome.exe"
) else if exist "%LOCALAPPDATA%\Aura\Application\chrome.exe" (
    set "CHROME_EXE=%LOCALAPPDATA%\Aura\Application\chrome.exe"
) else if exist "%PROGRAMFILES%\Aura\Application\chrome.exe" (
    set "CHROME_EXE=%PROGRAMFILES%\Aura\Application\chrome.exe"
) else if exist "%PROGRAMFILES(X86)%\Aura\Application\chrome.exe" (
    set "CHROME_EXE=%PROGRAMFILES(X86)%\Aura\Application\chrome.exe"
)

if "%CHROME_EXE%"=="" (
    echo [Aura Launcher] Looking for Aura / Chromium executable in PATH...
    where chrome.exe >nul 2>&1
    if %errorlevel% equ 0 (
        set "CHROME_EXE=chrome.exe"
    ) else (
        echo [ERROR] Could not find chrome.exe / Aura executable.
        echo Please place this script in the browser folder or install Aura first.
        pause
        exit /b 1
    )
)

:: 2. Pre-bundled Extensions
set "EXT_FLAGS="
if exist "%SCRIPT_DIR%aura-assets\extensions\ublock-origin\manifest.json" (
    set "EXT_FLAGS=--load-extension="%SCRIPT_DIR%aura-assets\extensions\ublock-origin""
)

:: 3. Launch with optimal flags
start "" "%CHROME_EXE%" ^
    --renderer-process-limit=8 ^
    --enable-gpu-rasterization ^
    --enable-zero-copy ^
    --enable-features=WebContentsForceDark:choice/selective_inversion_only ^
    --fingerprinting-canvas-image-data-noise ^
    --fingerprinting-client-rects-noise ^
    --no-default-browser-check ^
    --no-pings ^
    %EXT_FLAGS% ^
    %*
