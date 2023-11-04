n = int(input())
matrix = [[int(x) for x in input().split()]for _ in range(n)]

while True:
    command = input()
    if command == "END":
        break
    order, row, col, value = command.split()
    row, col, value = int(row), int(col), int(value)
    if order == "Add":
        if row in range(n) and col in range(n):
            matrix[row][col] += value
        else:
            print("Invalid coordinates")
    elif order == "Subtract":
        if row in range(n) and col in range(n):
            matrix[row][col] -= value
        else:
            print("Invalid coordinates")

[print(*row, sep=' ')for row in matrix]