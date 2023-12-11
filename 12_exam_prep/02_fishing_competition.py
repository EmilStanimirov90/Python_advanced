n = int(input())
matrix = []
moves = {"left": (0, -1), "right": (0, 1), "down": (1, 0), "up": (-1, 0)}
qty_fish = 0
whirlpool = False
for row in range(n):
    matrix.append(list(input()))
    for col in range(n):
        if matrix[row][col] == "S":
            matrix[row][col] = "-"
            row_, col_ = [row, col]

while True:
    command = input()
    if command == "collect the nets":
        break
    matrix[row_][col_] = "-"
    new_row = row_ + moves[command][0]
    new_col = col_ + moves[command][1]
    if new_row > n - 1:
        new_row -= n
    if new_row < 0:
        new_row += n
    if new_col > n - 1:
        new_col -= n
    if new_col < 0:
        new_col += n

    if matrix[new_row][new_col].isdigit():
        qty_fish += int(matrix[new_row][new_col])
        matrix[new_row][new_col] = 'S'
    elif matrix[new_row][new_col] == "W":
        print(f"You fell into a whirlpool! The ship"
              f" sank and you lost the fish you caught."
              f" Last coordinates of the ship: [{new_row},{new_col}]")
        whirlpool = True
        break
    else:
        matrix[new_row][new_col] = "S"

    row_ = new_row
    col_ = new_col

if qty_fish >= 20:
    print("Success! You managed to reach the quota!")

if qty_fish < 20 and not whirlpool:
    print(f"You didn't catch enough fish and didn't reach the quota! "
          f"You need {20 - qty_fish} tons of fish more."
)
if qty_fish > 0 and not whirlpool:
    print(f"Amount of fish caught: {qty_fish} tons.")

if not whirlpool:
    [print("".join(r)) for r in matrix]