import sys

from utils import currency_rates


def print_rates(argv):
    _, *arg = argv
    if len(arg) != 1:
        print("Укажите один код валюты в качестве параметра")
    else:
        currency_rate, currency_date = currency_rates(*arg)
        if currency_rate is None:
            print(f"Код валюты {arg[0].upper()} отсутствует в списке валют")
        else:
            print(f"На {currency_date} курс {arg[0].upper()}/RUB "
                  f"= {currency_rate}")

    return 0


exit(print_rates(sys.argv))
