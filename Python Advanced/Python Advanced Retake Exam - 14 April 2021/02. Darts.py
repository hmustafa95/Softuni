size = 7
matrix = []
player_one_score = 501
counter_player_one = 0
player_two_score = 501
counter_player_two = 0
player_one, player_two = input().split(', ')
turns = [player_one, player_two]

for _ in range(size):
    matrix.append(input().split())

while True:
    if player_one_score <= 0:
        print(f"{player_one} won the game with {counter_player_one} throws!")
        break
    if player_two_score <= 0:
        print(f"{player_two} won the game with {counter_player_two} throws!")
        break
    hit_position = list(map(int, eval(input())))
    player_turn = turns.pop(0)
    turns.append(player_turn)
    if player_turn == player_one:
        counter_player_one += 1
    elif player_turn == player_two:
        counter_player_two += 1
    if not all((0 <= hit_position[0] < size, 0 <= hit_position[1] < size)):
        continue
    if matrix[hit_position[0]][hit_position[1]] == 'B':
        if player_turn == player_one:
            player_one_score = 0
            continue
        else:
            player_two_score = 0
            continue
    elif matrix[hit_position[0]][hit_position[1]].isdigit():
        if player_turn == player_one:
            player_one_score -= int(matrix[hit_position[0]][hit_position[1]])
        else:
            player_two_score -= int(matrix[hit_position[0]][hit_position[1]])
    elif matrix[hit_position[0]][hit_position[1]] == 'D':
        result = 0
        for idx_row in matrix[hit_position[0]]:
            if idx_row.isdigit():
                result += int(idx_row)
        for idx_col in matrix:
            if idx_col[hit_position[1]].isdigit():
                result += int(idx_col[hit_position[1]])
        add_number = result * 2
        if player_turn == player_one:
            player_one_score -= add_number
        else:
            player_two_score -= add_number
    elif matrix[hit_position[0]][hit_position[1]] == 'T':
        result = 0
        for idx_row in matrix[hit_position[0]]:
            if idx_row.isdigit():
                result += int(idx_row)
        for idx_col in matrix:
            if idx_col[hit_position[1]].isdigit():
                result += int(idx_col[hit_position[1]])
        add_number = result * 3
        if player_turn == player_one:
            player_one_score -= add_number
        else:
            player_two_score -= add_number


def coordinate_validator(r, c):
    if 0 <= r < SIZE and 0 <= c < SIZE:
        return True


def corresponding_numbers_finder(r, c):
    num1 = board[r][0]
    num2 = board[0][c]
    num3 = board[r][SIZE - 1]
    num4 = board[SIZE - 1][c]
    total = num1 + num2 + num3 + num4
    return total


SIZE = 7

players = input().split(", ")

board = [[int(x) if x.isdigit() else x for x in input().split()] for _ in range(SIZE)]

score_info = {players[0]: [501, 0], players[1]: [501, 0]}
# Ivan: 501(points), 0(throws)

while True:
    row, col = [int(x) for x in input().strip("()").split(", ")]
    current_player = players.pop(0)
    score_info[current_player][1] += 1

    if not coordinate_validator(row, col):
        players.append(current_player)
        continue

    if board[row][col] == "B":
        print(f"{current_player} won the game with {score_info[current_player][1]} throws!")
        break

    if board[row][col] != "D" and board[row][col] != "T":
        score_info[current_player][0] -= board[row][col]

    elif board[row][col] == "D":
        score_info[current_player][0] -= 2 * corresponding_numbers_finder(row, col)

    elif board[row][col] == "T":
        score_info[current_player][0] -= 3 * corresponding_numbers_finder(row, col)

    if score_info[current_player][0] <= 0:
        print(f"{current_player} won the game with {score_info[current_player][1]} throws!")
        break

    players.append(current_player)
