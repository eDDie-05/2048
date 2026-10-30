# 2048 — Python

A desktop 2048-style number puzzle built with Python and Pygame. Combine equal tiles by moving them across a 4×4 board.

## Features
- 4×4 tile grid
- Random tile generation
- Tile merging and score tracking
- Keyboard-controlled gameplay
- Win and game-over states

## Requirements
- Python 3.9 or newer
- Pygame

## Run locally
```bash
python -m venv .venv
# macOS / Linux
source .venv/bin/activate
# Windows PowerShell
.venv\Scripts\Activate.ps1
python -m pip install pygame
python 2048.py
```

## Controls
Use the arrow keys to move tiles. Close the game window to exit.

## Project files
- `2048.py` — board state, tile generation, drawing and game loop

## Current scope
A standalone learning project. Add automated tests for merge behavior and edge cases before describing it as a verified release.
