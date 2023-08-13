destination = input()

while destination != 'End':
    min_budget = float(input())
    saved_money = 0
    while saved_money < min_budget:
        saved = float(input())
        saved_money = saved_money + saved
    print(f'Going to {destination}!')
    destination = input()
