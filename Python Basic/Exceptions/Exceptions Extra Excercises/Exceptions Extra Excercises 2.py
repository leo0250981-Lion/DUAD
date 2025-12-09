def convert_to_int(lst):
    converted_values = []
    invalid_values = []

    for item in lst:
        try:
            converted = int(item)
            converted_values.append(converted)
            print(f"{item} converted to {converted}")
        except ValueError:
            invalid_values.append(item)
            print(f"Could not convert element: {item}")

    return converted_values, invalid_values


def sum_values(lst):
    total = 0
    successful = []
    invalid = []

    for item in lst:
        try:
            number = float(item)
            total += number
            successful.append(number)
            print(f"{number} added successfully")
        except ValueError:
            invalid.append(item)
            print(f"Invalid element: {item}")

    print("Total sum:", total)
    return total, successful, invalid 

#Example of Usage 
# Testing convert_to_int
my_list = ['4', 'hello', '10', '5.2']
converted, invalid = convert_to_int(my_list)
print("\nConverted:", converted)
print("Invalid:", invalid)

# Testing sum_values
values = ['10', 'apple', '5.5', '3', 'n/a']
total, success, invalid_sum = sum_values(values)
print("\nSuccess:", success)
print("Invalid:", invalid_sum)
print("Final Total:", total)