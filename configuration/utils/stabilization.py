

def try_again(func, delay=3, attempts=5):
    """
    just an example of writing decorator.
    :param func:
    :param delay:
    :param attempts:
    :return:
    """
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

