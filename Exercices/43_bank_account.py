# Exercise 43: Bank Account Manager
# Objective: Practice creating multiple helper functions for deposits,
# withdrawals, and formatting account statements.

balance = 100

def deposit(balance, amount):
    return balance + amount

def withdraw(balance, amount):
    return balance - amount

def format_statement(name, balance):
    return f"Account: {name} | Current Balance: ${balance}"

print(deposit(balance, 20))
print(withdraw(balance, 20))
print(format_statement("Tiago", balance))
