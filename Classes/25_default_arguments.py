# Default arguments make parameters optional by assigning them a fallback value.
# Optional parameters with default values must always appear after required parameters.

def increment(number, by=1):
    return number + by


print(increment(2))
