n = int(input())
matrix = []
matrix = [[int(x) for x in input().split(', ')]for _ in range(n)]
prime_diagonal = [matrix[i][i] for i in range(n)]
# sec_diagonal = [matrix[i][n - 1 - i] for i in range(n)]
sec_diagonal = [matrix[i][- 1 - i] for i in range(n)]

print(f'Primary diagonal: {", ".join([str(x) for x in prime_diagonal])}. Sum: {sum(prime_diagonal)}')
print(f'Secondary diagonal: {", ".join([str(x) for x in sec_diagonal])}. Sum: {sum(sec_diagonal)}')
# for _ in range(n):
#     elements = [int(x) for x in input().split(', ')]
#     matrix.append(elements)
#
# prime_diagonal = []
# sec_diagonal = []
# prime_sum = 0
# sec_sum = 0
# col = 0
#
# for row in range(len(matrix)):
#
#     prime_sum += matrix[row][col]
#     prime_diagonal.append(matrix[row][col])
#     sec_sum += matrix[row][len(matrix) - 1 - col]
#     sec_diagonal.append(matrix[row][len(matrix) - 1 - col])
#     col += 1
#
# print(f'Primary diagonal: {", ".join([str(x) for x in prime_diagonal])}. Sum: {prime_sum}')
# print(f'Secondary diagonal: {", ".join([str(x) for x in sec_diagonal])}. Sum: {sec_sum}')