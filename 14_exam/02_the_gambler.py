n = int(input())
winnings = 100
matrix = []
jackpot = False
out = False
moves = {"left": (0, -1), "right": (0, 1), "down": (1, 0), "up": (-1, 0)}
for row in range(n):
    matrix.append(list(input()))
    for col in range(n):
        if matrix[row][col] == "G":
            r = row
            c = col

while True:
    command = input()
    if command == "end":
        break
    new_row = r + moves[command][0]
    new_col = c + moves[command][1]
    if new_row not in range(n) or new_col not in range(n):
        winnings = 0
        out = True
        break

    elif matrix[new_row][new_col] == 'W':
        winnings += 100

    elif matrix[new_row][new_col] == 'P':
        winnings -= 200
        if winnings < 0:
            matrix[new_row][new_col] = "G"
            matrix[r][c] = "-"
            out = True
            break

    elif matrix[new_row][new_col] == 'J':
        matrix[new_row][new_col] = "G"
        matrix[r][c] = "-"
        winnings += 100000
        jackpot = True
        break

    matrix[new_row][new_col] = "G"
    matrix[r][c] = "-"
    r = new_row
    c = new_col

if jackpot and not out:
    print(f"You win the Jackpot!")
    print(f"End of the game. Total amount: {winnings}$")
elif not jackpot and not out:
    print(f"End of the game. Total amount: {winnings}$")
elif out:
    print("Game over! You lost everything!")
if winnings > 0:
    [print(''.join(x)) for x in matrix]