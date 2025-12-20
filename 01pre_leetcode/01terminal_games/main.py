"""
Main Launcher for Terminal Games Collection

This file provides a unified entry point for all terminal-based games.
Each game can be run individually or through this menu system.
"""

import os
import sys

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu():
    """Display the game selection menu."""
    clear_screen()
    print("=" * 50)
    print("🎮 TERMINAL GAMES COLLECTION 🎮")
    print("=" * 50)
    print("\nSelect a game to play:\n")
    print("1.  Hangman")
    print("2.  Number Guessing Game")
    print("3.  Rock Paper Scissors")
    print("4.  Tic-Tac-Toe")
    print("5.  Connect Four")
    print("6.  Blackjack")
    print("7.  Minesweeper")
    print("8.  Snake Game")
    print("9.  Text Adventure")
    print("10. Chess")
    print("\n0.  Exit")
    print("=" * 50)

def run_game(module_name):
    """Import and run a game module."""
    try:
        game_module = __import__(module_name, fromlist=[''])
        
        # Try different common entry point names
        if hasattr(game_module, 'main'):
            game_module.main()
        elif hasattr(game_module, 'play'):
            game_module.play()
        elif hasattr(game_module, 'run'):
            game_module.run()
        else:
            print(f"Error: {module_name} doesn't have a main/play/run function!")
            input("\nPress Enter to continue...")
    except ImportError as e:
        print(f"Error: Could not import {module_name}")
        print(f"Details: {e}")
        input("\nPress Enter to continue...")
    except Exception as e:
        print(f"Error running {module_name}: {e}")
        import traceback
        traceback.print_exc()
        input("\nPress Enter to continue...")

def main():
    """Main game launcher loop."""
    games = {
        '1': 'hangman',
        '2': 'number_guessing',
        '3': 'rock_paper_scissors',
        '4': 'tic_tac_toe',
        '5': 'connect_four',
        '6': 'blackjack',
        '7': 'minesweeper',
        '8': 'snake_game',
        '9': 'text_adventure',
        '10': 'chess'
    }
    
    while True:
        show_menu()
        choice = input("\nEnter your choice (0-10): ").strip()
        
        if choice == '0':
            clear_screen()
            print("Thanks for playing! 👋\n")
            break
        elif choice in games:
            clear_screen()
            run_game(games[choice])
        else:
            print("\nInvalid choice! Please enter a number between 0-10.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        clear_screen()
        print("\n\nGame interrupted. Goodbye! 👋\n")
        sys.exit(0)

