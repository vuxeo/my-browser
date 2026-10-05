# ⚡ Aura Browser

<p align="center">
  <img src="aura-assets/aura-logo.svg" alt="Aura Logo" width="140" height="140" />
</p>

<p align="center">
  <b>A lightweight, privacy-focused Chromium browser with zero Google telemetry, native Yandex search, RTX hardware acceleration, and full Manifest V2 extension support.</b>
</p>

<p align="center">
  <a href="https://github.com/vuxeo/my-browser/releases"><img src="https://img.shields.io/badge/Release-v0.1.0--aura-blue?style=flat-square" alt="Release" /></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-BSD--3--Clause-green?style=flat-square" alt="License" /></a>
  <a href="https://github.com/vuxeo/my-browser/actions"><img src="https://img.shields.io/badge/CI-GitHub_Actions-purple?style=flat-square" alt="CI" /></a>
</p>

---

## 🌟 Key Features

- 🛡️ **Zero Google Bloat & Telemetry:** Stripped of all Google background pings, SafeBrowsing URL tracking, and account integrations.
- ⚡ **Optimized Memory Architecture:** No annoying tab discarding (tabs stay loaded and responsive), paired with strict renderer process limits (`--renderer-process-limit=8`) to prevent RAM bloat.
- 🚀 **Hardware Accelerated:** Deep GPU rasterization and zero-copy rendering tailored for NVIDIA GeForce RTX graphics cards (NVDEC & D3D11).
- 🔍 **Native Yandex Search:** Clean, tracker-free Yandex search in the address bar (omnibox) with fast suggestions.
- 🧩 **Manifest V2 & Web Store:** 1-click extension installs from Chrome Web Store with uncompromised ad blocking (pre-bundled with uBlock Origin).
- 🎨 **Aura Dark Dashboard:** Sleek, minimal, ultra-fast New Tab page with digital clock, speed-dial bookmarks, and performance stats.

---

## 🚀 Releases & Downloads

Pre-built Windows 64-bit installers and portable `.zip` archives are automatically compiled and published in [Releases](https://github.com/vuxeo/my-browser/releases).

---

## 🛠️ Building from Source

Google only supports [Windows 10 x64 or newer](https://chromium.googlesource.com/chromium/src/+/refs/heads/main/docs/windows_build_instructions.md#system-requirements).

### Quick Build

Run in `Developer Command Prompt for VS` (as administrator):

```cmd
git clone --recurse-submodules https://github.com/vuxeo/my-browser.git
cd my-browser
python3 build.py
python3 package.py
```

A zip archive and an installer will be created under `build`.

---

## 📜 License

See [LICENSE](LICENSE). Based on [ungoogled-chromium](https://github.com/ungoogled-software/ungoogled-chromium) and Chromium.
