# Exercise 25: Warehouse Stock Checker
# Objective: Loop through a list of stock numbers, use if/elif/else conditions,
# and track a total counter outside the loop.

stock_levels = [12, 3, 25, 0, 4]
out_of_stock_counter = 0

for stock in stock_levels:
    if stock == 0:
        out_of_stock_counter += 1
        print(f"Stock: {stock} -> OUT OF STOCK !")
    elif stock < 5:
        print(f"Stock: {stock} -> LOW STOCK !")
    else:
        print(f"Stock: {stock} -> In Stock")

print(f"\nTotal out of stock items: {out_of_stock_counter}")
