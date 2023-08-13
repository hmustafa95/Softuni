import math

time_first = int(input())
time_second = int(input()) + 15

minutes = time_second % 60

time_first = math.floor(time_first)
bonus = 0

if time_second >= 60:
    bonus = 1

hours = time_first + bonus

if hours <= 23:
    hours = hours
else:
    hours = hours - 24

if minutes < 10:
    print(f'{hours}:0{minutes}')
else:
    print(f'{hours}:{minutes}')
