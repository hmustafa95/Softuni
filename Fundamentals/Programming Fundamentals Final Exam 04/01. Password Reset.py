password = input()

while True:
    command = input()
    if command == 'Done':
        break
    command_list = command.split(' ')
    if command_list[0] == 'TakeOdd':
        password = password[1::2]
        print(password)
    elif command_list[0] == 'Cut':
        cut_index = int(command_list[1])
        length = int(command_list[2]) + cut_index
        password = password[:cut_index] + password[length:]
        print(password)
    elif command_list[0] == 'Substitute':
        substring = command_list[1]
        substitute = command_list[2]
        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print('Nothing to replace!')

print(f'Your password is: {password}')