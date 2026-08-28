# Exercise 44: Student Grade Calculator
# Objective: Practice helper functions for math calculations and pass/fail logic.

def grades(score1, score2, score3):
    return (score1 + score2 + score3) / 3

def get_grade_status(average):
    if average >= 50:
        return "You passed"
    else:
        return "Fail"


avg = grades(50, 80, 40)
print(get_grade_status(avg))
