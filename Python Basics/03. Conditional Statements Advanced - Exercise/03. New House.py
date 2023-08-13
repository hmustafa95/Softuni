flower = input()
amount = int(input())
budget = int(input())

if flower == 'Roses':
    if amount > 80:
        price = amount * 5 * 0.90
    else:
        price = amount * 5
elif flower == 'Dahlias':
    if amount > 90:
        price = amount * 3.80 * 0.85
    else:
        price = amount * 3.80
elif flower == 'Tulips':
    if amount > 80:
        price = amount * 2.80 * 0.85
    else:
        price = amount * 2.80
elif flower == 'Narcissus':
    if amount < 120:
        price = amount * 3 * 1.15
    else:
        price = amount * 3
elif flower == 'Gladiolus':
    if amount < 80:
        price = amount * 2.50 * 1.20
    else:
        price = amount * 2.50

remaining = budget - price
needed = price - budget

if budget >= price:
    print(f'Hey, you have a great garden with {amount} {flower} and {remaining:.2f} leva left.')
else:
    print(f'Not enough money, you need {needed:.2f} leva more.')
