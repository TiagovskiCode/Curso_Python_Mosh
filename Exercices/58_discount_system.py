# Exercise 58: Discount System
# Objective: Process a list of numbers and apply logic based on thresholds.

original_prices = [5, 25, 50, 10, 100]

def apply_discounts(prices):
    final_prices=[]
    for price in prices:
        if price > 20:
            final_prices.append(price * 0.9)
        else:
            final_prices.append(price)

    return final_prices


print(apply_discounts(original_prices))
