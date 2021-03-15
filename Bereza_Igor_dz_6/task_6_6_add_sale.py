import argparse

parser = argparse.ArgumentParser()
parser.add_argument('sales_sum', type=float, help='сумма продаж')
args = parser.parse_args()

with open('bakery.csv', 'a', encoding='UTF-8') as f:
    f.write(f'{str(args.sales_sum)}\n')
