# создаем список
arr = []
for number in range(1, 1000, 2):
    arr.append(number ** 3)

# задание a
sum_multiples_seven = 0
for number in arr:
    sum_digits = 0
    for i in range(0, len(str(number))):
        digit = number % 10 ** (i + 1) // 10 ** i
        sum_digits += digit
    if sum_digits % 7 == 0:
        sum_multiples_seven += number
print(sum_multiples_seven)

# задание b
arr_plus_17 = []
for number in arr:
    number += 17
    arr_plus_17.append(number)
sum_multiples_seven = 0
for number in arr_plus_17:
    sum_digits = 0
    for i in range(0, len(str(number))):
        digit = number % 10 ** (i + 1) // 10 ** i
        sum_digits += digit
    if sum_digits % 7 == 0:
        sum_multiples_seven += number
print(sum_multiples_seven)

# задание c
sum_multiples_seven = 0
for number in arr:
    number += 17
    sum_digits = 0
    for i in range(0, len(str(number))):
        digit = number % 10 ** (i + 1) // 10 ** i
        sum_digits += digit
    if sum_digits % 7 == 0:
        sum_multiples_seven += number
print(sum_multiples_seven)
