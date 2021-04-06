class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        if self.b >= 0:
            return f'{self.a} + {self.b}i'
        else:
            return f'{self.a} - {-self.b}i'

    def __add__(self, other):
        a = self.a + other.a
        b = self.b + other.b
        return ComplexNumber(a, b)

    def __mul__(self, other):
        a = self.a * other.a - self.b * other.b
        b = self.b * other.a + self.a * other.b
        return ComplexNumber(a, b)


cx_number_1 = ComplexNumber(-1, -1)
print(f'Комплексное число 1: {cx_number_1}')
cx_number_2 = ComplexNumber(3, 6)
print(f'Комплексное число 2: {cx_number_2}')
sum_cx_numbers = cx_number_1 + cx_number_2
print(f'Сумма комплексных чисел: {sum_cx_numbers}')
mul_cx_numbers = cx_number_1 * cx_number_2
print(f'Произведение комплексных чисел: {mul_cx_numbers}')
