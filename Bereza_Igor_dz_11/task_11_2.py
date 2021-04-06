class DivByZero(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    a = float(input('Введите делимое: '))
    b = float(input('Введите делитель: '))
    if b == 0:
        raise DivByZero("На ноль делить нельзя!")
except ValueError:
    print("Вы ввели не число")
except DivByZero as err:
    print(err)
else:
    print(f"Результат деления: {a / b}")
