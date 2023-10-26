# rows = int(input())
# matrix = []
# for row in range(rows):
#     elements = [int(el) for el in input().split()]
#     matrix.append(elements)
#
# current_row_index = 0
# sum_col_nums = 0
# for col_index in range(rows):
#
#     sum_col_nums += matrix[current_row_index][col_index]
#     current_row_index += 1
# print(sum_col_nums)
#
#
# n = int(input())
# matrix = []
# for row in range(n):
#     elements = [int(el) for el in input().split()]
#     matrix.append(elements)
# sum_ = 0
# for row_index in range(n):
#     sum_ += matrix[row_index][row_index]
#
# print(sum_)

n = int(input())
matrix = []
for row in range(n):
    elements = [int(el) for el in input().split()]
    matrix.append(elements)
sum_reversed_diagonal = 0
for row_index in range(n - 1, -1, -1):
    sum_reversed_diagonal += matrix[row_index][row_index]

print(sum_reversed_diagonal)