people = int(input())
season = input()
price = 0
total_amount = 0

if people <= 5 and season == 'spring':
    price = 50
    total_amount = people * price
elif people > 5 and season == 'spring':
    price = 48
    total_amount = people * price
elif people <= 5 and season == 'summer':
    price = 48.50
    total_amount = people * price * 0.85
elif people > 5 and season == 'summer':
    price = 45
    total_amount = people * price * 0.85
elif people <= 5 and season == 'autumn':
    price = 60
    total_amount = people * price
elif people > 5 and season == 'autumn':
    price = 49.50
    total_amount = people * price
elif people <= 5 and season == 'winter':
    price = 86
    total_amount = people * price * 1.08
elif people > 5 and season == 'winter':
    price = 85
    total_amount = people * price * 1.08

print(f'{total_amount:.2f} leva.')