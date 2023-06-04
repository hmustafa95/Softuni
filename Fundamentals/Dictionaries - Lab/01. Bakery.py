ingredients = input().split(' ')
bakery = {}

for index in range(0, len(ingredients), 2):
    key = ingredients[index]
    value = ingredients[index + 1]
    bakery[key] = int(value)

print(bakery)