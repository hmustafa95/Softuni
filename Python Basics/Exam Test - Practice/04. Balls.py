number = int(input())
total_points = 0
red_balls = 0
orange_balls = 0
yellow_balls = 0
white_balls = 0
other_color = 0
divides_black = 0
import math

for something in range(1, number + 1):
    colors = input()
    if colors == 'red':
        total_points += 5
        red_balls += 1
    elif colors == 'orange':
        total_points += 10
        orange_balls += 1
    elif colors == 'yellow':
        total_points += 15
        yellow_balls += 1
    elif colors == 'white':
        total_points += 20
        white_balls += 1
    elif colors == 'black':
        total_points /= 2
        total_points = math.floor(total_points)
        divides_black += 1
    else:
        other_color += 1

print(f"Total points: {total_points}")
print(f"Red balls: {red_balls}")
print(f"Orange balls: {orange_balls}")
print(f"Yellow balls: {yellow_balls}")
print(f"White balls: {white_balls}")
print(f"Other colors picked: {other_color}")
print(f"Divides from black balls: {divides_black}")
