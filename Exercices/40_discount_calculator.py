# Exercise 40: Discount Calculator
# Objective: Practice function definition, default parameters (discount=10),
# calculating values, and returning the final price.

def calculate_discount(price, discount=10):
    final_price = price - (price * discount / 100)
    return final_price


print(calculate_discount(100))
