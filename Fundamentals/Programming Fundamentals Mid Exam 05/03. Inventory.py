received_list = input().split(', ')

while True:
    command = input()
    if command == 'Craft!':
        break
    command_list = command.split(' - ')
    if command_list[0] == 'Collect':
        if command_list[1] not in received_list:
            received_list.append(command_list[1])
    elif command_list[0] == 'Drop':
        if command_list[1] in received_list:
            received_list.remove(command_list[1])
    elif command_list[0] == 'Combine Items':
        split_items = command_list[1].split(':')
        if split_items[0] in received_list:
            received_list.insert((received_list.index(split_items[0]) + 1), split_items[1])
    elif command_list[0] == 'Renew':
        if command_list[1] in received_list:
            received_list.remove(command_list[1])
            received_list.append(command_list[1])

print(', '.join(received_list))
