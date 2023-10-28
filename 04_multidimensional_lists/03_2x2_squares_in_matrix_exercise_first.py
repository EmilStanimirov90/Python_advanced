rows, cols = [int(x) for x in input().split()]
matrix = [[x for x in input().split()]for _ in range(rows)]
matches = 0

for row in range(len(matrix) - 1):
    for col in range(len(matrix[row]) - 1):
        if matrix[row][col] == matrix[row][col+1] == matrix[row+1][col] == matrix[row+1][col+1]:
            matches += 1
print(matches)
