lst = ['в', '5', 'часов', '17', 'минут', 'температура',
       'воздуха', 'была', '+5', 'градусов']

_lst = []
for item in lst:
    if item[0] in ('+', '-'):
        if item[1:].isnumeric():
            _num = f'{item[0]}{int(item[1:]):02d}'
            _lst.extend(['"', _num, '"'])
        else:
            _lst.append(item)
    elif item.isnumeric():
        _num = f'{int(item):02d}'
        _lst.extend(['"', _num, '"'])
    else:
        _lst.append(item)

lst = _lst
print(lst)

message = " ".join(lst)
for i in range(message.count(' " ') // 2):
    message = message.replace(' " ', ' "', 1)
    message = message.replace(' " ', '" ', 1)
print(message)
