def factorial(a):
    for current_index in range(1, a):
        a *= current_index
    return a

first_number = int(input())
second_number = int(input())
first_factorial = factorial(first_number)
second_factorial = factorial(second_number)
result = first_factorial / second_factorial
print(f'{result:.2f}')
