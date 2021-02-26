from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный",
              "мягкий"]


def get_jokes(count):
    """returns a random set of jokes"""
    jokes = []
    for i in range(count):
        jokes.append(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')
    return jokes


print(get_jokes(5))
