from collections import deque

seats = input().split(', ')
first = deque(map(str, input().split(', ')))
second = list(map(str, input().split(', ')))
taken = []
rotations = 0
matches = 0

while matches < 3 and rotations < 10:
    rotations += 1
    first_number = first.popleft()
    second_number = second.pop()
    result = chr(int(first_number) + int(second_number))
    for seat in seats:
        if (first_number + result) == seat or (second_number + result) == seat:
            if seat not in taken:
                matches += 1
                taken.append(seat)
    else:
        first.append(first_number)
        second.insert(0, second_number)


print(f"Seat matches: {', '.join(taken)}")
print(f"Rotations count: {rotations}")