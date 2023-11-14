ROWS = 6
COLS = 7


class FullColumnError(Exception):
    pass


def print_matrix(m):
    for row in matrix:
        print(row)


def is_valid_column_choice(selected_column_num):
    if selected_column_index in range(COLS):
        return True
    return False


def place_player_number(column_index, m, player_number):
    for row_index in range(ROWS - 1, -1, -1):
        if m[row_index][column_index] == 0:
            m[row_index][column_index] = player_number
            return row_index, column_index
    else:
        raise FullColumnError


def is_winner(current_row, current_col, matrix, player):

    directions = {"up": (-1, 0),  "left": (0, -1),
                  'top_right': (-1, 1), "down_right": (1, 1), }

    for r, c in directions.items():
        row = current_row
        col = current_col
        opposite_row = current_row
        opposite_col = current_col
        positions_in_a_row = 1
        opposite_direction = 0
        for _ in range(3):
            row += c[0]
            col += c[1]
            if row in range(ROWS) and col in range(COLS):
                if matrix[row][col] == player:
                    positions_in_a_row += 1
                else:
                    break
            else:
                break
        for _ in range(3):
            opposite_row -= c[0]
            opposite_col -= c[1]
            if opposite_row in range(ROWS) and opposite_col in range(COLS):
                if matrix[opposite_row][opposite_col] == player:
                    opposite_direction += 1
                else:
                    break
            else:
                break
        if positions_in_a_row + opposite_direction >= 4:
            return True
    else:
        return False

def is_it_tie(matrix):
    for r in range(ROWS):
        for c in range(COLS):
            if matrix[r][c] == 0:
                return False
    return True



matrix = [[0 for _ in range(COLS)] for row in range(ROWS)]
print_matrix(matrix)
player = 1
while True:
    try:
        selected_column_number = int(input(f"Player {player}, please choose a column: "))
        selected_column_index = selected_column_number - 1
        if not is_valid_column_choice(selected_column_index):
            raise ValueError
        current_row, current_col = place_player_number(selected_column_index, matrix, player)
        print_matrix(matrix)
        if is_winner(current_row, current_col, matrix, player):
            print(f"Player {player} is the winner!!!")
            break
    except ValueError:
        print(f"Player {player}, please select number between 1-{COLS}")
        continue
    except FullColumnError:
        print(f"Player {player}, this column is full, please select another")
        continue

    player += 1
    player = 2 if player % 2 == 0 else 1

    if is_it_tie(matrix):
        print("Game over, it's a tie!")
        break
        