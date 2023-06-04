def perfect_number(a):
    sum = 0
    for divisor in range(1, a):
        if a % divisor == 0:
            sum += divisor
    if sum == a:
        return "We have a perfect number!"
    return "It's not so perfect."

number = int(input())
print(perfect_number(number))
