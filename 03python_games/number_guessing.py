""" 
1. generate number 1-10
. limit to 3 guesses
2. input to guess
3. To the user higher or lower
4
5. If they guess correct "w" and if not "L"

"""
import random

list_of_numbers = range(1,11)
number_selected = random.choice(list_of_numbers)
attempts = 3


while attempts != 0: 
    guess = input(f"please enter a number 1-10: ")
    guess = int(guess)

    if guess == number_selected:
        print("Congrats you Win")
        break
    

    elif guess < number_selected:
        print("Guess Higher")
        attempts -= 1
  
    else:
        guess > number_selected
        print ("guess lower")
        attempts -= 1

if attempts == 0 and guess != number_selected:
    print(f"Game Over! The correct number was {number_selected}")

