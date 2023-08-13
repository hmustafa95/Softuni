size = 6
matrix = []

for _ in range(size):
    matrix.append(input().split())

position = [int(x) for x in input().strip('(').strip(')').split(', ')]

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

while True:
    command = input()
    if command == 'Stop':
        break
    command_list = command.split(', ')
    action = command_list[0]
    direction = command_list[1]
    row, col = [
        position[0] + directions[direction][0],
        position[1] + directions[direction][1]
    ]
    position[0] += directions[direction][0]
    position[1] += directions[direction][1]
    if action == 'Create':
        if matrix[row][col] == '.':
            matrix[row][col] = command_list[2]
    elif action == 'Update':
        if matrix[row][col] != '.':
            matrix[row][col] = command_list[2]
    elif action == 'Delete':
        if matrix[row][col] != '.':
            matrix[row][col] = '.'
    elif action == 'Read':
        if matrix[row][col] != '.':
            print(matrix[row][col])

for row in matrix:
    print(*row, sep=' ')