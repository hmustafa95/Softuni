projection = input()
column = int(input())
row = int(input())

if projection == 'Premiere':
    income = row * column * 12
    print(f'{income:.2f}')
elif projection == 'Normal':
    income = row * column * 7.50
    print(f'{income:.2f}')
elif projection == 'Discount':
    income = row * column * 5
    print(f'{income:.2f}')
