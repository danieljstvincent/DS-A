"While attempts is and All the letter are not guessed, Keep running"
import random

words = ["cat","dog","fish", "pig"]
word = random.choice(words)
guessed = ['_'] * len(words)
attempts = 10


while attempts > 0 and '_' in guessed:
    print(' '.join(guessed))
    guess = input(f"Attempts left: {attempts}. Guess a letter: ").lower()

    if guess in word:
        for i, letter in enumerate(word):
            if letter == guess:
                guessed[i] = guess
    else:
        attempts -= 1 
        print("Your answer is wrong")