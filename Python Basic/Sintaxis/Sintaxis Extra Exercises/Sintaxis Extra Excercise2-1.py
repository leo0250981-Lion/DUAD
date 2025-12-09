#Exercise 2-1: Create a flowchart that contains a secret number from 1 to 10 and asks the user to guess that number. The algorithm should not end until the user guesses the number.

import random

# Generate a secret number from 1 to 10
secret_number = random.randint(1, 10)

print("Guess the secret number between 1 and 10")

# Loop until the user guesses correctly
guess = None  # Temporary value to start the loop

while guess != secret_number:
    guess = int(input("Enter your guess: "))

    if guess == secret_number:
        print("🎉 Correct! You guessed the secret number.")
    else:
        print("❌ Incorrect, try again...")