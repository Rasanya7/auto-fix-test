# Student Report Card Generator
# This file has bugs - used to test the Agentic Auto-Fix Pipeline

students = [
    {"name": "Kalyan", "marks": [85, 90, 78, 92, 88]},
    {"name": "Priya",  "marks": [70, 65, 80, 75, 90]},
    {"name": "Ravi",   "marks": [55, 60, 50, 45, 58]},
]

def calculate_average(marks):
    total = 0
    for i in range(len(marks) + 1):   # Bug 1: IndexError — goes one step too far
        total += marks[i]
    return total / len(marks)

def get_grade(average):
    if average >= 85:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 55:
        return "C"
    else:
        return "F"

def print_report(student):
    avg = calculate_average(student["marks"])
    grade = get_grade(avg)
    print("Student : " + student["name"])
    print("Average : " + avg)             # Bug 2: TypeError — can't concat float to str
    print("Grade   : " + grade)
    print("-" * 30)

for s in students:
    print_report(s)

print("Top scorer: " + topper["name"])    # Bug 3: NameError — 'topper' is never defined
