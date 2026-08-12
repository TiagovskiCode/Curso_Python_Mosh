# The ternary operator evaluates a condition in a single line.
# Syntax: value_if_true if condition else value_if_false

age = 25

# Standard if/else (4 lines)
# if age >= 18:
#     message = "You are eligible!"
# else:
#     message = "You are not eligible!"

# Ternary operator (1 line)
message = "You are eligible!" if age >= 18 else "You are not eligible!"

print(message)
