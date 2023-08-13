number = input()
min_number = 10000000

while number != 'Stop':
    num = int(number)
    if min_number > num:
        min_number = num
    number = input()

print(min_number)
