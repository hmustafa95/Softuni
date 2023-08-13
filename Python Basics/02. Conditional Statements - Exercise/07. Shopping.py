videocard = 250

budget = float(input())
sum_videocard = int(input())
sum_processor = int(input())
sum_ram = int(input())

price_videocard = videocard * sum_videocard
price_processor = price_videocard * sum_processor * 0.35
price_ram = price_videocard * sum_ram * 0.10

total_price = price_ram + price_processor + price_videocard

if sum_videocard > sum_processor:
    total_price = total_price * 0.85
else:
    total_price = total_price

result = budget - total_price
needed_amount = abs(result)

if budget >= total_price:
    print(f'You have {result:.2f} leva left!')
else:
    print(f'Not enough money! You need {needed_amount:.2f} leva more!')
