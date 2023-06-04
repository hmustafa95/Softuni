numbers_list = list(map(int, input().split(' ')))
average = sum(numbers_list) / len(numbers_list)
result = []

for current_index in numbers_list:
    if current_index > average:
        result.append(current_index)

result.sort(reverse=True)

while len(result) > 5:
    del result[5]

if len(result) == 0:
    print('No')
else:
    print(' '.join([str(x) for x in result]))
