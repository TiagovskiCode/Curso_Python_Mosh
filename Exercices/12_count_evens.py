# Exercise 12: Count Even Numbers
# Objective: Loop through numbers 1 to 30, check if each number is even,
# and count the total amount of even numbers found using 'even_count += 1'.

even_count = 0

for number in range(1, 31):
    if number % 2 == 0:
        even_count += 1

print(even_count)
