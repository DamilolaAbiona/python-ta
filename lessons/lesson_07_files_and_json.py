# ============================================================
# LESSON 7: Files and JSON (saving data permanently)
# ============================================================
# Run this file:  python lessons/lesson_07_files_and_json.py
# ============================================================

# When your program closes, ALL variables disappear.
# To keep data, you need to save it to a FILE.
#
# JSON is the most popular format for saving structured data.
# It looks almost exactly like Python dictionaries and lists.

import json
import os


# --- WRITING TO A FILE ---

print("--- Writing to a file ---")

# 'with' opens the file and automatically closes it when done.
# "w" means WRITE mode (creates the file or overwrites it).

with open("lessons/my_file.txt", "w") as f:
    f.write("Hello from Python!\n")
    f.write("This is line 2.\n")
    f.write("This is line 3.\n")

print("File written!")


# --- READING FROM A FILE ---

print("")
print("--- Reading from a file ---")

# "r" means READ mode.

with open("lessons/my_file.txt", "r") as f:
    content = f.read()

print("File contents:")
print(content)


# --- READING LINE BY LINE ---

print("--- Reading line by line ---")

with open("lessons/my_file.txt", "r") as f:
    for line_number, line in enumerate(f, 1):
        print(f"  Line {line_number}: {line.strip()}")


# --- JSON: SAVING PYTHON DATA ---
# JSON can save: strings, numbers, booleans, lists, and dicts.
# That covers everything we need for our inventory!

print("")
print("--- JSON: Saving data ---")

products = [
    {"name": "Laptop", "price": 999.99, "quantity": 50},
    {"name": "Mouse", "price": 29.99, "quantity": 200},
    {"name": "Keyboard", "price": 79.99, "quantity": 5},
]

# json.dump() saves Python data to a file as JSON
with open("lessons/products.json", "w") as f:
    json.dump(products, f, indent=2)
    # indent=2 makes it pretty (2 spaces per level)

print("Saved 3 products to products.json!")


# --- JSON: LOADING DATA BACK ---

print("")
print("--- JSON: Loading data ---")

# json.load() reads JSON from a file back into Python
with open("lessons/products.json", "r") as f:
    loaded_products = json.load(f)

print("Loaded products:")
for p in loaded_products:
    print(f"  {p['name']}: ${p['price']:.2f} (qty: {p['quantity']})")


# --- HANDLING MISSING FILES ---
# What if the file doesn't exist? Your program crashes!
# Use try/except or os.path.exists() to handle this.

print("")
print("--- Handling missing files ---")

# Method 1: Check first
if os.path.exists("lessons/products.json"):
    print("File exists!")
else:
    print("File not found!")

# Method 2: Try and catch the error
try:
    with open("lessons/nonexistent.json", "r") as f:
        data = json.load(f)
except FileNotFoundError:
    print("File not found! Starting with empty data.")
    data = []

print(f"Data has {len(data)} items")


# --- THE FULL PATTERN (used in our inventory app) ---

print("")
print("--- The full save/load pattern ---")

FILEPATH = "lessons/inventory_demo.json"

def save(products):
    with open(FILEPATH, "w") as f:
        json.dump(products, f, indent=2)
    print(f"  Saved {len(products)} products.")

def load():
    if not os.path.exists(FILEPATH):
        return []
    with open(FILEPATH, "r") as f:
        return json.load(f)

# Start fresh
save([])

# Add a product
data = load()
data.append({"name": "Laptop", "price": 999.99, "quantity": 50})
save(data)

# Add another
data = load()
data.append({"name": "Mouse", "price": 29.99, "quantity": 200})
save(data)

# Load and display
data = load()
print(f"  {len(data)} products in file:")
for p in data:
    print(f"    {p['name']}: ${p['price']:.2f}")


# Clean up demo files
os.remove("lessons/my_file.txt")
os.remove("lessons/products.json")
os.remove(FILEPATH)
print("\nCleaned up demo files.")
