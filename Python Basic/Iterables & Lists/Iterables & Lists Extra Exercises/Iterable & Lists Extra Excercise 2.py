my_list = [3, 6, 0, -2, 4]

# We assume at the beginning that all numbers are positive
all_positive = True

# Loop through the list
for num in my_list:
    if num <= 0:        # If we find a negative number or zero
        all_positive = False
        break           # We stop because the condition is already broken

# Show the result
if all_positive:
    print("All the numbers are positive.")
else:
    print("There is at least one negative number or zero.")