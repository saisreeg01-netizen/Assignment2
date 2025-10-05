def assign_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    else:
        return "F"

marks = 85
grade = assign_grade(marks)
print(f"Marks: {marks}, Grade: {grade}")
