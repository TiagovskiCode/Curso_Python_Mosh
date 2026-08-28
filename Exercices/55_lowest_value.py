# Exercise 55: Find the Lowest Value
# Objective: Practice tracking a minimum value manually through a list.

scores = [42, 15, 88, 9, 23]

def get_lowest(numbers):
    lowest = numbers[0]
    for numbers in scores:
        if numbers < lowest:
            lowest = numbers
    return lowest

print(get_lowest(scores))
