number = int(input())

for smth in range(1, number + 1):
    current_number = int(input())
    if current_number == 88:
        print('Hello')
    elif current_number == 86:
        print('How are you?')
    elif current_number < 88 and current_number != 86:
        print('GREAT!')
    elif current_number > 88:
        print('Bye.')
