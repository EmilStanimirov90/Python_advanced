n, m = input().split()
n= int(n)
m = int(m)
matrix = []
moves = {"left": (0, -1), "right": (0, 1), "down": (1, 0), "up": (-1, 0)}
start_position = []

for row in range(n):
    matrix.append(list(input()))
    for col in range(m):
        if matrix[row][col] == "B":

            r, c = row, col
            start_position = [row, col]

while True:
    command = input()

    new_r = r + moves[command][0]
    new_c = c + moves[command][1]
    if new_r not in range(n) or new_c not in range(m):
        print("The delivery is late. Order is canceled.")
        matrix[start_position[0]][start_position[1]] = " "
        break
    if matrix[new_r][new_c] == "*":
        continue
    elif matrix[new_r][new_c] == "-":
        matrix[new_r][new_c] = "."
    elif matrix[new_r][new_c] == "P":
        print("Pizza is collected. 10 minutes for delivery.")
        matrix[new_r][new_c] = "R"
    elif matrix[new_r][new_c] == "A":
        print("Pizza is delivered on time! Next order...")
        matrix[new_r][new_c] = "P"
        break
    r = new_r
    c = new_c

[print(''.join(r)) for r in matrix]
