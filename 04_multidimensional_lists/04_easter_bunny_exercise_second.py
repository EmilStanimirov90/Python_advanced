n = int(input())
matrix = []
bunny_starting_position = []
for row in range(n):
    matrix.append(input().split())
    for col in range(n):
        if matrix[row][col] == "B":
            bunny_starting_position = [row, col]

right = 0
right_positions = []
for _ in range(1, n):
    new_col = bunny_starting_position[1]
    new_col += _

    if new_col in range(n):
        if matrix[bunny_starting_position[0]][new_col] == "X":
            break
        right += int(matrix[bunny_starting_position[0]][new_col])
        right_positions.append([bunny_starting_position[0], new_col])

up = 0
up_positions = []
for _ in range(1, n):
    new_row = bunny_starting_position[0]
    new_row -= _

    if new_row in range(n):
        if matrix[new_row][bunny_starting_position[1]] == "X":
            break
        up += int(matrix[new_row][bunny_starting_position[1]])
        up_positions.append([new_row, bunny_starting_position[1]])

down = 0
down_positions = []
for _ in range(1, n):
    new_row = bunny_starting_position[0]
    new_row += _

    if new_row in range(n):
        if matrix[new_row][bunny_starting_position[1]] == "X":
            break
        down += int(matrix[new_row][bunny_starting_position[1]])
        down_positions.append([new_row, bunny_starting_position[1]])

left = 0
left_positions = []
for _ in range(1, n):
    new_col = bunny_starting_position[1]
    new_col -= _

    if new_col in range(n):
        if matrix[bunny_starting_position[0]][new_col] == "X":
            break
        left += int(matrix[bunny_starting_position[0]][new_col])
        right_positions.append([bunny_starting_position[0], new_col])

if left > up and left > right and left > down:
    print("left")
    for position in range(len(left_positions)):
        print(left_positions[position])
    print(left)
elif right > up and right > left and right > down:
    print("right")
    for position2 in range(len(right_positions)):
        print(right_positions[position2])
    print(right)
elif up > left and up > right and up > down:
    print("up")
    for position3 in range(len(up_positions)):
        print(up_positions[position3])
    print(up)
elif down > up and down > right and down > left:
    print("down")
    for position4 in range(len(down_positions)):
        print(down_positions[position4])
    print(down)

