data = [int(x) for x in input().split(', ')]
rows, cols = data
matrix = []
sum_matrix = 0
for row in range(rows):
    elements = [int(x) for x in input().split(', ')]
    sum_matrix += sum(elements)
    matrix.append(elements)

print(sum_matrix)
print(matrix)