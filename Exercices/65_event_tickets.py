# Exercise 65: Event Ticket Calculator
# Objective: Process ticket sales, apply group discounts, and track VIP attendees.

tickets = [
    {"name": "Alice", "qty": 4, "type": "standard"},
    {"name": "Bob", "qty": 1, "type": "vip"},
    {"name": "Charlie", "qty": 3, "type": "standard"},
    {"name": "Diana", "qty": 2, "type": "vip"}
]


def process_tickets(ticket_list):
    vip_buyers = []
    total_revenue = 0

    for buyer in ticket_list:
        if buyer["type"] == "standard":
            if buyer["qty"] >= 3:
                total_revenue += buyer["qty"] * 40
            else:
                total_revenue += buyer["qty"] * 50
        else:
            vip_buyers.append(buyer["name"])
            total_revenue += buyer["qty"] * 100

    return {"total_revenue": total_revenue, "vip_buyers": vip_buyers}


print(process_tickets(tickets))
