# ============================================================
# LESSON 3: Loops (doing things over and over)
# ============================================================
# Run this file:  python lessons/lesson_03_loops.py
# ============================================================

# A loop repeats code. Instead of writing the same thing 100 times,
# you write it once and tell Python to repeat it.


# --- FOR LOOP ---
# "For each item in this group, do something."

print("--- For loop: counting ---")

for number in range(5):    # range(5) gives you 0, 1, 2, 3, 4
    print(f"  Number: {number}")

# range(5) means "give me 5 numbers starting from 0"
# range(1, 6) means "give me numbers from 1 to 5"
# range(0, 10, 2) means "from 0 to 9, counting by 2" = 0, 2, 4, 6, 8


print("")
print("--- For loop: going through a list ---")

fruits = ["Apple", "Banana", "Cherry", "Mango"]

for fruit in fruits:
    print(f"  I like {fruit}")

# Think of it as:
#   Take the first fruit (Apple), print it.
#   Take the next fruit (Banana), print it.
#   Keep going until you run out of fruits.


# --- WHILE LOOP ---
# "Keep going WHILE this condition is true."

print("")
print("--- While loop: countdown ---")

countdown = 5
while countdown > 0:
    print(f"  {countdown}...")
    countdown = countdown - 1    # subtract 1 each time

print("  Liftoff!")

# WARNING: If the condition NEVER becomes False, the loop runs forever!
# That's called an "infinite loop" and it freezes your program.
# Always make sure something changes to eventually stop the loop.


# --- BREAK and CONTINUE ---

print("")
print("--- Break: stop the loop early ---")

for number in range(1, 100):
    if number > 5:
        print("  Stopping early!")
        break                    # EXIT the loop immediately
    print(f"  {number}")

print("")
print("--- Continue: skip this one, keep going ---")

for number in range(1, 8):
    if number == 4:
        continue                 # SKIP number 4, go to next
    print(f"  {number}")


# --- INVENTORY EXAMPLE ---
# This is exactly how our inventory app displays all products!

print("")
print("--- Inventory: showing all products ---")

products = [
    {"name": "Laptop", "price": 999.99, "qty": 50},
    {"name": "Mouse", "price": 29.99, "qty": 200},
    {"name": "Keyboard", "price": 79.99, "qty": 5},
    {"name": "Monitor", "price": 349.99, "qty": 0},
]

print(f"  {'Name':<12} {'Price':>8} {'Stock':>8} {'Status'}")
print(f"  {'-' * 45}")

for product in products:
    # Figure out the status
    if product["qty"] == 0:
        status = "OUT OF STOCK"
    elif product["qty"] <= 10:
        status = "LOW STOCK"
    else:
        status = "In Stock"

    print(f"  {product['name']:<12} ${product['price']:>7.2f} {product['qty']:>8} {status}")


# --- BUILDING A LIST WITH A LOOP ---
# A very common pattern: start empty, add items one by one.

print("")
print("--- Building a list ---")

expensive_items = []

for product in products:
    if product["price"] > 100:
        expensive_items.append(product["name"])

print(f"  Expensive items: {expensive_items}")
