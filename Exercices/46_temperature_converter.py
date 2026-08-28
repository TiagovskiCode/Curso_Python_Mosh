# Exercise 46: Temperature Converter
# Objective: Practice creating math helper functions for unit conversion.

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

print(celsius_to_fahrenheit(20))
print(fahrenheit_to_celsius(20))
