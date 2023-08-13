number = input()
max_number = -100000

while number != 'Stop':
    num = int(number)
    if num > max_number:
        max_number = num
    number = input()

print(max_number)
