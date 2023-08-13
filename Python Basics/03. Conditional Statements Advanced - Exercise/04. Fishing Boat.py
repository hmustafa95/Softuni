budget = int(input())
season = input()
fishers = int(input())

# Need to check which season
# Need to check how many people
# if people are even there's additional discount except in the autumn

if season == 'Spring':
    price = 3000
elif season == 'Summer' or season == 'Autumn':
    price = 4200
elif season == 'Winter':
    price = 2600

if fishers <= 6:
    discount = price * 0.90
elif 7 < fishers <= 11:
    discount = price * 0.85
else:
    discount = price * 0.75

if fishers % 2 == 0 and season != 'Autumn':
    discount = discount * 0.95
else:
    discount = discount

remaining = budget - discount
needed = discount - budget

if budget >= discount:
    print(f'Yes! You have {remaining:.2f} leva left.')
else:
    print(f'Not enough money! You need {needed:.2f} leva.')
