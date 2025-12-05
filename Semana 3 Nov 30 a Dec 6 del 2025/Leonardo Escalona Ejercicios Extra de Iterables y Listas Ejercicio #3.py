my_list = [9, 4, 7, 1, 5]

# Assume the first value is the smallest
smallest = my_list[0]

# Compare each number with the current smallest value
for num in my_list:
    if num < smallest:
        smallest = num

print("The smallest value is", smallest)