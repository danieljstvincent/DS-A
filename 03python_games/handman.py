"While attempts is and All the letter are not guessed, Keep running"
""" 
A way to guess letter by letter
a loop that goes until all the attempts are used or all the letters are guess

 """
import random

animals = ["dog","cat","frog"]
animal = random.choice(animals)
guessed = "_" * len(animal)
attempts = 6



while attempts > 0 and  '_' and guessed:
    print(''.join(guessed))
    guess = input(f"You have {attempts}. left Guess a letter: ").lower()

    if guess in animal:
        for i, letter in enumerate(animal):
            if letter == guess:
                guessed[i] = letter
        print(guessed)
    else:
        attempts -= 1
        print("wrong guess!")
