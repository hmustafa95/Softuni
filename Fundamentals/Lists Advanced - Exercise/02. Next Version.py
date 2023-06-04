received_list = input().split('.')
numarized_list = [int(x) for x in received_list]

result = [numarized_list[0], numarized_list[1], (numarized_list[2] + 1)]

if result[2] > 9:
    result[2] = 0
    result[1] = result[1] + 1

if result[1] > 9:
    result[1] = 0
    result[0] = result[0] + 1

print(*result, sep='.')
