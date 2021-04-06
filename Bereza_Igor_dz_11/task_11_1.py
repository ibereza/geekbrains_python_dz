class Date:
    date_str = ''

    def __init__(self, date_str):
        Date.date_str = date_str

    @classmethod
    def parse_date(cls):
        return [int(el) for el in cls.date_str.split('-')]

    @staticmethod
    def verify_date():
        date_lst = Date.parse_date()
        if date_lst[0] not in range(1, 32):
            result = 'Значение дня задано не корректно'
        elif date_lst[1] not in range(1, 13):
            result = 'Значение месяца задано не корректно'
        elif date_lst[2] not in range(2000, 2022):
            result = 'Значение года задано не корректно'
        else:
            result = 'Дата задана корректно'
        return result


date = Date('31-01-2021')
print(date.parse_date())
print(date.verify_date())

