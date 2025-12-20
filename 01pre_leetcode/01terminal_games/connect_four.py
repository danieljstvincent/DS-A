"""
Connect Four Game

Drop pieces in columns to get four in a row!
"""

import os

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def create_board(rows=6, cols=7):
    """Create an empty Connect Four board."""
    return [[' ' for _ in range(cols)] for _ in range(rows)]

def print_board(board):
    """Print the current board state."""
    print("\n  " + " ".join(str(i) for i in range(len(board[0]))))
    print("  " + "-" * (len(board[0]) * 2 - 1))
    for row in board:
        print("|" + "|".join(row) + "|")
    print("  " + "-" * (len(board[0]) * 2 - 1))

def drop_piece(board, col, piece):
    """Drop a piece in the specified column."""
    for row in reversed(range(len(board))):
        if board[row][col] == ' ':
            board[row][col] = piece
            return row
    return -1  # Column full

def check_win(board, row, col, piece):
    """Check if a player has won after placing a piece."""
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]  # horizontal, vertical, diagonals
    
    for dr, dc in directions:
        count = 1
        # Check both directions
        for direction in [1, -1]:
            r, c = row, col
            for _ in range(3):
                r += dr * direction
                c += dc * direction
                if (0 <= r < len(board) and 0 <= c < len(board[0]) 
                    and board[r][c] == piece):
                    count += 1
                else:
                    break
        if count >= 4:
            return True
    return False

def is_board_full(board):
    """Check if the board is completely full."""
    return all(cell != ' ' for row in board for cell in row)

def main():
    """Main game loop."""
    board = create_board()
    current_player = 'X'
    player_symbols = {'X': '🔴', 'O': '🟡'}
    
    clear_screen()
    print("=" * 50)
    print("🔴🟡 CONNECT FOUR 🟡🔴")
    print("=" * 50)
    print("\nDrop pieces in columns (0-6) to get four in a row!")
    print("Player X: 🔴  |  Player O: 🟡\n")
    
    while True:
        print_board(board)
        
        try:
            col = int(input(f"\nPlayer {current_player} ({player_symbols[current_player]}), choose column (0-6): "))
            
            if not (0 <= col < len(board[0])):
                print("Invalid column! Please choose 0-6.")
                input("Press Enter to continue...")
                clear_screen()
                continue
            
            row = drop_piece(board, col, current_player)
            if row == -1:
                print("Column is full! Try another column.")
                input("Press Enter to continue...")
                clear_screen()
                continue
            
            clear_screen()
            print_board(board)
            
            # Check for win
            if check_win(board, row, col, current_player):
                print(f"\n{'=' * 50}")
                print(f"🎉 Player {current_player} ({player_symbols[current_player]}) wins! 🎉")
                print("=" * 50)
                break
            
            # Check for tie
            if is_board_full(board):
                print(f"\n{'=' * 50}")
                print("🤝 It's a tie! 🤝")
                print("=" * 50)
                break
            
            # Switch player
            current_player = 'O' if current_player == 'X' else 'X'
        
        except ValueError:
            print("Please enter a valid number (0-6).")
            input("Press Enter to continue...")
            clear_screen()
        except KeyboardInterrupt:
            print("\n\nGame cancelled.")
            break
    
    input("\nPress Enter to return to menu...")

if __name__ == "__main__":
    main()