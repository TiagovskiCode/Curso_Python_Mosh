# Exercise 66: Gym Membership Renewal Tracker
# Objective: Process member renewals, apply loyalty discounts, and track overdue accounts.
from os import name

members = [
    {"name": "Elena", "months": 12, "status": "active"},
    {"name": "Marcus", "months": 3, "status": "overdue"},
    {"name": "Sophia", "months": 6, "status": "active"},
    {"name": "Lucas", "months": 1, "status": "overdue"}
]

def process_membership(member_list):
    monthly_fee = 30
    total_revenue = 0
    overdue_members = []

    for member in member_list:
        if member["status"] == "active":
            if (member["months"]) >= 6:
                total_revenue += 25 * member["months"]
            else:
                total_revenue += monthly_fee * member["months"]

        else:
            overdue_members.append(member["name"])

    return {"total revenue": total_revenue, "overdue members": overdue_members}

print(process_membership(members))
