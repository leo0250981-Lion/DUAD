# Syntax Exercise #3
# Create a program with a secret number from 1 to 10. The program should not close until the user guesses the number.
## You must research how to generate a random number that changes each time the program runs.
import random   # We import the library to generate random numbers

# We generate a secret number from 1 to 10
secret_number = random.randint(1, 10)

print("Guess the secret number between 1 and 10")

# Loop that continues until the user guesses it
while True:
    attempt = int(input("Enter your guess: "))

    if attempt == secret_number:
        print("🎉 Correct! You guessed the secret number.")
        break  # Exits the loop when the user gets it right
    else:
        print("❌ Incorrect, try again...")
