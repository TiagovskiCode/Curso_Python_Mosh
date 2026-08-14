# Exercise 30: Security Log Scanner
# Objective: Control loop execution using 'continue' to skip items
# and 'break' to terminate the loop early.

logs = ["OK", "WARNING", "OK", "CRITICAL", "OK", "ERROR"]

for log in logs:
    if log == "WARNING":
        continue
    elif log == "CRITICAL":
        print(f"LOG {log} -> Shutting down scanner!")
        break
    else:
        print(f"LOG {log} -> Normal")
