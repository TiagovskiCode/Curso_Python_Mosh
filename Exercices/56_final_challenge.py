# Final Exercise: Coffee Shop Order Processor
# Objective: Consolidate functions, loops, dictionaries, and conditional logic.

coffee_menu = {"espresso": 1.50, "latte": 3.00, "cappuccino": 2.50}
customer_order = ["espresso", "latte", "juice", "espresso"]

def calculate_order(menu, order):
    total = 0
    for item in order:
        if item in menu:
            total += menu[item]
        else:
            print(f"This item ´{item}´ does not exist")
    return f"The total price of your order is $´{total}´"

print(calculate_order(coffee_menu, customer_order))
