my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Create a new list to store only the even numbers
even_numbers = []

# Loop through the original list
for num in my_list:
    # If the number is even, add it to the new list
    if num % 2 == 0:
        even_numbers.append(num)

print(even_numbers)