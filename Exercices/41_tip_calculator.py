# Exercise 41: Tip Calculator
# Objective: Practice parameters, default values (percentage=15),
# and returning a calculated result.

def calculate_tip(bill_amount, percentage=15):
    return bill_amount * (percentage / 100)


print(calculate_tip(50))
print(calculate_tip(50, 20))
