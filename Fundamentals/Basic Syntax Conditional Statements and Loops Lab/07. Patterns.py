number = int(input())

for num in range(1, number + 1):
    for onum in range(0, num):
        print('*', end='')
    print()

for num in range(number -1, 0, -1):
    for onum in range(0, num):
        print('*', end='')
    print()
