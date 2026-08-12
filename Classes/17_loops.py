# For loops are used to repeat an action for a specific number of times or iterate over a sequence.

# 1. range(start, stop, step)
# Starts at 1, ends before 10, increments by 2
for number in range(1, 10, 2):
    print("Attempt", number, number * ".")

print("-" * 30)

# 2. For...Else Loop Pattern
# The 'else' block executes ONLY if the loop completes all iterations without hitting a 'break'
successful = True

for number in range(1, 4):
    print("Attempt", number)
    if successful:
        print("Successful!")
        break
else:
    print("Attempted 3 times and failed.")
