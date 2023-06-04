def even_numbers(func_ref):
    def wrapper(numbers):
        result = func_ref(numbers)
        return [x for x in result if x % 2 == 0]
    return wrapper
