first_number = int(input())
second_number = int(input())

s1 = first_number // 1000 % 10
s2 = first_number // 100 % 10
s3 = first_number // 10 % 10
s4 = first_number % 10

e1 = second_number // 1000 % 10
e2 = second_number // 100 % 10
e3 = second_number // 10 % 10
e4 = second_number % 10

for number in range(s1, e1 + 1):
    if number % 2 == 0:
        continue
    for number1 in range(s2, e2 + 1):
        if number1 % 2 == 0:
            continue
        for number2 in range(s3, e3 + 1):
            if number2 % 2 == 0:
                continue
            for number3 in range(s4, e4 + 1):
                if number3 % 2 == 0:
                    continue
                print(f'{number}{number1}{number2}{number3}', end= ' ')
