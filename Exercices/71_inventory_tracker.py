# Exercise 71: Warehouse Inventory & Reorder Tracker
# Objective: Calculate inventory value, apply category discounts, and track low-stock items.

inventory = [
    {"item": "Laptop", "price": 800, "stock": 4, "category": "electronics"},
    {"item": "Desk Chair", "price": 150, "stock": 12, "category": "furniture"},
    {"item": "Mouse", "price": 25, "stock": 2, "category": "electronics"},
    {"item": "Monitor", "price": 300, "stock": 5, "category": "electronics"}
]

def process_inventory(item_list):
    total_value = 0
    reorder_items = []

    for item in inventory:

        item_cost = item["price"] * item["stock"]

        if item["category"] == "electronics":
            item_cost *= 0.90

        total_value += item_cost

        if item["stock"] < 5:
            reorder_items.append(item["item"])

    return {"total value": round(total_value, 2), "Reorder items": reorder_items}

print(process_inventory(inventory))
