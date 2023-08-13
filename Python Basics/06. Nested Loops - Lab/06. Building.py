floors_number = int(input())
rooms_number = int(input())

for f in range(floors_number, 0, -1):
    for r in range(rooms_number):
        if f == floors_number:
            print(f'L{f}{r}', end=" ")
        elif f % 2 == 0:
            print(f'O{f}{r}', end=" ")
        else:
            print(f'A{f}{r}', end=" ")
    print()
