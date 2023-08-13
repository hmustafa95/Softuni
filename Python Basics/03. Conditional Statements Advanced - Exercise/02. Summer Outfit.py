temperature = int(input())
day = input()

if 10 <= temperature <= 18 and day == 'Morning':
    outfit = 'Sweatshirt'
    shoes = 'Sneakers'
    print(f"It's {temperature} degrees, get your {outfit} and {shoes}.")
elif 18 < temperature <= 24 and day == 'Morning':
    outfit = 'Shirt'
    shoes = 'Moccasins'
    print(f"It's {temperature} degrees, get your {outfit} and {shoes}.")
elif 25 <= temperature and day == 'Morning':
    outfit = 'T-Shirt'
    shoes = 'Sandals'
    print(f"It's {temperature} degrees, get your {outfit} and {shoes}.")
elif 10 <= temperature <= 18 and day == 'Afternoon':
    outfit = 'Shirt'
    shoes = 'Moccasins'
    print(f"It's {temperature} degrees, get your {outfit} and {shoes}.")
elif 18 < temperature <= 24 and day == 'Afternoon':
    outfit = 'T-Shirt'
    shoes = 'Sandals'
    print(f"It's {temperature} degrees, get your {outfit} and {shoes}.")
elif 25 <= temperature and day == 'Afternoon':
    outfit = 'Swim Suit'
    shoes = 'Barefoot'
    print(f"It's {temperature} degrees, get your {outfit} and {shoes}.")
if 10 <= temperature <= 18 and day == 'Evening':
    outfit = 'Shirt'
    shoes = 'Moccasins'
    print(f"It's {temperature} degrees, get your {outfit} and {shoes}.")
elif 18 < temperature <= 24 and day == 'Evening':
    outfit = 'Shirt'
    shoes = 'Moccasins'
    print(f"It's {temperature} degrees, get your {outfit} and {shoes}.")
elif 25 <= temperature and day == 'Evening':
    outfit = 'Shirt'
    shoes = 'Moccasins'
    print(f"It's {temperature} degrees, get your {outfit} and {shoes}.")
