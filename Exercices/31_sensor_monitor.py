# Exercise 31: Temperature Sensor Monitor
# Objective: Practice using 'continue' to skip bad data (-999)
# and 'break' to halt the loop on extreme threshold (>80).

readings = [22, 25, -999, 28, 95, 24]

for temp in readings:
    if temp == -999:
        continue
    elif temp > 80:
        print(f"Temp: {temp}ºC -> OVERHEAT DETECTED! Stopping system...")
        break
    else:
        print(f"Temp: {temp}ºC -> Normal")
