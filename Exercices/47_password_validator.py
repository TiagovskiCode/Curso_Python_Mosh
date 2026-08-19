# Exercise 47: Password Validator
# Objective: Practice creating helper functions to validate text input with conditionals.

def len_verification(password):
    if len(password) >= 8:
        return True
    else:
        return False

def digit_verification(password):
    for char in password:
        if char.isdigit():
            return True
    return False

def general_verification(password):
    if len_verification(password) and digit_verification(password):
        return "Valid"
    else:
        return "Invalid"

print(general_verification("Tiago54cr9"))
print(general_verification("Tiago"))
print(general_verification("Tiagocristiano"))
