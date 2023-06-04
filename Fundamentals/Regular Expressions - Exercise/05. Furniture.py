import re

regex = r'>>([A-Za-z]+)<<([0-9]+[\.0-9]*)\!([0-9]+)'
total_cost = 0
furniture_bought = []

while True:
    command = input()
    if command == 'Purchase':
        break
    matches = re.search(regex, command)
    if matches:
        furniture = matches.group(1)
        price = matches.group(2)
        quantity = matches.group(3)
        furniture_bought.append(furniture)
        total_cost += int(quantity) * float(price)

print('Bought furniture:')
for current in furniture_bought:
    print(current)
print(f'Total money spend: {total_cost:.2f}')