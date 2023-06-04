length = int(input())
result = [0] * length

while True:
    command = input()
    if command == 'End':
        break
    command_list = command.split(' ')
    if command_list[0] == 'add':
        result[-1] += int(command_list[1])
    elif command_list[0] == 'insert':
        index = int(command_list[1])
        result[index] += int(command_list[2])
    elif command_list[0] == 'leave':
        index = int(command_list[1])
        result[index] -= int(command_list[2])
        if result[index] < 0:
            result[index] = 0

print(result)
