received_numbers = input().split(" ")
list_of_numbers = []
for current_number in received_numbers:
    add_number = abs(float(current_number))
    list_of_numbers.append(add_number)

print(list_of_numbers)
