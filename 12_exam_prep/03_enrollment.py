def gather_credits(req_credits: int, *args):
    taken_courses = []
    collected_credits = 0
    for course, credits_ in args:

        if collected_credits >= req_credits:
            break

        if course not in taken_courses:
            taken_courses.append(course)
            collected_credits += credits_

    if collected_credits >= req_credits:
        result = f"Enrollment finished! Maximum credits: {collected_credits}.\n"
        result += f"Courses: {', '.join(sorted(taken_courses))}"
        return result

    return f"You need to enroll in more courses! You have to gather {req_credits - collected_credits} credits more."


print(gather_credits(
    80,
    ("Basics", 79),
))
print()
print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 50),
    ("Fundamentals", 27),
))
print()
print(gather_credits(
    120,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Basics1", 27),
    ("Basics2", 27),
    ("Basics3", 27),
    ("Advanced", 30),
    ("Web", 30)
))
