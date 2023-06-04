number = int(input())
compositions = {}

for index in range(number):
    command = input().split('|')
    compositions[command[0]] = [command[1], command[2]]

while True:
    task = input()
    if task == 'Stop':
        break
    command_list = task.split('|')
    if command_list[0] == 'Add':
        if command_list[1] not in compositions:
            compositions[command_list[1]] = [command_list[2], command_list[3]]
            print(f"{command_list[1]} by {command_list[2]} in {command_list[3]} added to the collection!")
        else:
            print(f"{command_list[1]} is already in the collection!")
    elif command_list[0] == 'Remove':
        if command_list[1] not in compositions:
            print(f"Invalid operation! {command_list[1]} does not exist in the collection.")
        else:
            print(f"Successfully removed {command_list[1]}!")
            del compositions[command_list[1]]
    elif command_list[0] == 'ChangeKey':
        if command_list[1] not in compositions:
            print(f"Invalid operation! {command_list[1]} does not exist in the collection.")
        else:
            print(f"Changed the key of {command_list[1]} to {command_list[2]}!")
            the_list = compositions[command_list[1]]
            the_list[1] = command_list[2]

for current_index in compositions.keys():
    for index in range(0, len(compositions[current_index]), 2):
        the_list = compositions[current_index]
        key = the_list[index + 1]
        comp = the_list[index]
        print(f"{current_index} -> Composer: {comp}, Key: {key}")
