# Exercise 32: Quality Control Serial Scanner
# Objective: Practice filtering invalid items with continue
# and halting execution with break on corrupted data.

serials = ["SN-101", "INVALID", "SN-102", "HALT", "SN-103"]

for serial in serials:
    if serial == "INVALID":
        continue
    elif serial == "HALT":
        print(f"🚨 Critical error HALT encountered! Stopping scanner...")
        break
    else:
        print(f"Verified: {serial}")
