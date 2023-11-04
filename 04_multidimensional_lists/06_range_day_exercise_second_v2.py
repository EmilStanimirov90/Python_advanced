matrix = []
my_position = []
n_targets = 0
targets_down = 0
for row in range(5):
    matrix.append(input().split())
    for col in range(5):
        if matrix[row][col] == "A":
            my_position = [row, col]
            matrix[row][col] = "."
        elif matrix[row][col] == "x":
            n_targets += 1

targets_hit = []
directions = {"up": (-1, 0), "down": (1, 0), "right": (0, 1), "left": (0, -1)}
n = int(input())

for _ in range(n):
    command = input().split()
    direction = directions[command[1]]
    if command[0] == "move":
        row = my_position[0]
        col = my_position[1]
        steps = int(command[2])

        for _ in range(steps):
            row += direction[0]
            col += direction[1]

            if row in range(5) and col in range(5) and matrix[row][col] == '.':
                my_position = [row, col]

    elif command[0] == "shoot":

        row = my_position[0] + direction[0]
        col = my_position[1] + direction[1]

        while row in range(5) and col in range(5):

            if matrix[row][col] == "x":
                n_targets -= 1
                targets_hit.append([row, col])
                matrix[row][col] = '.'
                targets_down += 1
                break
            row += direction[0]
            col += direction[1]

    if n_targets == 0:
        break

if n_targets == 0:
    print(f"Training completed! All {targets_down} targets hit.")
else:
    print(f"Training not completed! {n_targets} targets left.")
[print(row) for row in targets_hit]
