def type_check(type_par):
    def decorator(func_ref):
        def wrapper(*args):
            if type(*args) != type_par:
                return 'Bad Type'
            return func_ref(*args)
        return wrapper
    return decorator
