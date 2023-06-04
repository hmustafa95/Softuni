capacity = int(input())
messenger = {}

while True:
    command = input()
    if command == 'Statistics':
        break
    command_list = command.split('=')
    if command_list[0] == 'Add':
        if command_list[1] not in messenger:
            messenger[command_list[1]] = [int(command_list[2]), int(command_list[3])]
    elif command_list[0] == 'Message':
        if command_list[1] in messenger and command_list[2] in messenger:
            messenger[command_list[1]][0] += 1
            messenger[command_list[2]][1] += 1
            if sum(messenger[command_list[1]]) >= capacity:
                print(f'{command_list[1]} reached the capacity!')
                del messenger[command_list[1]]
            if sum(messenger[command_list[2]]) >= capacity:
                print(f'{command_list[2]} reached the capacity!')
                del messenger[command_list[2]]
    elif command_list[0] == 'Empty':
        if command_list[1] == 'All':
            messenger.clear()
        elif command_list[1] in messenger:
            del messenger[command_list[1]]

print(f'Users count: {len(messenger)}')
for index in messenger.keys():
    sum_messages = sum(messenger[index])
    print(f'{index} - {sum_messages}')