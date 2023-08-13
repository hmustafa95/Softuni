def get_primes(numbers):
    for num in numbers:
        if num <= 1:
            continue
        for nums in range(2, num):
            if num % nums == 0:
                break
        else:
            yield num
