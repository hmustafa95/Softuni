numbers = int(input())
sum_total = 0
biggest = ''

for i in range(0, numbers):
    num = int(input())
    if i == 0:
        biggest = num
    sum_total += num
    if num > biggest:
        biggest = num

if biggest == sum_total - biggest:
    print('Yes')
    print(f'Sum = {biggest}')
else:
    sum_other = abs(biggest - (sum_total - biggest))
    print('No')
    print(f'Diff = {sum_other}')
