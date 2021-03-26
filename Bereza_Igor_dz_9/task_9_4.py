class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина начала движение')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print(f'Машина повернула {direction}')

    def show_speed(self):
        print(f'Текущая скорость: {self.speed} км/ч')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police, max_speed=60):
        super().__init__(speed, color, name, is_police)
        self.max_speed = max_speed

    def show_speed(self):
        if self.speed > self.max_speed:
            print(f'Текущая скорость: {self.speed} км/ч')
            print(f'Машина превысила допустимую скорость {self.max_speed} '
                  f'км/ч на {self.speed - self.max_speed} км/ч!')
        else:
            print(f'Текущая скорость: {self.speed} км/ч')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police, max_speed=40):
        super().__init__(speed, color, name, is_police)
        self.max_speed = max_speed

    def show_speed(self):
        if self.speed > self.max_speed:
            print(f'Текущая скорость: {self.speed} км/ч')
            print(f'Машина превысила допустимую скорость {self.max_speed} '
                  f'км/ч на {self.speed - self.max_speed} км/ч!')
        else:
            print(f'Текущая скорость: {self.speed} км/ч')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


def test_car(car):
    if car.is_police:
        print(f'Полицейская машина {car.name} цвета {car.color}')
    else:
        print(f'Машина {car.name} цвета {car.color}')
    car.go()
    car.show_speed()
    car.turn('на право')
    car.speed += 30
    print(f'Машина изменила скорость')
    car.show_speed()
    car.turn('на лево')
    car.speed -= 30 + 20
    print(f'Машина изменила скорость')
    car.show_speed()
    car.stop()


town_car = TownCar(50, '"Спелая вишня"', 'Chevrolet Aveo', False)
test_car(town_car)
print('-------')
sport_car = SportCar(90, '"Сакура"', 'Porsche 911', False)
test_car(sport_car)
print('-------')
work_car = WorkCar(25, 'желтый', 'CAT DP25NT', False)
test_car(work_car)
print('-------')
police_car = PoliceCar(70, 'белый', 'Toyota Prius', True)
test_car(police_car)
