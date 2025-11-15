"While attempts is and All the letter are not guessed, Keep running"
""" 
A way to guess letter by letter
a loop that goes until all the attempts are used or all the letters are guess

 """
import random

names = ["Daniel", "Dillon", "Gizzell"]
name = random.choice(names)
gessed = "_" * len(name)
attempts = 6

gessus = input(f"Guessed left {attempts}")

while attempts > 0 and "_" in gessed:
    ''.join(g)