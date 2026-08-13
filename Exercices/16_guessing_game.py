# Exercise 16: Guessing Game
# Objective: Use a 'while' loop to repeatedly prompt the user to guess
# a secret number until the correct value is entered.

number = 6

guess = int(input("Guess a number: "))

while number != guess:
    print("Try again.")
    guess = int(input("Guess a number: "))

print("You guessed the number!")
