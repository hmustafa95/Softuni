def math_solve(first_number, second_number, command):
    if command == 'multiply':
        result = first_number * second_number
        return result
    elif command == 'divide':
        result = first_number // second_number
        return result
    elif command == 'add':
        result = first_number + second_number
        return result
    elif command == 'subtract':
        result = first_number - second_number
        return result

operator_math = input()
first = int(input())
second = int(input())
print(math_solve(first, second, operator_math))
