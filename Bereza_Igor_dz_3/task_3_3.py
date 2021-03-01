def thesaurus(*arg):
    _dict = {}
    for item in arg:
        _dict.setdefault(item[0], []).append(item)

    return _dict


print(thesaurus("Иван", "Мария", "Петр", "Илья", "Василий", "Михаил"))
