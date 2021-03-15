from sys import exit
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('line', type=int, help='номер записи')
parser.add_argument('sum', type=float, help='новая сумма')
args = parser.parse_args()

if args.line <= 0:
    print('[-] Номер записи должен быть больше 0')
    exit(1)

with open('bakery.csv', 'r', encoding='UTF-8') as f:
    list_sum = []
    for line in f:
        list_sum.append(line)

if args.line > len(list_sum):
    print('[-] Записи с этим номером не существует')
    exit(1)

with open('bakery.csv', 'w', encoding='UTF-8') as f:
    for i, line in enumerate(list_sum):
        if i + 1 == args.line:
            f.write(f'{args.sum}\n')
            print(f'[+] Запись номер {args.line} была изменена с '
                  f'{line.strip()} на {args.sum}')
        else:
            f.write(line)
