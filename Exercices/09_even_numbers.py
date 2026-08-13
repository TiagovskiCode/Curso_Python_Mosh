# Exercise 09: Even Numbers Counter
# Objective: Loop through numbers 1 to 9, print each even number,
# count how many even numbers are found, and print the total at the end.

count = 0

for numbers in range(1, 10):
    if numbers % 2 == 0:
        count += 1
        print(numbers)

print(f"We have {count} even numbers.")
