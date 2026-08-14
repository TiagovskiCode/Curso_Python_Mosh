# Exercise 21: Inventory Search
# Objective: Loop through a list of strings and use an 'if' condition
# to trigger a custom message when a specific item is found.

inventory = ["Assault Rifle", "Medkit", "Shotgun", "Mini Shield"]

for item in inventory:
    if item == "Medkit":
        print(f"item: {item} --> Found healing item!")
    else:
        print(f"item: {item}")
