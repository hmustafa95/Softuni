budget = float(input())
season = input()
destination = ''
type_vacation = ''
amount = 0

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        amount = budget * 0.30
        type_vacation = 'Camp'
    elif season == 'winter':
        amount = budget * 0.70
        type_vacation = 'Hotel'
elif 100 < budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        amount = budget * 0.40
        type_vacation = 'Camp'
    elif season == 'winter':
        amount = budget * 0.80
        type_vacation = 'Hotel'
elif 1000 < budget:
    destination = 'Europe'
    amount = budget * 0.90
    type_vacation = 'Hotel'

print(f'Somewhere in {destination}')
print(f'{type_vacation} - {amount:.2f}')
