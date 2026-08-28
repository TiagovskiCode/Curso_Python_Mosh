# Exercise 67: Online Store Shipping Calculator
# Objective: Calculate shipping totals, apply free shipping, and flag express deliveries.

orders = [
    {"customer": "Alex", "weight": 5, "express": True},
    {"customer": "Taylor", "weight": 12, "express": False},
    {"customer": "Jordan", "weight": 2, "express": True},
    {"customer": "Morgan", "weight": 8, "express": False}
]

def process_shipping(order_list):
    base_shipping = 4
    total_shipping = 0
    express_costumers = []

    for customer in orders:
        if customer["express"] == True:
            express_costumers.append(customer["name"])
            total_shipping += 15 + customer["weight"]*4

        else:
            