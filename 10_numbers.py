import math

#Math is a library for mathematics, and in this situation it is an
# object

# 1. Number Types in Python
x = 1       # Integer (int)
y = 1.1     # Floating point (float)
z = 1 + 2j  # Complex number (complex)

print(type(x))
print(type(y))
print(type(z))

# 2. Basic Arithmetic Operators
a = 10
b = 3

print(a + b)   # Addition (13)
print(a - b)   # Subtraction (7)
print(a * b)   # Multiplication (30)
print(a / b)   # Division (returns float: 3.3333...)
print(a // b)  # Floor Division (returns integer: 3)
print(a % b)   # Modulus / Remainder (1)
print(a ** b)  # Exponentiation / Power (10^3 = 1000)

# 3. Augmented Assignment Operators
a += 3         # Same as: a = a + 3
print(a)

# 4. Built-in Functions
print(round(2.9))  # Rounds to nearest integer (3)
print(abs(-2.9))   # Absolute value (2.9)

# 5. Math Module Functions
print(math.ceil(2.2))   # Rounds UP (3)
print(math.floor(2.9))  # Rounds DOWN (2)
