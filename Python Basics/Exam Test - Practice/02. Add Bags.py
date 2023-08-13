price_luggage_over_20 = float(input())
luggage_weight = float(input())
days_until_travel = int(input())
number_luggages = int(input())
price = 0
total_price = 0

if luggage_weight < 10:
    price = price_luggage_over_20 * 0.20
elif 10 <= luggage_weight <= 20:
    price = price_luggage_over_20 * 0.50
elif 20 < luggage_weight:
    price = price_luggage_over_20

if days_until_travel > 30:
    total_price = price * 1.10
elif 7 <= days_until_travel <= 30:
    total_price = price * 1.15
else:
    total_price = price * 1.40

all_price = total_price * number_luggages

print(f'The total price of bags is: {all_price:.2f} lv.')
