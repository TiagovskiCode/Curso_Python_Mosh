# Exercise 39: Area Calculator
# Objective: Practice function definition, default parameters (width=1),
# returning values, and calling functions with positional arguments.

def calculate_area(length, width=1):
    return length * width


area1 = calculate_area(5, 4)
print(f"Area with length 5 and width 4: {area1}")

area2 = calculate_area(5)
print(f"Area with length 5 and default width: {area2}")
