# Exercise 63: Flight Manifest Processor
# Objective: Process passenger records, sum up extra luggage fees, and identify VIPs.

passengers = [
    {"name": "Sarah", "bags": 2, "is_vip": False},
    {"name": "David", "bags": 0, "is_vip": True},
    {"name": "Lara", "bags": 3, "is_vip": False},
    {"name": "John", "bags": 1, "is_vip": True}
]


def process_manifest(passenger_list):
    vip_passengers = []
    total_bag_fees = 0

    for p in passenger_list:
        if p["is_vip"] == True:
            vip_passengers.append(p["name"])
        else:
            total_bag_fees += p["bags"] * 30

    return{"total bag fees": total_bag_fees, "vip_passengers": vip_passengers}

print(process_manifest(passengers))
