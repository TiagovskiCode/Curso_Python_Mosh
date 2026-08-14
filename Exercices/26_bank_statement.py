# Exercise 26: Bank Statement Analyzer
# Objective: Loop through a list of positive and negative floats,
# classify each item with if/else, and maintain a running balance total.

transactions = [100.0, -20.0, 50.0, -15.0]
balance = 0

for amount in transactions:
    balance += amount
    if amount > 0:
        print(f"+ ${amount} (Deposit)")
    else:
        print(f"- ${abs(amount)} (Withdraw)")

print(f"\nFinal Balance: {balance}")
