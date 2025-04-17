"""
@decorator
def decorated_func(*args, **kwargs):
     ...
     return result


decorated_func()
"""
import time


def decorator(arg_type): # decorator behaviour arguments
    def decorator_inner(func): # decorated function object
        def wrapper(*args, **kwargs): # decorated function arguments
            if not all([isinstance(arg, arg_type) for arg in args]):
                raise TypeError("All args need to be integers")

            start_time = time.time()

            result = func(*args, **kwargs)

            exec_time = time.time() - start_time
            print(f"Exec time for {func.__name__}: {exec_time}")
            result += 100
            return result
        return wrapper
    return decorator_inner

@decorator(arg_type=int)
def decorated_func(a, b):
    return a + b


# print(decorated_func(5, "a"))
print(decorated_func(5, 4))
print(decorated_func(5, 4))
print(decorated_func(5, 4))
print(decorated_func(5, 4))
