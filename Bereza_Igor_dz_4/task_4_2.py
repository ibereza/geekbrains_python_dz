from requests import get, utils
from decimal import Decimal

URL = "http://www.cbr.ru/scripts/XML_daily.asp"


def get_site_content(url):
    response = get(url)
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)

    return content


def parsing_content(content):
    _lst = content.split("<")
    currency_dict = {}

    for index, item in enumerate(_lst):
        if item.startswith("CharCode"):
            currency_dict.setdefault(item[-3:], {})
            currency_dict[item[-3:]].setdefault(
                "Nominal", int(_lst[index + 2].split(">")[1]))
            currency_dict[item[-3:]].setdefault(
                "Name", _lst[index + 4].split(">")[1])
            currency_dict[item[-3:]].setdefault("Value",
                    Decimal(_lst[index + 6].split(">")[1].replace(",", ".")))

    return currency_dict


def currency_rates(currency):
    site_content = get_site_content(URL)
    currency_dict = parsing_content(site_content)
    currency = currency.upper()
    if currency in currency_dict:
        currency_rate = (currency_dict[currency]["Value"] /
                         currency_dict[currency]["Nominal"])
    else:
        currency_rate = None

    return currency_rate


if __name__ == "__main__":
    print(currency_rates("USD"))
    print(currency_rates("EUR"))
