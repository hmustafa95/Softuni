seaTripAmount = int(input())
mountainTripAmount = int(input())
destination = input()

profit = 0
prices_sea = 680
prices_mountain = 499

while destination != 'Stop':
    if destination == 'sea' and seaTripAmount > 0:
        profit += prices_sea
        seaTripAmount -= 1
    elif destination == 'mountain' and mountainTripAmount > 0:
        profit += prices_mountain
        mountainTripAmount -= 1
    if seaTripAmount == 0 and mountainTripAmount == 0:
        print('Good job! Everything is sold.')
        break
    destination = input()

print(f'Profit: {profit} leva.')