def shopping_cart(*args):
    shopping_list = {
        'Soup': [],
        'Pizza': [],
        'Dessert': []
    }
    for idx in range(len(args)):
        if args[idx] == 'Stop':
            break
        key, value = args[idx]
        if key == 'Soup' and len(shopping_list[key]) == 3 or key == 'Pizza' and len(shopping_list[key]) == 4 or key == 'Dessert' and len(shopping_list[key]) == 2:
            continue
        if value in shopping_list[key]:
            continue
        shopping_list[key].append(value)
    result = ''
    sorted_list = dict(sorted(shopping_list.items(), key=lambda x: (-len(x[1]), x[0])))
    if len(shopping_list['Soup']) > 0 or len(shopping_list['Dessert']) > 0 or len(shopping_list['Pizza']) > 0:
        for k, v in sorted_list.items():
            result += f"{k}:\n"
            for items in sorted(v):
                result += f" - {items}" + '\n'
    else:
        result = "No products in the cart!"
    return result
