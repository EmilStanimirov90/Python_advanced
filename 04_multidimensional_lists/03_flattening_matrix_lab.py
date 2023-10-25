rows = int(input())
matrix = []
flattened = []
for row in range(rows):
    elements = [int(x) for x in input().split(', ')]
    matrix.append(elements)

for row in matrix:
    for el in row:
        flattened.append(el)

print(flattened)


