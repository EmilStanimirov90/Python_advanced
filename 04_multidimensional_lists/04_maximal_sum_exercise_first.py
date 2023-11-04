rows, cols = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for _ in range(rows)]
max_sum = float('-inf')
sub_matrix = []
max_col = 0
max_row = 0
for row in range(rows - 2):
    for col in range(cols - 2):
        current_sum = 0

        for r in range(row, row + 3):
            for c in range(col, col + 3):
                current_sum += matrix[r][c]

        if current_sum > max_sum:
            max_sum = current_sum
            max_col = col
            max_row = row


print(f'Sum = {max_sum}')
sub_matrix = [matrix[r][max_col:max_col+3]for r in range(max_row, max_row + 3)]

[print(*row) for row in sub_matrix]