# Exercise 24: 10% Cart Discount
# Objective: Loop through a list of prices, calculate a math operation
# inside the loop, and display the transformed values.

cart_prices = [20.0, 50.0, 100.0, 15.0]

for price in cart_prices:
    discounted_price = price * 0.9
    print(f"Price: {price} --> Discounted: ${discounted_price}")
