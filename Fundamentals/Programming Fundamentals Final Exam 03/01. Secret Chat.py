message = input()

while True:
    command = input()
    if command == 'Reveal':
        break
    command_list = command.split(':|:')
    if command_list[0] == 'InsertSpace':
        insert_index = int(command_list[1])
        message = message[:insert_index] + ' ' + message[insert_index:]
        print(message)
    elif command_list[0] == 'Reverse':
        if command_list[1] in message:
            reverse_index = message.index(command_list[1])
            message = message[:reverse_index] + message[reverse_index + len(command_list[1]):] + command_list[1][::-1]
            print(message)
        else:
            print('error')
    elif command_list[0] == 'ChangeAll':
        message = message.replace(command_list[1], command_list[2])
        print(message)
print(f'You have a new text message: {message}')
