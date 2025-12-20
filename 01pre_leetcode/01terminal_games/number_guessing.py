"""
Number Guessing Game

Guess the number between 1 and 10 in 3 attempts!
"""

import random
import os

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    """Main game loop."""
    clear_screen()
    print("=" * 50)
    print("🎯 NUMBER GUESSING GAME 🎯")
    print("=" * 50)
    print("\nI'm thinking of a number between 1 and 10.")
    print("You have 3 attempts to guess it!\n")
    
    number_selected = random.randint(1, 10)
    attempts = 3
    guess = None
    
    while attempts > 0:
        try:
            guess = int(input(f"Attempts left: {attempts}. Enter your guess (1-10): "))
            
            if guess < 1 or guess > 10:
                print("Please enter a number between 1 and 10!")
                continue
            
            if guess == number_selected:
                print("\n" + "=" * 50)
                print("🎉🎉🎉 Congratulations! You Win! 🎉🎉🎉")
                print(f"You guessed the number: {number_selected}")
                print("=" * 50)
                break
            
            elif guess < number_selected:
                print("📈 Guess Higher!")
            else:
                print("📉 Guess Lower!")
            
            attempts -= 1
            
            if attempts > 0:
                print()
        
        except ValueError:
            print("Please enter a valid number!")
    
    if attempts == 0 and guess != number_selected:
        print("\n" + "=" * 50)
        print("💀 Game Over! You ran out of attempts!")
        print(f"The correct number was: {number_selected}")
        print("=" * 50)
    
    input("\nPress Enter to return to menu...")

if __name__ == "__main__":
    main()

