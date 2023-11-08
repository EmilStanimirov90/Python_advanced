def fill_the_box(h, l, w, *args):
    box_size = h*l*w
    cubes_left = 0
    free_space = box_size
    for cubes in args:
        if cubes == "Finish":
            break
        cubes_left += cubes
        for cube in range(cubes):

            if free_space == 0:
                break
            free_space -= 1
            cubes_left -= 1

    if free_space > 0:
        return f"There is free space in the box. You could put {free_space} more cubes."

    return f"No more free space! You have {cubes_left} more cubes."




print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
