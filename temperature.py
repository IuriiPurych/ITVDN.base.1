# Задание 3
# Используя ссылки в конце данного урока, ознакомьтесь с таким средством инкапсуляции как свойства.
# Ознакомьтесь с декоратором property в Python. Создайте класс,
# описывающий температуру и позволяющий задавать и получать температуру по шкале Цельсия и Фаренгейта,
# причём данные могут быть заданы в одной шкале, а получены в другой.
class Temperature:
    _temperature_kelvin = 0.0

    def __init__(self, t_c=0, t_f=0):
        if (t_c == 0 and t_f == 0) or (t_c != 0 and t_f != 0):
            print('For indicate temperature use Temperature(t_c = something) for indicate Celsius temperature\n'
                  ' or Temperature(t_f = something) for Fahrenheit temperature.\n'
                  'Don\'t indicate both arguments!\n'
                  'The Temperature set Absolute Zero.')
            self._temperature_kelvin = 0.0
        elif t_c != 0:
            self.temperature_celsius = t_c
        else:
            self.temperature_fahrenheit = t_f

    def get_temperature_celsius(self):
        return self._temperature_kelvin - 273.15

    def set_temperature_celsius(self, value):
        self._temperature_kelvin = value + 273.15

    temperature_celsius = property(get_temperature_celsius, set_temperature_celsius)

    def get_temperature_fahrenheit(self):
        return (self._temperature_kelvin - 273.15) * (9 / 5) + 32

    def set_temperature_fahrenheit(self, value):
        self._temperature_kelvin = (value - 32) * (5 / 9) + 273.15

    temperature_fahrenheit = property(get_temperature_fahrenheit, set_temperature_fahrenheit)

    def __str__(self):
        return f'The Celsius temperature is {self.temperature_celsius:4.2f}. \n' \
               f'The Fahrenheit temperature is {self.temperature_fahrenheit:4.2f}.'


t = Temperature(t_f=100)
print(t)
t.temperature_celsius = 37
print(t)
t.temperature_fahrenheit = 0
print(t)
