

def try_again(func, delay=3, attempts=5):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

