# ============================================================
# LESSON 5: Lists and Dictionaries (storing groups of data)
# ============================================================
# Run this file:  python lessons/lesson_05_lists_and_dicts.py
# ============================================================

# So far, one variable holds one thing.
# But what if you have 100 products?
# You need CONTAINERS that hold multiple things.


# ==========================
# LISTS - ordered collection
# ==========================
# A list is like a numbered shelf. Each item has a position (index).
# Positions start at 0, not 1!

print("--- LISTS ---")

fruits = ["Apple", "Banana", "Cherry", "Mango"]
#  index:    0        1         2        3

print(f"All fruits: {fruits}")
print(f"First fruit: {fruits[0]}")     # Apple    (index 0)
print(f"Second fruit: {fruits[1]}")    # Banana   (index 1)
print(f"Last fruit: {fruits[-1]}")     # Mango    (-1 means last)

# --- Adding to a list ---
print("")
print("--- Adding and removing ---")

fruits.append("Orange")        # add to the END
print(f"After append: {fruits}")

fruits.insert(1, "Grape")      # insert at position 1
print(f"After insert: {fruits}")

# --- Removing from a list ---

fruits.remove("Banana")        # remove by value
print(f"After remove Banana: {fruits}")

last = fruits.pop()            # remove and return the LAST item
print(f"Popped: {last}")
print(f"After pop: {fruits}")

# --- List basics ---
print("")
print("--- List basics ---")

numbers = [5, 2, 8, 1, 9, 3]

print(f"Length: {len(numbers)}")          # how many items
print(f"Is 8 in the list? {8 in numbers}")  # check membership
print(f"Sorted: {sorted(numbers)}")       # returns a sorted copy
print(f"Sum: {sum(numbers)}")             # add them all up
print(f"Max: {max(numbers)}")             # biggest
print(f"Min: {min(numbers)}")             # smallest

# --- Looping through a list ---
print("")
print("--- Looping through a list ---")

prices = [9.99, 24.99, 4.99, 49.99]
total = 0

for price in prices:
    total = total + price
    print(f"  ${price:.2f} (running total: ${total:.2f})")

print(f"Final total: ${total:.2f}")


# ================================
# DICTIONARIES - labeled data
# ================================
# A dictionary stores KEY:VALUE pairs.
# Think of it like a real dictionary:
#   word (key) -> definition (value)
#
# Or like a product card:
#   "name" -> "Laptop"
#   "price" -> 999.99

print("")
print("")
print("--- DICTIONARIES ---")

product = {
    "name": "Laptop",
    "price": 999.99,
    "quantity": 50,
    "category": "Electronics"
}

# Access values by their key:
print(f"Product: {product['name']}")
print(f"Price: ${product['price']}")

# Change a value:
product["quantity"] = 45
print(f"New quantity: {product['quantity']}")

# Add a new key:
product["brand"] = "TechCo"
print(f"Brand: {product['brand']}")

# Safely get a value (returns a default if key doesn't exist):
color = product.get("color", "Unknown")
print(f"Color: {color}")   # "Unknown" because "color" key doesn't exist


# --- Looping through a dictionary ---
print("")
print("--- Looping through a dictionary ---")

for key, value in product.items():
    print(f"  {key}: {value}")


# ==========================================
# LIST OF DICTIONARIES (this is the big one)
# ==========================================
# In real apps, you almost always have a LIST of things,
# where each thing is a DICTIONARY of properties.
# This is how our inventory app stores products!

print("")
print("")
print("--- LIST OF DICTIONARIES (how real apps work) ---")

inventory = [
    {"name": "Laptop",   "price": 999.99, "qty": 50},
    {"name": "Mouse",    "price": 29.99,  "qty": 200},
    {"name": "Keyboard", "price": 79.99,  "qty": 5},
    {"name": "Monitor",  "price": 349.99, "qty": 30},
    {"name": "Cable",    "price": 9.99,   "qty": 500},
]

# Print all products
for product in inventory:
    print(f"  {product['name']}: ${product['price']:.2f} (stock: {product['qty']})")

# Find a specific product
print("")
print("--- Finding a product ---")

search_name = "Mouse"
found = None

for product in inventory:
    if product["name"] == search_name:
        found = product
        break    # stop looking, we found it

if found:
    print(f"Found: {found['name']} at ${found['price']:.2f}")
else:
    print(f"{search_name} not found!")

# Calculate total inventory value
print("")
print("--- Total inventory value ---")

total_value = 0
for product in inventory:
    value = product["price"] * product["qty"]
    total_value = total_value + value
    print(f"  {product['name']}: ${value:.2f}")

print(f"  TOTAL: ${total_value:.2f}")


# --- LIST COMPREHENSION (shortcut) ---
# This is a compact way to build a new list from an existing one.
# Interviewers LOVE this. Learn this pattern.

print("")
print("--- List comprehension ---")

# The long way:
expensive = []
for p in inventory:
    if p["price"] > 50:
        expensive.append(p["name"])

# The short way (same result):
expensive = [p["name"] for p in inventory if p["price"] > 50]

print(f"Expensive items (>$50): {expensive}")

# Pattern:
# [WHAT_YOU_WANT  for ITEM in LIST  if CONDITION]
#
# Read it like English:
# "Give me the NAME, for each PRODUCT in INVENTORY, if PRICE > 50"

all_prices = [p["price"] for p in inventory]
print(f"All prices: {all_prices}")

low_stock = [p["name"] for p in inventory if p["qty"] <= 10]
print(f"Low stock: {low_stock}")
