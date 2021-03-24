import re

RE_NAME = re.compile(
    r'^(.*)\s-\s-\s.*\[(.+)]\s\"(\w*)\s(.*?)\"\s(\d{3})\s(\d*)\s')

with open("nginx_logs.txt", "r", encoding="UTF-8") as f:
    result = []
    counter = 1
    for line in f:
        result.append(RE_NAME.findall(line)[0])

print(f'Всего кол-во строк: {len(result)}')
print(f'Строка 1: {result[0]}')
print(f'Строка {len(result)}: {result[len(result) - 1]}')
