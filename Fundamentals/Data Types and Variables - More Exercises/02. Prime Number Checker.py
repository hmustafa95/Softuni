number = int(input())

def isprime(number):
    if number> 1:
        for n in range(2,number):
            if (number % n) == 0:
                return False
        return True
    else:
        return False
print(isprime(number))
