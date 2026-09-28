# Shopping List Manager

This project practices Python lists, loops, and list operations.

- `list_warmup.py` — Demonstrates creating a list, accessing items by index, using append(), remove(), and len().
- `shopping_list.py` — A simple interactive shopping list manager that can add, remove, show, and finish.
- `list_report.py` — Prints a numbered shopping list, counts item names with more than 4 letters, and finds the longest item.

Checking `in` before calling `.remove()` is safer because it prevents Python from raising an error when the item is not in the list. It allows the program to handle a missing item gracefully and continue running.