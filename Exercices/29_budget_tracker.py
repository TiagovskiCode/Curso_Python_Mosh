# Exercise 29: Daily Budget Tracker
# Objective: Calculate a running total and trigger a warning condition
# as soon as the accumulator exceeds a threshold.

expenses = [25.0, 40.0, 45.0, 10.0]
total_spend = 0

for amount in expenses:
    total_spend += amount
    if total_spend > 100:
        print(f"Spent: ${amount} | Total: ${total_spend} -> ⚠️ BUDGET EXCEEDED!")
    else:
        print(f"Spent: ${amount} | Total: ${total_spend}")

print(f"The total expend was ${total_spend}")