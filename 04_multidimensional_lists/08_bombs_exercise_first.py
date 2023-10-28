n = int(input())
matrix = [[int(x) for x in input().split()] for r in range(n)]
bombs = input().split()
sum_matrix = 0
alive_cells = 0

for bomb in bombs:
    bomb_row, bomb_col = [int(x) for x in bomb.split(",")]
    bomb_power = matrix[bomb_row][bomb_col]

    for row in range(bomb_row - 1, bomb_row + 2):
        for col in range(bomb_col - 1, bomb_col + 2):
            if row in range(n) and col in range(n) and matrix[row][col] > 0:
                matrix[row][col] -= bomb_power

for r in range(n):
    for c in range(n):
        if matrix[r][c] > 0:
            sum_matrix += matrix[r][c]
            alive_cells += 1

print(f"Alive cells: {alive_cells}")
print(f"Sum: {sum_matrix}")
[print(*row) for row in matrix]
