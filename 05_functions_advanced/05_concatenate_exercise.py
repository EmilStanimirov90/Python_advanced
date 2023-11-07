def concatenate(*args, **kwargs):
    string = ''
    for st in args:
        string += st

    for k, v in kwargs.items():
        if k in string:
            string = string.replace(k, v)

    return string


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))
