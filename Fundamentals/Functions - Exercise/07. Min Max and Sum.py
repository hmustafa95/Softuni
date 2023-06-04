def minimum_amount(any_list):
    result = min(any_list)
    return f"The minimum number is {result}"

def maximum_amount(any_list):
    result = max(any_list)
    return f"The maximum number is {result}"

def sum_of_amount(any_list):
    result = sum(any_list)
    return f"The sum number is: {result}"

received_list = input().split(" ")
numarized_list = [int(a) for a in received_list]

print(minimum_amount(numarized_list))
print(maximum_amount(numarized_list))
print(sum_of_amount(numarized_list))
