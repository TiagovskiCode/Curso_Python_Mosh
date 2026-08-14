# Exercise 34: Savings Goal Tracker
# Objective: Practice using a 'while' loop with user float inputs
# to accumulate a running total until a target goal is met.

balance = 0
goal = 100

while balance < goal:
    print(f"Goal: ${goal} | Current savings: ${balance}")
    deposit = float(input("Enter deposit amount: "))
    balance += deposit
    print(f"Added ${deposit}. Total savings: ${balance}")
print(f"🎉 Congratulations! Savings goal reached! Total saved: ${balance}")
