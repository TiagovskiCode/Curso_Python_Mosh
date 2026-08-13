# Exercise 11: Sum Multiples of 3
# Objective: Loop through numbers 1 to 20, find multiples of 3,
# and accumulate their total sum using 'total_sum += number'.

total_sum = 0

for number in range(1, 21):
    if number % 3 == 0:
        total_sum += number

print(total_sum)
