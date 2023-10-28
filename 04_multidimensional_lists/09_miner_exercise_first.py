n = int(input())
commands = input().split()

matrix = [[x for x in input().split()] for row in range(n)]
collected_coal = 0
sum_coal_on_map = 0
third_ending = True
for row in range(n):
    for col in range(n):
        if matrix[row][col] == "s":
            current_row = row
            current_col = col
        if matrix[row][col] == "c":
            sum_coal_on_map += 1

for command in commands:
    if command == "left":
        if current_col - 1 in range(0, n):
            current_col -= 1
    elif command == "right":
        if 0 <= current_col + 1 in range(0, n):
            current_col += 1
    elif command == "up":
        if 0 <= current_row - 1 in range(0, n):
            current_row -= 1
    elif command == "down":
        if 0 <= current_row + 1 in range(0, n):
            current_row += 1

    if matrix[current_row][current_col] == "c":
        collected_coal += 1
        matrix[current_row][current_col] = '*'

    if matrix[current_row][current_col] == "e":
        print(f"Game over! ({current_row}, {current_col})")
        third_ending = False
        break

    elif collected_coal == sum_coal_on_map:
        print(f"You collected all coal! ({current_row}, {current_col})")
        third_ending = False
        break

if third_ending:
    print(f"{sum_coal_on_map - collected_coal} pieces of coal left. ({current_row}, {current_col})")
