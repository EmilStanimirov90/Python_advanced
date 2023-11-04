presents = int(input())
n = int(input())
santa_position = []
matrix = []
nice_kid = 0
happy_nice_kid = 0
for row in range(n):
    matrix.append(input().split())
    for col in range(n):
        if matrix[row][col] == "V":
            nice_kid += 1
        elif matrix[row][col] == "S":
            santa_position = [row, col]

possible_moves = {'up': (-1, 0), 'down': (1, 0), 'right': (0, 1), 'left': (0, -1)}

while True:
    command = input()
    if command == "Christmas morning":
        break
    if presents == 0:
        break
    matrix[santa_position[0]][santa_position[1]] = "-"
    move = possible_moves[command]
    row = santa_position[0] + move[0]
    col = santa_position[1] + move[1]

    santa_position = [row, col]

    if matrix[row][col] == 'V':

        presents -= 1
        nice_kid -= 1
        happy_nice_kid += 1
        if presents == 0:
            matrix[row][col] = "S"
            break
    elif matrix[row][col] == 'C':
        matrix[row][col] = "S"
        for d, v in possible_moves.items():
            row1 = santa_position[0] + v[0]
            col1 = santa_position[1] + v[1]

            if matrix[row1][col1] == "V":
                matrix[row1][col1] = "-"
                presents -= 1
                nice_kid -= 1
                happy_nice_kid += 1
            elif matrix[row1][col1] == "X":
                matrix[row1][col1] = "-"
                presents -= 1
            if presents == 0:
                break
        if presents == 0:
            break
    matrix[row][col] = "S"

if nice_kid > 0 and presents == 0:
    print("Santa ran out of presents!")
[print(*row) for row in matrix]
if nice_kid <= 0:
    print(f'Good job, Santa! {happy_nice_kid} happy nice kid/s.')

else:
    print(f'No presents for {nice_kid} nice kid/s.')
