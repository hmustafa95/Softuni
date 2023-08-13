start_interval = int(input())
end_interval = int(input())
magic_number = int(input())
combination = 0
flag = False

for x1 in range(start_interval, end_interval + 1):
    for x2 in range(start_interval, end_interval +1):
        combination += 1
        if x1 + x2 == magic_number:
            flag = True
            break
    if flag:
        break

if flag:
    print(f'Combination N:{combination} ({x1} + {x2} = {(x1 + x2)})')
else:
    print(f'{combination} combinations - neither equals {magic_number}')
