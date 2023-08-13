minutes = int(input())
walks = int(input())
calories = int(input())

burnt_calories = minutes * 5 * walks

if burnt_calories >= 0.50 * calories:
    print(f'Yes, the walk for your cat is enough. Burned calories per day: {burnt_calories}.')
else:
    print(f'No, the walk for your cat is not enough. Burned calories per day: {burnt_calories}.')
