def genrange(n, m):
    start = n
    end = m

    while start <= end:
        yield start
        start += 1
