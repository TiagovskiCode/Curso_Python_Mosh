# Exercise 68: Hotel Booking Summary
# Objective: Calculate total revenue, handle weekend surcharges, and track long-stay guests.

bookings = [
    {"guest": "Sarah", "nights": 2, "weekend": False},
    {"guest": "David", "nights": 5, "weekend": True},
    {"guest": "Emma", "nights": 1, "weekend": True},
    {"guest": "Liam", "nights": 4, "weekend": False}
]

def hotel_booking(nights_spend):
    hotel_revenue = 0
    long_stay_guests = []

    for night in nights_spend:
        cost = night["nights"] * 100

        if night["weekend"]:
            cost += 30

        if night["nights"] >= 3:
            cost -= 20
            long_stay_guests.append(night["guest"])

        hotel_revenue += cost

    return {"total_revenue": hotel_revenue, "long_stay_guests": long_stay_guests}

print(hotel_booking(bookings))
