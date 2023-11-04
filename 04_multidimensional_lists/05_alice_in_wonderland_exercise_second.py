n = int(input())
matrix = []
alice = []
rabbit_hole = []
tea_collected = 0
not_tea = ['.', 'R', 'A', "*"]
for row in range(n):
    matrix.append(input().split())
    for col in range(n):
        if matrix[row][col] == "A":
            alice = [row, col]
        elif matrix[row][col] == "R":
            rabbit_hole = [row, col]

while True:
    if tea_collected > 9 or alice == rabbit_hole or alice[0] not in range(n) or alice[1] not in range(n):
        break
    move = input()
    matrix[alice[0]][alice[1]] = "*"
    if move == 'left':
        alice = [alice[0], alice[1] - 1]
        if alice[0] in range(n) or alice[1] in range(n):

            if matrix[alice[0]][alice[1]] not in not_tea:
                tea_collected += int(matrix[alice[0]][alice[1]])
            matrix[alice[0]][alice[1]] = "*"

    elif move == "right":
        alice = [alice[0], alice[1] + 1]
        if alice[0] in range(n) or alice[1] in range(n):

            if matrix[alice[0]][alice[1]] not in not_tea:
                tea_collected += int(matrix[alice[0]][alice[1]])
            matrix[alice[0]][alice[1]] = "*"

    elif move == "up":
        alice = [alice[0] - 1, alice[1]]
        if alice[0] in range(n) or alice[1] in range(n):

            if matrix[alice[0]][alice[1]] not in not_tea:
                tea_collected += int(matrix[alice[0]][alice[1]])
            matrix[alice[0]][alice[1]] = "*"

    elif move == "down":
        alice = [alice[0] + 1, alice[1]]
        if alice[0] in range(n) or alice[1] in range(n):

            if matrix[alice[0]][alice[1]] not in not_tea:
                tea_collected += int(matrix[alice[0]][alice[1]])
            matrix[alice[0]][alice[1]] = "*"


if tea_collected > 9:
    print("She did it! She went to the party.")
elif alice == rabbit_hole or alice[0] not in range(n) or alice[1] not in range(n):
    print("Alice didn't make it to the tea party.")

[print(*row, sep=' ') for row in matrix]