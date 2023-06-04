divisor = int(input())
boundary = int(input())

for smth in range(boundary, divisor, - 1):
    if smth % divisor == 0:
        print(smth)
        break
