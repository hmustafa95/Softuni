fruit = input()
size = input()
order = int(input())
price = 0
price_order = 0
discount = 0

if fruit == 'Watermelon' and size == 'small':
        price = 56 * 2
        price_order = price * order
elif fruit == 'Watermelon' and size == 'big':
        price = 28.70 * 5
        price_order = price * order
elif fruit == 'Mango' and size == 'small':
        price = 36.66 * 2
        price_order = price * order
elif fruit == 'Mango' and size == 'big':
        price = 19.60 * 5
        price_order = price * order
elif fruit == 'Pineapple' and size == 'small':
        price = 42.10 * 2
        price_order = price * order
elif fruit == 'Pineapple' and size == 'big':
        price = 24.80 * 5
        price_order = price * order
elif fruit == 'Raspberry' and size == 'small':
        price = 20 * 2
        price_order = price * order
elif fruit == 'Raspberry' and size == 'big':
        price = 15.20 * 5
        price_order = price * order

if 400 <= price_order <= 1000:
    discount = price_order * 0.15
elif 1000 < price_order:
    discount = price_order * 0.50

total_price = price_order - discount
print(f'{total_price:.2f} lv.')