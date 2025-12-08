# This program handles exceptions
# Simple calculator program with separated functions

# ===== OPERATION FUNCTIONS =====
def add(current, num):
    return current + num

def subtract(current, num):
    return current - num

def multiply(current, num):
    return current * num

def divide(current, num):
    if num == 0:
        print("Error: Cannot divide by zero.")
        return current
    return current / num

# ===== INTERFACE FUNCTIONS =====
def display_menu(current): 
    print("\nCurrent number:", current)
    print("Choose an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Reset result")
    print("6. Exit")

def get_option():
    choice = input("Enter your option: ")
    if choice not in ["1", "2", "3", "4", "5", "6"]:
        print("Error: Invalid option. Please enter a number between 1 and 6.")
        return None
    return choice

def get_number():
    try:
        return float(input("Enter a number: "))
    except ValueError:
        print("Error: Invalid number. You must enter a numeric value.")
        return None

# ===== MAIN CALCULATOR FUNCTION =====
def calculator():
    current = 0
    while True:
        display_menu(current)
        choice = get_option()

        if choice is None:
            continue

        if choice == "6":
            print("Exiting calculator...")
            break

        if choice == "5":
            current = 0
            print("Result has been reset to 0.")
            continue

        num = get_number()
        if num is None:
            continue
        
        if choice == "1":
            current = add(current, num)
        elif choice == "2":
            current = subtract(current, num)
        elif choice == "3":
            current = multiply(current, num)
        elif choice == "4":
            current = divide(current, num)

        print("Updated result:", current)

# Run calculator
calculator()