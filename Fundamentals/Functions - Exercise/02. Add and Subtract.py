def sum_numbers(a, b):
    result = a + b
    return result

def subtract_numbers(a, b):
    result = a - b
    return result

first = int(input())
second = int(input())
third = int(input())

result = subtract_numbers(sum_numbers(first, second), third)
print(result)
