towns = {}

while True:
    targets = input()
    if targets == 'Sail':
        break
    targets_list = targets.split('||')
    if targets_list[0] not in towns:
        towns[targets_list[0]] = [int(targets_list[1]), int(targets_list[2])]
    else:
        towns[targets_list[0]][0] += int(targets_list[1])
        towns[targets_list[0]][1] += int(targets_list[2])

while True:
    command = input()
    if command == 'End':
        break
    command_list = command.split('=>')
    if command_list[0] == 'Plunder':
        town = command_list[1]
        people = int(command_list[2])
        gold = int(command_list[3])
        towns[town][0] -= people
        towns[town][1] -= gold
        print(f'{town} plundered! {gold} gold stolen, {people} citizens killed.')
        if towns[town][0] <= 0 or towns[town][1] <= 0:
            print(f'{town} has been wiped off the map!')
            del towns[town]

    elif command_list[0] == 'Prosper':
        town = command_list[1]
        gold = int(command_list[2])
        if gold > 0:
            towns[town][1] += gold
            print(f'{gold} gold added to the city treasury. {town} now has {towns[town][1]} gold.')
        else:
            print('Gold added cannot be a negative number!')

if len(towns) > 0:
    print(f'Ahoy, Captain! There are {len(towns)} wealthy settlements to go to:')
    for index in towns.keys():
        for current in range(0, len(towns[index]), 2):
            the_list = towns[index]
            people = the_list[0]
            gold = the_list[1]
            print(f'{index} -> Population: {people} citizens, Gold: {gold} kg')
else:
    print('Ahoy, Captain! All targets have been plundered and destroyed!')
