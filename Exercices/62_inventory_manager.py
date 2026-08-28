# Exercise 62: Inventory Stock Manager
# Objective: Process product stock, track low-inventory alerts, and calculate total store value.

inventory = [
    {"product": "Laptop", "price": 1000, "stock": 5},
    {"product": "Mouse", "price": 25, "stock": 40},
    {"product": "Monitor", "price": 300, "stock": 2},
    {"product": "Keyboard", "price": 80, "stock": 15}
]

def analyze_inventory(stock_list):
    total_value = 0
    low_stock_products = []

    for product in stock_list:
        total_value += product["price"] * product["stock"]
        if product["stock"] < 10:
            low_stock_products.append(product["product"])

    return {"Total value": total_value, "Low Stock Alert": low_stock_products}

print(analyze_inventory(inventory))
