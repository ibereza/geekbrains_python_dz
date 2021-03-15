from sys import exit
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('start', type=int, nargs='?', help='начало вывода')
parser.add_argument('end', type=int, nargs='?', help='конец вывода')
args = parser.parse_args()

if args.start is not None and args.start <= 0:
    print('[-] Аргумент должен быть больше 0')
    exit(1)
elif args.end is not None and args.start >= args.end:
    print('[-] Аргументы должны быть больше 0 и первый аргумент '
          'должен быть меньше второго')
    exit(1)

with open('bakery.csv', 'r', encoding='UTF-8') as f:
    counter = 1
    for line in f:
        if args.start is None or args.start <= counter:
            print(line.strip())
        counter += 1
        if args.end is not None and counter > args.end:
            break
