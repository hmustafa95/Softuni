number = int(input())
heroes = {}

for index in range(number):
    command = input().split(' ')
    heroes[command[0]] = [int(command[1]), int(command[2])]

while True:
    action = input()
    if action == 'End':
        break
    list_action = action.split(' - ')
    if list_action[0] == 'CastSpell':
        mp_needed = int(list_action[2])
        mp_available = heroes[list_action[1]][1]
        if mp_available >= mp_needed:
            mana_left = mp_available - mp_needed
            print(f'{list_action[1]} has successfully cast {list_action[3]} and now has {mana_left} MP!')
            heroes[list_action[1]][1] = mana_left
        else:
            print(f'{list_action[1]} does not have enough MP to cast {list_action[3]}!')
    elif list_action[0] == 'TakeDamage':
        damage_received = int(list_action[2])
        hp = heroes[list_action[1]][0]
        hp_left = hp - damage_received
        if hp_left > 0:
            heroes[list_action[1]][0] = hp_left
            print(f'{list_action[1]} was hit for {damage_received} HP by {list_action[3]} and now has {hp_left} HP left!')
        else:
            print(f'{list_action[1]} has been killed by {list_action[3]}!')
            heroes.pop(list_action[1])
    elif list_action[0] == 'Recharge':
        mp_recharged = int(list_action[2])
        mp_available = heroes[list_action[1]][1]
        if (mp_recharged + mp_available) > 200:
            amount_recharged = 200 - mp_available
            heroes[list_action[1]][1] = 200
            print(f'{list_action[1]} recharged for {amount_recharged} MP!')
        else:
            total_mp = mp_available + mp_recharged
            heroes[list_action[1]][1] = total_mp
            print(f'{list_action[1]} recharged for {mp_recharged} MP!')
    elif list_action[0] == 'Heal':
        heal_amount = int(list_action[2])
        hp_available = heroes[list_action[1]][0]
        if (hp_available + heal_amount) > 100:
            amount_healed = 100 - hp_available
            heroes[list_action[1]][0] = 100
            print(f'{list_action[1]} healed for {amount_healed} HP!')
        else:
            total_hp = hp_available + heal_amount
            heroes[list_action[1]][0] = total_hp
            print(f'{list_action[1]} healed for {heal_amount} HP!')

for current_index in heroes.keys():
    for status in range(0, len(heroes[current_index]), 2):
        the_list = heroes[current_index]
        hp = the_list[status]
        mp = the_list[status + 1]
        print(f'{current_index}')
        print(f'  HP: {hp}')
        print(f'  MP: {mp}')
