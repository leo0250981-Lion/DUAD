#Exercise 3: Temperature unit converter

# Ask the user for a temperature in Celsius
celsius = float(input("Enter temperature in Celsius: "))

# Convert to Fahrenheit and Kelvin
fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15

# Show the results
print("\n--- Temperature Conversion ---")
print(f"Celsius: {celsius}")
print(f"Fahrenheit: {fahrenheit}")
print(f"Kelvin: {kelvin}")