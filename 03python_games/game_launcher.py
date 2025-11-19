import os
import importlib

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu():
    print("🎮 TEXT-BASED GAME COLLECTION 🎮")
    print("=" * 40)
    print("1. Hangman")
    print("2. Number Guessing Game")
    print("3. Tic-Tac-Toe")
    print("4. Rock Paper Scissors")
    print("5. Connect Four")
    print("6. Text Adventure")
    print("7. Blackjack")
    print("8. Minesweeper")
    print("9. Snake Game")
    print("10. Battleship")
    print("0. Exit")
    print("=" * 40)

def main():
    while True:
        clear_screen()
        show_menu()
        
        choice = input("Choose a game (0-10): ").strip()
        
        games = {
            '1': 'hangman',
            '2': 'number_guessing',
            '3': 'tic_tac_toe',
            '4': 'rock_paper_scissors',
            '5': 'connect_four',
            '6': 'text_adventure',
            '7': 'blackjack',
            '8': 'minesweeper',
            '9': 'snake_game',
            '10': 'battleship'
        }
        
        if choice == '0':
            print("Thanks for playing! 👋")
            break
        elif choice in games:
            try:
                # Import and run the game
                game_module = importlib.import_module(games[choice])
                if hasattr(game_module, 'main'):
                    game_module.main()
                elif hasattr(game_module, 'play'):
                    game_module.play()
                else:
                    print(f"Game {games[choice]} doesn't have a main/play function!")
                
                input("\nPress Enter to return to menu...")
            except ImportError:
                print(f"Game {games[choice]}.py not found!")
                input("Press Enter to continue...")
            except Exception as e:
                print(f"Error running game: {e}")
                input("Press Enter to continue...")
        else:
            print("Invalid choice! Please try again.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()