number_cars = int(input())
cars = {}

for index in range(number_cars):
    cars_listed = input().split('|')
    cars[cars_listed[0]] = [int(cars_listed[1]), int(cars_listed[2])]

while True:
    command = input()
    if command == 'Stop':
        break
    command_list = command.split(' : ')
    if command_list[0] == 'Drive':
        if cars[command_list[1]][1] >= int(command_list[3]):
            cars[command_list[1]][0] += int(command_list[2])
            cars[command_list[1]][1] -= int(command_list[3])
            print(f'{command_list[1]} driven for {command_list[2]} kilometers. {command_list[3]} liters of fuel consumed.')
            if cars[command_list[1]][0] >= 100000:
                cars.pop(command_list[1])
                print(f'Time to sell the {command_list[1]}!')
        else:
            print('Not enough fuel to make that ride')
    elif command_list[0] == 'Refuel':
        if int(command_list[2]) >= 75:
            refuel = 75
            current_gas = cars[command_list[1]][1]
            needed_gas = 75 - current_gas
            cars[command_list[1]][1] = 75
            print(f'{command_list[1]} refueled with {needed_gas} liters')
        else:
            refuel = int(command_list[2])
            if (refuel + cars[command_list[1]][1]) < 75:
                cars[command_list[1]][1] += refuel
                print(f'{command_list[1]} refueled with {refuel} liters')
            else:
                refueled = 75 - cars[command_list[1]][1]
                cars[command_list[1]][1] = 75
                print(f'{command_list[1]} refueled with {refueled} liters')
    elif command_list[0] == 'Revert':
        result = cars[command_list[1]][0] - int(command_list[2])
        if result < 10000:
            cars[command_list[1]][0] = 10000
        else:
            cars[command_list[1]][0] -= int(command_list[2])
            print(f'{command_list[1]} mileage decreased by {command_list[2]} kilometers')

for current_index in cars.keys():
    for index in range(0, len(cars[current_index]), 2):
        the_list = cars[current_index]
        mileage = the_list[0]
        fuel = the_list[1]
        print(f"{current_index} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt.")
