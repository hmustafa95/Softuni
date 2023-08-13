number_tabs = int(input())
wage = int(input())
ticket = 0
sum_wage = 0

for something in range(number_tabs):
    tab_name = input()
    if tab_name == 'Facebook':
        ticket += 150
    elif tab_name == 'Instagram':
        ticket += 100
    elif tab_name == 'Reddit':
        ticket += 50
    sum_wage = wage - ticket
    if sum_wage <= 0:
        break

if sum_wage <= 0:
    print("You have lost your salary.")
else:
    print(sum_wage)
