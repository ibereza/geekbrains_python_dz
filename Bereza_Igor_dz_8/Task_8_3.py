from functools import wraps


def type_logger(func):
    @wraps(func)
    def tag_wrapper(*args, **kwargs):
        for arg in args:
            print(f'{arg}: {type(arg)}', end=', ')
        print()
        for name, value in kwargs.items():
            print(f'Именованный аргумент: {name}={value}:{type(value)}')
        result = func(args[0])
        print(f'Результат выполнения фунции = {result}: {type(result)}')
        print(f'{func.__name__}({args[0]}: {type(args[0])})')
        return result

    return tag_wrapper


@type_logger
def calc_cube(x):
    return x ** 3


calc_cube(3, 5.5, 'Строка', ['Список'], ('Кортеж',), {'Словарь': 1},
          x=7, y='5.5')
