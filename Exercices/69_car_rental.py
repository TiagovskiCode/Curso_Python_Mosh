# Exercise 69: Car Rental Agency Tracker
# Objective: Calculate total rental costs, apply weekly discounts, and flag luxury rentals.

rentals = [
    {"driver": "Alex", "days": 8, "luxury": False},
    {"driver": "Beatriz", "days": 3, "luxury": True},
    {"driver": "Carlos", "days": 7, "luxury": True},
    {"driver": "Diana", "days": 2, "luxury": False}
]

def car_rental(days_rented):
    total_revenue = 0
    luxury_drivers = []

    for car in days_rented:
        cost = car["days"] * 40

        if car["days"] >= 7:
            cost -= 40

        if car["luxury"]:
            cost += 50 * car["days"]
            luxury_drivers.append(car["driver"])

        total_revenue += cost

    return {"total revenue": total_revenue, "luxury drivers": luxury_drivers}

print(car_rental(rentals))
