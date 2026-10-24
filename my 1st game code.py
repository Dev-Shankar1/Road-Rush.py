import os
import random
import time

# --- Constants ---
SCREEN_WIDTH = 40
SCREEN_HEIGHT = 15
ROAD_WIDTH = 10
FPS = 10

# --- Game functions ---
def clear_screen():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_game(player_x, obstacles, coins, score):
    """Draws the game to the console."""
    clear_screen()
    game_map = [[' ' for _ in range(SCREEN_WIDTH)] for _ in range(SCREEN_HEIGHT)]

    # Draw road
    road_start = (SCREEN_WIDTH - ROAD_WIDTH) // 2
    for y in range(SCREEN_HEIGHT):
        for x in range(road_start, road_start + ROAD_WIDTH):
            game_map[y][x] = '|' if x == road_start or x == road_start + ROAD_WIDTH - 1 else ' '

    # Draw player car
    game_map[SCREEN_HEIGHT - 2][player_x] = '^'

    # Draw obstacles
    for obs in obstacles:
        if 0 <= obs['y'] < SCREEN_HEIGHT:
            game_map[obs['y']][obs['x']] = 'O'
    
    # Draw coins
    for coin in coins:
        if 0 <= coin['y'] < SCREEN_HEIGHT:
            game_map[coin['y']][coin['x']] = '$'

    # Print the map
    for row in game_map:
        print(''.join(row))

    print(f"Score: {score}")
    print("Use 'a' and 'd' to move. Press 'q' to quit.")

def main_game():
    """The main game loop for the text-based version."""
    player_x = SCREEN_WIDTH // 2
    obstacles = []
    coins = []
    score = 0
    
    running = True
    while running:
        # --- Handle input ---
        try:
            import sys, tty, termios
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            tty.setraw(sys.stdin.fileno())
            if sys.stdin in [sys.stdin]:
                char = sys.stdin.read(1)
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        except ImportError:
            # Fallback for systems without termios
            char = input("Move (a/d) or quit (q): ")

        if char == 'a':
            player_x = max((SCREEN_WIDTH - ROAD_WIDTH) // 2 + 1, player_x - 1)
        elif char == 'd':
            player_x = min((SCREEN_WIDTH + ROAD_WIDTH) // 2 - 2, player_x + 1)
        elif char == 'q':
            running = False
        
        # --- Game logic ---
        # Add new obstacles and coins
        if random.random() < 0.2:
            obstacles.append({'x': random.randint((SCREEN_WIDTH - ROAD_WIDTH) // 2 + 1, (SCREEN_WIDTH + ROAD_WIDTH) // 2 - 2), 'y': 0})
        if random.random() < 0.1:
            coins.append({'x': random.randint((SCREEN_WIDTH - ROAD_WIDTH) // 2 + 1, (SCREEN_WIDTH + ROAD_WIDTH) // 2 - 2), 'y': 0})

        # Move objects
        for obs in obstacles:
            obs['y'] += 1
        for coin in coins:
            coin['y'] += 1

        # Check for collisions and collect coins
        for obs in list(obstacles):
            if obs['y'] == SCREEN_HEIGHT - 2 and obs['x'] == player_x:
                print("Game Over!")
                running = False
            if obs['y'] >= SCREEN_HEIGHT:
                obstacles.remove(obs)
        
        for coin in list(coins):
            if coin['y'] == SCREEN_HEIGHT - 2 and coin['x'] == player_x:
                score += 10
                coins.remove(coin)
            if coin['y'] >= SCREEN_HEIGHT:
                coins.remove(coin)

        draw_game(player_x, obstacles, coins, score)
        time.sleep(1 / FPS)
    
    print(f"Final Score: {score}")

# Run the text-based game
if __name__ == "__main__":
    main_game()
    