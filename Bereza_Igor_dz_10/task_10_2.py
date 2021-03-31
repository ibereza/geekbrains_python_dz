from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        self.__size = size

    def consumption(self):
        return round(self.__size / 6.5 + 0.5, 2)


class Suit(Clothes):
    def __init__(self, height):
        self.__height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    def consumption(self):
        return round(self.__height * 2 + 0.3, 2)


coat = Coat(14)
print(f'Для изготовления пальто {coat.size}-го размера необходимо '
      f'{coat.consumption()} м2 ткани.')
suit = Suit(1.67)
print(f'Для изготовления костюма на рост {suit.height} м необходимо '
      f'{suit.consumption()} м2 ткани.')
print(f'Общий расход ткани {coat.consumption() + suit.consumption()} м2')

print()

coat.size = 18
print(f'Для изготовления пальто {coat.size}-го размера необходимо '
      f'{coat.consumption()} м2 ткани.')
suit.height = 1.83
print(f'Для изготовления костюма на рост {suit.height} м необходимо '
      f'{suit.consumption()} м2 ткани.')
print(f'Общий расход ткани {coat.consumption() + suit.consumption()} м2')
