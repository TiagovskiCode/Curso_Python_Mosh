# Nested loops put one loop inside another.
# The inner loop completes ALL of its iterations for EVERY single iteration of the outer loop.

# Outer loop runs 5 times (x = 0 to 4)
for x in range(5):
    # Inner loop runs 3 times for every x (y = 0 to 2)
    for y in range(3):
        print(f"({x}, {y})")

# Total iterations = 5 * 3 = 15 lines printed