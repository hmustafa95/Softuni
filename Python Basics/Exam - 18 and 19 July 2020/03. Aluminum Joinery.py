order = int(input())
dimensions = input()
delivery = input()
price = 0
discounted_price = 0

if dimensions == '90X130':
    price = 110
    if 30 <= order < 60:
        price = price * 0.95 * order
    elif 60 <= order:
        price = price * 0.92 * order
    if delivery == 'With delivery':
        price = price + 60
elif dimensions == '100X150':
    price = 140
    if 40 <= order < 80:
        price = price * 0.94 * order
    elif 80 <= order:
        price = price * 0.90 * order
    if delivery == 'With delivery':
        price = price + 60
elif dimensions == '130X180':
    price = 190
    if 20 <= order < 50:
        price = price * 0.93 * order
    elif 50 <= order:
        price = price * 0.88 * order
    if delivery == 'With delivery':
        price = price + 60
elif dimensions == '200X300':
    price = 150
    if 25 <= order < 50:
        price = price * 0.91 * order
    elif 50 <= order:
        price = price * 0.86 * order
    if delivery == 'With delivery':
        price = price + 60

if order < 10:
    print('Invalid order')
elif order > 99:
    discounted_price = price * 0.96
    print(f'{discounted_price:.2f} BGN')
else:
    print(f'{price:.2f} BGN')
