# Exercise 19: Highest Score
# Objective: Iterate through a list of numbers to find the maximum value
# using an 'if' condition inside a 'for' loop.

scores = [35, 62, 95, 40, 88]
highest_score = scores[0]

for score in scores[1:]:
    if score > highest_score:
        highest_score = score
print(f"\nHighest score: {highest_score}")
