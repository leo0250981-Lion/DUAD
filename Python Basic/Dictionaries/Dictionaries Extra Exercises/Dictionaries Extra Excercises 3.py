products = [
    {"name": "Headphones", "category": "Audio", "price": 80},
    {"name": "Desk Lamp", "category": "Home", "price": 45},
    {"name": "Bluetooth Speaker", "category": "Audio", "price": 120},
    {"name": "Office Chair", "category": "Furniture", "price": 210},
    {"name": "Bookshelf", "category": "Furniture", "price": 150},
    {"name": "Candle Set", "category": "Home", "price": 25},
]

# Dictionary to accumulate totals per category
total_by_category = {}

# Loop through the products list
for product in products:
    category = product["category"]
    price = product["price"]

    # If category not yet stored, initialize it
    if category not in total_by_category:
        total_by_category[category] = price
    else:
        # Otherwise add the price to the existing total
        total_by_category[category] += price

print(total_by_category)
