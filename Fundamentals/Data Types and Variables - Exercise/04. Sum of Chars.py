number = int(input())
sum_numbers = 0

for digit in range(1, number + 1):
    symbol = input()
    sum_numbers += ord(symbol)

print(f'The sum equals: {sum_numbers}')
