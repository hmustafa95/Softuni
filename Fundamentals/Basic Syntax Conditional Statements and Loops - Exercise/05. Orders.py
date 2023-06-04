number_of_orders = int(input())
price_order = 0
total_price = 0
price_capsule = 0
days = 0
needed_capsules = 0

for smth in range(1, number_of_orders + 1):
    price_capsule = float(input())
    days = int(input())
    needed_capsules = int(input())
    if 0.01 > price_capsule or price_capsule > 100:
        continue
    elif days < 1 or days > 31:
        continue
    elif needed_capsules < 1 or needed_capsules > 2000:
        continue
    price_order = price_capsule * days * needed_capsules
    print(f'The price for the coffee is: ${price_order:.2f}')
    total_price += price_order

print(f'Total: ${total_price:.2f}')
