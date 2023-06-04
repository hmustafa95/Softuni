size = int(input())

for row in range(1, size + 1):
    print(' ' * (size - row), end='')
    print('* ' * row)

for row in range(size - 1, - 1, - 1):
    print(' ' * (size - row), end='')
    print('* ' * row)