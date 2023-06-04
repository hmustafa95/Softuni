def tags(tag):
    def decorator(func_ref):
        def wrapper(*args):
            result = func_ref(*args)
            return f"<{tag}>{result}</{tag}>"
        return wrapper
    return decorator
