record_seconds = float(input())
distance_meters = float(input())
speed = float(input())
import math

time_one = distance_meters * speed
slow_down_faggotery = math.floor(distance_meters / 50) * 30
total_time = time_one + slow_down_faggotery
gay_time = abs(record_seconds - total_time)

if total_time < record_seconds:
    print(f'Yes! The new record is {total_time:.2f} seconds.')
else:
    print(f'No! He was {gay_time:.2f} seconds slower.')
