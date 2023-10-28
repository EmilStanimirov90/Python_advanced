from collections import deque

r, c = [int(x) for x in input().split()]
line = deque(input())

matrix = [[''for col in range(c)]for row in range(r)]

for row in range(r):
    for col in range(c):
        if row % 2 == 0:
            matrix[row][col] = line[0]
        else:
            matrix[row][-1 - col] = line[0]
        line.rotate(-1)

[print(*row, sep='') for row in matrix]