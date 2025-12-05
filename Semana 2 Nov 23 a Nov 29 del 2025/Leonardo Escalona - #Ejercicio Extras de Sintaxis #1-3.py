#Exercise #1-3: Create a program that asks the user for a number and sums all numbers from 1 up to that number

# Ask the user for a number
number = int(input("Enter a number: "))

# Variable to store the total sum
total_sum = 0

# Loop to add numbers from 1 to the entered number
for i in range(1, number + 1):
    total_sum += i

# Show the result
print(f"The total sum from 1 to {number} is: {total_sum}")