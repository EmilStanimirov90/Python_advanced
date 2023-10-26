n = int(input())

matrix = []

for _ in range(n):
    elements = list(input())
    matrix.append(elements)

symbol = input()
found = False
for row in range(n):
    if found:
        break
    for el in range(len(matrix[row])):
        if matrix[row][el] == symbol:
            print(f'({row}, {el})')
            found = True
            break
if not found:
    print(f"{symbol} does not occur in the matrix")