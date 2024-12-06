# Grading System: Write a program that takes a student’s marks as input and prints the grade (A, B, C, or F) based on given thresholds.

marks = int(input("Enter your marks:"))

def grade_of_students(marks):
    if marks >= 90:
        print("GRADE A")
    elif marks >= 80 and marks < 90:
        print("GRADE B")
    elif marks >= 70 and marks < 80:
        print("GRADE C")
    elif marks >= 50 and marks < 70:
        print("GRADE D")
    elif marks >= 30 and marks < 50:
        print("GRADE E")
    else:
        print("GRADE F")

grade_of_students(marks)
