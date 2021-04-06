class CountIsNotInt(Exception):
    def __init__(self):
        message = 'Параметр count - должен быть целым числом'
        super().__init__(message)


class Stock:
    def __init__(self):
        self.stock_dict = {}

    def add_to_stock(self, equipment):
        self.stock_dict.setdefault(equipment.equip_type, {})
        if equipment.equip_name in self.stock_dict[equipment.equip_type]:
            self.stock_dict[equipment.equip_type][equipment.equip_name][
                'count'] = \
                self.stock_dict[equipment.equip_type][equipment.equip_name][
                    'count'] + equipment.equip_dict['count']
        else:
            self.stock_dict[equipment.equip_type].setdefault(
                equipment.equip_name,
                equipment.equip_dict)

    def remove_from_stock(self, equipment, brand, model, count):
        if type(count) != int:
            raise CountIsNotInt
        equip_name = f'{brand} {model}'
        if equipment in self.stock_dict:
            if equip_name in self.stock_dict[equipment]:
                count_on_stock = self.stock_dict[equipment][equip_name][
                    'count']
                if count_on_stock < count:
                    print(f'Из запрашиваемых {count} "{equip_name}" будет '
                          f'списано {count_on_stock} шт. оборудования.')
                    print(f'На складе больше нет "{equip_name}"')
                    self.stock_dict[equipment].pop(equip_name)
                elif count_on_stock == count:
                    print(f'Со склада списано {count_on_stock} '
                          f'единиц "{equip_name}".')
                    print(f'На складе больше нет "{equip_name}"')
                    self.stock_dict[equipment].pop(equip_name)
                else:
                    print(f'Со склада списано {count} шт. "{equip_name}".')
                    self.stock_dict[equipment][equip_name]['count'] = \
                        count_on_stock - count
            else:
                print(f'Модель "{equip_name}" отсутствует в списке '
                      'оборудования на складе')
        else:
            print(f'"{equipment}" отсутствует в списке типов оборудования '
                  'на складе')


class OfficeEquipment:
    def __init__(self, brand, model, count):
        if type(count) != int:
            raise CountIsNotInt
        else:
            self.equip_type = self.__class__.__name__
            self.equip_name = f'{brand} {model}'
            self.equip_dict = {
                'count': count
            }


class Printer(OfficeEquipment):
    def __init__(self, brand, model, printer_type, count):
        super().__init__(brand, model, count)
        self.equip_dict['type'] = printer_type


class Scanner(OfficeEquipment):
    def __init__(self, brand, model, resolution, scan_format, count):
        super().__init__(brand, model, count)
        self.equip_dict['resolution'] = resolution
        self.equip_dict['format'] = scan_format


stock = Stock()
printer = Printer('Canon', 'iPF-710', 'ink jet', 3)
stock.add_to_stock(printer)
print(stock.stock_dict)
printer = Printer('Xerox', 'N25', 'laser', 5)
stock.add_to_stock(printer)
print(stock.stock_dict)
# добавили уже существующую модель оборудования:
printer = Printer('Xerox', 'N25', 'laser', 3)
stock.add_to_stock(printer)
print(stock.stock_dict)
scanner = Scanner('Epson', 'Perfection V19', '4800x4800', 'A4', 2)
stock.add_to_stock(scanner)
print(stock.stock_dict)
# запрашиваем не существующее на складе оборудование:
stock.remove_from_stock('Xerox', 'Xerox', 'i3', 4)
print(stock.stock_dict)
# запрашиваем не существующую на складе модель оборудования:
stock.remove_from_stock('Printer', 'Xerox', 'N44', 4)
print(stock.stock_dict)
# запрашиваем 4 из 8 доступных единиц оборудования:
stock.remove_from_stock('Printer', 'Xerox', 'N25', 4)
print(stock.stock_dict)
# запрашиваем 3 из 2 доступных единиц оборудования:
stock.remove_from_stock('Scanner', 'Epson', 'Perfection V19', 3)
print(stock.stock_dict)
# запрашиваем 3 из 3 доступных единиц оборудования:
stock.remove_from_stock('Printer', 'Canon', 'iPF-710', 3)
print(stock.stock_dict)
