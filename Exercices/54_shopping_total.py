# Exercise 54: Shopping Total with Tax
# Objective: Practice summing numbers in a list and applying simple math logic.

item_prices = [12.50, 5.00, 22.99]
tax = 8


def calculate_total(prices, tax_rate):
    # 1. Manual sum using a loop
    subtotal = 0
    for price in prices:
        subtotal += price

    # 2. Add tax percentage
    total = subtotal + (subtotal * (tax_rate / 100))
    return total


print(calculate_total(item_prices, tax))
