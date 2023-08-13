word = input()
size = int(input())
matrix = []
player_location = []
input_row = []

for row in range(size):
    line = input()
    for idx in range(len(line)):
        input_row.append(line[idx])
        if 'P' == line[idx]:
            player_location = [row, idx]
    matrix.append(input_row)
    input_row = []

matrix[player_location[0]][player_location[1]] = '-'

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'right': (0, 1),
    'left': (0, -1)
}

steps = int(input())

for step in range(steps):
    direction = input()
    row, col = [
        player_location[0] + directions[direction][0],
        player_location[1] + directions[direction][1]
    ]
    if row < 0:
        row = player_location[0]
        if word:
            word = word[:-1]
        if step == steps - 1:
            matrix[player_location[0]][player_location[1]] = 'P'
        continue
    elif row >= size:
        row = player_location[0]
        if word:
            word = word[:-1]
        if step == steps - 1:
            matrix[player_location[0]][player_location[1]] = 'P'
        continue
    elif col < 0:
        col = player_location[1]
        if word:
            word = word[:-1]
        if step == steps - 1:
            matrix[player_location[0]][player_location[1]] = 'P'
        continue
    elif col >= size:
        col = player_location[1]
        if word:
            word = word[:-1]
        if step == steps - 1:
            matrix[player_location[0]][player_location[1]] = 'P'
        continue
    player_location[0] += directions[direction][0]
    player_location[1] += directions[direction][1]
    if matrix[row][col].isalpha():
        word += matrix[row][col]
        matrix[row][col] = '-'
    if step == steps - 1:
        matrix[player_location[0]][player_location[1]] = 'P'

print(word)
for row in matrix:
    print(*row, sep='')