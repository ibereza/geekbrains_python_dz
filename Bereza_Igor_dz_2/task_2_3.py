lst = ['в', '5', 'часов', '17', 'минут', 'температура',
       'воздуха', 'была', '+5', 'градусов']

for i in reversed(range(0, len(lst))):
    if lst[i][0] in ('+', '-'):
        if lst[i][1:].isnumeric():
            lst.insert(i + 1, '"')
            lst[i] = f'{lst[i][0]}{int(lst[i][1:]):02d}'
            lst.insert(i, '"')
    elif lst[i].isnumeric():
        lst.insert(i + 1, '"')
        lst[i] = f'{int(lst[i]):02d}'
        lst.insert(i, '"')

print(lst)

message = " ".join(lst)
for i in range(message.count(' " ') // 2):
    message = message.replace(' " ', ' "', 1)
    message = message.replace(' " ', '" ', 1)
print(message)
