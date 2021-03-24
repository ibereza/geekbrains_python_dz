from functools import wraps


def val_checker(lambda_func):
    def decorator(func):
        @wraps(func)
        def wrapper(arg):
            try:
                if not lambda_func(arg):
                    raise ValueError
                result = func(arg)
                return result
            except ValueError:
                return f'ValueError: wrong val {arg}'

        return wrapper

    return decorator


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


a = calc_cube(5)
print(a)
a = calc_cube(-5)
print(a)
print(f'Имя функции: {calc_cube.__name__}')
