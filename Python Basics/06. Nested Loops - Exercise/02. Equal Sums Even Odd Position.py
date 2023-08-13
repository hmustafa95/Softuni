first_number = int(input())
second_number = int(input())

for monkeycheese in range(first_number, second_number + 1):
    number_to_str = str(monkeycheese)
    sum_odd = 0
    sum_even = 0
    for monkey, digit in enumerate(number_to_str):
        if monkey % 2 == 0:
            sum_odd += int(digit)
        else:
            sum_even += int(digit)
    if sum_even == sum_odd:
        print(monkeycheese, end=' ')
