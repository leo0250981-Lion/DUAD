# Syntax Exercise #4
# Create a program that asks the user for three numbers and displays the largest.

# Ask the user for three numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Determine the largest number
largest = num1  # temporarily assume the first number is the largest

if num2 > largest:
    largest = num2

if num3 > largest:
    largest = num3

# Display the result
print(f"The largest number is: {largest}")