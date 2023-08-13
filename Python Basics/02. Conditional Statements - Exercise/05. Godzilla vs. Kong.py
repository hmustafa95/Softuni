budget = float(input())
statists = int(input())
decor = budget * 0.10
suit = float(input()) * statists

if statists > 150:
    suit = suit * 0.90
else:
    suit = suit

expenses = decor + suit

money = budget - decor - suit
left_over = abs(money)

if expenses > budget:
    print('Not enough money!')
    print(f'Wingard needs {left_over:.2f} leva more.')
else:
    print('Action!')
    print(f'Wingard starts filming with {left_over:.2f} leva left.')
