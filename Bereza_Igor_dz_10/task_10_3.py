class Cell:
    def __init__(self, amount_nucleus):
        self.amount_nucleus = int(amount_nucleus)

    def __add__(self, other_cell):
        return self.amount_nucleus + other_cell.amount_nucleus

    def __sub__(self, other_cell):
        result = self.amount_nucleus - other_cell.amount_nucleus
        if result > 0:
            return result
        else:
            return ('Разность количества ячеек двух клеток '
                    'не может быть меньше нуля')

    def __mul__(self, other_cell):
        return self.amount_nucleus * other_cell.amount_nucleus

    def __floordiv__(self, other_cell):
        return self.amount_nucleus // other_cell.amount_nucleus

    def make_order(self, cell, num_row):
        result = ''
        for _ in range(cell.amount_nucleus // num_row):
            result += ''.join(['*' for i in range(num_row)]) + '\n'
        for _ in range(cell.amount_nucleus % num_row):
            result += '*'
        return result



cell_1 = Cell(12)
cell_2 = Cell(15)
print(f'Кол-во ячеек первой клетки: {cell_1.amount_nucleus}')
print(f'Кол-во ячеек второй клетки: {cell_2.amount_nucleus}')
print('-------')
print(f'Сумма количества ячеек двух клеток: {cell_1 + cell_2}')
print('-------')
print(f'Разность количества ячеек первой и второй клеток: {cell_1 - cell_2}')
print(f'Разность количества ячеек второй и первой клеток: {cell_2 - cell_1}')
print('-------')
print(f'Умножение количества ячеек двух клеток: {cell_1 * cell_2}')
print('-------')
print(f'Деление количества ячеек первой и второй клеток: {cell_1 // cell_2}')
print(f'Деление количества ячеек второй и первой клеток: {cell_2 // cell_1}')
print('-------')
print('Первая клетка при организации ячеек 5 в ряду:')
print(cell_1.make_order(cell_1, 5))
print('-------')
print('Вторая клетка при организации ячеек 5 в ряду:')
print(cell_2.make_order(cell_2, 5))
