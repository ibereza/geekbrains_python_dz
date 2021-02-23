lst = ['в', '5', 'часов', '17', 'минут', 'температура',
       'воздуха', 'была', '+5', 'градусов']

_lst = []
for item in lst:
    if item[0] in ('+', '-'):
        if item[1:].isnumeric():
            _lst.append('"')
            _lst.append(f'{item[0]}{int(item[1:]):02d}')
            _lst.append('"')
        else:
            _lst.append(item)
    elif item.isnumeric():
        _lst.append('"')
        _lst.append(f'{int(item):02d}')
        _lst.append('"')
    else:
        _lst.append(item)

lst = _lst
print(lst)

message = " ".join(lst)
for i in range(message.count(' " ') // 2):
    message = message.replace(' " ', ' "', 1)
    message = message.replace(' " ', '" ', 1)
print(message)
