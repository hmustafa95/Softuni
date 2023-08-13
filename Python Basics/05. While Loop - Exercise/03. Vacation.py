needed_money = float(input())
account_money = float(input())
spending_counter = 0
days_counter = 0

while account_money < needed_money and spending_counter < 5:
    action = input()
    moved_money = float(input())
    days_counter += 1
    if action == 'spend':
        account_money -= moved_money
        spending_counter += 1
        if account_money < 0:
            account_money = 0
    elif action == 'save':
        account_money += moved_money
        spending_counter = 0

if spending_counter == 5:
    print("You can't save the money.")
    print(f'{days_counter}')

if account_money >= needed_money:
    print(f'You saved the money for {days_counter} days.')
