first_player = int(input())
second_player = int(input())
line_input = input()

while line_input != 'End of battle':
    if line_input == 'one':
        second_player = second_player - 1
    elif line_input == 'two':
        first_player = first_player - 1

    if first_player == 0 or second_player == 0:
        break
    line_input = input()

if first_player == 0:
    print(f'Player one is out of eggs. Player two has {second_player} eggs left.')
elif second_player == 0:
    print(f'Player two is out of eggs. Player one has {first_player} eggs left.')
else:
    print(f'Player one has {first_player} eggs left.')
    print(f'Player one has {second_player} eggs left.')
