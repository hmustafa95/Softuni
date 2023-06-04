message = input()

while True:
    command = input()
    if command == 'Decode':
        break
    command_list = command.split('|')
    if command_list[0] == 'Move':
        index = int(command_list[1])
        message = message[index:] + message[0:index]
    elif command_list[0] == 'Insert':
        insert_index = int(command_list[1])
        message = message[:insert_index] + command_list[2] + message[insert_index:]
    elif command_list[0] == 'ChangeAll':
        for char in message:
            if char == command_list[1]:
                message = message.replace(command_list[1], command_list[2])

print(f"The decrypted message is: {message}")