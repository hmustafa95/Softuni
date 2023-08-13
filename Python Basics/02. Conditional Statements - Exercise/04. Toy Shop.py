puzzle = 2.60
doll = 3
bear = 4.10
minion = 8.20
truck = 2

travel = float(input())
number_puzzle = int(input())
number_doll = int(input())
number_bear = int(input())
number_minion = int(input())
number_truck = int(input())

income = puzzle * number_puzzle + doll * number_doll + bear * number_bear + minion * number_minion + truck * number_truck
total_order = number_truck + number_minion + number_bear + number_doll + number_puzzle
if total_order >= 50:
    income = income * 0.75
else:
    income = income

rent = income * 0.10

net_income = income - rent
left_over = abs(net_income - travel)

if net_income >= travel:
    print(f'Yes! {left_over:.2f} lv left.')
else:
    print(f'Not enough money! {left_over:.2f} lv needed.')
