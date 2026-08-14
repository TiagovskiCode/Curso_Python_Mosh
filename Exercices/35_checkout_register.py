# Exercise 35: Store Checkout Register
# Objective: Practice using an infinite 'while True' loop with a 'break'
# condition triggered by a specific exit value (0).

total_bill = 0

while True:
    price = float(input("Enter a item price ($0 to checkout): "))
    if price == 0:
        break
    total_bill += price
    print(f"Item added. Current: ${total_bill}")
print(f"\n🛒 Checkout complete! Final total: ${total_bill}")
