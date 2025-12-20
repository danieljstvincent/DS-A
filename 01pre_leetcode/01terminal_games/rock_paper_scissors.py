"""
Rock Paper Scissors Game

Play the classic game against the computer!
"""

import random
import os

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    """Main game loop."""
    choices = ['rock', 'paper', 'scissors']
    win_conditions = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}
    
    player_score = 0
    computer_score = 0
    
    clear_screen()
    print("=" * 50)
    print("🪨📄✂️  ROCK PAPER SCISSORS ✂️📄🪨")
    print("=" * 50)
    print("\nChoose: rock, paper, or scissors")
    print("First to win 3 rounds wins the game!\n")
    
    while True:
        player_choice = input("Your choice (rock/paper/scissors or 'quit'): ").lower().strip()
        
        if player_choice == 'quit':
            break
        
        if player_choice not in choices:
            print("Invalid choice! Please choose rock, paper, or scissors.")
            continue
        
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")
        
        if player_choice == computer_choice:
            print("It's a tie!")
        elif win_conditions[player_choice] == computer_choice:
            print("You win this round! 🎉")
            player_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1
        
        print(f"\nScore - You: {player_score} | Computer: {computer_score}\n")
        
        if player_score >= 3:
            print("=" * 50)
            print("🎉🎉🎉 You won the game! 🎉🎉🎉")
            print("=" * 50)
            break
        elif computer_score >= 3:
            print("=" * 50)
            print("💀 Computer won the game! Better luck next time!")
            print("=" * 50)
            break
    
    input("\nPress Enter to return to menu...")

if __name__ == "__main__":
    main()