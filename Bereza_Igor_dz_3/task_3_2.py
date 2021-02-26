DICTIONARY = {
    "zero": "ноль",
    "one": "один",
    "two": "два",
    "three": "три",
    "four": "четыре",
    "five": "пять",
    "six": "шесть",
    "seven": "семь",
    "eight": "восемь",
    "nine": "девять",
    "ten": "десять",
}


def num_translate_adv(word):
    if word.istitle():
        return DICTIONARY.get(word.lower()).title()
    return DICTIONARY.get(word)


print(num_translate_adv("six"))
