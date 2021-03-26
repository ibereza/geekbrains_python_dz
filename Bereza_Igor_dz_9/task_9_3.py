class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f'{self.position} {self.name} {self.surname}'

    def get_total_income(self):
        total = self._income['wage'] + self._income['bonus']
        return total


position = Position('Иван', 'Иванов', 'старший сотрудник', 100000, 20000)
print(position.get_full_name())
print(position.get_total_income())
