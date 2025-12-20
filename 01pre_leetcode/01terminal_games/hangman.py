"""
Hangman Game

Guess the word letter by letter before running out of attempts.
"""

import random
import os

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_word():
    """Get a random word from the word list."""
    words = [
        "python", "javascript", "hangman", "computer", "programming",
        "algorithm", "function", "variable", "dictionary", "terminal",
        "keyboard", "mouse", "screen", "monitor", "laptop",
        "software", "hardware", "internet", "network", "server"
    ]
    return random.choice(words).upper()

def display_word(word, guessed_letters):
    """Display the word with guessed letters shown."""
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def get_hangman_drawing(attempts_left):
    """Return ASCII art for hangman based on attempts remaining."""
    drawings = [
        """
           +---+
           |   |
               |
               |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
               |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
           |   |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
          /|   |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
          /|\\  |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
          /|\\  |
          /    |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        =========
        """
    ]
    return drawings[6 - attempts_left]

def main():
    """Main game loop."""
    word = get_word()
    guessed_letters = set()
    attempts_left = 6
    incorrect_guesses = []
    
    clear_screen()
    print("=" * 50)
    print("🎯 HANGMAN GAME 🎯")
    print("=" * 50)
    print("\nGuess the word letter by letter!")
    print("You have 6 attempts to guess incorrectly.\n")
    
    while attempts_left > 0:
        # Display current state
        print(get_hangman_drawing(attempts_left))
        print(f"\nWord: {display_word(word, guessed_letters)}")
        print(f"Attempts left: {attempts_left}")
        
        if incorrect_guesses:
            print(f"Incorrect guesses: {', '.join(incorrect_guesses)}")
        
        # Check if word is complete
        if all(letter in guessed_letters for letter in word):
            print("\n" + "=" * 50)
            print(f"🎉 Congratulations! You guessed the word: {word}")
            print("=" * 50)
            break
        
        # Get player input
        guess = input("\nEnter a letter: ").upper().strip()
        
        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter!")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue
        
        guessed_letters.add(guess)
        
        # Check if guess is correct
        if guess in word:
            print(f"✓ Correct! '{guess}' is in the word.")
        else:
            print(f"✗ Wrong! '{guess}' is not in the word.")
            incorrect_guesses.append(guess)
            attempts_left -= 1
        
        print("\n" + "-" * 50)
    
    # Game over
    if attempts_left == 0:
        print(get_hangman_drawing(0))
        print("\n" + "=" * 50)
        print(f"💀 Game Over! The word was: {word}")
        print("=" * 50)
    
    input("\nPress Enter to return to menu...")

if __name__ == "__main__":
    main()

