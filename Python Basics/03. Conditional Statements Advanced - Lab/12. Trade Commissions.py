city = input()
sales = float(input())

if city == 'Sofia' and 0 <= sales <= 500:
    commission = sales * 0.05
    print(f'{commission:.2f}')
elif city == 'Sofia' and 500 < sales <= 1000:
    commission = sales * 0.07
    print(f'{commission:.2f}')
elif city == 'Sofia' and 1000 < sales <= 10000:
    commission = sales * 0.08
    print(f'{commission:.2f}')
elif city == 'Sofia' and 10000 < sales:
    commission = sales * 0.12
    print(f'{commission:.2f}')
elif city == 'Varna' and 0 <= sales <= 500:
    commission = sales * 0.045
    print(f'{commission:.2f}')
elif city == 'Varna' and 500 < sales <= 1000:
    commission = sales * 0.075
    print(f'{commission:.2f}')
elif city == 'Varna' and 1000 < sales <= 10000:
    commission = sales * 0.10
    print(f'{commission:.2f}')
elif city == 'Varna' and 10000 < sales:
    commission = sales * 0.13
    print(f'{commission:.2f}')
elif city == 'Plovdiv' and 0 <= sales <= 500:
    commission = sales * 0.055
    print(f'{commission:.2f}')
elif city == 'Plovdiv' and 500 < sales <= 1000:
    commission = sales * 0.08
    print(f'{commission:.2f}')
elif city == 'Plovdiv' and 1000 < sales <= 10000:
    commission = sales * 0.12
    print(f'{commission:.2f}')
elif city == 'Plovdiv' and 10000 < sales:
    commission = sales * 0.145
    print(f'{commission:.2f}')
else:
    print('error')
