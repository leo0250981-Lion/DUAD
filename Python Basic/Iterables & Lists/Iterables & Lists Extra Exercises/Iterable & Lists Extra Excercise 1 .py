# Ask the user to enter numbers separated by commas
user_input = input("Enter a list of numbers separated by commas: ")

# Convert that input into a list of numbers
my_list = []
current_number = ""

for char in user_input:
    if char != ",":
        current_number += char
    else:
        my_list.append(int(current_number))
        current_number = ""

# Add the last number after the loop
my_list.append(int(current_number))

# Ask for the number to search
number_to_find = int(input("Enter the number you want to search for: "))

# Count manually how many times it appears
count = 0

for num in my_list:
    if num == number_to_find:
        count += 1

print("The number", number_to_find, "appears", count, "times.")