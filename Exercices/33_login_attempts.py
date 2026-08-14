# Exercise 33: Login Attempt Limiter
# Objective: Practice using a 'while' loop with a counter condition
# that stops automatically once maximum attempts are reached.

password = "gaming"
attempts = 0

while attempts < 3:
    user_pass = input("Write the password: ")

    if user_pass == password:
        print("✅ Access granted!")
        break

    attempts += 1
    print(f"Attempt {attempts}: Incorrect password!")

if attempts == 3 and user_pass != password:
    print("\n🔒 Account locked due to too many failed attempts!")
