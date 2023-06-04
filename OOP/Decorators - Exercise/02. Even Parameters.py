def even_parameters(func_ref):
    def wrapper(*args):
        for argument in args:
            if not type(argument) == int or argument % 2 != 0:
                return "Please use only even numbers!"
        return func_ref(*args)
    return wrapper
