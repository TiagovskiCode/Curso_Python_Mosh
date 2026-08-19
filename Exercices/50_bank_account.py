# Exercise 50: Bank Account Balance Tracker
# Objective: Practice creating helper functions to handle balance updates and transaction rules.

balance = 100

def deposit(amount):
    global balance
    balance += amount
    return f"Your account balance is ${balance}"

def withdraw(amount):
    global balance
    if amount > balance:
        return "Transaction not possible"
    else:
        balance -= amount
        return f"Your account balance is ${balance}"

def display_balance():
    return f"Your account balance is ${balance}"

print(deposit(100))
print(withdraw(50))
print(display_balance())
