# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         print(matrix[i][j], end=" ")
# print()

size = int(input())
matrix = [[0] * size for row in range(0, size)]

for x in range(0, size):
    line = list(map(int, input().split()))
    for y in range(0, size):
        matrix[x][y] = line[y]

sum_diagonal = sum(matrix[size - i - 1][size - i - 1] for i in range(size))
print(sum_diagonal)