def create_board(rows=6, cols=7):
    return [[' ' for _ in range(cols)] for _ in range(rows)]

def drop_piece(board, col, piece):
    for row in reversed(range(len(board))):
        if board[row][col] == ' ':
            board[row][col] = piece
            return row
    return -1  # Column full

def check_win(board, row, col, piece):
    # Check horizontal, vertical, and diagonals
    directions = [(0,1), (1,0), (1,1), (1,-1)]
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

# === JUST ADD THIS ===
def main():
    board = create_board()
    current_player = 'X'
    
    while True:
        # Print board
        for row in board:
            print('|' + '|'.join(row) + '|')
        print('-' * 15)
        
        # Get player input
        col = int(input(f"Player {current_player}, choose column (0-6): "))
        
        # Drop piece
        row = drop_piece(board, col, current_player)
        if row == -1:
            print("Column full! Try again.")
            continue
        
        # Check win
        if check_win(board, row, col, current_player):
            for row in board:
                print('|' + '|'.join(row) + '|')
            print(f"Player {current_player} wins!")
            break
        
        # Switch player
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    main()