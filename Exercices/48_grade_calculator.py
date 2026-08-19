# Exercise 48: Grade Calculator
# Objective: Practice working with list processing and conditional logic functions.

def grades(grade1, grade2, grade3):
    return (grade1 + grade2 + grade3) / 3

def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif 89 > score > 80:
        return "B"
    elif 79 > score > 70:
        return "C"
    elif 69 > score > 60:
        return "D"
    else:
        return "F"

print(grades(80, 65, 70))
avg = grades(80, 65, 70)
print(get_letter_grade(avg))
