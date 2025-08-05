import random

choices = ["rock","paper","sissors"]

personal_choice = input("Please select rock, paper or sissors: ")
computer_choice = random.choices

print(f"CHooses {choices}")

winner_count = 3
player_one_count = 0
computer_count = 0

def match(personal_choice, computer_chice):
    if personal_choice == computer_choice:
        return ("It is a tie, Nobody wins")
    elif(
        if personal_choice == "rock" and computer_choice == "sissors" {
        
        } or 
        personal_choice == "sissors" and computer_choice == "paper" or 
        personal_choice == "paper" and computer_choice == "rock"
    ):
        return ("You win")
    else :
        return ("You lose")
    

        


