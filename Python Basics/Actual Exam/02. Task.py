days_missing = int(input())
left_food = int(input())
one_raindeer_food = float(input())
two_raindeer_food = float(input())
three_raindeer_food = float(input())

first_food = days_missing * one_raindeer_food
second_food = days_missing * two_raindeer_food
third_food = days_missing * three_raindeer_food

total_needed = first_food + second_food + third_food

difference = abs(left_food - total_needed)
import math

if left_food >= total_needed:
    print(f'{math.floor(difference)} kilos of food left.')
else:
    print(f'{math.ceil(difference)} more kilos of food are needed.')
