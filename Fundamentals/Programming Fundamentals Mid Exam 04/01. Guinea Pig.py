food_quantity = float(input()) * 1000
hay_quantity = float(input()) * 1000
cover_quantity = float(input()) * 1000
weight = float(input()) * 1000

for number_day in range(1, 31):
    food_quantity -= 300
    if number_day % 2 == 0:
        hay_quantity -= food_quantity * 0.05
    if number_day % 3 == 0:
        cover_quantity -= weight / 3
    if food_quantity <= 0 or hay_quantity <= 0 or cover_quantity <= 0:
        print('Merry must go to the pet store!')
        break
    if number_day % 30 == 0:
        print(f"Everything is fine! Puppy is happy! Food: {(food_quantity / 1000):.2f}, Hay: {(hay_quantity / 1000):.2f}, Cover: {(cover_quantity / 1000):.2f}.")
