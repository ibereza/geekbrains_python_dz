class Matrix:
    def __init__(self, matrix_list):
        self.matrix_list = matrix_list

    def __str__(self):
        __str = ''
        for el_list in self.matrix_list:
            __str += '\t'.join([str(i) for i in el_list]) + '\n'
        return __str

    def __add__(self, other):
        try:
            if len(self.matrix_list) == len(other.matrix_list):
                for i in range(len(self.matrix_list)):
                    if len(self.matrix_list[i]) != len(other.matrix_list[i]):
                        raise ValueError
            else:
                raise ValueError
        except ValueError:
            return 'Размерность матриц не совпадает!'
        else:
            result = [[(el[0] + el[1]) for el in zip(el[0], el[1])]
                      for el in zip(self.matrix_list, other.matrix_list)]
            return Matrix(result)


matrix = Matrix([[31, 22], [37, 43], [51, 86]])
print(f'матрица 1:')
print(matrix)
matrix.matrix_list = [[3, 5, 32], [2, 4, 6], [-1, 64, -8]]
print('матрица 2:')
print(matrix)
matrix.matrix_list = [[3, 5, 8, 3], [8, 3, 7, 1]]
print('матрица 3:')
print(matrix)

matrix_1 = Matrix([[3, 5, 8, 3], [8, 3, 7, 1]])
matrix_2 = Matrix([[7, 5, 2, 7], [2, 7, 3, 9]])
print('сумма двух матриц:')
print(matrix_1, end='')
print('+')
print(matrix_2, end='')
print('=')
print(matrix_1 + matrix_2)

matrix_1.matrix_list = [[3, 5, 32], [2, 4, 6], [-1, 64, -8]]
matrix_2.matrix_list = [[-3, -5, -32], [-2, -4, -6], [1, -64, 8]]
print('сумма двух матриц:')
print(matrix_1, end='')
print('+')
print(matrix_2, end='')
print('=')
print(matrix_1 + matrix_2)
