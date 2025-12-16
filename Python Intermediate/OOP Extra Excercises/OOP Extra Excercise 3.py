#Product Class
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total_value(self):
        return self.price * self.quantity

#Inventory Class
class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def show_products(self):
        for product in self.products:
            print(
                f"Name: {product.name}, "
                f"Price: {product.price}, "
                f"Quantity: {product.quantity}"
            )

    def calculate_total_value_of_inventory(self):
        total = 0
        for product in self.products:
            total += product.get_total_value()
        return total

#Using the Classes 
product1 = Product("Mouse", 5000, 3)
product2 = Product("Teclado", 8000, 2)

inventory = Inventory()
inventory.add_product(product1)
inventory.add_product(product2)

print(inventory.calculate_total_value_of_inventory())  # 34000 
#