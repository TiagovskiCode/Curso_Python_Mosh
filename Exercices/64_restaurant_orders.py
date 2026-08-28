# Exercise 64: Restaurant Order Calculator
# Objective: Process customer food orders, apply discounts, and track requested drinks.

orders = [
    {"item": "Burger", "price": 12, "category": "food"},
    {"item": "Iced Tea", "price": 4, "category": "drink"},
    {"item": "Pizza", "price": 18, "category": "food"},
    {"item": "Lemonade", "price": 5, "category": "drink"}
]

def process_orders(order_list):
    drinks_ordered = []
    total_bill = 0

    for item in order_list:
        if item["category"] == "food":
            total_bill += item["price"] - 2
        else:
            total_bill += item["price"]
            drinks_ordered.append(item["item"])

    return {"total bill": total_bill, "drinks ordered": drinks_ordered}

print(process_orders(orders))
