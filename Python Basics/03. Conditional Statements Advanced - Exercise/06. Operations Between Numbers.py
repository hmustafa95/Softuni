n1 = int(input())
n2 = int(input())
one_symbol = input()

if one_symbol == '+':
    result = n1 + n2
    if result % 2 == 0:
        even = 'even'
    else:
        even = 'odd'
    print(f'{n1} {one_symbol} {n2} = {result} - {even}')
elif one_symbol == '-':
    result = n1 - n2
    if result % 2 == 0:
        even = 'even'
    else:
        even = 'odd'
    print(f'{n1} {one_symbol} {n2} = {result} - {even}')
if one_symbol == '*':
    result = n1 * n2
    if result % 2 == 0:
        even = 'even'
    else:
        even = 'odd'
    print(f'{n1} {one_symbol} {n2} = {result} - {even}')
elif one_symbol == '/' and n2 != 0:
    result = n1 / n2
    print(f'{n1} / {n2} = {result:.2f}')
elif one_symbol == '%' and n2 != 0:
    remaining = n1 % n2
    print(f'{n1} % {n2} = {remaining}')
elif one_symbol == '/' or one_symbol == '%' and n2 == 0:
    print(f'Cannot divide {n1} by zero')
