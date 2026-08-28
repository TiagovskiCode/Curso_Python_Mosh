# Functions can perform a task (like printing) or calculate and return a value.
# Returning a value allows you to store the result in a variable and reuse it elsewhere.

def greet(name):
    print(f"Hi {name}")


def get_greeting(name):
    return f"Hi {name}"


message = get_greeting("Mosh")
file = open("content.txt", "W")
file.write(message)
