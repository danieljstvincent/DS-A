import random

choices = ['rock', 'paper', 'scissors']
win_conditions = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}

player_score = 0
computer_score = 0

while True:
    player_choice = input("\nChoose rock, paper, or scissors (or 'quit'): ").lower()
    
    if player_choice == 'quit':
        break
    
    if player_choice not in choices:
        print("Invalid choice!")
        continue
    
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")
    
    if player_choice == computer_choice:
        print("It's a tie!")
    elif win_conditions[player_choice] == computer_choice:
        print("You win!")
        player_score += 1
    else:
        print("Computer wins!")
        computer_score += 1
    
    print(f"Score - You: {player_score}, Computer: {computer_score}")