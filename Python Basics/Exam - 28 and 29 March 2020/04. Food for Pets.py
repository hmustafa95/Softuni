days = int(input())
total_food = float(input())
dog_food_eaten = 0
cat_food_eaten = 0
cookies = 0

for monkey in range(1, days + 1):
    dog_eaten = int(input())
    cat_eaten = int(input())
    dog_food_eaten += dog_eaten
    cat_food_eaten += cat_eaten
    if monkey % 3 == 0:
        cookies += (dog_eaten + cat_eaten) * 0.10

total_eaten = dog_food_eaten + cat_food_eaten
cookies_eaten = round(cookies)

percent_eaten_food = total_eaten / total_food * 100
percent_dog_eaten = dog_food_eaten / total_eaten * 100
percent_cat_eaten = cat_food_eaten / total_eaten * 100

print(f'Total eaten biscuits: {cookies_eaten}gr.')
print(f'{percent_eaten_food:.2f}% of the food has been eaten.')
print(f'{percent_dog_eaten:.2f}% eaten from the dog.')
print(f'{percent_cat_eaten:.2f}% eaten from the cat.')
