#Exercise #1-2: Create a Program that evaluates a time entered in seconds and compares it with 10 minutes

# Ask the user for a time in seconds
seconds = int(input("Enter a time in seconds: "))

# 10 minutes expressed in seconds
ten_minutes = 600

# Compare the entered value
if seconds < ten_minutes:
    missing = ten_minutes - seconds
    print(f"Less — {missing} seconds left to reach 10 minutes.")
elif seconds > ten_minutes:
    print("Greater")
else:
    print("Equal")