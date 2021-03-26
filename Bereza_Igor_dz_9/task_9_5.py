class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Рисуем ручкой')


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Рисуем карандашом')


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Рисуем маркером')


stationary = Stationery('Канцелярские принадлежности')
print(stationary.title)
stationary.draw()

pen = Pen('Ручка')
print(pen.title)
pen.draw()

pencil = Pencil('Карандаш')
print(pencil.title)
pencil.draw()

handle = Handle('Маркер')
print(handle.title)
handle.draw()
