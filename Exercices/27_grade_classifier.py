# Exercise 27: Student Pass/Fail Tracker
# Objective: Loop through scores, classify each with if/else,
# and track multiple separate counters outside the loop.

scores = [85, 42, 76, 90, 55, 30]
passed_count = 0
failed_count = 0

for score in scores:
    if score >= 60:
        passed_count += 1
        print(f"Score: {score} -> You passed !")
    else:
        failed_count += 1
        print(f"Score: {score} -> FAIL !")
print(f"\n{passed_count} have passed and {failed_count} have failed !")
