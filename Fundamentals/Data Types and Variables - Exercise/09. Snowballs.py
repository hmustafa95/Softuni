number_of_snowballs = int(input())
max_weight = 0
max_time_needed = 0
max_quality = 0
max_result = 0

for digit in range(1, number_of_snowballs + 1):
    weight = int(input())
    time_needed = int(input())
    quality = int(input())
    current_snowball_result = (weight / time_needed) ** quality
    if current_snowball_result > max_result:
        max_weight = weight
        max_time_needed = time_needed
        max_quality = quality
        max_result = current_snowball_result

print(f'{max_weight} : {max_time_needed} = {max_result:.0f} ({max_quality})')
