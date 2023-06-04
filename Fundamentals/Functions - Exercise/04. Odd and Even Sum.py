def odd_or_even(a):
    odd_sum = 0
    even_sum = 0
    x = [int(c) for c in str(a)]
    for current_index in x:
        if current_index % 2 == 0:
            even_sum += current_index
        else:
            odd_sum += current_index
    return f'Odd sum = {odd_sum}, Even sum = {even_sum}'

number = int(input())
print(odd_or_even(number))
