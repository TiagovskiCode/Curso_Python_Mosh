# A while loop repeats a block of code as long as its condition remains True.
# 'while True:' creates an intentional infinite loop, usually exited using 'break'.

while True:
    command = input(">")
    if command.lower() == "quit":
        break
    print("ECHO", command)
