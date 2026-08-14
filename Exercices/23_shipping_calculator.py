# Exercise 23: Free Shipping Filter
# Objective: Iterate through a list of prices and check which items
# qualify for free shipping using an 'if/else' condition.

prices = [15.99, 65.00, 8.50, 120.00, 49.99]

for price in prices:
    if price >= 50:
        print(f"Price: {price} --> Free Shipping !")
    else:
        print(f"Price: {price} --> Standard Shipping !")
