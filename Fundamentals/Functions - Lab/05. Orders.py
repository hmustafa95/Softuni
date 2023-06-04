def order(drink, quantity):
    if drink == 'water':
        price = 1
        result = quantity * price
        return result
    elif drink == 'snacks':
        price = 2
        result = quantity * price
        return result
    elif drink == 'coffee':
        price = 1.5
        result = quantity * price
        return result
    elif drink == 'coke':
        price = 1.4
        result = quantity * price
        return result

drink = input()
quantity = int(input())
result = order(drink, quantity)
print(f'{result:.2f}')
