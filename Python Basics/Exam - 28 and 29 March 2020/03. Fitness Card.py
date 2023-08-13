amount_available = float(input())
sex = input()
age = int(input())
sport = input()
price = 0
discount = 0

if sex == 'm' and sport == 'Gym':
    price = 42
elif sex == 'f' and sport == 'Gym':
    price = 35
elif sex == 'm' and sport == 'Boxing':
    price = 41
elif sex == 'f' and sport == 'Boxing':
    price = 37
elif sex == 'm' and sport == 'Yoga':
    price = 45
elif sex == 'f' and sport == 'Yoga':
    price = 42
elif sex == 'm' and sport == 'Zumba':
    price = 34
elif sex == 'f' and sport == 'Zumba':
    price = 31
elif sex == 'm' and sport == 'Dances':
    price = 51
elif sex == 'f' and sport == 'Dances':
    price = 53
elif sex == 'm' and sport == 'Pilates':
    price = 39
elif sex == 'f' and sport == 'Pilates':
    price = 37

if age <= 19:
    discount = price * 0.20

real_price = price - discount

if amount_available >= real_price:
    print(f'You purchased a 1 month pass for {sport}.')
else:
    needed = real_price - amount_available
    print(f"You don't have enough money! You need ${needed:.2f} more.")