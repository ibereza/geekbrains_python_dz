class Road:
    def __init__(self, width, length):
        self._width = width
        self._length = length

    def weight(self, weight_1m2, thickness):
        return self._length * self._width * weight_1m2 * thickness


road = Road(20, 5000)
print(road.weight(25, 5))
