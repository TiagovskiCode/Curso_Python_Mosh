# Exercise 49: Shopping Cart Total
# Objective: Practice processing lists of items and applying discounts with functions.

def items_price(price):
    if price >= 100:
        print("You have a 10% discount")
        return price - price * (10 / 100)
    else:
        return f"You dont have a discount and the final price is ${price}"


print(items_price(20))
print(items_price(150))
