my_string = "Pizza with pineapple"

# We loop through the string starting from the last index and moving backward to 0
for i in range(len(my_string) - 1, -1, -1):
    print(my_string[i])