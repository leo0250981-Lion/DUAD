# Ask for a valid name
while True:
    name = input("Enter your name: ")
    if name.isdigit():
        print("Error: The name cannot be a number. Try again.\n")
    else:
        break

# Ask for a valid age
while True:
    age = input("Enter your age: ")
    if age.isdigit():
        age = int(age)
        break
    else:
        print("Error: Invalid number. Try again.\n")

# Final message
print(f"\nHello {name}, your age is {age}")