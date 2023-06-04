force = {}

while True:
    command = input()
    if command == 'Lumpawaroo':
        break
    if '|' in command:
        force_side, user_force = command.split(' | ')
        if user_force not in force:
            if force_side not in force:
                force[force_side] = []
            force[force_side] += [user_force]
        else:
            continue
    else:
        force_side, user_force = command.split(' -> ')
        for key, value in force.items():
            if user_force not in force:
                if force_side not in force:
                    force[force_side] = []
                force[force_side] += [user_force]
            else:
                force[force_side].pop(value.index(user_force))

print(force)