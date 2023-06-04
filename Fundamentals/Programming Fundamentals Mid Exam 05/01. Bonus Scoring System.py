import math

students_number = int(input())
lectures_number = int(input())
add_bonus = int(input())
bonus_counter = []
attendance_list = []

for current_student in range(1, students_number + 1):
    attendance_count = int(input())
    total_bonus = attendance_count / lectures_number * (5 + add_bonus)
    bonus_counter.append(total_bonus)
    attendance_list.append(attendance_count)

result_bonus = max(bonus_counter)
result_attendance = max(attendance_list)

if students_number != 0:
    print(f"Max Bonus: {math.ceil(result_bonus)}.")
    print(f"The student has attended {result_attendance} lectures.")
else:
    print(f"Max Bonus: 0.")
    print(f"The student has attended 0 lectures.")
