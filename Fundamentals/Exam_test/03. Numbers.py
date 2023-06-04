numbers = [int(x) for x in input().split(' ')]
result = []
sum_of_numbers = 0

for index in range(len(numbers)):
    sum_of_numbers += numbers[index]

average = sum_of_numbers / len(numbers)

for number in numbers:
    if number > average:
        result.append(number)

sorted_result = sorted(result, reverse=True)
top_five = sorted_result[:5]

if top_five:
    print(*top_five, sep=' ')
else:
    print('No')