orders = {}
prices = {}
result = {}

while True:
    command = input()
    if command == 'buy':
        break
    command_list = command.split(' ')
    name = command_list[0]
    price = float(command_list[1])
    quantity = int(command_list[2])
    if name not in orders:
        orders[name] = 0
    orders[name] += quantity
    if name not in prices:
        prices[name] = 0
    prices[name] = price

for index in orders.keys():
    for current_index in prices.keys():
        if index == current_index:
            total_price = orders[index] * prices[current_index]
            if index not in result:
                result[index] = 0
            result[index] += total_price

for key, value in result.items():
    print(f"{key} -> {value:.2f}")
