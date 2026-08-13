# Exercise 18: High Score Filter
# Objective: Loop through a list of numbers, use an 'if' condition to filter values
# greater than or equal to 80, and count the occurrences.

scores = [45, 88, 62, 95, 100]
high_score_count = 0

for score in scores:
    if score >= 80:
        high_score_count += 1
        print(f"Score: {score} -> High Score")
    else:
        print(f"Score: {score} -> Low Score")

print(f"\nTotal high scores: {high_score_count}")
