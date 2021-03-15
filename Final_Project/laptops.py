import csv
import os
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
    def screen_size(self):
        return f'{self._screen_size}"'

    @screen_size.setter
    def screen_size(self, value):
        if isinstance(value, (int, float)):
            self._screen_size = float(value)
        else:
            error = ValueError('Screen size must be entered in <13.0"> format.')

            if value[-1] != '"':
                raise error

            try:
                self._screen_size = float(value[:-1])
            except ValueError:
                raise error

    @property
    def price(self):
        return f'{self._price:.2f}€'

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

    @property
    def ram(self):
        unit = 'GB'

        if self._ram < 1:
            unit = 'MB'
            value = self._ram * 1024
        else:
            value = self._ram

        if value % 1 == 0:
            value = int(value)

        return f'{value}{unit}'

    @ram.setter
    def ram(self, value):

        pattern = r'\d+(.\d+)?[gG]'
        value = value.replace(' ', '').replace(',', '.')

        matched = re.search(pattern, value)

        if not matched:
            raise ValueError('RAM must be entered in Gigabytes. "G" must follow the RAM value.'
                             '\n\t\t\te.g 512MB must be entered as 0.5GB')

        self._ram = float(matched[0][:-1])  # float, in case value is not a whole number

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

        pattern = r'\d+(.\d+)?[gkGK]'
        value = value.replace(' ', '').replace(',', '.')

        matched = re.search(pattern, value)

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
            f'{self.the_os}{"".join((" ", self.os_version)) if self.os_version else ""}, '
            f'{self.weight}'
        )


def laptops():
    file = 'laptops.csv'
    dir_path = os.path.dirname(os.path.abspath(__file__))  # current directory
    file_path = os.path.join(dir_path, file)

    with open(file_path) as f:
        reader = csv.DictReader(f)

        for row in reader:
            yield LaptopWithSpecs(
                row['Manufacturer'],
                row['Model Name'],
                row['Screen Size'],
                row['Price (Euros)'],
                row['Category'],
                row['Screen'],
                row['CPU'],
                row['RAM'],
                row['Storage'],
                row['GPU'],
                row['Operating System'],
                row['Operating System Version'],
                row['Weight'],
            )


if __name__ == '__main__':

    i = 0
    for lap in laptops():
        i += 1
        print(i, lap)
