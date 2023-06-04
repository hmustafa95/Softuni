def rounding_numbers(any_list):
    for current_index in any_list:
        current_number = float(current_index)
        rounded_number = round(current_number)
        actual_list.append(rounded_number)
    return actual_list

received_list = input().split(" ")
actual_list = []

print(rounding_numbers(received_list))
