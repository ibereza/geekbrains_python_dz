lst = [57.8, 46.51, 97, 101.5, 5.3, 19.99, 33.3, 99.99, 1, 75.05]

# задача A
print('Задача A')
for item in lst:
    number = str(float(item)).split(".")
    print(f'{number[0]} руб {number[1]:0<2} коп', end=', ')
print('\n------------------')

# задача B
print('Задача B')
print(f'{id(lst)} ==', end=' ')
lst.sort()
print(id(lst))

for item in lst:
    number = str(float(item)).split(".")
    print(f'{number[0]} руб {number[1]:0<2} коп', end=', ')
print('\n------------------')

# задача C
print('Задача C')
print(f'{id(lst)} !=', end=' ')
_lst = sorted(lst, reverse=True)
print(id(_lst))

for item in _lst:
    number = str(float(item)).split(".")
    print(f'{number[0]} руб {number[1]:0<2} коп', end=', ')
print('\n------------------')

# задача D
print('Задача D')
for item in sorted(lst)[-5:]:
    number = str(float(item)).split(".")
    print(f'{number[0]} руб {number[1]:0<2} коп', end=', ')
print()
