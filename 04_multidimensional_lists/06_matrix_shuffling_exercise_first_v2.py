r, c = [int(x) for x in input().split()]
matrix = [[x for x in input().split()]for _ in range(r)]


while True:
    command = input()
    if command == "END":
        break
    command = command.split()

    if command[0] != 'swap' or len(command) != 5:
        print("Invalid input!")
        continue

    row1, col1, row2, col2 = [int(x) for x in command[1:]]

    if 0 <= row1 < r and 0 <= row2 < r and 0 <= col1 < c and 0 <= col2 < c:
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
        [print(*row)for row in matrix]
    else:
        print("Invalid input!")