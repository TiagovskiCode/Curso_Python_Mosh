# Exercise 67: Online Store Shipping Calculator
# Objective: Calculate shipping totals, apply free shipping, and flag express deliveries.

orders = [
    {"customer": "Alex", "weight": 5, "express": True},
    {"customer": "Taylor", "weight": 12, "express": False},
    {"customer": "Jordan", "weight": 2, "express": True},
    {"customer": "Morgan", "weight": 8, "express": False}
]

def process_shipping(order_list):
    total_shipping = 0
    express_customers = []

    for customer in order_list:
        if customer["weight"] < 10:
            total_shipping += customer["weight"] * 4

        if customer["express"]:
            total_shipping += 15
            express_customers.append(customer["customer"])

    return {"total_shipping": total_shipping, "express_customers": express_customers}

print(process_shipping(orders))
