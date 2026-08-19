# Exercise 42: Final Price Calculator
# Objective: Practice parameters, default values, and returning a total value.

def calculate_total(price, tax_rate = 5):
    tax = price + (price * tax_rate / 100)
    return tax


print(calculate_total(100))
print(calculate_total(100, 5))
