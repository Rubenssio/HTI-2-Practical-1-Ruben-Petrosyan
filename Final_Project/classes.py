import math
import re


class Laptop:
    def __init__(self, manufacturer, model, screen_size, price):
        self.manufacturer = manufacturer
        self.model = model

        self._screen_size = None
        self.screen_size = screen_size

        self._price = None
        self.price = price

    @property
    def raw_screen_size(self):
        return self._screen_size

    @property
    def screen_size(self):
        return f'{self._screen_size}"'

    @screen_size.setter
    def screen_size(self, value):
        error = ValueError('Screen size must be entered in inches in <13.0"> format.')

        if value[-1] != '"':
            raise error

        try:
            self._screen_size = float(value[:-1].replace(',', '.'))
        except ValueError:
            raise error

    @property
    def raw_price(self):
        return self._price

    @property
    def price(self):
        value = f'{self._price:.2f}€'.replace('.', ',')
        return value

    @price.setter
    def price(self, value):
        if isinstance(value, (int, float)):
            self._price = float(value)
        else:
            try:
                self._price = float(value.replace(',', '.'))
            except ValueError:
                raise ValueError('Price must be entered in euros as a number (without letters or characters.')

    def __repr__(self):
        return f'{self.manufacturer} {self.model} {self.screen_size} {self.price}'


class LaptopWithSpecs(Laptop):
    def __init__(self, manufacturer, model, screen_size, price,
                 category, screen, cpu, ram, storage, gpu, the_os, os_version, weight):
        super().__init__(manufacturer, model, screen_size, price)
        self.category = category
        self.screen = screen
        self.cpu = cpu

        self._ram = None
        self.ram = ram

        self.storage = storage
        self.gpu = gpu
        self.the_os = the_os
        self.os_version = os_version

        self._weight = None
        self.weight = weight

    @staticmethod
    def byte_to_human(byte):
        p = int(math.log(byte, 1024))

        value = byte / 1024 ** p  # getting more human readable version
        value = round(value, 1)  # rounding to the nearest 0.1
        value = int(value) if value % 1 == 0 else value  # converting into 'int' if no decimal

        units = 'B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'

        return f'{value}{units[p]}'

    @property
    def raw_ram(self):
        return self._ram

    @property
    def ram(self):
        return self.byte_to_human(self._ram)

    @ram.setter
    def ram(self, value):

        pattern = (
            r'\d+'                      # first character must be a digit (one or more digits)
            r'(.\d+)?'                  # followed by a dot and one or more digits (repeated zero times or once)
            r'[kKmMgGtTpPeEzZyY]?[bB]'  # unit must be right after the digits
        )

        value = value.replace(' ', '').replace(',', '.')

        matched = re.match(pattern, value)

        if not matched:
            raise ValueError('The unit of the RAM must be indicated. e.g. "16" is not acceptable,'
                             '\n\t\t\tthe value must be entered as "16GB" or "16MB" or etc.'
                             '\n\t\t\t"512MB" can be entered as "0.5GB"')

        units = 'B', 'K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y'

        unit_index = -2  # to isolate last two characters as the unit
        if matched[0][-2] not in units:  # if it's 16B for example,
            unit_index = -1              # than we need to isolate only the last character

        value = float(matched[0][:unit_index])  # getting only the numeric part of the RAM as a float

        value = value * 1024 ** units.index(matched[0][unit_index])  # converting to bytes based on units

        self._ram = int(value)  # we're not using quantum computers yet. 'value' is in bytes, it can't have decimals

    @property
    def raw_weight(self):
        return self._weight

    @property
    def weight(self):
        unit = 'kg'

        if self._weight < 1:
            unit = 'gr'
            value = self._weight * 1000
        else:
            value = self._weight

        if value % 1 == 0:
            value = int(value)

        return f'{value}{unit}'

    @weight.setter
    def weight(self, value):

        pattern = (
            r'\d+'      # first character must be a digit (one or more digits)
            r'(.\d+)?'  # followed by a dot and one or more digits (repeated zero times or once)
            r'[gkGK]'   # unit must be right after the digits
        )

        value = value.replace(' ', '').replace(',', '.')

        matched = re.match(pattern, value)

        if not matched:
            raise ValueError('Weight must be entered in grams or kilograms. "g" or "k" must follow the weight value.')

        if matched[0][-1].lower() == 'g':
            self._weight = float(matched[0][:-1]) / 1000
        else:
            self._weight = float(matched[0][:-1])

    def __repr__(self):
        return (
            f'{self.manufacturer} {self.model} {self.screen_size} {self.price}'
            f'\n\tSpecs: {self.category}, {self.screen}, {self.cpu}, {self.ram}, {self.storage}, {self.gpu}, '
            f'{self.the_os}{"".join((" ", self.os_version)) if self.os_version else ""}, '  # OS and OS version
            f'{self.weight}'
        )
