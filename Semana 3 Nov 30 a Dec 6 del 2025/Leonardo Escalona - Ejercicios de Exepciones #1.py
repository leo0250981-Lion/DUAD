def calculator():
    current = 0

    while True:
        print("\nCurrent number:", current)
        print("Choose an operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Reset result")
        print("6. Exit")

        choice = input("Enter your option: ")

        # Validate option
        if choice not in ["1", "2", "3", "4", "5", "6"]:
            print("Error: Invalid option. Please enter a number between 1 and 6.")
            continue

        if choice == "6":
            print("Exiting calculator...")
            break

        if choice == "5":
            current = 0
            print("Result has been reset to 0.")
            continue

        # Ask for number
        try:
            num = float(input("Enter a number: "))
        except ValueError:
            print("Error: Invalid number. You must enter a numeric value.")
            continue

        # Math operations
        if choice == "1":
            current += num
        elif choice == "2":
            current -= num
        elif choice == "3":
            current *= num
        elif choice == "4":
            if num == 0:
                print("Error: Cannot divide by zero.")
                continue
            current /= num
        
        print("Updated result:", current)


# Run calculator
calculator()