sentence = input()

while True:
    command = input()
    if command == 'Generate':
        break
    command_list = command.split('>>>')
    action = command_list[0]
    if action == 'Contains':
        substring = command_list[1]
        if substring in sentence:
            print(f'{sentence} contains {substring}')
        else:
            print('Substring not found!')
    elif action == 'Flip':
        start_index = int(command_list[2])
        end_index = int(command_list[3])
        if sentence[start_index:end_index].isupper():
            sentence = sentence[:start_index] + sentence[start_index:end_index].lower() + sentence[end_index:]
            print(sentence)
        elif sentence[start_index:end_index].islower():
            sentence = sentence[:start_index] + sentence[start_index:end_index].upper() + sentence[end_index:]
            print(sentence)
    elif action == 'Slice':
        start_index = int(command_list[1])
        end_index = int(command_list[2])
        sentence = sentence[:start_index] + sentence[end_index:]
        print(sentence)

print(f'Your activation key is: {sentence}')

#variant 2
key = input()

while True:
    command = input().split('>>>')
    current_command = command[0]

    if current_command == 'Generate':
        print(f"Your activation key is: {key}")
        break

    elif current_command == 'Slice':
        key = key[:int(command[1])] + key[int(command[2]):]
        print(key)

    elif current_command == 'Flip':
        if command[1] == 'Upper':
            key = key[:int(command[2])] + key[int(command[2]):int(command[3])].upper() + key[int(command[3]):]
        else:
            key = key[:int(command[2])] + key[int(command[2]):int(command[3])].lower() + key[int(command[3]):]

        print(key)

    elif current_command == 'Contains':
        substring = command[1]
        if substring in key:
            print(f"{key} contains {substring}")
        else:
            print(f"Substring not found!")