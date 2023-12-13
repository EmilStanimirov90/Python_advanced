def softuni_students(*args,**kwargs):
    student_courses = {}
    invalid_students = []
    sorted_args = sorted(args, key=lambda x: x[1])
    for c_id, s_name in sorted_args:
        if c_id in kwargs:
            if s_name not in student_courses:
                student_courses[s_name] = []
            student_courses[s_name].append(kwargs[c_id])
        else:
            invalid_students.append(s_name)
    result = ''
    for s, c in student_courses.items():
        result += f"*** A student with the username {s} has successfully finished the course {', '.join(c)}!\n"
    if invalid_students:
        result += f"!!! Invalid course students: {', '.join(invalid_students)}"

    return result



print(softuni_students(
    ('id_1', 'Kaloyan9905'),
    id_1='Python Web Framework',
))
print()
print(softuni_students(
    ('id_7', 'Silvester1'),
    ('id_32', 'Katq21'),
    ('id_7', 'The programmer'),
    id_76='Spring Fundamentals',
    id_7='Spring Advanced',
))
print()
print(softuni_students(
    ('id_22', 'Programmingkitten'),
    ('id_11', 'MitkoTheDark'),
    ('id_321', 'Bobosa253'),
    ('id_08', 'KrasimirAtanasov'),
    ('id_32', 'DaniBG'),
    id_321='HTML & CSS',
    id_22='Machine Learning',
    id_08='JS Advanced',
))
