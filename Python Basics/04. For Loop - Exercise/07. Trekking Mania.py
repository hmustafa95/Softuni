climbers_groups = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
total_climbers = 0

for something in range(climbers_groups):
    number_climbers = int(input())
    if number_climbers < 6:
        p1 += number_climbers
    elif number_climbers < 13:
        p2 += number_climbers
    elif number_climbers < 26:
        p3 += number_climbers
    elif number_climbers < 41:
        p4 += number_climbers
    else:
        p5 += number_climbers
    total_climbers += number_climbers

print(f'{p1 / total_climbers * 100:.2f}%')
print(f'{p2 / total_climbers * 100:.2f}%')
print(f'{p3 / total_climbers * 100:.2f}%')
print(f'{p4 / total_climbers * 100:.2f}%')
print(f'{p5 / total_climbers * 100:.2f}%')
