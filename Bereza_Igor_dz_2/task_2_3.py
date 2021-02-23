lst = ['в', '5', 'часов', '17', 'минут', 'температура',
       'воздуха', 'была', '+5', 'градусов']

count = 0

while count < len(lst):
    if lst[count][0] in ('+', '-'):
        if lst[count][1:].isnumeric():
            lst.insert(count, '"')
            count += 1
            lst[count] = f'{lst[count][0]}{int(lst[count][1:]):02d}'
            count += 1
            lst.insert(count, '"')
            count += 1
        else:
            count += 1
    elif lst[count].isnumeric():
        lst.insert(count, '"')
        count += 1
        lst[count] = f'{int(lst[count]):02d}'
        count += 1
        lst.insert(count, '"')
        count += 1
    else:
        count += 1
print(lst)

message = " ".join(lst)
for i in range(message.count(' " ') // 2):
    message = message.replace(' " ', ' "', 1)
    message = message.replace(' " ', '" ', 1)
print(message)
