first_employee = int(input())
second_employee = int(input())
third_employee = int(input())
students_count = int(input())
hours = 0
total_per_hour = first_employee + second_employee + third_employee

while True:
    hours += 1
    if hours % 4 == 0:
        continue
    students_count -= total_per_hour
    if students_count <= 0:
        print(f'Time needed: {hours}h.')
        break
