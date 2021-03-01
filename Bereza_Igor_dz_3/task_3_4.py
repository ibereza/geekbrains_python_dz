def thesaurus_adv(*arg):
    _dict = {}
    for i in arg:
        _dict.setdefault(i[i.index(' ') + 1], {}).setdefault(i[0], []) \
            .append(i)

    return _dict


print(thesaurus_adv("Иван Сергеев", "Петр Алексеев",
                    "Илья Иванов", "Анна Савельева", "Инна Серова"))
