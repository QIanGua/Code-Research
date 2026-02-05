# OpenClaw Research Notes

## Overview
OpenClaw is a multiplatform C++ reimplementation of the original Captain Claw (1997) platformer game. The codebase is written from scratch and utilizes assets from the original game archive.

## Technology Stack
- **Languages**: C++
- **Graphics/Input/Audio**: SDL2 Libraries (SDL2, SDL_Image, SDL_TTF, SDL_Mixer, SDL2_Gfx)
- **Physics**: Box2D Library
- **Data**: Tinyxml library (data-driven approach)

## Build System & Tools
- **Build System**: CMake (cross-platform), Visual Studio 2017 solution (Windows)
- **CI/CD**: AppVeyor (Windows), Travis CI (Linux/macOS/Android/Emscripten), Coverity (Static Analysis)

## Supported Platforms
- Windows
- Linux (Debian/Ubuntu tested)
- macOS
- Android
- WebAssembly (Emscripten)

## Prerequisites & Assets
- **Original Game Archive**: Requires `CLAW.REZ` from the original game to be placed in the `Build_Release` directory.
- **Assets**: Content inside `Build_Release/ASSETS` must be zipped into `ASSETS.ZIP`.

## Platform Specifics
- **Linux**: Requires `libsdl2-dev` and related packages. For background music, `timidity` (or `timidity++`) and `freepats` are needed.
- **WebAssembly**:
  - Compiled using Emscripten.
  - No MIDI support currently.
  - Some browsers may have issues with `.wav` files.
  - IE not supported.
- **Claw Launcher**:
  - Tool to configure Video/Audio/Assets.
  - Precompiled for Windows.
  - Runs on Linux using Mono runtime (`mono ClawLauncher.exe`).

## Directory Structure Highlights
(Based on repository observation)
- `OpenClaw/`: Core source code.
- `Build_Release/`: Deployment folder (place `CLAW.REZ` here).
- `Box2D/`: Physics engine source/config.
- `ClawLauncher/`: Launcher source/binary.
- `ThirdParty/`: External dependencies (e.g., Tinyxml).
