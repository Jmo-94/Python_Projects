#This script allows you to guess the correct number picked by the application

import random

def guess(x):
    random_number= random.randint(1,x)
    guess=0
    while guess !=random_number:
        guess = int(input(f"guess a number between 1 and {x}: "))
        if guess == random_number:
            print("Congrats you have guessed the right number!")
        elif guess < random_number+3 and guess > random_number-3:
            print("You're getting warmer")
        else:
            print(" You're getting colder") 
        
    print("Thank you for playing!")


guess(20)

