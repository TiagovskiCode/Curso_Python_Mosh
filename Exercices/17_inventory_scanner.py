# Exercise 17: Inventory Scanner
# Objective: Loop through a list of items, display them with a slot counter,
# and print the total length of the list using len().

inventory = ["Shield Potion", "Medkit", "Assault Rifle", "Shotgun", "Sniper Rifle"]
slot = 1

for item in inventory:
    print(f"Slot {slot}: {item}")
    slot += 1

print(f"\nTotal items in inventory: {len(inventory)}")
