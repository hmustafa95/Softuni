from math import floor

companions = int(input())
days = int(input())
coins = 0

for digit in range(1, days + 1):
    if digit % 10 == 0:
        companions -= 2
    if digit % 15 == 0:
        companions += 5
    if digit % 3 == 0:
        coins -= companions * 3
    if digit % 5 == 0:
        coins += companions * 20
        if digit % 5 == 0 and digit % 3 == 0:
            coins -= companions * 2
    coins += 50
    coins -= companions * 2

coins_each = floor(coins / companions)
print(f'{companions} companions received {coins_each} coins each.')
