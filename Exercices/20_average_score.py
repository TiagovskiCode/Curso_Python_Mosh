# Exercise 20: Average Calculator
# Objective: Calculate the total sum of a list using a 'for' loop
# and compute the average value using len().

scores = [10, 20, 30, 40, 50]
total = 0

for score in scores:
    total += score

average = total / len(scores)

print(f"Total score: {total}")
print(f"Average score: {average}")
