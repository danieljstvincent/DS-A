"""
Chess Game

Play a full game of chess in the terminal!
"""

import os

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

class ChessBoard:
    """Represents a chess board and game state."""
    
    # Unicode chess pieces
    PIECES = {
        'white': {
            'king': '♔', 'queen': '♕', 'rook': '♖',
            'bishop': '♗', 'knight': '♘', 'pawn': '♙'
        },
        'black': {
            'king': '♚', 'queen': '♛', 'rook': '♜',
            'bishop': '♝', 'knight': '♞', 'pawn': '♟'
        }
    }
    
    def __init__(self):
        self.board = self.create_initial_board()
        self.current_player = 'white'
        self.move_history = []
    
    def create_initial_board(self):
        """Create the initial chess board setup."""
        board = [[' ' for _ in range(8)] for _ in range(8)]
        
        # Place pawns
        for col in range(8):
            board[1][col] = ('black', 'pawn')
            board[6][col] = ('white', 'pawn')
        
        # Place other pieces
        back_row = ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook']
        for col in range(8):
            board[0][col] = ('black', back_row[col])
            board[7][col] = ('white', back_row[col])
        
        return board
    
    def get_piece_symbol(self, piece):
        """Get the Unicode symbol for a piece."""
        if piece == ' ':
            return '·'
        color, piece_type = piece
        return self.PIECES[color][piece_type]
    
    def print_board(self):
        """Print the current board state."""
        clear_screen()
        print("=" * 50)
        print(f"♔ CHESS GAME - {self.current_player.upper()}'s Turn ♔")
        print("=" * 50)
        print("\n   a b c d e f g h")
        print("  " + "-" * 17)
        
        for row in range(8):
            print(f"{8-row}| ", end="")
            for col in range(8):
                piece = self.board[row][col]
                symbol = self.get_piece_symbol(piece)
                print(symbol, end=" ")
            print(f"|{8-row}")
        
        print("  " + "-" * 17)
        print("   a b c d e f g h\n")
    
    def parse_position(self, pos):
        """Parse a position string like 'e4' to (row, col)."""
        if len(pos) != 2:
            return None
        col = ord(pos[0].lower()) - ord('a')
        try:
            row = 8 - int(pos[1])
            if 0 <= row < 8 and 0 <= col < 8:
                return (row, col)
        except ValueError:
            pass
        return None
    
    def is_valid_move(self, from_pos, to_pos):
        """Check if a move is valid (simplified version)."""
        from_row, from_col = from_pos
        to_row, to_col = to_pos
        
        piece = self.board[from_row][from_col]
        if piece == ' ':
            return False
        
        color, piece_type = piece
        if color != self.current_player:
            return False
        
        target = self.board[to_row][to_col]
        if target != ' ':
            target_color, _ = target
            if target_color == color:
                return False
        
        # Basic movement rules (simplified)
        if piece_type == 'pawn':
            direction = -1 if color == 'white' else 1
            start_row = 6 if color == 'white' else 1
            
            # Forward move
            if from_col == to_col and self.board[to_row][to_col] == ' ':
                if to_row == from_row + direction:
                    return True
                if from_row == start_row and to_row == from_row + 2 * direction:
                    return True
            
            # Capture diagonally
            if abs(to_col - from_col) == 1 and to_row == from_row + direction:
                if self.board[to_row][to_col] != ' ':
                    return True
        
        elif piece_type == 'rook':
            if from_row == to_row or from_col == to_col:
                # Check if path is clear
                return self.is_path_clear(from_pos, to_pos)
        
        elif piece_type == 'bishop':
            if abs(to_row - from_row) == abs(to_col - from_col):
                return self.is_path_clear(from_pos, to_pos)
        
        elif piece_type == 'queen':
            if (from_row == to_row or from_col == to_col or 
                abs(to_row - from_row) == abs(to_col - from_col)):
                return self.is_path_clear(from_pos, to_pos)
        
        elif piece_type == 'king':
            if abs(to_row - from_row) <= 1 and abs(to_col - from_col) <= 1:
                return True
        
        elif piece_type == 'knight':
            dr = abs(to_row - from_row)
            dc = abs(to_col - from_col)
            return (dr == 2 and dc == 1) or (dr == 1 and dc == 2)
        
        return False
    
    def is_path_clear(self, from_pos, to_pos):
        """Check if the path between two positions is clear."""
        from_row, from_col = from_pos
        to_row, to_col = to_pos
        
        row_step = 0 if to_row == from_row else (1 if to_row > from_row else -1)
        col_step = 0 if to_col == from_col else (1 if to_col > from_col else -1)
        
        row, col = from_row + row_step, from_col + col_step
        while (row, col) != (to_row, to_col):
            if self.board[row][col] != ' ':
                return False
            row += row_step
            col += col_step
        
        return True
    
    def make_move(self, from_pos, to_pos):
        """Make a move on the board."""
        if not self.is_valid_move(from_pos, to_pos):
            return False
        
        from_row, from_col = from_pos
        to_row, to_col = to_pos
        
        piece = self.board[from_row][from_col]
        captured = self.board[to_row][to_col]
        
        self.board[to_row][to_col] = piece
        self.board[from_row][from_col] = ' '
        
        self.move_history.append((from_pos, to_pos, piece, captured))
        
        # Switch players
        self.current_player = 'black' if self.current_player == 'white' else 'white'
        
        return True
    
    def is_check(self, color):
        """Check if a king is in check (simplified)."""
        # Find the king
        king_pos = None
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if piece != ' ':
                    piece_color, piece_type = piece
                    if piece_color == color and piece_type == 'king':
                        king_pos = (row, col)
                        break
            if king_pos:
                break
        
        if not king_pos:
            return False
        
        # Check if any opponent piece can attack the king
        opponent = 'black' if color == 'white' else 'white'
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if piece != ' ':
                    piece_color, _ = piece
                    if piece_color == opponent:
                        if self.is_valid_move((row, col), king_pos):
                            return True
        
        return False

def main():
    """Main game loop."""
    board = ChessBoard()
    
    print("\nWelcome to Chess!")
    print("Enter moves in algebraic notation (e.g., 'e2 e4')")
    print("Or enter 'q' to quit.\n")
    input("Press Enter to start...")
    
    while True:
        board.print_board()
        
        if board.is_check(board.current_player):
            print(f"⚠️  CHECK! {board.current_player} king is in check!")
        
        move_input = input(f"\n{board.current_player.capitalize()} move (from to, e.g., 'e2 e4'): ").strip().lower()
        
        if move_input == 'q':
            print("\nGame ended.")
            break
        
        move_parts = move_input.split()
        if len(move_parts) != 2:
            print("Invalid format! Use: 'e2 e4'")
            input("Press Enter to continue...")
            continue
        
        from_pos = board.parse_position(move_parts[0])
        to_pos = board.parse_position(move_parts[1])
        
        if from_pos is None or to_pos is None:
            print("Invalid positions! Use format like 'e2', 'a1', etc.")
            input("Press Enter to continue...")
            continue
        
        if board.make_move(from_pos, to_pos):
            print("Move made successfully!")
        else:
            print("Invalid move! Try again.")
            input("Press Enter to continue...")
    
    input("\nPress Enter to return to menu...")

if __name__ == "__main__":
    main()

