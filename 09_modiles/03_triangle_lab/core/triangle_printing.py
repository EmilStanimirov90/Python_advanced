def print_upper_part(num):
    for i in range(1, num + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


def print_lower_part(num):
    for i in range(num-1, 0, -1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


def print_triangle(num):
    print_upper_part(num)
    print_lower_part(num)

