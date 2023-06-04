def check_numbers(a, b, c):
    negative = 0
    if a < 0:
        negative += 1
    elif b < 0:
        negative += 1
    elif c < 0:
        negative += 1
    if a == 0 or b == 0 or c == 0:
        return "zero"
    if negative == 1 or negative == 3:
        return "negative"
    return "positive"

first = int(input())
second = int(input())
third = int(input())
print(check_numbers(first, second, third))
