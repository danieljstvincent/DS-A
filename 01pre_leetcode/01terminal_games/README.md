# Terminal Games Collection

A collection of terminal-based games implemented in Python, designed for learning data structures and algorithms.

## Prerequisites

- **Python 3.7 or higher**
- No external dependencies required (uses only Python standard library)
- A terminal/console that supports Unicode characters (for chess pieces and emojis)

## Installation

No installation needed! Just clone the repository and run:

```bash
python main.py
```

Or if you prefer Python 3 explicitly:

```bash
python3 main.py
```

## 📁 Project Structure

```
01terminal_games/
├── main.py                 # Main launcher - run this to play any game
├── game_functions.py       # Function stubs - think through game logic here
├── utils.py                # Shared utilities (clear_screen, input validation, etc.)
├── requirements.txt        # Python requirements (standard library only)
├── .gitignore              # Git ignore file
├── README.md               # This file
├── QUICK_START.md          # Quick start guide for learners
├── PROGRESS.md             # Progress tracking template
├── solutions/              # Documentation folder
│   └── solutions.md        # Detailed solutions and algorithm explanations
├── hangman.py              # Full game implementations
├── number_guessing.py
├── rock_paper_scissors.py
├── tic_tac_toe.py
├── connect_four.py
├── blackjack.py
├── minesweeper.py
├── snake_game.py
├── text_adventure.py
└── chess.py
```

## 🎮 How to Use

### Playing Games

**Option 1: Use the main launcher**
```bash
python main.py
```
Then select a game from the menu.

**Option 2: Run individual games**
```bash
python hangman.py
python chess.py
# etc.
```

### Learning Approach

**Step 1: Think Through Logic**
- Open `game_functions.py`
- Each function has TODO comments explaining what needs to be implemented
- Think through the algorithm before coding

**Step 2: Implement**
- Create or modify the actual game file (e.g., `hangman.py`)
- Use the functions you designed in `game_functions.py` as reference
- Implement the full game with user interface

**Step 3: Review Solutions**
- Check `solutions/solutions.md` for detailed explanations
- Compare your implementation with the documented algorithms
- Learn about time/space complexity

## 🎯 Games Included

1. **Hangman** - Word guessing game
2. **Number Guessing** - Guess the number in limited attempts
3. **Rock Paper Scissors** - Classic hand game
4. **Tic-Tac-Toe** - 3×3 grid game
5. **Connect Four** - Drop pieces to get 4 in a row
6. **Blackjack** - Card game to 21
7. **Minesweeper** - Find mines without exploding
8. **Snake Game** - Grow the snake by eating food
9. **Text Adventure** - Explore rooms and solve puzzles
10. **Chess** - Full chess implementation

## 📚 Learning Benefits

Each game teaches different concepts:

- **Data Structures**: Lists, dictionaries, sets, tuples
- **Algorithms**: Search, recursion, graph traversal, pathfinding
- **Game Logic**: State management, validation, win conditions
- **Problem Solving**: Breaking down complex problems into functions
- **Code Organization**: Modular design, separation of concerns

## 🔧 Development Workflow

1. **Design**: Use `game_functions.py` to design your functions
2. **Implement**: Build the full game in individual game files
3. **Test**: Play the game and debug
4. **Document**: Add notes about your implementation
5. **Review**: Check solutions.md for optimization ideas

## 💡 Tips

- Start with simpler games (Number Guessing, Rock Paper Scissors)
- Work through the function stubs in `game_functions.py` first
- Read the solutions documentation to understand best practices
- Experiment with different algorithms and approaches
- Add your own variations and features!

---

**Happy Coding! 🚀**

