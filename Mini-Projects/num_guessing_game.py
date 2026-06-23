# Number Guessing Game

import random

print("\n-----Welcome to Number Guessing Game-----\n")

secret_num = random.randint(1,10)
attempts = 0

while True:
    guess = int(input(("Guess the number: ")))
    attempts+=1

    #check answer
    if guess == secret_num:
        print("\n🎉 Congratulations!,You guessed the number correct.")
        print(f"Attempts: {attempts}\n")
        break
    elif guess < secret_num:
        print("Too Low! Try again.\n")
    else:
        print("Too High! Try again.\n")