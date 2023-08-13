import math

record = float(input())
distance = float(input())
time = float(input())

target = distance * time
bonus = distance / 15
bonus = math.floor(bonus)
bonus_time = bonus * 12.5

total_time = target + bonus_time
left_over = total_time - record

if total_time < record:
    print(f'Yes, he succeeded! The new world record is {total_time:.2f} seconds.')
else:
    print(f'No, he failed! He was {left_over:.2f} seconds slower.')
