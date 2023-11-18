rows, cols = [int(el) for el in input().split(",")]

matrix = []
total_cheese_count = 0
mouse_position = [0, 0]
last_position = [0, 0]
for row_index in range(rows):
    matrix.append(list(input()))
    for col_index in range(cols):
        if matrix[row_index][col_index] == "M":
            mouse_position = [row_index, col_index]

        elif matrix[row_index][col_index] == "C":
            total_cheese_count += 1

moves = {"down": (1, 0), "up": (-1, 0), 'left': (0, -1), "right": (0, 1)}

while True:
    command = input()

    if command in moves.keys():
        row = mouse_position[0] + moves[command][0]
        col = mouse_position[1] + moves[command][1]
        last_row = mouse_position[0]
        last_col = mouse_position[1]

        if row not in range(rows) or col not in range(cols):
            print("No more cheese for tonight!")
            matrix[last_row][last_col] = "M"
            break
        elif matrix[row][col] == "C":
            total_cheese_count -= 1
            matrix[last_row][last_col] = "*"
            mouse_position = [row, col]
            matrix[row][col] = "M"
            if total_cheese_count == 0:
                print("Happy mouse! All the cheese is eaten, good night!")
                break
        elif matrix[row][col] == "*":
            matrix[last_row][last_col] = "*"
            mouse_position = [row, col]
            matrix[row][col] = "M"
        elif matrix[row][col] == "@":
            continue
        elif matrix[row][col] == "T":
            matrix[last_row][last_col] = "*"
            matrix[row][col] = "M"
            print("Mouse is trapped!")
            break
    if command == "danger":
        print("Mouse will come back later!")
        break

[print("".join(r)) for r in matrix]
