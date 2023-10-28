r, c = [int(x) for x in input().split()]

matrix = [[x for x in input()] for row in range(r)]
commands = input()
new_bunnies = []

for row in range(r):
    for col in range(c):
        if matrix[row][col] == 'P':
            current_row = row
            current_col = col
            matrix[row][col] = '.'

for command in commands:

    old_row = current_row
    old_col = current_col

    if command == "U":
        current_row -= 1
    elif command == "L":
        current_col -= 1
    elif command == "D":
        current_row += 1
    elif command == "R":
        current_col += 1

    for row in range(r):
        for col in range(c):
            if matrix[row][col] == "B":
                if [row, col] not in new_bunnies:
                    new_bunnies.append([row, col])
                if row + 1 in range(r):
                    new_bunnies.append([row + 1, col])
                if row - 1 in range(r):
                    new_bunnies.append([row - 1, col])
                if col + 1 in range(c):
                    new_bunnies.append([row, col + 1])
                if col - 1 in range(c):
                    new_bunnies.append([row, col - 1])
    for new_bunnie in new_bunnies:
        matrix[new_bunnie[0]][new_bunnie[1]] = "B"

    if current_row not in range(r) or current_col not in range(c):
        [print(*row, sep='') for row in matrix]
        print(f"won: {old_row} {old_col}")
        break

    if matrix[current_row][current_col] == "B":
        [print(*row, sep='') for row in matrix]
        print(f'dead: {current_row} {current_col}')
        break


