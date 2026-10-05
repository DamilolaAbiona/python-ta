# ============================================================
# LESSON 1: The Absolute Basics
# ============================================================
# Run this file:  python lessons/lesson_01_basics.py
# ============================================================

# WHAT IS PROGRAMMING?
# Programming is giving instructions to a computer.
# The computer reads your instructions top to bottom,
# one line at a time, and does exactly what you say.


# --- PRINTING ---
# print() shows text on your screen. That's it.
# It's how your program talks to you.

print("Hello! Welcome to Python.")
print("I am a computer program.")
print("I do what you tell me, line by line.")


# --- VARIABLES ---
# A variable is a NAME for a piece of information.
# Think of it like a labeled box:
#   You put something IN the box.
#   The label (variable name) lets you find it later.

name = "Damilola"           # a box labeled "name" with "Damilola" inside
age = 25                     # a box labeled "age" with 25 inside
height = 5.8                 # a box labeled "height" with 5.8 inside
is_student = True            # a box labeled "is_student" with True inside

print("")
print("My name is", name)
print("I am", age, "years old")
print("My height is", height, "feet")
print("Am I a student?", is_student)


# --- DATA TYPES ---
# There are 4 basic types of data:
#
# 1. str   (string)  = text,   always in quotes    "hello"
# 2. int   (integer) = whole numbers               42
# 3. float           = decimal numbers             3.14
# 4. bool  (boolean) = True or False               True

city = "Lagos"        # str   - text
population = 15000000 # int   - whole number
temperature = 32.5    # float - decimal number
is_hot = True         # bool  - yes or no

print("")
print(city, "has a population of", population)
print("Temperature:", temperature, "degrees")
print("Is it hot?", is_hot)


# --- MATH ---
# Python can do math. Just type it.

apples = 10
oranges = 5

total = apples + oranges        # addition
difference = apples - oranges   # subtraction
doubled = apples * 2            # multiplication
half = apples / 2               # division
leftover = apples % 3           # remainder (modulo) - "what's left over"

print("")
print("Apples:", apples)
print("Oranges:", oranges)
print("Total fruit:", total)
print("Difference:", difference)
print("Double the apples:", doubled)
print("Half the apples:", half)
print("10 divided by 3, remainder:", leftover)


# --- F-STRINGS (formatted strings) ---
# The easiest way to mix text and variables.
# Put an f before the quotes, then use {curly braces} for variables.

item = "Laptop"
price = 999.99

print("")
print(f"The {item} costs ${price}")
print(f"Two of them cost ${price * 2}")
print(f"Price with 2 decimal places: ${price:.2f}")

# ============================================================
# TRY IT: Change the variables above and run this file again.
# There is no wrong answer. Experiment!
# ============================================================
