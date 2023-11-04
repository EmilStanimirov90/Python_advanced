def knight_possible_attacks(r, c, limit):
    power = 0
    if r - 2 in range(limit) and c - 1 in range(limit):
        if board[r - 2][c - 1] == 'K':
            power += 1
    if r - 2 in range(limit) and c + 1 in range(limit):
        if board[r - 2][c + 1] == 'K':
            power += 1
    if r - 1 in range(limit) and c + 2 in range(limit):
        if board[r - 1][c + 2] == 'K':
            power += 1
    if r + 1 in range(limit) and c + 2 in range(limit):
        if board[r + 1][c + 2] == 'K':
            power += 1
    if r + 2 in range(limit) and c + 1 in range(limit):
        if board[r + 2][c + 1] == 'K':
            power += 1
    if r + 2 in range(limit) and c - 1 in range(limit):
        if board[r + 2][c - 1] == 'K':
            power += 1
    if r + 1 in range(limit) and c - 2 in range(limit):
        if board[r + 1][c - 2] == 'K':
            power += 1
    if r - 1 in range(limit) and c - 2 in range(limit):
        if board[r - 1][c - 2] == 'K':
            power += 1

    return power


n = int(input())
board = []
knights = []
removed = 0
for row in range(n):
    board.append([])
    elements = input()
    for col in range(n):
        board[row].append(elements[col])
        if board[row][col] == "K":
            knights.append([row, col, 0])

# print(len(knights))
top_knight = [0, 0, 0]
top_knight_count = 0

while True:
    knights_attacks = 0

    for knight in knights:
        knight[2] = knight_possible_attacks(knight[0], knight[1], n)
        knights_attacks += knight[2]

    if knights_attacks == 0:
        break

    for knight in knights:
        if knight[2] > top_knight[2]:
            top_knight = knight

    for knight in knights:
        if top_knight[2] == knight[2]:
            top_knight_count += 1

    if top_knight_count == 1:
        knights.remove(top_knight)
        top_knight_count = 0
        removed += 1
        board[top_knight[0]][top_knight[1]] = "0"
        top_knight = [0, 0, 0]
    elif top_knight_count > 1:
        for knight in knights:
            if knight[2] == top_knight[2]:
                knights.remove(knight)
                board[top_knight[0]][top_knight[1]] = "0"
                removed += 1
                top_knight = [0, 0, 0]
                top_knight_count = 0
#     [print(*line, sep=' ')for line in board]
#     print()
# print(len(knights))
print(removed)
