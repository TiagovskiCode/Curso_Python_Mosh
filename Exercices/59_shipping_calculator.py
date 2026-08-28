# Exercise 59: Multi-Tier VIP Shipping Calculator
# Objective: Process customer orders, apply order thresholds, and account for VIP tier perks.

orders = [
    {"customer": "Alice", "subtotal": 120, "is_vip": True},
    {"customer": "Bob", "subtotal": 40, "is_vip": False},
    {"customer": "Charlie", "subtotal": 80, "is_vip": False},
    {"customer": "Diana", "subtotal": 30, "is_vip": True}
]

def calculate_final_prices(order_list):
    results = []

    for order in order_list:
        if order["subtotal"] >= 100 or order["is_vip"] == True:
            shipping = 0
        else:
            shipping = 10

        total = order["subtotal"] + shipping
        results.append(f"{order['customer']}: ${total}")

    return results

print(calculate_final_prices(orders))
