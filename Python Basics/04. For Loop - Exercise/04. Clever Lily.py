age = int(input())
price_washer = float(input())
price_toy = int(input())
money = 0
sum_toy = 0
birthday_money = 0

for current_age in range(1, age + 1):
    if current_age % 2 != 0:
        sum_toy += 1
    else:
        birthday_money += 10
        money += birthday_money - 1
money += sum_toy * price_toy
difference = abs(price_washer - money)
if money >= price_washer:
    print(f'Yes! {difference:.2f}')
else:
    print(f'No! {difference:.2f}')
