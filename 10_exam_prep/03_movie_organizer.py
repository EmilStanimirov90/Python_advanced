def is_valid_move(matrix, row, col):
    # Check if the move is within the boundaries of the matrix
    return 0 <= row < len(matrix) and 0 <= col < len(matrix[0])


def find_mouse(matrix):
    # Find the current position of the mouse in the matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 'M':
                return i, j
    return -1, -1  # Mouse not found


def update_matrix(matrix, new_row, new_col):
    # Update the matrix with the new position of the mouse
    old_row, old_col = find_mouse(matrix)
    matrix[old_row][old_col] = '*'  # Update old position
    matrix[new_row][new_col] = 'M'  # Update new position


def print_matrix(matrix):
    for row in matrix:
        print(''.join(row))


def mouse_in_the_kitchen():
    n, m = map(int, input().split(','))
    kitchen = []

    # Reading the kitchen layout
    for _ in range(n):
        kitchen.append(list(input()))

    directions = []

    # Reading the directions until "danger" command
    while True:
        direction = input()
        if direction == "danger":
            break
        directions.append(direction)

    # Your logic to simulate the movement of the mouse goes here

    # Print the final state of the matrix and the corresponding message
    print("Message here")
    print_matrix(kitchen)


# Run the function
mouse_in_the_kitchen()