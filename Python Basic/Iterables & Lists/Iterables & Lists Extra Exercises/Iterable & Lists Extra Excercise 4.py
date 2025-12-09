my_list = [10, 20, 30, 40, 50]

# Step 1: Calculate the average manually
total = 0

for num in my_list:
    total += num

average = total / len(my_list)

print("Average:", average)

# Step 2: Create a new list with values greater than the average
new_list = []

for num in my_list:
    if num > average:
        new_list.append(num)

print("New list:", new_list)