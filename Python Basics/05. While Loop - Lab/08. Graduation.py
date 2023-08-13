name = input()
grades = 1.0
sum_grades = 0.0
excluded = 0

while grades <= 12:
    grade = float(input())
    if grade < 4.00:
        excluded += 1
        if excluded > 1:
            break
        continue
    sum_grades += grade
    grades += 1

average = sum_grades / 12

if excluded > 1:
    print(f'{name} has been excluded at {grades:.0f} grade')
else:
    print(f'{name} graduated. Average grade: {average:.2f}')
