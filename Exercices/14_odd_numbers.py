# Exercise 14: Print Odd Numbers
# Objective: Loop through numbers 1 to 15, filter out even numbers,
# and print only the odd numbers directly to the console.

for number in range(1, 16):
    if number % 2 != 0:
        print(number)
