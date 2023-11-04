matrix = []
my_position = []
n_targets = 0
n_targets_hit = 0
for row in range(5):
    matrix.append(input().split())
    for col in range(5):
        if matrix[row][col] == "A":
            my_position = [row, col]
            matrix[row][col] = "."
        elif matrix[row][col] == "x":
            n_targets += 1

targets_hit = []
possible_moves = {"up": (-1, 0), "down": (1, 0), "right": (0, 1), "left": (0, -1)}
n = int(input())
for _ in range(n):
    command = input().split()

    if command[0] == "move":
        move = possible_moves[command[1]]
        steps = int(command[2])
        row = my_position[0]
        col = my_position[1]
        for _ in range(steps):

            row += move[0]
            col += move[1]

            if row in range(5) and col in range(5):
                if matrix[row][col] == '.':
                    my_position = [row, col]

    elif command[0] == "shoot":
        direction = possible_moves[command[1]]
        row = my_position[0]
        col = my_position[1]

        for _ in range(5):
            row += direction[0]
            col += direction[1]

            if row in range(5) and col in range(5):
                if matrix[row][col] == "x":
                    n_targets -= 1
                    n_targets_hit += 1
                    targets_hit.append([row, col])
                    matrix[row][col] = '.'
                    break
        if n_targets == 0:
            break

if n_targets == 0:
    print(f"Training completed! All {n_targets_hit} targets hit.")
else:
    print(f"Training not completed! {n_targets} targets left.")
[print(row) for row in targets_hit]
