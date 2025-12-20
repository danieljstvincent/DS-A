"""
Minesweeper Game

Uncover all cells without hitting a mine!
"""

import random
import os

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def create_board(size=8, num_mines=10):
    """Create a minesweeper board."""
    board = [[' ' for _ in range(size)] for _ in range(size)]
    revealed = [[False for _ in range(size)] for _ in range(size)]
    
    # Place mines randomly
    mines_placed = 0
    while mines_placed < num_mines:
        row = random.randint(0, size - 1)
        col = random.randint(0, size - 1)
        if board[row][col] != '*':
            board[row][col] = '*'
            mines_placed += 1
    
    # Calculate numbers for each cell
    for row in range(size):
        for col in range(size):
            if board[row][col] != '*':
                count = 0
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        if dr == 0 and dc == 0:
                            continue
                        r, c = row + dr, col + dc
                        if 0 <= r < size and 0 <= c < size and board[r][c] == '*':
                            count += 1
                board[row][col] = str(count) if count > 0 else ' '
    
    return board, revealed

def print_board(board, revealed):
    """Print the current board state."""
    size = len(board)
    print("\n   " + " ".join(str(i) for i in range(size)))
    print("   " + "-" * (size * 2 - 1))
    
    for i, row in enumerate(board):
        print(f"{i}| ", end="")
        for j, cell in enumerate(row):
            if revealed[i][j]:
                print(cell, end=" ")
            else:
                print("?", end=" ")
        print()

def reveal_cell(board, revealed, row, col):
    """Reveal a cell and recursively reveal adjacent empty cells."""
    size = len(board)
    if not (0 <= row < size and 0 <= col < size) or revealed[row][col]:
        return
    
    revealed[row][col] = True
    
    # If cell is empty, reveal adjacent cells
    if board[row][col] == ' ':
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                reveal_cell(board, revealed, row + dr, col + dc)

def check_win(board, revealed):
    """Check if all non-mine cells are revealed."""
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != '*' and not revealed[i][j]:
                return False
    return True

def reveal_all(board, revealed):
    """Reveal all cells (for game over)."""
    for i in range(len(board)):
        for j in range(len(board[0])):
            revealed[i][j] = True

def main():
    """Main game loop."""
    size = 8
    num_mines = 10
    board, revealed = create_board(size, num_mines)
    
    clear_screen()
    print("=" * 50)
    print("💣 MINESWEEPER 💣")
    print("=" * 50)
    print(f"\nBoard size: {size}x{size}")
    print(f"Number of mines: {num_mines}")
    print("Enter row and column to reveal a cell.")
    print("Try to reveal all cells without hitting a mine!\n")
    
    while True:
        print_board(board, revealed)
        
        try:
            row = int(input("\nEnter row (0-7): "))
            col = int(input("Enter column (0-7): "))
            
            if not (0 <= row < size and 0 <= col < size):
                print("Invalid coordinates! Please enter values between 0-7.")
                continue
            
            if revealed[row][col]:
                print("This cell is already revealed!")
                continue
            
            # Check if mine
            if board[row][col] == '*':
                reveal_all(board, revealed)
                clear_screen()
                print_board(board, revealed)
                print("\n" + "=" * 50)
                print("💥 BOOM! You hit a mine! Game Over!")
                print("=" * 50)
                break
            
            # Reveal the cell
            reveal_cell(board, revealed, row, col)
            clear_screen()
            
            # Check win condition
            if check_win(board, revealed):
                reveal_all(board, revealed)
                print_board(board, revealed)
                print("\n" + "=" * 50)
                print("🎉 Congratulations! You cleared all mines!")
                print("=" * 50)
                break
                
        except ValueError:
            print("Please enter valid numbers.")
        except KeyboardInterrupt:
            print("\nGame cancelled.")
            break
    
    input("\nPress Enter to return to menu...")

if __name__ == "__main__":
    main()

