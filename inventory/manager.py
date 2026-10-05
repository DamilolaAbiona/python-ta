"""
CONCEPT: Data Structures and Algorithms

This file is the BRAIN of the app. It manages all the products.

KEY DATA STRUCTURES used here:
- List: ordered collection [item1, item2, item3]
- Dictionary: key-value pairs {"name": "Apple", "price": 1.50}

WHY THIS MATTERS IN INTERVIEWS:
- Searching, filtering, sorting are VERY common interview questions
- List comprehensions are expected Python knowledge
- Understanding when to use which data structure
"""

from inventory.product import Product
from inventory.storage import save_inventory, load_inventory


class InventoryManager:
    """Manages the complete inventory of products."""

    def __init__(self, filepath="inventory_data.json"):
        """Load existing inventory from file on startup."""
        self.filepath = filepath
        self.products = load_inventory(filepath)

    def save(self):
        """Save current inventory to file."""
        save_inventory(self.products, self.filepath)

    # ---- CREATE ----

    def add_product(self, name, price, quantity, category="General"):
        """
        Add a new product to the inventory.

        CONCEPT: Input validation
        Before saving data, CHECK that it makes sense.
        This prevents bugs and is expected in interviews.
        """
        if price < 0:
            raise ValueError("Price cannot be negative")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        if not name.strip():
            raise ValueError("Name cannot be empty")

        for product in self.products:
            if product.name.lower() == name.lower():
                raise ValueError(f"Product '{name}' already exists")

        product = Product(name.strip(), price, quantity, category)
        self.products.append(product)
        self.save()
        return product

    # ---- READ ----

    def find_product(self, name):
        """
        Find a product by name.

        CONCEPT: Linear Search
        We check each product one by one. This is O(n) time complexity.

        INTERVIEW TIP: Know Big O notation:
        - O(1)    = constant time (instant, like dict lookup)
        - O(n)    = linear time (check every item, like this search)
        - O(n^2)  = quadratic (nested loops, slow for big data)
        - O(log n) = logarithmic (binary search, very fast)
        """
        for product in self.products:
            if product.name.lower() == name.lower():
                return product
        return None

    def list_products(self):
        """Return all products."""
        return self.products

    def search_products(self, keyword):
        """
        Search products by keyword in name or category.

        CONCEPT: List Comprehension
        This is a compact way to filter a list. It's the SAME as:

            results = []
            for p in self.products:
                if keyword.lower() in p.name.lower() or keyword.lower() in p.category.lower():
                    results.append(p)
            return results

        But the list comprehension below does it in ONE line.

        INTERVIEW TIP: List comprehensions are a MUST-KNOW for Python interviews.
        Pattern: [expression FOR item IN iterable IF condition]
        """
        keyword = keyword.lower()
        return [
            p for p in self.products
            if keyword in p.name.lower() or keyword in p.category.lower()
        ]

    def get_products_by_category(self, category):
        """Filter products by category using list comprehension."""
        return [
            p for p in self.products
            if p.category.lower() == category.lower()
        ]

    # ---- UPDATE ----

    def update_quantity(self, name, new_quantity):
        """
        Update the quantity of a product.

        CONCEPT: Raising Exceptions
        When something goes wrong, we RAISE an error instead of
        silently failing. The caller can then handle it.
        """
        if new_quantity < 0:
            raise ValueError("Quantity cannot be negative")

        product = self.find_product(name)
        if product is None:
            raise KeyError(f"Product '{name}' not found")

        product.quantity = new_quantity
        self.save()
        return product

    def update_price(self, name, new_price):
        """Update the price of a product."""
        if new_price < 0:
            raise ValueError("Price cannot be negative")

        product = self.find_product(name)
        if product is None:
            raise KeyError(f"Product '{name}' not found")

        product.price = new_price
        self.save()
        return product

    def restock(self, name, amount):
        """Add more stock for a product."""
        if amount <= 0:
            raise ValueError("Restock amount must be positive")

        product = self.find_product(name)
        if product is None:
            raise KeyError(f"Product '{name}' not found")

        product.quantity += amount
        self.save()
        return product

    def sell(self, name, amount):
        """
        Record a sale (reduce stock).

        This checks that we have enough stock before selling.
        """
        if amount <= 0:
            raise ValueError("Sale amount must be positive")

        product = self.find_product(name)
        if product is None:
            raise KeyError(f"Product '{name}' not found")
        if product.quantity < amount:
            raise ValueError(
                f"Not enough stock. Have {product.quantity}, tried to sell {amount}"
            )

        product.quantity -= amount
        self.save()
        return product

    # ---- DELETE ----

    def remove_product(self, name):
        """
        Remove a product from inventory.

        CONCEPT: List filtering
        We rebuild the list WITHOUT the product we want to remove.
        """
        product = self.find_product(name)
        if product is None:
            raise KeyError(f"Product '{name}' not found")

        self.products = [
            p for p in self.products
            if p.name.lower() != name.lower()
        ]
        self.save()
        return product

    # ---- REPORTS (common interview-style questions) ----

    def total_inventory_value(self):
        """
        Calculate total value of all inventory.

        CONCEPT: sum() with a generator expression
        This is like a list comprehension but doesn't build the whole list
        in memory. Uses () instead of [].

        INTERVIEW TIP: Generators are memory-efficient for large data.
        """
        return sum(p.total_value() for p in self.products)

    def low_stock_products(self, threshold=10):
        """Find all products with low stock."""
        return [p for p in self.products if p.is_low_stock(threshold)]

    def most_valuable_product(self):
        """
        Find the product with the highest total value in stock.

        CONCEPT: max() with key function
        max() can take a 'key' argument - a function that tells it
        HOW to compare items.

        INTERVIEW TIP: The key parameter works with max(), min(), sorted().
        It's a very clean pattern.
        """
        if not self.products:
            return None
        return max(self.products, key=lambda p: p.total_value())

    def sort_by_price(self, descending=False):
        """
        Return products sorted by price.

        CONCEPT: sorted() with lambda
        'lambda' is a tiny anonymous function written in one line.
            lambda p: p.price
        is the same as:
            def get_price(p):
                return p.price

        INTERVIEW TIP: Know how to use sorted() with custom keys.
        """
        return sorted(self.products, key=lambda p: p.price, reverse=descending)

    def get_categories(self):
        """
        Get all unique categories.

        CONCEPT: Sets
        A set is like a list but with NO DUPLICATES and NO ORDER.
        Converting a list to a set removes duplicates automatically.

        INTERVIEW TIP: Sets have O(1) lookup, lists have O(n).
        Use a set when you need to check "is X in this collection?"
        """
        return sorted(set(p.category for p in self.products))

    def inventory_summary(self):
        """
        Generate a summary report.

        CONCEPT: Dictionary comprehension
        Same idea as list comprehension, but builds a dict.
        Pattern: {key: value FOR item IN iterable}
        """
        categories = self.get_categories()
        return {
            "total_products": len(self.products),
            "total_value": self.total_inventory_value(),
            "categories": categories,
            "low_stock_count": len(self.low_stock_products()),
            "value_by_category": {
                cat: sum(
                    p.total_value()
                    for p in self.get_products_by_category(cat)
                )
                for cat in categories
            },
        }
