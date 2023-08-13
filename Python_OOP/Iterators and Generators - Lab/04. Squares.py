def squares(number):
    start = 1

    while start <= number:
        yield start ** 2
        start += 1
