# Exercise 13: Multiplication Table
# Objective: Generate and print the multiplication table for the number 7
# (from 1 to 10) formatted using an f-string inside the loop.

multiplier_base = 7

for step in range(1, 11):
    result = multiplier_base * step
    print(f"{multiplier_base} x {step} = {result}")
