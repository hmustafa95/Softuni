days = int(input())
rent = input()
opinion = input()

nights = days - 1
price = 0

if rent == 'room for one person':
    price = 18
elif rent == 'apartment':
    if nights < 10:
        price = 25 * 0.70
    elif 10 <= nights <= 15:
        price = 25 * 0.65
    else:
        price = 25 * 0.50
elif rent == 'president apartment':
    if nights < 10:
        price = 35 * 0.90
    elif 10 <= nights <= 15:
        price = 35 * 0.85
    else:
        price = 35 * 0.80

if opinion == 'positive':
    total = price * 1.25 * nights
elif opinion == 'negative':
    total = price * 0.90 * nights

print(f'{total:.2f}')
