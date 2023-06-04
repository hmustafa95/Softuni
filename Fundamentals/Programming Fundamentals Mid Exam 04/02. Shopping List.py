received_list = input().split('!')

while True:
    command = input()
    if command == 'Go Shopping!':
        break
    command_list = command.split(' ')
    if command_list[0] == 'Urgent':
        if command_list[1] not in received_list:
            received_list.insert(0, command_list[1])
    elif command_list[0] == 'Unnecessary':
        if command_list[1] in received_list:
            received_list.remove(command_list[1])
    elif command_list[0] == 'Correct':
        if command_list[1] in received_list:
            index = received_list.index(command_list[1])
            received_list[index] = command_list[2]
    elif command_list[0] == 'Rearrange':
        if command_list[1] in received_list:
            received_list.remove(command_list[1])
            received_list.append(command_list[1])

print(', '.join(received_list))
