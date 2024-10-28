# Aim Trainer Game

A simple aim trainer game built with Python and Pygame, designed to help players improve their aiming speed and accuracy across different difficulty levels. Choose a difficulty and try to hit as many targets as possible before the timer runs out!

## Table of Contents
- [Gameplay](#gameplay)
- [Features](#features)
- [Installation](#installation)
- [How to Play](#how-to-play)
- [Project Structure](#project-structure)

## Gameplay
The game begins with a welcome menu where you can choose between three levels of difficulty: Easy, Medium, and Hard. Once you select a level, a countdown timer will start. Your goal is to hit as many targets as you can by clicking on them before the timer ends. After each round, your accuracy and score will be displayed.

## Features
- **Three Difficulty Levels**: Each level changes the number and size of targets, making the game more challenging.
- **Real-Time Score and Accuracy Tracking**: See your progress throughout the game.
- **Simple Menu System**: Easy navigation through the game's interface.

## Installation

### Prerequisites
- Python 3.6+
- Pygame library

### Setup
1. Clone this repository:
   ```bash
   git clone https://github.com/AadityaPanda/AimTrainer.git
   ```
2. Install Pygame:
   ```bash
   pip install pygame
   ```

3. Run the game:
   ```bash
   python AimTrainer.py
   ```

## How to Play
1. Start the game by running the script.
2. Choose a difficulty level from the welcome menu:
   - **Easy**: Larger targets, fewer total targets.
   - **Medium**: Smaller targets, medium difficulty.
   - **Hard**: Small targets, increased difficulty.
3. Use the mouse to aim and click on targets.
4. Your accuracy and score will be displayed at the end of each round.
5. Press **ESC** to exit the game.

## Project Structure
```
AimTrainer/
├── assets/
│   ├── images/
│   │   └── targetblue.jpg         # Target image
│   ├── sounds/
│   │   ├── snipersound.wav        # Shooting sound effect
│   │   └── metalHit.wav           # Hit sound effect
│   └── texts/
│       ├── easy.txt               # Config file for easy difficulty
│       ├── medium.txt             # Config file for medium difficulty
│       └── hard.txt               # Config file for hard difficulty
├── aim_trainer_game.py            # Main game file
└── README.md
```
