# Useful String Methods in Python

course = "  python programming  "

# 1. upper() - Converts the string to uppercase
print(course.upper())

# 2. lower() - Converts the string to lowercase
print(course.lower())

# 3. title() - Capitalizes the first letter of each word
print(course.title())

# 4. strip() - Removes leading and trailing whitespace
print(course.strip())
# Note: lstrip() removes left spaces, rstrip() removes right spaces

# 5. find() - Returns the index of the substring (-1 if not found)
print(course.find("pro"))

# 6. replace() - Replaces characters or substrings
print(course.replace("p", "j"))

# 7. 'in' operator - Checks if a substring exists (returns True or False)
print("pro" in course)

# 8. 'not in' operator - Checks if a substring does NOT exist
print("swift" not in course)
