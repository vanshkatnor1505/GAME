# Number guessing game using python

import random

def guessing_game():
    n_to_guess = random.randint(1, 100)
    guess = None
    attempts = 0
    print("Welcome to the Guessing Game!")
    print("I have selected a number between 1 and 100.")    

    while guess != n_to_guess:
        guess = int(input("Please enter your guess: "))
        attempts += 1
        if guess < n_to_guess:
            print("Too low! Try again.")
        elif guess > n_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {n_to_guess} in {attempts} attempts.")





guessing_game()
