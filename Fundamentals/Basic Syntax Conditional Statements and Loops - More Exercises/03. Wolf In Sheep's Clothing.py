command = input()
list_commands = command.split(", ")
counter = 0
counter_index = 0

for other_index in list_commands:
    counter_index += 1

for current_index in list_commands:
    counter += 1
    if current_index == 'wolf' and counter == counter_index:
        print('Please go away and stop eating my sheep')
    elif current_index == 'wolf':
        print(f'Oi! Sheep number {(counter_index - counter)}! You are about to be eaten by a wolf!')
