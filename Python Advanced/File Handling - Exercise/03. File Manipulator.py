import os

while True:
    command = input().split('-')
    if command[0] == 'End':
        break

    if command[0] == 'Create':
        file = open(f'file/{command[1]}', 'w')
        file.close()

    elif command[0] == 'Add':
        with open(f"files/{command[1]}", 'a') as file:
            file.write(command[2])

    elif command[0] == 'Replace':
        try:
            with open(f"files/{command[1]}", 'r') as file:
                text = file.readlines()

            file = open(f'files/{command[1]}', 'w')
            for i in range(len(text)):
                text[i] = text[i].replace(command[2], command[3])
            file.write(''.join(text))
            file.close()
        except FileNotFoundError:
            print('File not found')

    elif command[0] == 'Delete':
        try:
            os.remove(f'files/{command[1]}')
        except FileNotFoundError:
            print('File not found')
