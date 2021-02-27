def thesaurus_adv(*arg):
    _dict = {}
    for item in arg:
        name, surname = item.split(" ")
        if surname[0] in _dict:
            if name[0] in _dict[surname[0]]:
                _dict[surname[0]][name[0]].append(item)
            else:
                _dict[surname[0]][name[0]] = [item]
        else:
            _dict[surname[0]] = {}
            _dict[surname[0]][name[0]] = [item]
    return _dict


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев",
                    "Илья Иванов", "Анна Савельева"))
