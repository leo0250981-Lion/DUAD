#Exercise 4: # Custom multiplication table

# Ask the user for a number from 1 to 10
number = int(input("Enter a number (1–10): "))

print("\n--- Multiplication Table ---")

# Show multiplication table from 1 to 12
for i in range(1, 13):
    print(f"{number} x {i} = {number * i}")