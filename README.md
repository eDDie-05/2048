#  2048 — Python

##  Overview

**2048 Game** is a Python-based implementation of the popular number puzzle game. The player moves numbered tiles on a grid, combining tiles with the same value to create higher numbers.

The main objective is to combine tiles and reach the **2048 tile** while achieving the highest possible score.

This project was developed for educational purposes to practice Python programming and game development concepts.

##  Features

*  Interactive gameplay
*  Number tile merging
*  Score tracking
*  Keyboard controls
*  Win condition
*  Game-over detection
*  Restart/new game option
*  Simple graphical interface

## Technologies Used

* **Python 3**
* **Pygame** *(if used in the project)*
* Object-Oriented Programming
* Lists/arrays
* Functions
* Conditional statements
* Keyboard input

##  Requirements

Before running the game, make sure you have:

* Python 3.x
* Pip
* Pygame

##  Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/2048-game.git
```

### 2. Open the project directory

```bash
cd 2048-game
```

### 3. Install Pygame

```bash
pip3 install pygame
```

Or:

```bash
python3 -m pip install pygame
```

### 4. Run the game

```bash
python3 main.py
```

## 🎮 Controls

| Key            | Action           |
| -------------- | ---------------- |
|  Up Arrow    | Move tiles up    |
|  Down Arrow  | Move tiles down  |
|  Left Arrow  | Move tiles left  |
|  Right Arrow | Move tiles right |
| `R`            | Restart game     |
| `ESC`          | Exit game        |

> Controls may vary depending on the implementation.

##  How the Game Works

The game uses a **4 × 4 grid**.

When the player moves the tiles:

1. All tiles move in the selected direction.
2. Tiles with the same number combine.
3. The player's score increases.
4. A new tile is generated.
5. The game checks whether the player has won or has no valid moves remaining.

### Example

```text
2 + 2 = 4

4 + 4 = 8

8 + 8 = 16

...

1024 + 1024 = 2048
```

## 📁 Project Structure

```text
2048-game/
│
├── main.py
├── assets/
│   └── ...
├── requirements.txt
└── README.md
```

##  Project Objectives

This project demonstrates:

* Python programming fundamentals
* Working with 2D lists
* Functions and program organization
* Event handling
* Keyboard input
* Game logic
* Score management
* GUI/game development using Python

##  Future Improvements

Possible improvements include:

*  High-score system
*  Save game functionality
*  Sound effects
* Improved animations
*  Custom themes
*  Timer/game statistics
*  Mobile-friendly version
*  Leaderboard
*  Undo functionality

##  Disclaimer
This project is an independent implementation of the 2048 puzzle concept and is intended for educational purposes.

##  Author

eDDie

Developed using Python as a game development project.

##  License

This project is intended for educational purposes. Check the repository license and included assets before redistributing the project.
