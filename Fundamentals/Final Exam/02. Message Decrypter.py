import re

number = int(input())
regex = r'^([\$|\%])([A-Z][a-z][a-z]+)\1[\:][\ ]([\[][0-9]+[\]][\|][\[][0-9]+[\]][\|][\[][0-9]+[\]][\|])$'

for index in range(number):
    command = input()
    matches = re.search(regex, command)
    if matches:
        request = matches.group(2)
        listed_numbers = matches.group(3)
        the_list = listed_numbers.split('|')
        actual_list = []
        for current_index in the_list:
            current_index = current_index.replace('[', '')
            current_index = current_index.replace(']', '')
            actual_list.append(current_index)
        name = ''
        for current_number in actual_list[:-1]:
            name += chr(int(current_number))
        print(f'{request}: {name}')
    else:
        print('Valid message not found!')
