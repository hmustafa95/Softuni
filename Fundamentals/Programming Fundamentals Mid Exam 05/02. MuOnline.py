health = 100
bitcoins = 0
dungeons = input().split('|')
number_room = 0

for current_index in dungeons:
    number_room += 1
    command_list = current_index.split(' ')
    if command_list[0] == 'potion':
        if (int(command_list[1]) + health) <= 100:
            health += int(command_list[1])
            print(f'You healed for {command_list[1]} hp.')
            print(f'Current health: {health} hp.')
        else:
            print(f'You healed for {(100 - health)} hp.')
            health = 100
            print(f'Current health: {health} hp.')
    elif command_list[0] == 'chest':
        bitcoins += int(command_list[1])
        print(f'You found {command_list[1]} bitcoins.')
    else:
        health -= int(command_list[1])
        if health > 0:
            print(f'You slayed {command_list[0]}.')
        else:
            print(f'You died! Killed by {command_list[0]}.')
            print(f'Best room: {number_room}')
            break

if number_room == len(dungeons) and health > 0:
    print(f"You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")
