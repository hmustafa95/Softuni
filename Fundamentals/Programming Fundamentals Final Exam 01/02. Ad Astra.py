import re

given_string = input()
regex = r'([\#|\|])([A-Za-z\ ]+)\1([0-9]{2}\/[0-9]{2}\/[0-9]{2})\1([0-9]+)\1'
matches = re.finditer(regex, given_string)
total_calories = 0
food_list = []

for match in matches:
    food = match.group(2)
    food_list.append(food)
    date = match.group(3)
    food_list.append(date)
    calories = match.group(4)
    food_list.append(calories)
    total_calories += int(calories)

days_lasted = total_calories // 2000
print(f'You have food to last you for: {days_lasted} days!')
for current_index in range(0, len(food_list), 3):
    item = food_list[current_index]
    expire = food_list[current_index + 1]
    fats = food_list[current_index + 2]
    print(f'Item: {item}, Best before: {expire}, Nutrition: {fats}')
