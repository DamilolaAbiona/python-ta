"""
CONCEPT: The __main__.py file

This file makes the 'inventory' folder runnable as a module:
    python -m inventory

When Python sees '-m inventory', it looks for __main__.py inside
the inventory folder and runs it.

INTERVIEW TIP: Know the difference between:
    python inventory/cli.py        # runs a specific file
    python -m inventory            # runs the package (this file)
"""

from inventory.cli import run

if __name__ == "__main__":
    run()
