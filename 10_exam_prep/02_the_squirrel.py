n = int(input())
path = input().split(", ")
matrix = []
s_position = []
for row_index in range(n):
    matrix.append([ch for ch in input()])
    for col_index in range(n):
        if matrix[row_index][col_index] == "s":
            s_position = [row_index, col_index]
hazelnuts = 0
directions_mapper = {'up': (-1, 0), "down": (1, 0), 'left': (0, -1), "right": (0, 1)}

for move in path:
    last_row = s_position[0]
    last_col = s_position[1]
    current_row = last_row + directions_mapper[move][0]
    current_col = last_col + directions_mapper[move][1]
    if current_row not in range(n) or current_col not in range(n):
        print("The squirrel is out of the field.")
        break
    elif matrix[current_row][current_col] == "h":
        hazelnuts += 1
        matrix[current_row][current_col] = "*"
        if hazelnuts == 3:
            print("Good job! You have collected all hazelnuts!")
            break
    elif matrix[current_row][current_col] == "t":
        print("Unfortunately, the squirrel stepped on a trap...")
        break
    s_position = [current_row, current_col]

else:
    print("There are more hazelnuts to collect.")

print(f"Hazelnuts collected: {hazelnuts}")
