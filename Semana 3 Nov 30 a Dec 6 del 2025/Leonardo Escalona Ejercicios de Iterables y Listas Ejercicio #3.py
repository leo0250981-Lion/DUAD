my_list = [4, 3, 6, 1, 7]

# Store the first value in a temporary variable
temp = my_list[0]

# Replace the first value with the last one
my_list[0] = my_list[len(my_list) - 1]

# Assign the stored value to the last position
my_list[len(my_list) - 1] = temp

print(my_list)