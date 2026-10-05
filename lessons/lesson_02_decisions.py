# ============================================================
# LESSON 2: Making Decisions (if / elif / else)
# ============================================================
# Run this file:  python lessons/lesson_02_decisions.py
# ============================================================

# A program that can't make decisions is useless.
# if/elif/else lets your program CHOOSE what to do.
#
# Real life:
#   IF it's raining, take an umbrella.
#   ELSE, wear sunglasses.
#
# Python:
#   if condition:
#       do this
#   else:
#       do that

temperature = 35

print("--- Simple if/else ---")

if temperature > 30:
    print("It's hot outside!")
else:
    print("It's not too bad.")


# --- ELIF (else if) ---
# When you have MORE than two options.

print("")
print("--- Multiple choices with elif ---")

score = 75

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# Python checks from TOP to BOTTOM.
# The FIRST condition that is True wins. The rest are skipped.


# --- COMPARISON OPERATORS ---
# These are how you compare things:
#
#   ==   equals              (5 == 5 is True)
#   !=   not equals          (5 != 3 is True)
#   >    greater than        (5 > 3 is True)
#   <    less than           (3 < 5 is True)
#   >=   greater or equal    (5 >= 5 is True)
#   <=   less or equal       (3 <= 5 is True)
#
# IMPORTANT: = is ASSIGNMENT (put value in box)
#            == is COMPARISON (are these equal?)

print("")
print("--- Comparisons ---")

a = 10
b = 20

print(f"{a} == {b}?", a == b)    # False
print(f"{a} != {b}?", a != b)    # True
print(f"{a} > {b}?", a > b)      # False
print(f"{a} < {b}?", a < b)      # True


# --- AND, OR, NOT ---
# Combine conditions together.

print("")
print("--- Combining conditions ---")

age = 25
has_id = True

if age >= 18 and has_id:
    print("You can enter the venue.")

if age < 13 or age > 65:
    print("You get a discount.")
else:
    print("No discount for you.")

if not has_id:
    print("Please bring your ID.")
else:
    print("ID verified.")


# --- INVENTORY EXAMPLE ---
# This is how decisions work in our inventory app!

print("")
print("--- Inventory decision example ---")

product_name = "Laptop"
quantity = 3
price = 999.99

if quantity == 0:
    print(f"{product_name} is OUT OF STOCK!")
elif quantity <= 5:
    print(f"{product_name} is LOW STOCK! Only {quantity} left.")
elif quantity <= 20:
    print(f"{product_name} stock is OK. {quantity} in stock.")
else:
    print(f"{product_name} is well stocked. {quantity} available.")

if price > 500:
    print(f"  This is a high-value item (${price:.2f})")
