def command(a, b):
    if a == 'int':
        c = int(b)
        result = c * 2
        return result
    elif a == 'real':
        c = float(b)
        result = c * 1.5
        return f'{result:.2f}'
    elif a == 'string':
        return f'${b}$'

first = input()
second = input()
print(command(first, second))
