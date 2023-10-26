rows, cols = [int(x) for x in input().split(', ')]

matrix = []

for _ in range(rows):
    elements = [int(x) for x in input().split(', ')]
    matrix.append(elements)

top_sum = 0
top_sub_matrix = []
for row in range(len(matrix) - 1):

    for el in range(len(matrix[row]) - 1):
        current_sum = matrix[row][el] + matrix[row][el + 1] + matrix[row + 1][el] + matrix[row + 1][el + 1]
        if current_sum > top_sum:
            top_sum = current_sum
            top_sub_matrix = [[matrix[row][el], matrix[row][el + 1]], [matrix[row + 1][el], matrix[row + 1][el + 1]]]

for row in range(len(top_sub_matrix)):
    print(' '.join([str(x) for x in top_sub_matrix[row]]))
print(top_sum)
