"""
Game Function Templates - Think Through the Logic

This file contains function stubs and logic templates for each game.
Use this to think through the game logic before implementing.

Each function has:
- TODO comments describing what needs to be implemented
- Docstrings explaining the purpose
- Logic hints for algorithm design
"""

# ============================================================================
# HANGMAN FUNCTIONS
# ============================================================================

def get_word_hangman():
    """
    TODO: How do we select a random word?
    - Need a word list (predefined or from file)
    - Use random.choice() to pick one
    - Return the word (convert to uppercase for consistency)
    
    Returns:
        str: A random word in uppercase
    """
    pass

def display_word_hangman(word, guessed_letters):
    """
    TODO: How do we show the current state?
    - Loop through each character in the word
    - If letter is in guessed_letters set, show the letter
    - If not guessed, show underscore "_"
    - Add spaces between characters for readability
    - Return the display string
    
    Args:
        word (str): The target word to guess
        guessed_letters (set): Set of letters the player has guessed
    
    Returns:
        str: Display string like "P Y _ _ _ N"
    """
    pass

def check_guess_hangman(guess, word, guessed_letters):
    """
    TODO: How do we validate a guess?
    - Check if guess is a single letter (length == 1)
    - Check if guess is alphabetic
    - Check if already guessed (in guessed_letters set)
    - Check if in word (in word)
    - Update guessed_letters set if valid
    - Return status: (is_correct, is_repeat, is_invalid)
    
    Args:
        guess (str): The player's guess (single character)
        word (str): The target word
        guessed_letters (set): Set of previously guessed letters
    
    Returns:
        tuple: (is_correct: bool, is_repeat: bool, is_invalid: bool)
    """
    pass

def is_game_over_hangman(word, guessed_letters, attempts_left):
    """
    TODO: How do we know when game ends?
    - Win condition: All letters in word are in guessed_letters
      (no underscores left in display)
    - Lose condition: attempts_left == 0
    - Return status: 'win', 'lose', or 'playing'
    
    Args:
        word (str): The target word
        guessed_letters (set): Set of guessed letters
        attempts_left (int): Number of remaining incorrect guesses
    
    Returns:
        str: 'win', 'lose', or 'playing'
    """
    pass


# ============================================================================
# NUMBER GUESSING FUNCTIONS
# ============================================================================

def generate_random_number(min_val, max_val):
    """
    TODO: Generate a random number in range
    - Use random.randint(min_val, max_val)
    - Inclusive of both endpoints
    
    Args:
        min_val (int): Minimum value
        max_val (int): Maximum value
    
    Returns:
        int: Random number between min_val and max_val (inclusive)
    """
    pass

def compare_guess_number(guess, target):
    """
    TODO: Compare guess to target
    - If guess == target: return 'correct'
    - If guess < target: return 'higher'
    - If guess > target: return 'lower'
    
    Args:
        guess (int): Player's guess
        target (int): Target number
    
    Returns:
        str: 'correct', 'higher', or 'lower'
    """
    pass

def is_game_over_number(guess, target, attempts_left):
    """
    TODO: Check win/loss conditions
    - Win: guess == target
    - Lose: attempts_left == 0 and guess != target
    - Return status
    
    Args:
        guess (int): Player's current guess
        target (int): Target number
        attempts_left (int): Remaining attempts
    
    Returns:
        str: 'win', 'lose', or 'playing'
    """
    pass


# ============================================================================
# ROCK PAPER SCISSORS FUNCTIONS
# ============================================================================

def get_computer_choice_rps():
    """
    TODO: Generate random choice for computer
    - Choices: 'rock', 'paper', 'scissors'
    - Use random.choice() from list of choices
    - Return the choice string
    
    Returns:
        str: 'rock', 'paper', or 'scissors'
    """
    pass

def determine_winner_rps(player_choice, computer_choice):
    """
    TODO: Determine who wins
    - Rock beats Scissors
    - Paper beats Rock
    - Scissors beats Paper
    - Same choice = tie
    - Use dictionary mapping: {winner: loser}
    - Return: 'player', 'computer', or 'tie'
    
    Args:
        player_choice (str): Player's choice
        computer_choice (str): Computer's choice
    
    Returns:
        str: 'player', 'computer', or 'tie'
    
    Logic:
        win_conditions = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}
        if player_choice == computer_choice:
            return 'tie'
        elif win_conditions[player_choice] == computer_choice:
            return 'player'
        else:
            return 'computer'
    """
    pass


# ============================================================================
# TIC-TAC-TOE FUNCTIONS
# ============================================================================

def create_board_ttt():
    """
    TODO: Create 3x3 board
    - Return: 2D list (3 rows, 3 cols)
    - Initialize all cells with empty string or space ' '
    - Board representation: [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    
    Returns:
        list: 3x3 matrix filled with spaces
    """
    pass

def is_valid_move_ttt(board, row, col):
    """
    TODO: Check if move is valid
    - Check bounds: row in [0, 1, 2] and col in [0, 1, 2]
    - Check if cell is empty (board[row][col] == ' ')
    - Return True if valid, False otherwise
    
    Args:
        board (list): 3x3 game board
        row (int): Row index (0-2)
        col (int): Column index (0-2)
    
    Returns:
        bool: True if move is valid, False otherwise
    """
    pass

def make_move_ttt(board, row, col, player):
    """
    TODO: Place piece on board
    - Update board[row][col] with player symbol ('X' or 'O')
    - No return value (modifies board in place)
    
    Args:
        board (list): 3x3 game board
        row (int): Row index
        col (int): Column index
        player (str): Player symbol 'X' or 'O'
    """
    pass

def check_winner_ttt(board, player):
    """
    TODO: Check if player won
    - Check all 3 rows (all cells in row == player)
    - Check all 3 columns (all cells in column == player)
    - Check main diagonal (board[0][0], board[1][1], board[2][2])
    - Check anti-diagonal (board[0][2], board[1][1], board[2][0])
    - Return True if any line is complete
    
    Args:
        board (list): 3x3 game board
        player (str): Player symbol to check ('X' or 'O')
    
    Returns:
        bool: True if player won, False otherwise
    """
    pass

def is_board_full_ttt(board):
    """
    TODO: Check if all cells filled (tie condition)
    - Loop through all cells
    - Return True if no empty spaces (' '), False otherwise
    - Can use nested loops or any()/all() functions
    
    Args:
        board (list): 3x3 game board
    
    Returns:
        bool: True if board is full, False otherwise
    """
    pass


# ============================================================================
# CONNECT FOUR FUNCTIONS
# ============================================================================

def create_board_c4(rows=6, cols=7):
    """
    TODO: Create Connect Four board
    - Standard size: 6 rows x 7 columns
    - Initialize all cells with empty string or space
    - Return 2D list
    
    Args:
        rows (int): Number of rows (default 6)
        cols (int): Number of columns (default 7)
    
    Returns:
        list: rows x cols matrix filled with spaces
    """
    pass

def drop_piece_c4(board, col, piece):
    """
    TODO: Drop piece in column (gravity simulation)
    - Pieces fall to the bottom
    - Start checking from bottom row (highest row index)
    - Find first empty cell (' ') in the column
    - Place piece there
    - Return row index where piece was placed
    - Return -1 if column is full (all cells occupied)
    
    Args:
        board (list): Game board
        col (int): Column index (0-6)
        piece (str): Player piece ('X' or 'O')
    
    Returns:
        int: Row index where piece was placed, or -1 if column full
    """
    pass

def check_win_c4(board, row, col, piece):
    """
    TODO: Check for 4 in a row after placing piece
    - Check horizontal line (left-right)
    - Check vertical line (up-down)
    - Check diagonal / (top-left to bottom-right)
    - Check diagonal \\ (top-right to bottom-left)
    - For each direction, count consecutive pieces in both directions
    - If count >= 4, player wins
    - Only check around the newly placed piece (row, col)
    
    Args:
        board (list): Game board
        row (int): Row where piece was just placed
        col (int): Column where piece was just placed
        piece (str): Player piece ('X' or 'O')
    
    Returns:
        bool: True if 4+ in a row, False otherwise
    
    Logic:
        directions = [(0,1), (1,0), (1,1), (1,-1)]  # horizontal, vertical, 2 diagonals
        For each direction:
            count = 1  # count the piece we just placed
            Check both positive and negative direction
            If count >= 4: return True
    """
    pass


# ============================================================================
# BLACKJACK FUNCTIONS
# ============================================================================

def create_deck_bj():
    """
    TODO: Create 52-card deck
    - 4 suits: Hearts, Diamonds, Clubs, Spades
    - 13 ranks: A, 2-10, J, Q, K
    - Create list of (rank, suit) tuples
    - Shuffle the deck using random.shuffle()
    - Return shuffled deck
    
    Returns:
        list: List of (rank, suit) tuples, shuffled
    """
    pass

def get_card_value_bj(card):
    """
    TODO: Get numeric value of card
    - Face cards (J, Q, K) = 10
    - Ace = 11 (will be handled separately in calculate_hand_value)
    - Number cards = their numeric value
    - card is a tuple: (rank, suit)
    
    Args:
        card (tuple): (rank, suit) tuple
    
    Returns:
        int: Numeric value of the card
    """
    pass

def calculate_hand_value_bj(hand):
    """
    TODO: Calculate total hand value (handling aces)
    - Sum all card values (treat aces as 11 initially)
    - If total > 21 and hand contains aces:
      - Reduce ace value from 11 to 1 (subtract 10)
      - Repeat until total <= 21 or no more aces to adjust
    - Return final total
    
    Args:
        hand (list): List of (rank, suit) card tuples
    
    Returns:
        int: Total value of hand
    """
    pass

def should_dealer_hit_bj(dealer_value):
    """
    TODO: Dealer logic (house rules)
    - Dealer must hit if value < 17
    - Dealer must stand if value >= 17
    - Return True if dealer should hit, False to stand
    
    Args:
        dealer_value (int): Current total value of dealer's hand
    
    Returns:
        bool: True if dealer should hit, False to stand
    """
    pass


# ============================================================================
# MINESWEEPER FUNCTIONS
# ============================================================================

def create_board_ms(size, num_mines):
    """
    TODO: Create board with randomly placed mines
    - Create empty board (size x size)
    - Randomly place num_mines mines ('*' symbol)
    - Calculate numbers for each non-mine cell (count adjacent mines)
    - Return both board and revealed matrix
    - revealed matrix: tracks which cells have been revealed
    
    Args:
        size (int): Board size (e.g., 8 for 8x8)
        num_mines (int): Number of mines to place
    
    Returns:
        tuple: (board, revealed) where:
            board: 2D list with mines and numbers
            revealed: 2D boolean list (True = revealed, False = hidden)
    """
    pass

def count_adjacent_mines_ms(board, row, col, size):
    """
    TODO: Count mines in 8 adjacent cells
    - Check all 8 directions: up, down, left, right, and 4 diagonals
    - Skip if out of bounds
    - Skip the cell itself
    - Count how many are mines ('*')
    - Return count (0-8)
    
    Args:
        board (list): Game board
        row (int): Row index
        col (int): Column index
        size (int): Board size
    
    Returns:
        int: Number of adjacent mines (0-8)
    """
    pass

def reveal_cell_ms(board, revealed, row, col, size):
    """
    TODO: Reveal cell (recursive for empty cells)
    - Mark cell as revealed: revealed[row][col] = True
    - If cell is 0 (no adjacent mines), reveal all 8 neighbors
    - Use recursion: call reveal_cell_ms for each neighbor
    - Check bounds before revealing neighbors
    - Skip if already revealed
    - This creates a "flood fill" effect for empty areas
    
    Args:
        board (list): Game board
        revealed (list): Revealed cells matrix
        row (int): Row to reveal
        col (int): Column to reveal
        size (int): Board size
    """
    pass

def check_game_over_ms(board, revealed, row, col):
    """
    TODO: Check win/loss conditions
    - Loss: The cell just revealed (row, col) was a mine ('*')
    - Win: All non-mine cells are revealed
      (loop through board, check if all non-mines are in revealed)
    - Return status: 'win', 'lose', or 'playing'
    
    Args:
        board (list): Game board
        revealed (list): Revealed cells matrix
        row (int): Last revealed row
        col (int): Last revealed column
    
    Returns:
        str: 'win', 'lose', or 'playing'
    """
    pass


# ============================================================================
# SNAKE GAME FUNCTIONS
# ============================================================================

def create_board_snake(size):
    """
    TODO: Create game board
    - Square board of size x size
    - Initialize all cells with empty string or space
    - Return 2D list
    
    Args:
        size (int): Board size (e.g., 20 for 20x20)
    
    Returns:
        list: size x size matrix filled with spaces
    """
    pass

def initialize_snake_snake(start_row, start_col, length=3):
    """
    TODO: Create initial snake
    - Snake represented as list of (row, col) tuples
    - Head at start position
    - Body segments in a line (e.g., horizontally)
    - First element is head, rest is body
    - Example: [(10, 10), (10, 9), (10, 8)] for length 3
    
    Args:
        start_row (int): Starting row for snake head
        start_col (int): Starting column for snake head
        length (int): Initial snake length (default 3)
    
    Returns:
        list: List of (row, col) tuples representing snake
    """
    pass

def move_snake_snake(snake, direction):
    """
    TODO: Move snake one step
    - Calculate new head position based on direction:
      - 'w'/'up': (row-1, col)
      - 's'/'down': (row+1, col)
      - 'a'/'left': (row, col-1)
      - 'd'/'right': (row, col+1)
    - Insert new head at front of list
    - Remove tail (last element) if not growing
    - Return new snake list
    
    Args:
        snake (list): Current snake [(row, col), ...]
        direction (str): Movement direction ('w', 's', 'a', 'd')
    
    Returns:
        list: Updated snake with new head
    """
    pass

def check_collision_snake(snake, board_size):
    """
    TODO: Check for collisions
    - Wall collision: head position out of bounds
      (row < 0 or row >= board_size or col < 0 or col >= board_size)
    - Self collision: head position is in body (snake[1:])
    - Return True if collision detected, False otherwise
    
    Args:
        snake (list): Snake as list of (row, col) tuples
        board_size (int): Size of the board
    
    Returns:
        bool: True if collision, False otherwise
    """
    pass

def place_food_snake(board, snake):
    """
    TODO: Place food at random empty position
    - Find all empty cells (not in snake)
    - Randomly select one cell
    - Return (row, col) tuple
    - Return None if board is full (no empty cells)
    
    Args:
        board (list): Game board
        snake (list): Snake as list of (row, col) tuples
    
    Returns:
        tuple: (row, col) for food position, or None if full
    """
    pass


# ============================================================================
# TEXT ADVENTURE FUNCTIONS
# ============================================================================

def create_room_ta(name, description, items=None, exits=None):
    """
    TODO: Create a room object (can use dict or class)
    - Store room name, description
    - Store list of items in room
    - Store exits as dict: {direction: room_name}
    - Example: {'north': 'library', 'east': 'kitchen'}
    
    Args:
        name (str): Room name
        description (str): Room description
        items (list): List of items in room (default empty list)
        exits (dict): Dict mapping direction to room name (default empty dict)
    
    Returns:
        dict or object: Room representation
    """
    pass

def move_player_ta(current_room, direction, rooms):
    """
    TODO: Move player to new room
    - Get current room object from rooms dict
    - Check if exit exists in current_room.exits for direction
    - Check if door is locked (need key? - optional feature)
    - Update current_room to new room name
    - Return new room name, or None if move invalid
    
    Args:
        current_room (str): Current room name
        direction (str): Direction to move ('north', 'south', etc.)
        rooms (dict): Dictionary of all rooms {room_name: room_object}
    
    Returns:
        str: New room name, or None if invalid move
    """
    pass

def take_item_ta(room, item, inventory):
    """
    TODO: Pick up item from room
    - Check if item exists in room.items
    - Remove item from room.items
    - Add item to inventory list
    - Return True if successful, False if item not found
    
    Args:
        room (dict/object): Room object
        item (str): Item name to take
        inventory (list): Player's inventory list
    
    Returns:
        bool: True if item taken, False if not found
    """
    pass


# ============================================================================
# CHESS FUNCTIONS
# ============================================================================

def create_board_chess():
    """
    TODO: Initialize chess board with starting positions
    - 8x8 board
    - Store pieces as (color, piece_type) tuples: ('white', 'pawn')
    - Starting positions:
      - Row 0: black pieces (rook, knight, bishop, queen, king, bishop, knight, rook)
      - Row 1: black pawns
      - Row 6: white pawns
      - Row 7: white pieces (rook, knight, bishop, queen, king, bishop, knight, rook)
      - Rows 2-5: empty
    
    Returns:
        list: 8x8 matrix with piece tuples or empty strings
    """
    pass

def parse_position_chess(notation):
    """
    TODO: Convert algebraic notation to (row, col)
    - Input: "e4" format
    - First char = column (a-h -> 0-7)
    - Second char = row number (1-8 -> row 7-0, inverted!)
      Row 8 is at index 0, row 1 is at index 7
    - Return (row, col) tuple or None if invalid
    
    Args:
        notation (str): Algebraic notation like "e4"
    
    Returns:
        tuple: (row, col) or None if invalid
    
    Example:
        "e4" -> (4, 4)  # e=4, 4=row 4 (which is actually row 4 from top)
        Actually: row 1 is bottom (index 7), row 8 is top (index 0)
        So "e4" = column e (4), row 4 -> (8-4, 4) = (4, 4)
    """
    pass

def is_valid_move_chess(board, from_pos, to_pos):
    """
    TODO: Validate chess move (basic rules)
    - Get piece at from_pos
    - Check piece-specific movement rules:
      - Pawn: forward 1 or 2 (if starting), capture diagonal
      - Rook: horizontal or vertical, path must be clear
      - Bishop: diagonal, path must be clear
      - Queen: any direction, path must be clear
      - King: one square any direction
      - Knight: L-shape, can jump
    - Check if destination has same-color piece (can't capture own)
    - Check if path is clear (for rook, bishop, queen)
    - Return True if valid
    
    Args:
        board (list): Chess board
        from_pos (tuple): (row, col) of piece to move
        to_pos (tuple): (row, col) of destination
    
    Returns:
        bool: True if move is valid
    """
    pass

def is_path_clear_chess(board, from_pos, to_pos):
    """
    TODO: Check if path between two positions is clear
    - Calculate direction (row_delta, col_delta)
    - Normalize to unit vector (divide by gcd or use sign)
    - Step along path from from_pos to to_pos
    - Check each cell (except endpoints) is empty
    - Return True if path is clear
    
    Args:
        board (list): Chess board
        from_pos (tuple): Starting position
        to_pos (tuple): Ending position
    
    Returns:
        bool: True if path is clear
    """
    pass

def is_in_check_chess(board, color):
    """
    TODO: Check if king is in check
    - Find king position for given color
    - Loop through all opponent pieces
    - Check if any opponent piece can legally move to king position
    - Return True if king is in check
    
    Args:
        board (list): Chess board
        color (str): 'white' or 'black'
    
    Returns:
        bool: True if king is in check
    """
    pass

def is_checkmate_chess(board, color):
    """
    TODO: Check if king is in checkmate
    - King must be in check (use is_in_check_chess)
    - Try all possible moves for all pieces of that color
    - If no move can get out of check, it's checkmate
    - Return True if checkmate
    
    Args:
        board (list): Chess board
        color (str): 'white' or 'black'
    
    Returns:
        bool: True if checkmate
    """
    pass


# ============================================================================
# HELPER FUNCTIONS (used by multiple games)
# ============================================================================

def clear_screen():
    """
    Clear terminal screen (OS-agnostic)
    - Windows: 'cls'
    - Unix/Mac/Linux: 'clear'
    - Use os.system() to execute command
    
    Returns:
        None
    """
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def get_user_input(prompt, validation_func=None):
    """
    TODO: Get and validate user input
    - Display prompt to user
    - Get input using input()
    - If validation_func provided, call it with input
    - Retry if validation fails
    - Return validated input
    
    Args:
        prompt (str): Prompt to display
        validation_func (callable): Function to validate input, returns (is_valid, error_msg)
    
    Returns:
        str: Validated user input
    """
    pass

def print_board_formatted(board, row_labels=None, col_labels=None):
    """
    TODO: Generic function to print any 2D board nicely
    - Add row labels if provided
    - Add column labels if provided
    - Format with borders and separators
    - Useful for multiple games (tic-tac-toe, connect four, chess, etc.)
    
    Args:
        board (list): 2D list to print
        row_labels (list): Optional row labels
        col_labels (list): Optional column labels
    """
    pass

