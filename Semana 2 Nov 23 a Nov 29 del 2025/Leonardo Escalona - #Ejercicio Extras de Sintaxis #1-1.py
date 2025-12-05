#Exercise 1-1: Create a Program that calculates the final price with a discount based on the entered price

# Ask the user for the product price
price = float(input("Enter the product price: "))

# Calculate the discount based on the condition
if price < 100:
    discount = price * 0.02   # 2%
else:
    discount = price * 0.10   # 10%

# Calculate the final price
final_price = price - discount

# Show the result
print(f"The final price with discount is: {final_price}")