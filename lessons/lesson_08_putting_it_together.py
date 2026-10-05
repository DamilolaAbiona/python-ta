# ============================================================
# LESSON 8: Putting It All Together - Mini Inventory App
# ============================================================
# Run this file:  python lessons/lesson_08_putting_it_together.py
# ============================================================

# This is a SIMPLIFIED version of the full inventory app.
# Everything here uses concepts from Lessons 1-7.
# Read through it. You should recognize every single line.

import json
import os

DATA_FILE = "lessons/mini_inventory.json"


# --- STEP 1: The Product class (Lesson 6) ---

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} | ${self.price:.2f} | Qty: {self.quantity}"

    def to_dict(self):
        return {"name": self.name, "price": self.price, "quantity": self.quantity}


# --- STEP 2: Save and Load (Lesson 7) ---

def save_products(products):
    data = [p.to_dict() for p in products]
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

def load_products():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        content = f.read().strip()
        if not content:
            return []
        data = json.loads(content)
    return [Product(d["name"], d["price"], d["quantity"]) for d in data]


# --- STEP 3: Actions (Lessons 3, 4, 5 combined) ---

def add_product(products):
    """Add a new product. Uses: input, validation, append, functions."""
    name = input("  Product name: ").strip()
    if not name:
        print("  Name cannot be empty!")
        return

    try:
        price = float(input("  Price: $"))
        quantity = int(input("  Quantity: "))
    except ValueError:
        print("  Invalid number!")
        return

    if price < 0 or quantity < 0:
        print("  Price and quantity must be positive!")
        return

    # Check for duplicates (Lesson 3: loop + if)
    for p in products:
        if p.name.lower() == name.lower():
            print(f"  '{name}' already exists!")
            return

    product = Product(name, price, quantity)
    products.append(product)
    save_products(products)
    print(f"  Added: {product}")


def view_products(products):
    """Show all products. Uses: loop, f-strings."""
    if not products:
        print("  No products yet. Add some first!")
        return

    print(f"  {'Name':<15} {'Price':>8} {'Qty':>6} {'Value':>10}")
    print(f"  {'-' * 42}")

    for p in products:
        value = p.price * p.quantity
        print(f"  {p.name:<15} ${p.price:>7.2f} {p.quantity:>6} ${value:>9.2f}")

    total = sum(p.price * p.quantity for p in products)
    print(f"  {'-' * 42}")
    print(f"  {'TOTAL':<15} {'':>8} {'':>6} ${total:>9.2f}")


def sell_product(products):
    """Sell a product. Uses: find, validate, update."""
    name = input("  Product name: ").strip()

    # Find the product (Lesson 3: loop with break)
    found = None
    for p in products:
        if p.name.lower() == name.lower():
            found = p
            break

    if found is None:
        print(f"  '{name}' not found!")
        return

    try:
        amount = int(input(f"  How many to sell (have {found.quantity}): "))
    except ValueError:
        print("  Invalid number!")
        return

    if amount <= 0:
        print("  Amount must be positive!")
        return

    if amount > found.quantity:
        print(f"  Not enough stock! Only have {found.quantity}.")
        return

    found.quantity -= amount
    save_products(products)
    print(f"  Sold {amount}x {found.name}. Remaining: {found.quantity}")


def remove_product(products):
    """Remove a product. Uses: list comprehension to filter."""
    name = input("  Product name to remove: ").strip()

    # Check it exists first
    exists = False
    for p in products:
        if p.name.lower() == name.lower():
            exists = True
            break

    if not exists:
        print(f"  '{name}' not found!")
        return

    confirm = input(f"  Sure you want to remove '{name}'? (y/n): ")
    if confirm.lower() != "y":
        print("  Cancelled.")
        return

    # Remove using list comprehension (Lesson 5)
    products[:] = [p for p in products if p.name.lower() != name.lower()]
    save_products(products)
    print(f"  Removed '{name}'.")


# --- STEP 4: The Main Loop (Lesson 3: while loop) ---

def main():
    products = load_products()
    print("\n  Welcome to Mini Inventory!")
    print(f"  Loaded {len(products)} product(s).\n")

    while True:
        print("  --- MENU ---")
        print("  1. View products")
        print("  2. Add product")
        print("  3. Sell product")
        print("  4. Remove product")
        print("  0. Exit")

        choice = input("\n  Choice: ").strip()

        if choice == "1":
            view_products(products)
        elif choice == "2":
            add_product(products)
        elif choice == "3":
            sell_product(products)
        elif choice == "4":
            remove_product(products)
        elif choice == "0":
            print("\n  Goodbye!\n")
            break
        else:
            print("  Invalid choice!")

        print()


# --- STEP 5: The entry point ---
# This line means: "Only run main() if THIS file is being run directly."
# If this file is imported by another file, main() does NOT run.

if __name__ == "__main__":
    main()
