# Exercise 28: Shopping Receipt Calculator
# Objective: Loop through prices, apply a tax rate to each item,
# and sum up the final bill outside the loop.

prices = [10.0, 25.0, 5.0, 100.0]
total_bill = 0

for price in prices:
    taxed_price = price * 1.05
    total_bill += taxed_price
    print(f"Tem with tax: ${taxed_price}")

print(f"\nTotal bill: ${total_bill}")
