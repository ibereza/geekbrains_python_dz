def thesaurus(*arg):
    _dict = {}
    for item in arg:
        if _dict.get(item[0]):
            _dict[item[0]].append(item)
        else:
            _dict[item[0]] = [item]

    return _dict


print(thesaurus("Иван", "Мария", "Петр", "Илья", "Василий", "Михаил"))
