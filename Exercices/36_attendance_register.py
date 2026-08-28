# Exercise 36: Attendance Register
# Objective: Practice using 'while True', 'continue' for empty strings,
# and 'break' to terminate student registration.

student_count = 0

while True:
    name = input("Enter student name ('done' to finish): ")
    if name == "":
        continue
    elif name == "done":
        break
    else:
        print(f"Registered: {name}")
        student_count += 1

print(f"\n📋 Attendance complete! Total students present: {student_count}")
