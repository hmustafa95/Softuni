received_list = input().split(' ')
numarized_list = [int(x) for x in received_list]

while True:
    command = input()
    if command == 'end':
        break
    command_list = command.split(' ')
    if command_list[0] == 'swap':
        index_one = int(command_list[1])
        index_two = int(command_list[2])
        numarized_list[index_one], numarized_list[index_two] = numarized_list[index_two], numarized_list[index_one]
    elif command_list[0] == 'multiply':
        index_one = int(command_list[1])
        index_two = int(command_list[2])
        numarized_list[index_one] = numarized_list[index_one] * numarized_list[index_two]
    elif command_list[0] == 'decrease':
        numarized_list = [(x - 1) for x in numarized_list]

print(', '.join([str(x) for x in numarized_list]))
