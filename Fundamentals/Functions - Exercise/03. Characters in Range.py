def chars_in_range(a, b, any_list):
    for current_index in range(ord(a) + 1, ord(b)):
        current_symbol = chr(current_index)
        any_list.append(current_symbol)
    return any_list

side_a = input()
side_b = input()
actual_list = []

result = chars_in_range(side_a, side_b, actual_list)
print(' '.join(result))
