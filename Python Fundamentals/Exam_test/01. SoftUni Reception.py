first_employee = int(input())
second_employee = int(input())
third_employee = int(input())
students_count = int(input())
time = 0

total_efficiency = first_employee + second_employee + third_employee

while students_count > 0:
    time += 1
    if time % 4 == 0:
        continue
    students_count -= total_efficiency

print(f"Time needed: {time}h.")