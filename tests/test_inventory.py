"""
CONCEPT: Unit Testing

Tests prove your code works correctly. In interviews, you're often
asked to write tests or explain testing.

KEY IDEAS:
- Each test checks ONE specific thing
- Tests should be INDEPENDENT (one test shouldn't affect another)
- Use setUp() to create fresh data for each test
- Test both the HAPPY PATH (normal use) and EDGE CASES (errors)

HOW TO RUN:
    python -m pytest tests/test_inventory.py -v
    OR
    python -m unittest tests.test_inventory -v
"""

import unittest
import os
import tempfile

from inventory.product import Product
from inventory.manager import InventoryManager


class TestProduct(unittest.TestCase):
    """Tests for the Product class."""

    def test_create_product(self):
        """Test that we can create a product with correct attributes."""
        p = Product("Laptop", 999.99, 50, "Electronics")
        self.assertEqual(p.name, "Laptop")
        self.assertEqual(p.price, 999.99)
        self.assertEqual(p.quantity, 50)
        self.assertEqual(p.category, "Electronics")

    def test_default_category(self):
        """Test that category defaults to 'General'."""
        p = Product("Widget", 5.00, 100)
        self.assertEqual(p.category, "General")

    def test_total_value(self):
        """Test total value calculation."""
        p = Product("Book", 10.00, 5)
        self.assertEqual(p.total_value(), 50.00)

    def test_is_low_stock(self):
        """Test low stock detection."""
        p = Product("Rare Item", 100.00, 3)
        self.assertTrue(p.is_low_stock())
        self.assertTrue(p.is_low_stock(5))
        self.assertFalse(p.is_low_stock(2))

    def test_to_dict_and_back(self):
        """
        Test round-trip: Product -> dict -> Product

        INTERVIEW TIP: Testing serialization round-trips is common.
        """
        original = Product("Phone", 699.99, 30, "Electronics")
        data = original.to_dict()
        restored = Product.from_dict(data)

        self.assertEqual(original.name, restored.name)
        self.assertEqual(original.price, restored.price)
        self.assertEqual(original.quantity, restored.quantity)
        self.assertEqual(original.category, restored.category)

    def test_str_representation(self):
        """Test that str(product) gives readable output."""
        p = Product("Apple", 1.50, 100, "Fruit")
        result = str(p)
        self.assertIn("Apple", result)
        self.assertIn("1.50", result)


class TestInventoryManager(unittest.TestCase):
    """Tests for the InventoryManager class."""

    def setUp(self):
        """
        setUp runs BEFORE each test method.

        We use a temporary file so tests don't affect real data.

        CONCEPT: tempfile module
        Creates temporary files that are automatically cleaned up.
        """
        self.temp_file = tempfile.NamedTemporaryFile(
            suffix=".json", delete=False
        )
        self.temp_file.close()
        self.manager = InventoryManager(filepath=self.temp_file.name)

    def tearDown(self):
        """tearDown runs AFTER each test. Clean up temp files."""
        if os.path.exists(self.temp_file.name):
            os.unlink(self.temp_file.name)

    def test_add_product(self):
        """Test adding a product."""
        p = self.manager.add_product("Laptop", 999.99, 50, "Electronics")
        self.assertEqual(p.name, "Laptop")
        self.assertEqual(len(self.manager.products), 1)

    def test_add_duplicate_raises_error(self):
        """
        Test that adding a duplicate product raises ValueError.

        CONCEPT: assertRaises
        This checks that a specific error IS raised.
        """
        self.manager.add_product("Laptop", 999.99, 50)
        with self.assertRaises(ValueError):
            self.manager.add_product("Laptop", 499.99, 10)

    def test_add_negative_price_raises_error(self):
        """Test that negative price is rejected."""
        with self.assertRaises(ValueError):
            self.manager.add_product("Bad", -5.00, 10)

    def test_find_product(self):
        """Test finding a product by name (case-insensitive)."""
        self.manager.add_product("Laptop", 999.99, 50)
        found = self.manager.find_product("laptop")
        self.assertIsNotNone(found)
        self.assertEqual(found.name, "Laptop")

    def test_find_nonexistent_product(self):
        """Test that finding a missing product returns None."""
        found = self.manager.find_product("Ghost")
        self.assertIsNone(found)

    def test_search_products(self):
        """Test keyword search."""
        self.manager.add_product("Red Apple", 1.50, 100, "Fruit")
        self.manager.add_product("Green Apple", 1.75, 80, "Fruit")
        self.manager.add_product("Laptop", 999.99, 50, "Electronics")

        results = self.manager.search_products("apple")
        self.assertEqual(len(results), 2)

        results = self.manager.search_products("electronics")
        self.assertEqual(len(results), 1)

    def test_update_quantity(self):
        """Test updating product quantity."""
        self.manager.add_product("Laptop", 999.99, 50)
        updated = self.manager.update_quantity("Laptop", 75)
        self.assertEqual(updated.quantity, 75)

    def test_sell_product(self):
        """Test selling reduces stock."""
        self.manager.add_product("Book", 15.00, 20)
        self.manager.sell("Book", 5)
        product = self.manager.find_product("Book")
        self.assertEqual(product.quantity, 15)

    def test_sell_more_than_stock_raises_error(self):
        """Test that selling more than available stock fails."""
        self.manager.add_product("Book", 15.00, 5)
        with self.assertRaises(ValueError):
            self.manager.sell("Book", 10)

    def test_remove_product(self):
        """Test removing a product."""
        self.manager.add_product("Laptop", 999.99, 50)
        self.manager.remove_product("Laptop")
        self.assertEqual(len(self.manager.products), 0)

    def test_total_inventory_value(self):
        """Test total inventory value calculation."""
        self.manager.add_product("A", 10.00, 5)
        self.manager.add_product("B", 20.00, 3)
        self.assertEqual(self.manager.total_inventory_value(), 110.00)

    def test_sort_by_price(self):
        """Test sorting products by price."""
        self.manager.add_product("Cheap", 5.00, 10)
        self.manager.add_product("Mid", 15.00, 10)
        self.manager.add_product("Expensive", 50.00, 10)

        asc = self.manager.sort_by_price()
        self.assertEqual(asc[0].name, "Cheap")
        self.assertEqual(asc[-1].name, "Expensive")

        desc = self.manager.sort_by_price(descending=True)
        self.assertEqual(desc[0].name, "Expensive")

    def test_persistence(self):
        """
        Test that data survives closing and reopening.

        This is a critical test - we save data, create a NEW manager
        pointing to the same file, and check the data is still there.
        """
        self.manager.add_product("Laptop", 999.99, 50, "Electronics")

        new_manager = InventoryManager(filepath=self.temp_file.name)
        self.assertEqual(len(new_manager.products), 1)
        self.assertEqual(new_manager.products[0].name, "Laptop")

    def test_get_categories(self):
        """Test getting unique categories."""
        self.manager.add_product("Apple", 1.50, 100, "Fruit")
        self.manager.add_product("Banana", 0.75, 200, "Fruit")
        self.manager.add_product("Laptop", 999.99, 50, "Electronics")

        categories = self.manager.get_categories()
        self.assertEqual(categories, ["Electronics", "Fruit"])


if __name__ == "__main__":
    unittest.main()
