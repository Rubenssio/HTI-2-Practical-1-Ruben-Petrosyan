import time
from functools import wraps


def warn_slow(func):
    @wraps(func)
    def inner(*args, **kwargs):

        start = time.time()
        result = func(*args, **kwargs)
        duration = time.time() - start

        threshold = 2  # in seconds

        if duration > threshold:
            print(f'execution of {func.__name__} with {args} arguments took more than {threshold} seconds')

        return result

    return inner


@warn_slow
def func_slow(x, y):
    # imitating a slow function
    time.sleep(3)


@warn_slow
def func_fast(x, y):
    print(x, y)


func_slow(1, 2)
func_fast(1, 2)
