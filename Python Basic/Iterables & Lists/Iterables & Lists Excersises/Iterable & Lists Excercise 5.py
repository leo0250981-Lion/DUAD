numbers = []

# Pedimos 10 números al usuario
for i in range(10):
    user_number = int(input("Enter a number: "))
    numbers.append(user_number)

# Encontramos el número más alto manualmente
highest = numbers[0]

for num in numbers:
    if num > highest:
        highest = num

print(numbers)
print("The highest number was:", highest)