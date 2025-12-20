"""
Snake Game

Control the snake to eat food and grow. Avoid hitting walls or yourself!
"""

import random
import os
import time

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def create_board(size=20):
    """Create an empty game board."""
    return [[' ' for _ in range(size)] for _ in range(size)]

def print_board(board, score):
    """Print the game board."""
    clear_screen()
    print("=" * 50)
    print("🐍 SNAKE GAME 🐍")
    print("=" * 50)
    print(f"Score: {score}")
    print("Use WASD or arrow keys to move. Press 'q' to quit.\n")
    
    print("+" + "-" * len(board[0]) + "+")
    for row in board:
        print("|" + "".join(row) + "|")
    print("+" + "-" * len(board[0]) + "+")

def place_food(board, snake):
    """Place food at a random empty position."""
    empty_cells = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if (i, j) not in snake:
                empty_cells.append((i, j))
    
    if empty_cells:
        return random.choice(empty_cells)
    return None

def get_next_position(head, direction):
    """Calculate next position based on current direction."""
    row, col = head
    directions = {
        'w': (-1, 0), 'up': (-1, 0),
        's': (1, 0), 'down': (1, 0),
        'a': (0, -1), 'left': (0, -1),
        'd': (0, 1), 'right': (0, 1)
    }
    
    dr, dc = directions.get(direction.lower(), (0, 0))
    return (row + dr, col + dc)

def is_valid_move(new_head, board, snake):
    """Check if the move is valid."""
    row, col = new_head
    size = len(board)
    
    # Check wall collision
    if not (0 <= row < size and 0 <= col < size):
        return False
    
    # Check self collision
    if new_head in snake[:-1]:
        return False
    
    return True

def main():
    """Main game loop."""
    board_size = 15
    board = create_board(board_size)
    
    # Initialize snake in the center
    start_row = board_size // 2
    start_col = board_size // 2
    snake = [(start_row, start_col), (start_row, start_col - 1), (start_row, start_col - 2)]
    direction = 'd'  # Start moving right
    score = 0
    
    # Place initial food
    food = place_food(board, snake)
    
    print("\nGame starting in 3 seconds...")
    time.sleep(1)
    
    try:
        import select
        import sys
        import tty
        import termios
        
        def get_input():
            """Non-blocking input."""
            if select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], []):
                return sys.stdin.read(1)
            return None
        
        old_settings = termios.tcgetattr(sys.stdin)
        tty.setcbreak(sys.stdin.fileno())
        
        while True:
            # Update board
            board = create_board(board_size)
            
            # Place food
            if food:
                board[food[0]][food[1]] = '🍎'
            
            # Place snake
            for i, (row, col) in enumerate(snake):
                if i == 0:
                    board[row][col] = '🐍'
                else:
                    board[row][col] = '█'
            
            print_board(board, score)
            
            # Get input
            user_input = get_input()
            if user_input and user_input.lower() in ['w', 'a', 's', 'd', 'q']:
                if user_input.lower() == 'q':
                    break
                direction = user_input.lower()
            
            # Move snake
            new_head = get_next_position(snake[0], direction)
            
            if not is_valid_move(new_head, board, snake):
                print("\n" + "=" * 50)
                print("💥 Game Over! You hit a wall or yourself!")
                print(f"Final Score: {score}")
                print("=" * 50)
                break
            
            snake.insert(0, new_head)
            
            # Check if food eaten
            if new_head == food:
                score += 10
                food = place_food(board, snake)
                if food is None:
                    print("\n" + "=" * 50)
                    print("🎉 You won! Board is full!")
                    print(f"Final Score: {score}")
                    print("=" * 50)
                    break
            else:
                snake.pop()
            
            time.sleep(0.15)
        
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
    
    except (ImportError, AttributeError):
        # Fallback for Windows or systems without termios
        print("\nFor best experience, use a Unix-like system with termios.")
        print("Simple version: Press Enter after each move.\n")
        
        while True:
            # Update board
            board = create_board(board_size)
            
            if food:
                board[food[0]][food[1]] = '🍎'
            
            for i, (row, col) in enumerate(snake):
                board[row][col] = '🐍' if i == 0 else '█'
            
            print_board(board, score)
            
            user_input = input("\nDirection (w/a/s/d) or 'q' to quit: ").lower()
            if user_input == 'q':
                break
            if user_input in ['w', 'a', 's', 'd']:
                direction = user_input
            
            new_head = get_next_position(snake[0], direction)
            
            if not is_valid_move(new_head, board, snake):
                print("\n" + "=" * 50)
                print("💥 Game Over! You hit a wall or yourself!")
                print(f"Final Score: {score}")
                print("=" * 50)
                break
            
            snake.insert(0, new_head)
            
            if new_head == food:
                score += 10
                food = place_food(board, snake)
                if food is None:
                    print("\n" + "=" * 50)
                    print("🎉 You won! Board is full!")
                    print(f"Final Score: {score}")
                    print("=" * 50)
                    break
            else:
                snake.pop()
    
    input("\nPress Enter to return to menu...")

if __name__ == "__main__":
    main()

