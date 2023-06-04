def logged(func_ref):
    def decorator(*args):
        def wrapper():
            result = func_ref(*args)
            return f"you called {func_ref.__name__}{args}\nit returned {result}"
        return wrapper()
    return decorator
