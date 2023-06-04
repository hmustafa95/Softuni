spell = input()

while True:
    command = input()
    if command == 'Abracadabra':
        break
    command_list = command.split(' ')
    if command_list[0] == 'Abjuration':
        spell = spell.upper()
        print(spell)
    elif command_list[0] == 'Necromancy':
        spell = spell.lower()
        print(spell)
    elif command_list[0] == 'Illusion':
        illusion_index = int(command_list[1])
        if illusion_index < len(spell):
            spell = spell[:illusion_index] + command_list[2] + spell[(illusion_index + 1):]
            print('Done!')
        else:
            print('The spell was too weak.')
    elif command_list[0] == 'Divination':
        if command_list[1] in spell:
            spell = spell.replace(command_list[1], command_list[2])
            print(spell)
    elif command_list[0] == 'Alteration':
        if command_list[1] in spell:
            spell = spell.replace(command_list[1], '')
            print(spell)
    else:
        print('The spell did not work!')
