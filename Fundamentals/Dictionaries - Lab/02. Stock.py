ingredients = input().split(' ')
products_dict = {}

for index in range(0, len(ingredients), 2):
    key = ingredients[index]
    value = ingredients[index + 1]
    products_dict[key] = int(value)

query = input().split(' ')

for current_product in query:
    if current_product in products_dict.keys():
        print(f"We have {products_dict[current_product]} of {current_product} left")
    else:
        print(f"Sorry, we don't have {current_product}")
