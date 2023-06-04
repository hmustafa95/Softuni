travel_route = input()

while True:
    command = input()
    if command == 'Travel':
        print(f'Ready for world tour! Planned stops: {travel_route}')
        break
    command_list = command.split(':')
    if command_list[0] == 'Add Stop':
        index = int(command_list[1])
        if len(travel_route) >= index >= 0:
            travel_route = travel_route[:index] + command_list[2] + travel_route[index:]
        print(travel_route)
    elif command_list[0] == 'Remove Stop':
        start = int(command_list[1])
        end = int(command_list[2])
        if 0 <= start <= len(travel_route) and 0 <= end <= len(travel_route):
            actual_end = end + 1
            travel_route = travel_route[:start] + travel_route[actual_end:]
        print(travel_route)
    elif command_list[0] == 'Switch':
        while command_list[1] in travel_route:
            travel_route = travel_route.replace(command_list[1], command_list[2])
        print(travel_route)
