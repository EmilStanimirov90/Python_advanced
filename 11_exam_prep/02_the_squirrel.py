n = int(input())
seq_moves = input().split(", ")
matrix = []
position = []
hazelnuts = 0
moves = {"left": (0, -1), "right": (0, 1), "down": (1, 0), "up": (-1, 0)}

for row in range(n):
    matrix.append(list(input()))
    for col in range(n):
        if matrix[row][col] == "s":
            position = [row, col]

row, col = position
for move in seq_moves:

    new_row = row + moves[move][0]
    new_col = col + moves[move][1]

    if new_row not in range(n) or new_col not in range(n):
        print("The squirrel is out of the field.")
        break
    if matrix[new_row][new_col] == "h":
        hazelnuts += 1
        matrix[new_row][new_col] = "*"
        if hazelnuts == 3:
            print("Good job! You have collected all hazelnuts!")
            break
    elif matrix[new_row][new_col] == "t":
        print("Unfortunately, the squirrel stepped on a trap...")
        break
    row = new_row
    col = new_col
else:
    print("There are more hazelnuts to collect.")

print(f"Hazelnuts collected: {hazelnuts}")