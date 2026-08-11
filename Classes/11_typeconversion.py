# Type Conversion in Python

# 1. Getting user input (input always returns a string)
x = input("x: ")
y = int(x) + 1
print(f"x: {x}, y: {y}")

# 2. Type Conversion Functions
print(int(x))     # Converts to Integer
print(float(x))   # Converts to Float (e.g. 1 -> 1.0)
print(bool(x))    # Converts to Boolean (True/False)
print(str(y))     # Converts to String

# 3. Falsy Values in Python
# These values always evaluate to False when converted to boolean:
# "" (empty string), 0, None, False
print(bool(""))     # False
print(bool(0))      # False
print(bool(None))   # False

# Truthy Values (anything that is NOT falsy evaluates to True)
print(bool(1))       # True
print(bool("False")) # True (because the string is not empty!)
