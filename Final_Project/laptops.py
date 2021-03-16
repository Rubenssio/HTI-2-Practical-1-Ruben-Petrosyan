import csv
import math
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


def laptops():
    file = 'laptops.csv'  # this file must be in the same directory as THIS python file
    dir_path = os.path.dirname(os.path.abspath(__file__))  # current directory
    file_path = os.path.join(dir_path, file)  # the absolute path to the file

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

    my_iter = laptops()

    list_of_first_5 = []

    for _ in range(5):
        list_of_first_5.append(next(my_iter))

    top_5_expensive = list_of_first_5.copy()
    top_5_cheapest = list_of_first_5.copy()
    laptop_oss = {}
    top_5_heaviest = list_of_first_5.copy()
    top_5_rams = list_of_first_5.copy()
    laptop_rams = {}
    laptop_sizes = {'less than 10"': 0, '10" - 13"': 0, '13" - 15"': 0, '15" and bigger': 0}
    laptop_brands = {}

    for lap in laptops():

        # --- finding the MOST EXPENSIVE laptops ---
        min_in_exp = min(top_5_expensive, key=lambda x: x.raw_price)  # the cheapest in the most expensive list
        if lap.raw_price > min_in_exp.raw_price:
            top_5_expensive.remove(min_in_exp)
            top_5_expensive.append(lap)

        # --- finding the CHEAPEST laptops ---
        max_in_cheap = max(top_5_cheapest, key=lambda x: x.raw_price)  # most expensive in the cheapest list
        if lap.raw_price < max_in_cheap.raw_price:
            top_5_cheapest.remove(max_in_cheap)
            top_5_cheapest.append(lap)

        # --- finding number of laptops for each OS ---
        current_lap_os = lap.the_os.lower().replace(' ', '')
        if current_lap_os not in laptop_oss:
            laptop_oss[current_lap_os] = 1
        else:
            laptop_oss[current_lap_os] += 1

        # --- finding the HEAVIEST laptops ---
        swap_please = True
        lightest_so_far = min(top_5_heaviest, key=lambda x: x.raw_weight)  # lightest in the heavy list
        if lap.raw_weight > lightest_so_far.raw_weight:
            for item in top_5_heaviest:
                if item.model == lap.model:
                    if item.manufacturer == lap.manufacturer:
                        swap_please = False
                        if item.raw_weight < lap.raw_weight:
                            top_5_heaviest.remove(item)
                            top_5_heaviest.append(lap)
            if swap_please:
                top_5_heaviest.remove(lightest_so_far)
                top_5_heaviest.append(lap)

        # --- finding the laptops with the BIGGEST RAMs ---
        swap_please = True
        min_in_rams = min(top_5_rams, key=lambda x: x.raw_ram)  # the smallest ram in the ram's list
        if lap.raw_ram > min_in_exp.raw_ram:
            for item in top_5_rams:
                if item.model == lap.model:
                    if item.manufacturer == lap.manufacturer:
                        swap_please = False
                        if item.raw_ram < lap.raw_ram:
                            top_5_rams.remove(item)
                            top_5_rams.append(lap)
            if swap_please:
                top_5_rams.remove(min_in_rams)
                top_5_rams.append(lap)

        # --- finding number of laptops for EACH RAM SIZE ---
        current_ram = lap.raw_ram
        if current_ram not in laptop_rams:
            laptop_rams[current_ram] = 1
        else:
            laptop_rams[current_ram] += 1

        # --- finding number of laptops for EACH SCREEN SIZE range ---
        current_screen_size = lap.raw_screen_size
        if current_screen_size < 10:
            laptop_sizes['less than 10"'] += 1
        elif current_screen_size < 13:
            laptop_sizes['10" - 13"'] += 1
        elif current_screen_size < 15:
            laptop_sizes['13" - 15"'] += 1
        else:
            laptop_sizes['15" and bigger'] += 1

        # --- finding number of laptops for EACH BRAND ---
        current_brand = lap.manufacturer
        if current_brand not in laptop_brands:
            laptop_brands[current_brand] = 1
        else:
            laptop_brands[current_brand] += 1

    # the end of 'for'

    top_5_expensive.sort(reverse=True, key=lambda x: x.raw_price)
    print('\n--- TOP 5 Most Expensive Laptops ---')
    for el in top_5_expensive:
        print(el.manufacturer, el.model, el.price)

    top_5_cheapest.sort(key=lambda x: x.raw_price)
    print('\n--- TOP 5 Cheapest Laptops ---')
    for el in top_5_cheapest:
        print(el.manufacturer, el.model, el.price)

    print('\n--- Number of laptops for each Operating System ---')
    laptop_oss_keys_sorted_in_list = sorted(laptop_oss)  # to print in alphabetical order
    for oss in laptop_oss_keys_sorted_in_list:
        osf = oss.title()  # formatting the oss string
        if osf[-2:] == 'os':  # if there is 'os' at the end,
            osf = ' '.join((osf[:-2], 'OS'))  # let's make it uppercase
        print(f'{osf}: {laptop_oss[oss]}')

    top_5_heaviest.sort(reverse=True, key=lambda x: x.raw_weight)
    print('\n--- TOP 5 Heaviest Laptops ---')
    for el in top_5_heaviest:
        print(el.manufacturer, el.model, el.weight)

    top_5_rams.sort(reverse=True, key=lambda x: x.raw_ram)
    print('\n--- TOP 5 laptops with biggest RAMs ---')
    for el in top_5_rams:
        print(el.manufacturer, el.model, el.ram)

    print('\n--- Number of laptops for each RAM size ---')
    laptop_ram_keys_sorted_in_list = sorted(laptop_rams)  # to print in a sorted fashion
    for ram_size in laptop_ram_keys_sorted_in_list:
        print(f'{LaptopWithSpecs.byte_to_human(ram_size)}: {laptop_rams[ram_size]}')

    print('\n--- Number of laptops for each screen size ---')
    for size, count in laptop_sizes.items():
        print(f'{size}: {count}')

    print('\n--- Number of laptops for each brand ---')
    laptop_brand_keys_sorted_in_list = sorted(laptop_brands)  # to print in a alphabetical order
    for brand in laptop_brand_keys_sorted_in_list:
        print(f'{brand}: {laptop_brands[brand]}')
