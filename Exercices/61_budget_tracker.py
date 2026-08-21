# Exercise 61: Monthly Budget Tracker
# Objective: Process transaction records, categorize expenses vs income, and track account balance.

transactions = [
    {"type": "income", "amount": 2500, "category": "salary"},
    {"type": "expense", "amount": 800, "category": "rent"},
    {"type": "expense", "amount": 150, "category": "groceries"},
    {"type": "income", "amount": 200, "category": "freelance"},
    {"type": "expense", "amount": 50, "category": "groceries"}
]

def summarize_budget(transaction_list):
    income = 0
    expense = 0

    for item in transaction_list:
        if item["type"] == "income":
            income += item["amount"]
        elif item["type"] == "expense":
            expense += item["amount"]

    savings = income - expense
    return {"income": income, "expense": expense, "savings": savings}

print(summarize_budget(transactions))
