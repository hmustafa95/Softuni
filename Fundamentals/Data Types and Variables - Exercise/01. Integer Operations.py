from math import floor

first_number = int(input())
second_number = int(input())
third_number = int(input())
fourth_number = int(input())

result = floor((first_number + second_number) / third_number) * fourth_number

print(f'{result}')
