# Exercise 37: ATM PIN Verifier
# Objective: Practice validating secret strings with attempt limits
# using a 'while' loop and conditional checks.

correct_pin = "2805"
attempts = 0

while attempts < 3:
    entered_pin = input("Enter 4-digit PIN: ")
    if entered_pin == correct_pin:
        print("🔓 PIN correct! Access granted.")
        break
    else:
        attempts += 1
        print("Incorrect PIN. Try again.")
if attempts == 3 and entered_pin != correct_pin:
    print("\n🚨 Account locked after 3 failed attempts.")
