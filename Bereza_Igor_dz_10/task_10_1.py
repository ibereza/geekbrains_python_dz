class Matrix:
    def __init__(self, matrix_list):
        self.matrix_list = matrix_list

    def __str__(self):
        __str = ''
        for el_list in self.matrix_list:
            int_to_str = [str(i) for i in el_list]
            __str += '\t'.join(int_to_str) + '\n'
        return __str

    def __add__(self, other):
        add_matrix_list = []
        for i in range(len(self.matrix_list)):
            add_matrix_list.append([])
            for j in range(len(self.matrix_list[i])):
                el = self.matrix_list[i][j] + other.matrix_list[i][j]
                add_matrix_list[i].append(el)
        return Matrix(add_matrix_list)


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
