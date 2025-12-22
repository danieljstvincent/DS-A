# Quick Start Guide

## For Learners 📚

Follow these steps to get the most out of this project:

### Step 1: Understand the Structure

1. **`game_functions.py`** - Contains function stubs with TODO comments
2. **Individual game files** (e.g., `hangman.py`) - Full implementations
3. **`solutions/solutions.md`** - Detailed explanations and algorithms

### Step 2: Pick a Starting Game

**Recommended order for beginners:**
1. Number Guessing Game (simplest)
2. Rock Paper Scissors
3. Hangman
4. Tic-Tac-Toe
5. Connect Four
6. Blackjack
7. Minesweeper
8. Snake Game
9. Text Adventure
10. Chess (most complex)

### Step 3: Think Through the Logic

1. Open `game_functions.py`
2. Find the functions for your chosen game (e.g., `get_word_hangman()`)
3. Read the TODO comments carefully
4. Think about:
   - What data structures do you need?
   - What are the input/output of each function?
   - How do the functions work together?
   - What edge cases need handling?

### Step 4: Implement One Function at a Time

```python
# Example: Start with get_word_hangman()
def get_word_hangman():
    # Your implementation here
    word_list = ["python", "hangman", "computer"]
    import random
    return random.choice(word_list).upper()
```

### Step 5: Test Your Logic

1. Write simple test calls:
```python
# Test your function
word = get_word_hangman()
print(f"Selected word: {word}")
print(f"Length: {len(word)}")
```

2. Test edge cases (empty lists, invalid input, etc.)

### Step 6: Implement the Full Game

1. Look at the full implementation in the game file (e.g., `hangman.py`)
2. Compare your approach with the solution
3. Try running the full game: `python hangman.py`

### Step 7: Review and Learn

1. Check `solutions/solutions.md` for detailed explanations
2. Understand time/space complexity
3. Look for optimization opportunities
4. Try adding your own features!

---

## For Players 🎮

Just want to play? It's simple!

### Quick Start

```bash
# Run the main launcher
python main.py

# Or run individual games
python hangman.py
python chess.py
# etc.
```

### Game Controls

Most games use simple text input. Common patterns:

- **Number games**: Enter numbers when prompted
- **Choice games**: Type your choice (e.g., "rock", "paper", "scissors")
- **Grid games**: Enter coordinates (e.g., "e4" for chess, "0-2" for tic-tac-toe)
- **Quit**: Usually type 'q', 'quit', or press Ctrl+C

### Tips

- Read the on-screen instructions in each game
- Some games have different controls (Snake uses WASD)
- All games return to menu after completion
- Press Ctrl+C to quit at any time

---

## Common Issues

### Problem: Game crashes or shows errors

**Solution:**
- Make sure you're using Python 3.7+
- Check that all files are in the same directory
- Try running: `python --version`

### Problem: Unicode characters don't display correctly (chess pieces, emojis)

**Solution:**
- Your terminal might not support Unicode
- Try a different terminal (Terminal on Mac, Windows Terminal on Windows)
- The games will still work, just without the fancy symbols

### Problem: Clear screen doesn't work

**Solution:**
- On Windows, use Command Prompt or PowerShell (not Git Bash)
- On Unix/Mac, any terminal should work
- The game will still function, just without screen clearing

---

## Learning Path

### Week 1: Basics
- [ ] Number Guessing Game
- [ ] Rock Paper Scissors
- [ ] Understand basic input/output

### Week 2: Data Structures
- [ ] Hangman (lists, sets, strings)
- [ ] Tic-Tac-Toe (2D lists/arrays)

### Week 3: Algorithms
- [ ] Connect Four (search algorithms)
- [ ] Minesweeper (recursion, flood fill)

### Week 4: Advanced
- [ ] Blackjack (state management)
- [ ] Snake Game (game loops, collision detection)
- [ ] Text Adventure (graph traversal)

### Week 5: Expert
- [ ] Chess (complex state, move validation)
- [ ] Add your own games!

---

**Happy Learning! 🚀**

