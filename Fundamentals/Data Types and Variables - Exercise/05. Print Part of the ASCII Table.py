first = int(input())
last = int(input())
result = ''

for digit in range(first, last + 1):
    result += chr(digit) + ' '

print(result[:-1:])
