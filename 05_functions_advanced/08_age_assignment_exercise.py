# def age_assignment(*args, **kwargs):
#     result = []
#     for name in args:
#         for key in kwargs.keys():
#             if name.startswith(key):
#                 result.append(f"{name} is {kwargs[key]} years old.")
#     result = sorted(result, key=lambda x: x, reverse=False)
#     return "\n".join(result)
def age_assignment(*args, **kwargs):
    persons = {}

    for name in args:
        persons[name] = kwargs[name[0]]

    result = sorted(persons.items(), key=lambda x: x[0], reverse=False)
    final = []
    for name, age in result:
        final.append(f"{name} is {age} years old.")
    return "\n".join(final)


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
