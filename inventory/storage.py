"""
CONCEPT: File I/O (Input/Output) and JSON

Programs lose all data when they close. To PERSIST data (keep it),
we save to files. JSON is the most common format for structured data.

JSON looks like Python dictionaries:
    {"name": "Apple", "price": 1.50}

WHY THIS MATTERS IN INTERVIEWS:
- File handling with 'with' statements
- Error handling with try/except
- JSON serialization/deserialization
"""

import json
import os

from inventory.product import Product


def save_inventory(products, filepath="inventory_data.json"):
    """
    Save a list of Products to a JSON file.

    CONCEPT: The 'with' statement
    'with open(...)' automatically closes the file when done,
    even if an error occurs. This is called a CONTEXT MANAGER.

    INTERVIEW TIP: Always use 'with' for files. Never do:
        f = open("file.txt")  # BAD - you might forget to close it
        f.close()

    Instead:
        with open("file.txt") as f:  # GOOD - auto-closes
            ...
    """
    data = [product.to_dict() for product in products]

    with open(filepath, "w") as f:
        json.dump(data, f, indent=2)


def load_inventory(filepath="inventory_data.json"):
    """
    Load Products from a JSON file.

    CONCEPT: Error handling with try/except
    Things go wrong: the file might not exist, or contain bad data.
    try/except lets us handle these problems gracefully.

    INTERVIEW TIP: Be specific with exceptions.
        try:
            ...
        except Exception:    # BAD - too broad, hides real bugs
            ...

        try:
            ...
        except FileNotFoundError:  # GOOD - handles exactly what we expect
            ...
    """
    if not os.path.exists(filepath):
        return []

    try:
        with open(filepath, "r") as f:
            content = f.read().strip()
            if not content:
                return []
            data = json.loads(content)
        return [Product.from_dict(item) for item in data]
    except (json.JSONDecodeError, KeyError) as e:
        print(f"Warning: Could not load data - {e}")
        return []
