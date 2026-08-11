#In this exercise we will convert temperature (Celcius) to Fahrenheit and Kelvin

temperature = input("What is the temperature outside: ")
temperature_float = float(temperature)
fahrenheit = temperature_float * 9/5 + 32
kelvin = temperature_float + 273.15

print(f"The temperature outside is {temperature_float:.2f}ºC, converted to Fahrenheit is {fahrenheit:.2f}ºF, and to Kelvin is {kelvin:.2f}K")
