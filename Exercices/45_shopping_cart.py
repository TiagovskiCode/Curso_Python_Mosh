# Exercise 45: Shopping Cart Checkout
# Objective: Practice combining multiple functions with default parameters.

def apply_discount(price, discount_percent=10):
    return price - (price * (discount_percent / 100))

def add_tax(price, tax_rate=5):
    return price + (price * (tax_rate / 100))

discounted = apply_discount(100)
final_price = add_tax(discounted)

print(f"Discounted Price: ${discounted}")
print(f"Final Price: ${final_price}")
