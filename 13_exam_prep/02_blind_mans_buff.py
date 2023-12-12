n, m = input().split()
n = int(n)
m = int(m)
matrix = []
touched = 0
moves_made = 0
moves = {"left": (0, -1), "right": (0, 1), "down": (1, 0), "up": (-1, 0)}
for row in range(n):
    matrix.append(input().split())
    for col in range(m):
        if matrix[row][col] == "B":
            r = row
            c = col
while True:
    command = input()
    if command == "Finish":
        break
    new_r = r + moves[command][0]
    new_c = c + moves[command][1]
    if new_r not in range(n) or new_c not in range(m):
        new_r = r
        new_c = c

    if matrix[new_r][new_c] == "O":
        new_r = r
        new_c = c

    elif matrix[new_r][new_c] == "P":
        touched += 1
        moves_made += 1
        if touched == 3:
            break

    elif matrix[new_r][new_c] == "-":
        moves_made += 1

    matrix[r][c] = "-"
    matrix[new_r][new_c] = "B"
    r = new_r
    c = new_c

print("Game over!")
print(f"Touched opponents: {touched} Moves made: {moves_made}")


