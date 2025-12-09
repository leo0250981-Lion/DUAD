#Exercise 2-2: Create program that asks the user for three numbers and checks conditions based on the value 30

# Ask for three numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Check if any number is 30 or if their sum equals 30
if num1 == 30 or num2 == 30 or num3 == 30 or (num1 + num2 + num3) == 30:
    print("Correct")
else:
    print("Incorrect")