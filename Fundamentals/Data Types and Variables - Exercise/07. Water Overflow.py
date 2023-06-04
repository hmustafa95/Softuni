capacity = 0
number_lines = int(input())

for digit in range(1, number_lines + 1):
    liters_water = int(input())
    capacity += liters_water
    if capacity > 255:
        capacity -= liters_water
        print('Insufficient capacity!')

print(capacity)
