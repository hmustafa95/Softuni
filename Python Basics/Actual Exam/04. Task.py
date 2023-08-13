training_days = int(input())
km_ran_first_day = float(input())
total_ran = 0
total = km_ran_first_day
import math

for number in range(1, training_days + 1):
    increase = int(input())
    km_ran_first_day = km_ran_first_day + km_ran_first_day * (increase / 100)
    total += km_ran_first_day

total_ran = total

if total_ran >= 1000:
    print(f"You've done a great job running {math.ceil(total_ran - 1000)} more kilometers!")
else:
    print(f"Sorry Mrs. Ivanova, you need to run {math.ceil(1000 - total_ran)} more kilometers")
