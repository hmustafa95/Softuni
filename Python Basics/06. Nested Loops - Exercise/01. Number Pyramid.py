number = int(input())
counter = 1
statement = False

for row in range(1, number + 1):
    for column in range(1, row + 1):
        if counter > number:
            statement = True
            break
        print(str(counter) + ' ', end='')
        counter += 1
    if statement:
        break
    print()
