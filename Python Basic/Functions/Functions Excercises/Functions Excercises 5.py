def count_upper_lower(text):
    upper = 0
    lower = 0

    for char in text:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
    
    print(f"There are {upper} upper cases and {lower} lower cases")

count_upper_lower("I love Nación Sushi")