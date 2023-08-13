fruit = input()
day = input()
quantity = float(input())
price = 0

if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday':
    day = str('Weekday')
elif day == 'Saturday' or day == 'Sunday':
    day = str('Weekend')
else:
    day = str('nope')

if fruit == 'banana' and day == str('Weekday'):
    price = 2.50
elif fruit == 'banana' and day == str('Weekend'):
    price = 2.70
elif fruit == 'apple' and day == str('Weekday'):
    price = 1.20
elif fruit == 'apple' and day == str('Weekend'):
    price = 1.25
elif fruit == 'orange' and day == str('Weekday'):
    price = 0.85
elif fruit == 'orange' and day == str('Weekend'):
    price = 0.90
elif fruit == 'grapefruit' and day == str('Weekday'):
    price = 1.45
elif fruit == 'grapefruit' and day == str('Weekend'):
    price = 1.60
elif fruit == 'kiwi' and day == str('Weekday'):
    price = 2.70
elif fruit == 'kiwi' and day == str('Weekend'):
    price = 3.00
elif fruit == 'pineapple' and day == str('Weekday'):
    price = 5.50
elif fruit == 'pineapple' and day == str('Weekend'):
    price = 5.60
elif fruit == 'grapes' and day == str('Weekday'):
    price = 3.85
elif fruit == 'grapes' and day == str('Weekend'):
    price = 4.20
else:
    fruit = str('not')

total = quantity * price

if day != str('nope') and fruit != str('not'):
    print(f'{total:.2f}')
else:
    print('error')
