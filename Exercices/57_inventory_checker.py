# Exercise 57: Inventory Checker
# Objective: Check if items in an order are in stock and sum their available amounts.

current_inventory = {"apples": 10, "bananas": 5, "oranges": 8}
order = ["apples", "pears", "bananas"]

def check_inventory(inventory, items_needed):
    total = 0
    for item in items_needed:
        if item in inventory:
            total += inventory[item]
        else:
            print(f"The item ´{item}´ is not available !")
    return total


print(check_inventory(current_inventory, order))
