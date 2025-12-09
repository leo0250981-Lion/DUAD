# Syntax Exercise #2
# Create a program that asks the user for their first name, last name, and age,
# and displays whether they are a baby, child, preteen, teenager, young adult, adult, or senior.

# Ask the user for their information
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = int(input("Enter your age: "))

# Determine the category according to age
if age < 2:
    category = "baby"
elif age < 10:
    category = "child"
elif age < 13:
    category = "preteen"
elif age < 18:
    category = "teenager"
elif age < 30:
    category = "young adult"
elif age < 60:
    category = "adult"
else:
    category = "senior"

# Display the result
print(f"{first_name} {last_name}, at {age} years old, you are considered a {category}.")