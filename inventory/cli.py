"""
CONCEPT: Building a User Interface (CLI = Command Line Interface)

This is where users interact with the app through the terminal.

KEY CONCEPTS:
- While loops for menus
- Input validation
- String formatting with f-strings
- try/except for user errors
"""

from inventory.manager import InventoryManager


def print_header(title):
    """Print a formatted header."""
    print(f"\n{'=' * 50}")
    print(f"  {title}")
    print(f"{'=' * 50}")


def print_product_table(products):
    """
    Display products in a formatted table.

    CONCEPT: String formatting
    f-strings let you embed variables in strings:
        name = "Apple"
        f"Product: {name}"  -->  "Product: Apple"

    You can also format numbers:
        f"${price:.2f}"  -->  "$1.50"  (2 decimal places)
        f"{name:<20}"    -->  "Apple               "  (left-align, 20 chars wide)
    """
    if not products:
        print("  No products found.")
        return

    print(f"  {'Name':<20} {'Price':>10} {'Qty':>8} {'Value':>12} {'Category':<15}")
    print(f"  {'-' * 65}")

    for p in products:
        print(
            f"  {p.name:<20} ${p.price:>9.2f} {p.quantity:>8} "
            f"${p.total_value():>11.2f} {p.category:<15}"
        )


def get_float_input(prompt):
    """
    Safely get a number from the user.

    CONCEPT: Input validation loop
    Keep asking until the user gives valid input.
    This is a VERY common pattern.
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("  Please enter a valid number.")


def get_int_input(prompt):
    """Safely get a whole number from the user."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("  Please enter a whole number.")


def run():
    """
    Main application loop.

    CONCEPT: The main loop pattern
    Most interactive programs follow this pattern:
    1. Show a menu
    2. Get user's choice
    3. Do something based on the choice
    4. Repeat until user quits
    """
    manager = InventoryManager()

    while True:
        print_header("INVENTORY MANAGEMENT SYSTEM")
        print("  1. View all products")
        print("  2. Add a product")
        print("  3. Search products")
        print("  4. Update quantity")
        print("  5. Update price")
        print("  6. Restock a product")
        print("  7. Sell a product")
        print("  8. Remove a product")
        print("  9. View low stock")
        print("  10. Inventory summary")
        print("  11. Sort by price")
        print("  0. Exit")
        print()

        choice = input("  Enter your choice: ").strip()

        if choice == "1":
            print_header("ALL PRODUCTS")
            print_product_table(manager.list_products())

        elif choice == "2":
            print_header("ADD NEW PRODUCT")
            name = input("  Product name: ").strip()
            price = get_float_input("  Price: $")
            quantity = get_int_input("  Quantity: ")
            category = input("  Category (press Enter for 'General'): ").strip()
            category = category if category else "General"

            try:
                product = manager.add_product(name, price, quantity, category)
                print(f"\n  Added: {product}")
            except ValueError as e:
                print(f"\n  Error: {e}")

        elif choice == "3":
            print_header("SEARCH PRODUCTS")
            keyword = input("  Search keyword: ").strip()
            results = manager.search_products(keyword)
            print(f"\n  Found {len(results)} result(s):")
            print_product_table(results)

        elif choice == "4":
            print_header("UPDATE QUANTITY")
            name = input("  Product name: ").strip()
            quantity = get_int_input("  New quantity: ")
            try:
                product = manager.update_quantity(name, quantity)
                print(f"\n  Updated: {product}")
            except (KeyError, ValueError) as e:
                print(f"\n  Error: {e}")

        elif choice == "5":
            print_header("UPDATE PRICE")
            name = input("  Product name: ").strip()
            price = get_float_input("  New price: $")
            try:
                product = manager.update_price(name, price)
                print(f"\n  Updated: {product}")
            except (KeyError, ValueError) as e:
                print(f"\n  Error: {e}")

        elif choice == "6":
            print_header("RESTOCK")
            name = input("  Product name: ").strip()
            amount = get_int_input("  Amount to add: ")
            try:
                product = manager.restock(name, amount)
                print(f"\n  Restocked: {product}")
            except (KeyError, ValueError) as e:
                print(f"\n  Error: {e}")

        elif choice == "7":
            print_header("SELL PRODUCT")
            name = input("  Product name: ").strip()
            amount = get_int_input("  Amount to sell: ")
            try:
                product = manager.sell(name, amount)
                print(f"\n  Sold {amount}x {product.name}. Remaining: {product.quantity}")
            except (KeyError, ValueError) as e:
                print(f"\n  Error: {e}")

        elif choice == "8":
            print_header("REMOVE PRODUCT")
            name = input("  Product name: ").strip()
            confirm = input(f"  Are you sure you want to remove '{name}'? (y/n): ")
            if confirm.lower() == "y":
                try:
                    removed = manager.remove_product(name)
                    print(f"\n  Removed: {removed.name}")
                except KeyError as e:
                    print(f"\n  Error: {e}")

        elif choice == "9":
            print_header("LOW STOCK ALERT")
            threshold = get_int_input("  Low stock threshold (default 10): ")
            low = manager.low_stock_products(threshold)
            print(f"\n  {len(low)} product(s) with stock <= {threshold}:")
            print_product_table(low)

        elif choice == "10":
            print_header("INVENTORY SUMMARY")
            summary = manager.inventory_summary()
            print(f"  Total products:   {summary['total_products']}")
            print(f"  Total value:      ${summary['total_value']:.2f}")
            print(f"  Low stock items:  {summary['low_stock_count']}")
            print(f"  Categories:       {', '.join(summary['categories']) if summary['categories'] else 'None'}")
            if summary["value_by_category"]:
                print(f"\n  Value by category:")
                for cat, val in summary["value_by_category"].items():
                    print(f"    {cat:<20} ${val:.2f}")

        elif choice == "11":
            print_header("PRODUCTS SORTED BY PRICE")
            desc = input("  High to low? (y/n): ").lower() == "y"
            sorted_products = manager.sort_by_price(descending=desc)
            print_product_table(sorted_products)

        elif choice == "0":
            print("\n  Goodbye!\n")
            break

        else:
            print("\n  Invalid choice. Please try again.")

        input("\n  Press Enter to continue...")
