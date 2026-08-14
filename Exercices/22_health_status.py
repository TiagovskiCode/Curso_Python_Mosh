# Exercise 22: Health Level Status
# Objective: Loop through a list of numbers and use an 'if/else' condition
# to categorize values based on a threshold.

health_levels = [100, 45, 80, 15, 90]

for hp in health_levels:
    if hp > 50:
        print(f"Health: {hp} --> Healthy")
    else:
        print(f"Health: {hp} --> LOW HEALTH !")
