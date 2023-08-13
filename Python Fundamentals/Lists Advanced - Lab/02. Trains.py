length = int(input())
result = [0] * length

while True:
    command = input()
    command_list = command.split(" ")
    if command_list[0] == 'add':
        result[-1] += int(command_list[1])
    elif command_list[0] == 'insert':
        given_index = int(command_list[1])
        result[given_index] += int(command_list[2])
    elif command_list[0] == 'leave':
        given_index = int(command_list[1])
        result[given_index] -= int(command_list[2])
        if result[given_index] < int(command_list[2]):
            result[given_index] = 0
    if command == 'End':
        break

print(result)
