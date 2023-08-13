size = 8
matrix = []
white_position = []
black_position = []
turns = ['white', 'black']
chess_map_from_index_to_alpha = {
   0: "a",
   1: "b",
   2: "c",
   3: "d",
   4: "e",
   5: "f",
   6: "g",
   7: "h"
}

for row in range(size):
    line = input().split()
    matrix.append(line)
    if 'w' in line:
        white_position = [row, line.index('w')]
    if 'b' in line:
        black_position = [row, line.index('b')]

direction_white = (-1, 0)
direction_black = (1, 0)

while True:
    if turns[0] == 'white':
        left_diagonal = [(white_position[0] - 1), (white_position[1] - 1)]
        right_diagonal = [(white_position[0] - 1), (white_position[1] + 1)]
        if size > left_diagonal[0] >= 0 and size > left_diagonal[1] >= 0:
            if matrix[left_diagonal[0]][left_diagonal[1]] == 'b':
                print(f"Game over! White win, capture on {(chess_map_from_index_to_alpha[left_diagonal[1]] + str(size - left_diagonal[0]))}.")
                break
        if size > right_diagonal[0] >= 0 and size > right_diagonal[1] >= 0:
            if matrix[right_diagonal[0]][right_diagonal[1]] == 'b':
                print(f"Game over! White win, capture on {(chess_map_from_index_to_alpha[right_diagonal[1]] + str(size - right_diagonal[0]))}.")
                break
        if white_position[0] == 0:
            print(f"Game over! White pawn is promoted to a queen at {(chess_map_from_index_to_alpha[white_position[1]] + str(size - white_position[0]))}.")
            break
        white_position[0] += direction_white[0]
        white_position[1] += direction_white[1]
        if white_position[0] == 0:
            print(f"Game over! White pawn is promoted to a queen at {(chess_map_from_index_to_alpha[white_position[1]] + str(size - white_position[0]))}.")
            break
        turns.append(turns.pop(0))
    else:
        left_diagonal = [(black_position[0] + 1), (black_position[1] - 1)]
        right_diagonal = [(black_position[0] + 1), (black_position[1] + 1)]
        if size < left_diagonal[0] <= 0 and size < left_diagonal[1] <= 0:
            if matrix[left_diagonal[0]][left_diagonal[1]] == 'w':
                print(f"Game over! Black win, capture on {(chess_map_from_index_to_alpha[left_diagonal[1]] + str(size - left_diagonal[0]))}.")
                break
        if size < right_diagonal[0] <= 0 and size < right_diagonal[1] <= 0:
            if matrix[right_diagonal[0]][right_diagonal[1]] == 'w':
                print(f"Game over! Black win, capture on {(chess_map_from_index_to_alpha[right_diagonal[1]] + str(size - right_diagonal[0]))}.")
                break
        if black_position[0] == size - 1:
            print(f"Game over! Black pawn is promoted to a queen at {(chess_map_from_index_to_alpha[black_position[1]] + str(size - black_position[0]))}.")
            break
        black_position[0] += direction_black[0]
        black_position[1] += direction_black[1]
        turns.append(turns.pop(0))
        if black_position[0] == size - 1:
            print(f"Game over! Black pawn is promoted to a queen at {(chess_map_from_index_to_alpha[black_position[1]] + str(size - black_position[0]))}.")
            break

def check_if_can_capture(coordinates_attacker, coordinates_defender):
    row_a = coordinates_attacker[0]
    col_a = coordinates_attacker[1]
    row_d = coordinates_defender[0]
    col_d = coordinates_defender[1]
    if row_a - 1 >= 0 and col_a - 1 >= 0:
        if row_a - 1 == row_d and col_a - 1 == col_d:
            return [row_a - 1, col_a - 1]
    if row_a - 1 >= 0 and col_a + 1 < 8:
        if row_a - 1 == row_d and col_a + 1 == col_d:
            return [row_a - 1, col_a + 1]
    if row_a + 1 < 8 and col - 1 >= 0:
        if row_a + 1 == row_d and col_a - 1 == col_d:
            return [row_a + 1, col_a - 1]
    if row_a + 1 < 8 and col + 1 < 8:
        if row_a + 1 == row_d and col_a + 1 == col_d:
            return [row_a + 1, col_a + 1]


matrix = []
for _ in range(8):
    matrix.append(input().split())

white_pawn_coordinates = []
black_pawn_coordinates = []

position_row = {
    0: "8",
    1: "7",
    2: "6",
    3: "5",
    4: "4",
    5: "3",
    6: "2",
    7: "1",
}
positions_col = {
    0: "a",
    1: "b",
    2: "c",
    3: "d",
    4: "e",
    5: "f",
    6: "g",
    7: "h",
}

for row in range(8):
    for col in range(8):
        if matrix[row][col] == "w":
            white_pawn_coordinates = [row, col]
        if matrix[row][col] == "b":
            black_pawn_coordinates = [row, col]

for _ in range(8):
    capture_on = check_if_can_capture(white_pawn_coordinates, black_pawn_coordinates)
    if capture_on:
        position = positions_col[capture_on[1]] + position_row[capture_on[0]]
        print(f"Game over! White win, capture on {position}.")
        break

    white_pawn_coordinates[0] -= 1

    if white_pawn_coordinates[0] == 0:
        position = positions_col[white_pawn_coordinates[1]] + position_row[white_pawn_coordinates[0]]
        print(f"Game over! White pawn is promoted to a queen at {position}.")
        break

    capture_on = check_if_can_capture(black_pawn_coordinates, white_pawn_coordinates)
    if capture_on:
        position = positions_col[capture_on[1]] + position_row[capture_on[0]]
        print(f"Game over! Black win, capture on {position}.")
        break

    black_pawn_coordinates[0] += 1

    if black_pawn_coordinates[0] == 7:
        position = positions_col[black_pawn_coordinates[1]] + position_row[black_pawn_coordinates[0]]
        print(f"Game over! Black pawn is promoted to a queen at {position}.")
        break
