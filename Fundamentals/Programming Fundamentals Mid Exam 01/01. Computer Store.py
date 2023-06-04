cost = 0

while True:
    command = input()
    if command == 'special' or command == 'regular':
        break
    price = float(command)
    if price > 0:
        cost += price
    else:
        print('Invalid price!')
        continue

taxes = 0.2 * cost
total_cost = cost + taxes

if command == 'special':
    total_cost = total_cost * 0.90

if total_cost == 0:
    print('Invalid order!')
else:
    print(f"Congratulations you've just bought a new computer!\nPrice without taxes: {cost:.2f}$\nTaxes: {taxes:.2f}$\n-----------\nTotal price: {total_cost:.2f}$")
