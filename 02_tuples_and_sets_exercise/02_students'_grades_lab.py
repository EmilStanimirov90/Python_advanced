qty_students = int(input())
students_data = {}
for student in range(qty_students):
    name, grade = input().split()
    if name not in students_data:
        students_data[name] = []
    students_data[name].append(float(grade))

for student_name, grades in students_data.items():
    formatted_grades = " ".join([f"{grade:.2f}" for grade in grades])
    average_grade = sum(grades)/len(grades)
    print(f"{student_name} -> {formatted_grades} (avg: {average_grade:.2f})")