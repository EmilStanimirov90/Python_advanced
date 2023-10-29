sub_lists = input().split("|")
matrix = []

for i in range(len(sub_lists)-1, -1, -1):
    row = [int(x) for x in sub_lists[i].split()]
    if row:
        matrix.append(row)

[print(*row, sep=' ', end=' ')for row in matrix]


# new = []
# for index in range(-1, -(len(sub_lists)+1), -1):
#     new.append(sub_lists[index].split())
# print(new)
#
# for char in new:
#     for c in char:
#         if c != " ":
#             print(f'{c}', end=" ")
