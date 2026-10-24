# Terminal Retro Racer

A simple, lightweight retro racing game built completely in Python that runs right inside your terminal. Avoid obstacles, collect coins, and chase your high score in this text-based arcade experience.

Features

• Pure Python: Built using standard libraries with no external dependencies required.
• Dynamic Spawn System: Randomly generated obstacles and coins to keep gameplay unpredictable.
• Cross-Platform Compatibility: Supports native raw character inputs on Unix-like systems (Linux/macOS) with standard input fallbacks for other environments.

How to Play

Controls are simple and intuitive:
• a: Move left
• d: Move right
• q: Quit the game

Legend

• ^: Your Car
• O: Obstacle (Avoid these!)
• $: Coin (Collect for +10 points)

Prerequisites

• Python 3.x installed on your machine.

Getting Started

1. Clone this repository to your local machine:bash
git clone https://github.com
Use code with caution.
2. Navigate to the game directory:bash
cd terminal-retro-racer
Use code with caution.
3. Run the game:bash
python main.py
Use code with caution.

Customization

You can easily adjust the difficulty or styling by tweaking the constants at the top of main.py:
python
SCREEN_WIDTH = 40   # Width of the game display
SCREEN_HEIGHT = 15  # Height of the game display
ROAD_WIDTH = 10     # Width of the drivable road
FPS = 10            # Game speed (frames per second)
Use code with caution.

License

This project is open source and available under the MIT License.

