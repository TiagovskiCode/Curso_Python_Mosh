# Conditional statements execute different blocks of code based on
# whether a condition is True or False.

temperature = int(input("What is your temperature? "))

if temperature > 30:
    print("It's a hot day")
    print("Drink plenty of water")
elif temperature > 20:
    print("It's a nice day")
elif temperature > 10:
    print("It's a bit cold")
else:
    print("It's cold!")

print("Done")  # Runs regardless, because it is outside the indented block
