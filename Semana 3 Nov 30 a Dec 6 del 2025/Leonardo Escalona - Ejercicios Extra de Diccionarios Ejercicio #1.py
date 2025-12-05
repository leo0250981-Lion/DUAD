transactions = [
    {
        'date': '01/03/25',
        'customer_email': 'maria@gmail.com',
        'items': [
            {'name': 'Wireless Mouse', 'upc': 'UPC-901', 'unit_price': 18.99},
            {'name': 'Laptop Stand', 'upc': 'UPC-778', 'unit_price': 34.50},
            {'name': 'Notebook', 'upc': 'UPC-555', 'unit_price': 3.25},
        ],
    },
    {
        'date': '02/03/25',
        'customer_email': 'robert@gmail.com',
        'items': [
            {'name': 'Wireless Mouse', 'upc': 'UPC-901', 'unit_price': 18.99},
            {'name': 'Headphones', 'upc': 'UPC-112', 'unit_price': 49.99},
        ],
    },
    {
        'date': '03/03/25',
        'customer_email': 'sarah@gmail.com',
        'items': [
            {'name': 'Notebook', 'upc': 'UPC-555', 'unit_price': 3.25},
            {'name': 'Laptop Stand', 'upc': 'UPC-778', 'unit_price': 34.50},
        ],
    },
]

# Dictionary to store total sales per UPC
upc_totals = {}

# Process each transaction
for transaction in transactions:
    for product in transaction["items"]:
        upc = product["upc"]
        cost = product["unit_price"]

        # Initialize UPC total if not present
        if upc not in upc_totals:
            upc_totals[upc] = cost
        else:
            upc_totals[upc] += cost

print(upc_totals)
