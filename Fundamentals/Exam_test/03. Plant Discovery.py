number = int(input())
plants = {}

for _ in range(number):
    data = input().split('<->')
    plant_name = data[0]
    given_rarity = int(data[1])
    if plant_name not in plants:
        plants[plant_name] = {'rarity': given_rarity, 'rating': []}
    else:
        plants[plant_name]['rarity'] = given_rarity

while True:
    new_line = input()
    if new_line == 'Exhibition':
        break
    tokens = new_line.split(' ')
    command = tokens[0]

    if command == 'Rate:':
        plant = tokens[1]
        new_rating = int(tokens[3])

        if plant in plants:
            plants[plant]['rating'].append(new_rating)
        else:
            print("error")
    elif command == 'Update:':
        plant = tokens[1]
        new_rarity = int(tokens[3])

        if plant in plants:
            plants[plant]['rarity'] = new_rarity
        else:
            print("error")
    elif command == 'Reset:':
        plant = tokens[1]

        if plant in plants:
            plants[plant]['rating'].clear()
        else:
            print("error")

result = "Plants for the exhibition:"

for plant in plants:
    average = 0
    if plants[plant]['rating']:
        average = sum(plants[plant]['rating']) / len(plants[plant]['rating'])
    result += f"\n- {plant}; Rarity: {plants[plant]['rarity']}; Rating: {average:.2f}"

print(result)