# ============================================================
# LESSON 6: Classes (building your own data types)
# ============================================================
# Run this file:  python lessons/lesson_06_classes.py
# ============================================================

# In Lesson 5, we used dictionaries to represent products:
#   product = {"name": "Laptop", "price": 999.99, "qty": 50}
#
# This works, but has problems:
#   - Nothing stops you from writing product["naem"] (typo!)
#   - You can't attach BEHAVIOR (functions) to the data
#   - It's hard to validate data
#
# A CLASS solves this. A class is a BLUEPRINT for creating objects.
#
# Analogy:
#   A class is like a FORM (the blank template).
#   An object is like a FILLED-OUT FORM (with actual data).
#
#   The "Product Form" (class) says: every product has a name, price, qty.
#   A filled-out form (object) says: this product is "Laptop", $999.99, 50 units.


# --- DEFINING A CLASS ---

class Product:

    def __init__(self, name, price, quantity):
        """
        __init__ is the CONSTRUCTOR.
        It runs automatically when you create a new Product.
        'self' = "this specific product I'm creating right now"
        """
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        """A METHOD = a function that belongs to this object."""
        return self.price * self.quantity

    def is_low_stock(self):
        """Check if stock is low."""
        return self.quantity <= 10

    def sell(self, amount):
        """Sell some units."""
        if amount > self.quantity:
            print(f"  Error: Only {self.quantity} in stock!")
            return False
        self.quantity = self.quantity - amount
        print(f"  Sold {amount}x {self.name}. Remaining: {self.quantity}")
        return True

    def __str__(self):
        """Controls what print(product) shows."""
        return f"{self.name} - ${self.price:.2f} (qty: {self.quantity})"


# --- CREATING OBJECTS (instances) ---

print("--- Creating products ---")

laptop = Product("Laptop", 999.99, 50)
mouse = Product("Mouse", 29.99, 200)
cable = Product("USB Cable", 9.99, 3)

# Each object is independent. Changing one doesn't affect the others.

print(laptop)     # calls __str__ automatically
print(mouse)
print(cable)


# --- USING METHODS ---

print("")
print("--- Using methods ---")

print(f"Laptop total value: ${laptop.total_value():.2f}")
print(f"Is cable low stock? {cable.is_low_stock()}")
print(f"Is mouse low stock? {mouse.is_low_stock()}")

print("")
laptop.sell(5)
print(f"Laptop after sale: {laptop}")


# --- SELF EXPLAINED ---
# 'self' confuses everyone at first. Here's the trick:
#
# When you write:
#   laptop.sell(5)
#
# Python ACTUALLY does:
#   Product.sell(laptop, 5)
#
# 'self' is just the object BEFORE the dot.
# laptop.sell(5)  -->  self = laptop, amount = 5
# mouse.sell(3)   -->  self = mouse, amount = 3


# --- CLASS vs DICTIONARY ---

print("")
print("--- Why classes are better than dicts ---")

# With a dictionary:
product_dict = {"name": "Widget", "price": 5.0, "qty": 100}
# product_dict["naem"]  <-- typo! Python won't warn you until it crashes.
# You can't do product_dict.total_value()  <-- dicts don't have methods.

# With a class:
product_obj = Product("Widget", 5.0, 100)
# product_obj.naem  <-- Python tells you IMMEDIATELY this is wrong.
print(f"Total value: ${product_obj.total_value():.2f}")  # methods work!


# --- MANAGING A LIST OF OBJECTS ---
# The inventory app stores products in a list, just like lesson 5,
# but now each item is a Product OBJECT instead of a dictionary.

print("")
print("--- List of Product objects ---")

inventory = [
    Product("Laptop", 999.99, 50),
    Product("Mouse", 29.99, 200),
    Product("Keyboard", 79.99, 5),
    Product("Monitor", 349.99, 30),
]

# Print them all
for product in inventory:
    status = "LOW!" if product.is_low_stock() else "OK"
    print(f"  {product.name:<12} ${product.price:>8.2f}  Stock: {status}")

# Find the most expensive product
most_expensive = max(inventory, key=lambda p: p.price)
print(f"\nMost expensive: {most_expensive}")

# Total inventory value
total = sum(p.total_value() for p in inventory)
print(f"Total inventory value: ${total:.2f}")

# Filter low stock
low_stock = [p.name for p in inventory if p.is_low_stock()]
print(f"Low stock items: {low_stock}")
