# ============================================================
# LESSON 4: Functions (reusable blocks of code)
# ============================================================
# Run this file:  python lessons/lesson_04_functions.py
# ============================================================

# A function is a RECIPE. You write it once, then use it
# whenever you need it. Instead of copying the same code
# over and over, you give it a name and call that name.
#
# Real life example:
#   "Make a sandwich" is a function.
#   You don't explain the steps every time. You just say
#   "make a sandwich" and the steps happen.


# --- DEFINING A FUNCTION ---

def greet():
    print("Hello there!")

# Nothing happened yet! Defining a function is like WRITING
# the recipe. You still have to USE it.

# --- CALLING A FUNCTION ---

greet()       # NOW it runs. This prints "Hello there!"
greet()       # You can call it as many times as you want.


# --- PARAMETERS (inputs to the function) ---
# Most functions need information to do their job.
# Parameters are the inputs.

print("")
print("--- Functions with parameters ---")

def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Damilola")     # name = "Damilola"
greet_person("Ada")          # name = "Ada"


# Multiple parameters:

def describe_product(name, price, quantity):
    print(f"{name}: ${price:.2f} (stock: {quantity})")

describe_product("Laptop", 999.99, 50)
describe_product("Mouse", 29.99, 200)


# --- RETURN VALUES (output from the function) ---
# A function can GIVE BACK a result using 'return'.
# Think of it as: you ask a question, the function answers.

print("")
print("--- Return values ---")

def calculate_total(price, quantity):
    total = price * quantity
    return total          # send the answer back

laptop_total = calculate_total(999.99, 3)
print(f"3 Laptops cost: ${laptop_total:.2f}")

# You can use the return value directly:
print(f"5 Mice cost: ${calculate_total(29.99, 5):.2f}")


# --- DEFAULT PARAMETERS ---
# You can give a parameter a default value.
# If the caller doesn't provide it, the default is used.

print("")
print("--- Default parameters ---")

def check_stock(name, quantity, threshold=10):
    if quantity <= threshold:
        print(f"  WARNING: {name} is low! Only {quantity} left.")
    else:
        print(f"  {name} stock is fine. {quantity} in stock.")

check_stock("Laptop", 5)          # threshold defaults to 10
check_stock("Mouse", 200)         # threshold defaults to 10
check_stock("Keyboard", 8, 5)     # threshold is 5 (we provided it)


# --- FUNCTIONS THAT VALIDATE (check for problems) ---
# In the real world, you check inputs before using them.
# If something is wrong, you RAISE an error.

print("")
print("--- Input validation ---")

def add_product(name, price, quantity):
    # Check for problems FIRST
    if not name:
        raise ValueError("Product name cannot be empty")
    if price < 0:
        raise ValueError("Price cannot be negative")
    if quantity < 0:
        raise ValueError("Quantity cannot be negative")

    # If we get here, everything is valid
    print(f"  Added: {name} (${price:.2f}, qty: {quantity})")
    return {"name": name, "price": price, "quantity": quantity}

# Good input - works fine:
add_product("Laptop", 999.99, 50)

# Bad input - let's catch the error:
try:
    add_product("", 10, 5)
except ValueError as e:
    print(f"  Error caught: {e}")

try:
    add_product("Laptop", -50, 5)
except ValueError as e:
    print(f"  Error caught: {e}")


# --- WHY FUNCTIONS MATTER ---
#
# 1. REUSABILITY: Write once, use everywhere.
# 2. READABILITY: A function name explains what code does.
#    compare:
#      bad:   x = p * q * (1 + r)
#      good:  x = calculate_total_with_tax(price, quantity, tax_rate)
# 3. TESTING: You can test each function on its own.
# 4. INTERVIEWS: You will be asked to WRITE functions that
#    solve problems. Every answer is a function.
