class IsNotNumber(Exception):
    def __init__(self):
        message = 'Вы ввели не число'
        super().__init__(message)


lst = []
number = ''
print('Для заполнения списка вводите числа.')
print('Для завершения ввода введите "stop".')
while True:
    try:
        number = input('Введите число: ')
        if number.lower() == 'stop':
            break
        if number.isnumeric():
            lst.append(int(number))
        else:
            raise IsNotNumber
    except IsNotNumber:
        print('Вы ввели не число')
print(f'Был создан следующий список: {lst}')
