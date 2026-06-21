# Number Guessing Game

import random

print("\n-----Welcome to Number Guessing Game-----\n")

secret_num = random.randint(1,10)
num = int(input("Guess the number: "))

if num == secret_num :
    print("Computer's number:",secret_num)
    print("Congratulations!! You Guessed it right.")
else:
    print("Computer's number:",secret_num)
    print("You lost :( ")
    