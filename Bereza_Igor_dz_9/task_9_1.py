from time import sleep
import colorama
from colorama import Fore
import cursor


class TrafficLight:
    __color = ''

    def running(self):
        def print_color(wait, color):
            print(color + '● ', end='')
            sleep(wait)
            print('\r ')

        cursor.hide()
        colorama.init()

        __color = Fore.LIGHTRED_EX
        print_color(7, __color)

        __color = Fore.LIGHTYELLOW_EX
        print_color(2, __color)

        __color = Fore.LIGHTGREEN_EX
        print_color(5, __color)
        cursor.show()


traffic_light = TrafficLight()
traffic_light.running()
