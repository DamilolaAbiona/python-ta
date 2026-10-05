"""
CONCEPT: Classes and Object-Oriented Programming (OOP)

A class is a blueprint for creating objects. Think of it like a form:
- The form (class) defines what fields exist (name, price, quantity)
- Each filled-out form (object/instance) has its own values

WHY THIS MATTERS IN INTERVIEWS:
- OOP is asked about in almost every Python interview
- You need to know: __init__, __str__, __repr__, instance vs class variables
"""


class Product:
    """Represents a single product in our inventory."""

    def __init__(self, name, price, quantity, category="General"):
        """
        __init__ is the CONSTRUCTOR - it runs when you create a new Product.

        'self' refers to the specific object being created.
        Think of 'self' as "this particular product".

        Example:
            apple = Product("Apple", 1.50, 100, "Fruit")
            # self.name becomes "Apple" for THIS apple object
        """
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category

    def __str__(self):
        """
        __str__ controls what happens when you do print(product).
        Without it, you'd see something ugly like <Product object at 0x7f...>

        INTERVIEW TIP: __str__ is for users, __repr__ is for developers.
        """
        return f"{self.name} | ${self.price:.2f} | Qty: {self.quantity} | {self.category}"

    def __repr__(self):
        """
        __repr__ is the 'developer' view. It should look like valid Python
        that could recreate the object.

        INTERVIEW TIP: If you only define one, define __repr__.
        """
        return f'Product("{self.name}", {self.price}, {self.quantity}, "{self.category}")'

    def total_value(self):
        """Calculate the total value of this product in stock."""
        return self.price * self.quantity

    def is_low_stock(self, threshold=10):
        """
        Check if we're running low on this product.

        'threshold=10' is a DEFAULT PARAMETER - if you don't pass
        a value, it uses 10.

        Example:
            product.is_low_stock()      # uses threshold=10
            product.is_low_stock(5)     # uses threshold=5
        """
        return self.quantity <= threshold

    def to_dict(self):
        """
        Convert this Product to a dictionary.

        WHY: JSON (how we save data) works with dicts, not custom objects.
        This is a very common pattern in real apps and interviews.
        """
        return {
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity,
            "category": self.category,
        }

    @classmethod
    def from_dict(cls, data):
        """
        CONCEPT: @classmethod - A method that belongs to the CLASS, not an instance.

        'cls' is the class itself (Product), not a specific product.
        This is a FACTORY METHOD - it creates a Product from a dictionary.

        INTERVIEW TIP: Know the difference between:
        - instance method: operates on self (a specific object)
        - class method: operates on cls (the class itself)
        - static method: doesn't need self or cls at all

        Example:
            data = {"name": "Apple", "price": 1.50, "quantity": 100, "category": "Fruit"}
            apple = Product.from_dict(data)  # creates a Product from a dict
        """
        return cls(
            name=data["name"],
            price=data["price"],
            quantity=data["quantity"],
            category=data.get("category", "General"),
        )
