footballer = input()
player_name = ''
number_of_goals = 0

while footballer != 'END':
    goals = int(input())
    if goals >= 10:
        number_of_goals = goals
        player_name = footballer
        break
    elif goals > number_of_goals:
        number_of_goals = goals
        player_name = footballer
    footballer = input()

print(f'{player_name} is the best player!')

if goals >= 3:
    print(f'He has scored {number_of_goals} goals and made a hat-trick !!!')
else:
    print(f'He has scored {number_of_goals} goals.')
