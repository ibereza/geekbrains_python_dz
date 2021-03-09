src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

unique_set = set()
temp_set = set()

for el in src:
    if el not in temp_set:
        unique_set.add(el)
    else:
        unique_set.discard(el)
    temp_set.add(el)

result = [el for el in src if el in set(unique_set)]

print(result)
