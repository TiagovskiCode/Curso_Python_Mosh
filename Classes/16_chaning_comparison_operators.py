# Chaining comparison operators allows you to evaluate multiple range conditions cleanly.

age = int(input("What is your age? "))

# Standard way with logical operators:
# if age >= 18 and age < 65:

# Chained comparison operator (Pythonic way and math way):
if 18 <= age < 65:
    print("You are eligible")
else:
    print("You are not eligible")
