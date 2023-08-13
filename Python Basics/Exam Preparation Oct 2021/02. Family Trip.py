budget = float(input())
nights = int(input())
price_per_night = float(input())
additional_spending = int(input())
discount = 0

if nights > 7:
    price_per_night = price_per_night * 0.95

total_price = nights * price_per_night

expenses = budget * additional_spending / 100

all_price = total_price + expenses

diff = abs(all_price - budget)
if budget >= all_price:
    print(f'Ivanovi will be left with {diff:.2f} leva after vacation.')
else:
    print(f'{diff:.2f} leva needed.')
