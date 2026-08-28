# Exercise 60: Student Grade Analyzer
# Objective: Calculate average grades, check passing criteria, and classify student performance.

students = [
    {"name": "Elena", "grades": [85, 90, 92], "has_scholarship": True},
    {"name": "Marco", "grades": [55, 60, 58], "has_scholarship": False},
    {"name": "Sofia", "grades": [70, 75, 80], "has_scholarship": False},
    {"name": "Lucas", "grades": [40, 50, 45], "has_scholarship": True}
]

def evaluate_students(student_list):
    students_evaluation = []

    for student in student_list:
        final_grade = sum(student["grades"]) / len(student["grades"])

        if final_grade >= 70:
            status = "Passed"
        elif final_grade < 70 and student["has_scholarship"] == True:
            status = "Probation"
        else:
            status = "Failed"

        students_evaluation.append(f"{student['name']}: {status} (Avg: {round(final_grade, 1)})")


    return students_evaluation

print(evaluate_students(students))
