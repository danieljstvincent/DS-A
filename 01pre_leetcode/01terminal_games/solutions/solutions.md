# Terminal Games - Solutions & Documentation

This document provides detailed explanations of all terminal games, their functions, algorithms, and implementation details.

## Table of Contents

1. [Hangman](#hangman)
2. [Number Guessing Game](#number-guessing-game)
3. [Rock Paper Scissors](#rock-paper-scissors)
4. [Tic-Tac-Toe](#tic-tac-toe)
5. [Connect Four](#connect-four)
6. [Blackjack](#blackjack)
7. [Minesweeper](#minesweeper)
8. [Snake Game](#snake-game)
9. [Text Adventure](#text-adventure)
10. [Chess](#chess)

---

## Hangman

### Game Description
A word-guessing game where players try to guess a word letter by letter. Players have 6 incorrect guesses before losing.

### Key Functions

#### `get_word()`
- **Purpose**: Selects a random word from a predefined list
- **Returns**: A string (uppercase)
- **Algorithm**: Uses `random.choice()` to pick from a word list

#### `display_word(word, guessed_letters)`
- **Purpose**: Shows the current state of the word being guessed
- **Parameters**: 
  - `word`: The target word
  - `guessed_letters`: Set of correctly guessed letters
- **Returns**: String with guessed letters visible and others as underscores
- **Algorithm**: Iterates through word, displays letter if in guessed_letters, else "_"

#### `get_hangman_drawing(attempts_left)`
- **Purpose**: Returns ASCII art showing hangman state
- **Parameters**: `attempts_left` (int, 0-6)
- **Returns**: String containing ASCII art
- **Algorithm**: Returns predefined drawing based on attempts remaining

#### `main()`
- **Purpose**: Main game loop
- **Algorithm**:
  1. Select random word
  2. Initialize game state (attempts, guessed letters)
  3. Loop until win/loss:
     - Display current state
     - Get player input
     - Validate and process guess
     - Check win/loss conditions

### Time Complexity
- O(n) where n is the length of the word for display operations
- Overall game: O(n × m) where m is number of guesses

### Space Complexity
- O(n) for storing word and guessed letters

---

## Number Guessing Game

### Game Description
A simple number guessing game where players try to guess a number between 1-10 in 3 attempts.

### Key Functions

#### `main()`
- **Purpose**: Main game loop
- **Algorithm**:
  1. Generate random number (1-10)
  2. Initialize attempts counter (3)
  3. Loop until win or out of attempts:
     - Get player guess
     - Compare with target
     - Provide feedback (higher/lower)
     - Decrement attempts

### Time Complexity
- O(1) per guess
- Maximum 3 iterations: O(1) overall

### Space Complexity
- O(1)

---

## Rock Paper Scissors

### Game Description
Classic hand game where players compete against the computer. First to win 3 rounds wins.

### Key Functions

#### `main()`
- **Purpose**: Main game loop
- **Algorithm**:
  1. Initialize scores and win conditions dictionary
  2. Loop until one player reaches 3 wins:
     - Get player choice
     - Generate random computer choice
     - Determine winner using win_conditions mapping
     - Update scores
     - Check for game win

### Win Logic
- Uses dictionary: `{'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}`
- If player_choice beats computer_choice (checked via dictionary lookup), player wins

### Time Complexity
- O(1) per round
- Game continues until someone wins 3 rounds: O(1) per game

### Space Complexity
- O(1)

---

## Tic-Tac-Toe

### Game Description
Classic 3×3 grid game where two players alternate placing X and O. First to get three in a row wins.

### Key Functions

#### `create_board()`
- **Purpose**: Create empty 3×3 board
- **Returns**: 2D list (3×3) filled with spaces
- **Space Complexity**: O(1) - fixed size board

#### `print_board(board)`
- **Purpose**: Display current board state
- **Algorithm**: Iterate through rows and columns, print with separators

#### `is_valid_move(board, row, col)`
- **Purpose**: Validate if a move is legal
- **Returns**: Boolean
- **Algorithm**: Check bounds (0-2) and if cell is empty

#### `check_winner(board, player)`
- **Purpose**: Check if a player has won
- **Parameters**: 
  - `board`: Current board state
  - `player`: 'X' or 'O'
- **Returns**: Boolean
- **Algorithm**:
  1. Check all rows
  2. Check all columns
  3. Check main diagonal (0,0 to 2,2)
  4. Check anti-diagonal (0,2 to 2,0)

#### `is_board_full(board)`
- **Purpose**: Check if board is completely filled
- **Returns**: Boolean
- **Algorithm**: Check if all cells are non-empty

#### `main()`
- **Purpose**: Main game loop
- **Algorithm**:
  1. Create board
  2. Alternate players
  3. Get and validate moves
  4. Check for win/tie after each move
  5. Switch players

### Time Complexity
- Check winner: O(1) - fixed board size
- Overall game: O(1) - maximum 9 moves

### Space Complexity
- O(1) - fixed size board

---

## Connect Four

### Game Description
Two-player game where players drop colored discs into a 7-column, 6-row grid. First to get four in a row wins.

### Key Functions

#### `create_board(rows=6, cols=7)`
- **Purpose**: Create empty Connect Four board
- **Returns**: 2D list
- **Space Complexity**: O(rows × cols)

#### `drop_piece(board, col, piece)`
- **Purpose**: Drop a piece in a column (gravity simulation)
- **Parameters**:
  - `board`: Game board
  - `col`: Column index
  - `piece`: Player piece ('X' or 'O')
- **Returns**: Row index where piece landed, or -1 if column full
- **Algorithm**: 
  1. Start from bottom row
  2. Find first empty cell
  3. Place piece
  4. Return row position

#### `check_win(board, row, col, piece)`
- **Purpose**: Check if placing piece at (row, col) creates a win
- **Returns**: Boolean
- **Algorithm**:
  1. Check 4 directions: horizontal, vertical, both diagonals
  2. For each direction, count consecutive pieces in both directions
  3. If count >= 4, player wins
  4. Time Complexity: O(1) - checks fixed number of positions

#### `main()`
- **Purpose**: Main game loop
- **Algorithm**:
  1. Create board
  2. Alternate players
  3. Get column choice
  4. Drop piece
  5. Check for win or tie

### Time Complexity
- Drop piece: O(rows) = O(6)
- Check win: O(1)
- Overall: O(moves × rows) where moves ≤ 42

### Space Complexity
- O(rows × cols) = O(42) = O(1)

---

## Blackjack

### Game Description
Card game where players try to get as close to 21 as possible without going over.

### Key Functions

#### `create_deck()`
- **Purpose**: Create and shuffle a standard 52-card deck
- **Returns**: List of (rank, suit) tuples
- **Algorithm**: Generate all combinations, shuffle using `random.shuffle()`
- **Time Complexity**: O(52) = O(1)

#### `get_card_value(card)`
- **Purpose**: Get numeric value of a card
- **Returns**: Integer (1-11)
- **Algorithm**: Map face cards to 10, ace to 11, numbers to their value

#### `calculate_hand_value(hand)`
- **Purpose**: Calculate total value of a hand (handling aces)
- **Parameters**: List of cards
- **Returns**: Integer (total value)
- **Algorithm**:
  1. Sum all card values (aces as 11)
  2. If total > 21 and aces exist, reduce ace values to 1
  3. Return adjusted total
- **Time Complexity**: O(n) where n is hand size

#### `deal_card(deck, hand)`
- **Purpose**: Deal one card from deck to hand
- **Algorithm**: Pop from deck, append to hand
- **Time Complexity**: O(1)

#### `main()`
- **Purpose**: Main game loop
- **Algorithm**:
  1. Create and shuffle deck
  2. Deal initial 2 cards to each player
  3. Player turn: hit or stand
  4. Dealer turn: hit until >= 17
  5. Compare totals, determine winner

### Time Complexity
- Per game: O(cards dealt) ≈ O(10-15) = O(1)

### Space Complexity
- O(52) for deck = O(1)

---

## Minesweeper

### Game Description
Grid-based game where players reveal cells while avoiding hidden mines.

### Key Functions

#### `create_board(size=8, num_mines=10)`
- **Purpose**: Create board with randomly placed mines
- **Returns**: Tuple (board, revealed_matrix)
- **Algorithm**:
  1. Create empty board
  2. Randomly place mines
  3. Calculate numbers for each cell (adjacent mine count)
  4. Return board and revealed state matrix

#### `print_board(board, revealed)`
- **Purpose**: Display current board state
- **Algorithm**: Print revealed cells as numbers/empty, unrevealed as "?"

#### `reveal_cell(board, revealed, row, col)`
- **Purpose**: Reveal a cell and recursively reveal adjacent empty cells
- **Algorithm**: 
  1. Mark cell as revealed
  2. If cell is empty (no adjacent mines), recursively reveal neighbors
  3. Uses DFS (Depth-First Search)
- **Time Complexity**: O(size²) worst case
- **Space Complexity**: O(size²) for recursion stack

#### `check_win(board, revealed)`
- **Purpose**: Check if all non-mine cells are revealed
- **Returns**: Boolean
- **Algorithm**: Check all cells, return False if any non-mine unrevealed
- **Time Complexity**: O(size²)

#### `main()`
- **Purpose**: Main game loop
- **Algorithm**:
  1. Create board
  2. Get player input (row, col)
  3. Reveal cell
  4. Check for mine hit or win condition

### Time Complexity
- Per move: O(size²) in worst case (flood fill)
- Overall: O(moves × size²)

### Space Complexity
- O(size²) for board and revealed matrix

---

## Snake Game

### Game Description
Control a snake to eat food and grow. Avoid hitting walls or yourself.

### Key Functions

#### `create_board(size=20)`
- **Purpose**: Create empty game board
- **Returns**: 2D list
- **Space Complexity**: O(size²)

#### `place_food(board, snake)`
- **Purpose**: Place food at random empty position
- **Parameters**: Board and current snake positions
- **Returns**: Tuple (row, col) or None if no space
- **Algorithm**: Find all empty cells, randomly select one

#### `get_next_position(head, direction)`
- **Purpose**: Calculate next snake head position
- **Parameters**: Current head position, direction
- **Returns**: Tuple (new_row, new_col)
- **Algorithm**: Apply direction vector to current position

#### `is_valid_move(new_head, board, snake)`
- **Purpose**: Check if move is valid (no wall/self collision)
- **Returns**: Boolean
- **Algorithm**: 
  1. Check bounds
  2. Check self-collision (head in body)

#### `main()`
- **Purpose**: Main game loop
- **Algorithm**:
  1. Initialize snake (3 segments)
  2. Place food
  3. Game loop:
     - Get input
     - Move snake
     - Check collisions
     - Check food consumption
     - Grow snake if food eaten
     - Update display

### Time Complexity
- Per frame: O(snake_length) for collision check
- Overall: O(frames × snake_length)

### Space Complexity
- O(size²) for board + O(snake_length) for snake positions

---

## Text Adventure

### Game Description
Interactive fiction game where players explore rooms, collect items, and solve puzzles.

### Key Classes

#### `Room`
- **Attributes**:
  - `name`: Room name
  - `description`: Room description
  - `items`: List of items in room
  - `exits`: Dictionary mapping directions to room names
- **Methods**:
  - `add_exit(direction, room_name)`: Add exit to another room

#### `Game`
- **Attributes**:
  - `inventory`: List of collected items
  - `current_room`: Current room name
  - `rooms`: Dictionary of all rooms
- **Methods**:
  - `create_rooms()`: Initialize game world
  - `look_around()`: Display current room info
  - `go(direction)`: Move to another room
  - `take(item)`: Pick up item
  - `inventory_command()`: Display inventory

### Data Structure
- Graph structure: Rooms are nodes, exits are edges
- Items and inventory: Simple lists
- World state: Dictionary mapping room names to Room objects

### Time Complexity
- Room navigation: O(1) - dictionary lookup
- Item operations: O(n) where n is number of items

### Space Complexity
- O(rooms + items)

---

## Chess

### Game Description
Full chess game implementation with piece movement rules.

### Key Classes

#### `ChessBoard`
- **Attributes**:
  - `board`: 8×8 matrix storing (color, piece_type) tuples
  - `current_player`: 'white' or 'black'
  - `move_history`: List of moves
- **Methods**:
  - `create_initial_board()`: Set up starting position
  - `print_board()`: Display board with Unicode pieces
  - `parse_position(pos)`: Convert "e4" to (row, col)
  - `is_valid_move(from_pos, to_pos)`: Validate move legality
  - `is_path_clear(from_pos, to_pos)`: Check if path is unobstructed
  - `make_move(from_pos, to_pos)`: Execute move
  - `is_check(color)`: Check if king is in check

### Piece Movement Logic

#### Pawn
- Forward: 1 or 2 squares (if on starting row)
- Capture: Diagonal only
- Direction depends on color

#### Rook
- Horizontal or vertical
- Path must be clear

#### Bishop
- Diagonal only
- Path must be clear

#### Queen
- Any direction (horizontal, vertical, diagonal)
- Path must be clear

#### King
- One square in any direction

#### Knight
- L-shaped move (2+1 or 1+2)
- Can jump over pieces

### Time Complexity
- Move validation: O(1) to O(8) depending on piece type
- Check detection: O(64) - checks all opponent pieces
- Overall: O(moves × 64) per game

### Space Complexity
- O(64) for board = O(1)

---

## Running All Games

### Main Launcher

The `main.py` file provides a unified menu system to launch any game:

```python
python main.py
```

### Individual Games

Each game can also be run independently:

```python
python hangman.py
python number_guessing.py
# etc.
```

### Common Functions

Most games include:
- `clear_screen()`: OS-agnostic screen clearing
- `main()`: Main game entry point
- Input validation
- Error handling
- Return to menu functionality

---

## Design Patterns Used

1. **Game Loop Pattern**: All games use a main loop that continues until win/loss/quit
2. **State Management**: Games maintain state (board, scores, inventory, etc.)
3. **Input Validation**: User input is validated before processing
4. **Modular Functions**: Each game is broken into logical functions
5. **Object-Oriented Design**: Chess and Text Adventure use classes for complex state

---

## Future Enhancements

Possible improvements:
- Save/load game state
- Difficulty levels
- AI opponents
- Scoreboards/leaderboards
- Multiplayer networking
- Enhanced graphics/UI
- Sound effects
- Tutorial modes

---

## Testing

To test each game:
1. Run `python main.py`
2. Select game from menu
3. Play through to completion
4. Test edge cases (invalid input, win conditions, etc.)

---

*Last Updated: 2024*

