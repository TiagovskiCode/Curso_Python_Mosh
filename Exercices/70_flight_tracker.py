# Exercise 70: Flight Booking & Luggage Fee Tracker
# Objective: Process passenger tickets, handle extra bag fees, and track priority passengers.

passengers = [
    {"name": "Carlos", "class": "economy", "bags": 2},
    {"name": "Sofia", "class": "business", "bags": 1},
    {"name": "Andre", "class": "economy", "bags": 0},
    {"name": "Beatriz", "class": "business", "bags": 3}
]

def process_flights(passenger_list):
    priority_list = []
    total_revenue = 0

    for passenger in passenger_list:
        if passenger["class"] == "economy":
            total_revenue += 150
        elif passenger["class"] == "business":
            total_revenue += 400

        if passenger["bags"] > 1:
            total_revenue += (passenger["bags"] - 1) * 30

        if passenger["class"] == "business":
            priority_list.append(passenger["name"])

    return {"total_revenue": total_revenue, "priority_list": priority_list}

print(process_flights(passengers))
