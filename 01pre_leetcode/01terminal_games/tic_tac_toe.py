"""
Tic-Tac-Toe Game

Classic 3x3 grid game where two players take turns marking X and O.
"""

import os

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def create_board():
    """Create an empty 3x3 board."""
    return [[' ' for _ in range(3)] for _ in range(3)]

def print_board(board):
    """Print the current board state."""
    print("\n  0   1   2")
    for i, row in enumerate(board):
        print(f"{i} {row[0]} | {row[1]} | {row[2]}")
        if i < 2:
            print("  ---------")

def is_valid_move(board, row, col):
    """Check if a move is valid."""
    return 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' '

def check_winner(board, player):
    """Check if a player has won."""
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    
    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True
    
    return False

def is_board_full(board):
    """Check if the board is full."""
    return all(cell != ' ' for row in board for cell in row)

def get_player_move(player, board):
    """Get a valid move from the player."""
    while True:
        try:
            print(f"\nPlayer {player}'s turn")
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))
            
            if is_valid_move(board, row, col):
                return row, col
            else:
                print("Invalid move! That cell is already taken or out of range.")
        except ValueError:
            print("Please enter valid numbers (0-2).")
        except KeyboardInterrupt:
            return None, None

def main():
    """Main game loop."""
    board = create_board()
    current_player = 'X'
    
    clear_screen()
    print("=" * 50)
    print("❌⭕ TIC-TAC-TOE ⭕❌")
    print("=" * 50)
    print("\nPlayers take turns. X goes first!")
    print("Enter row and column (0-2) to make your move.\n")
    
    while True:
        print_board(board)
        
        # Get move from current player
        row, col = get_player_move(current_player, board)
        if row is None:
            print("\nGame cancelled.")
            break
        
        # Make the move
        board[row][col] = current_player
        clear_screen()
        print_board(board)
        
        # Check for winner
        if check_winner(board, current_player):
            print(f"\n{'=' * 50}")
            print(f"🎉 Player {current_player} wins! 🎉")
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
    
    input("\nPress Enter to return to menu...")

if __name__ == "__main__":
    main()

