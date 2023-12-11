def gather_credits(credits_needed, *courses):
    enrolled_courses = set()
    gathered_credits = 0

    for course, credit in courses:
        if gathered_credits >= credits_needed:
            break

        if course not in enrolled_courses:
            enrolled_courses.add(course)
            gathered_credits += credit

    if gathered_credits >= credits_needed:
        enrolled_courses_list = sorted(enrolled_courses)
        return f"Enrollment finished! Maximum credits: {gathered_credits}.\nCourses: {', '.join(enrolled_courses_list)}"
    else:
        credits_shortage = credits_needed - gathered_credits
        return f"You need to enroll in more courses! You have to gather {credits_shortage} credits more."

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
