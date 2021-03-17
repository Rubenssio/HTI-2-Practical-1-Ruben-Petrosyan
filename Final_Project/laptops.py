import csv
import os

from classes import LaptopWithSpecs


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


def top_5(lap1, t5_list, key, golf_logic=False):
    duplicate = False

    if golf_logic:
        last_in_list = max(t5_list, key=key)
        belongs_in_top_5 = key(lap1) < key(last_in_list)
    else:
        last_in_list = min(t5_list, key=key)
        belongs_in_top_5 = key(lap1) > key(last_in_list)

    if belongs_in_top_5:
        for item in t5_list:
            if (
                    item.model == lap1.model
                    and
                    item.manufacturer == lap1.manufacturer
                    and
                    key(item) == key(lap1)
            ):
                duplicate = True
                break

        if not duplicate:
            t5_list.remove(last_in_list)
            t5_list.append(lap1)


def adding_to_dict(dict1, lap1, key, reformat=False):
    if reformat:
        current = key(lap1).lower().replace(' ', '')
    else:
        current = key(lap1)

    if current not in dict1:
        dict1[current] = 1
    else:
        dict1[current] += 1


def print_like_a_table(list_of_laps, value, sort_key, print_key, golf_logic=False):
    brand_list = []
    model_list = []
    value_list = []

    list_of_laps.sort(key=sort_key, reverse=not golf_logic)

    for item in list_of_laps:
        brand_list.append(item.manufacturer)
        model_list.append(item.model)
        value_list.append(print_key(item))

    # table widths
    br_len = max(max(map(len, brand_list)), 7)  # len('BRAND') + 2 = 7
    mod_len = max(max(map(len, model_list)), 7)  # len('MODEL') + 2 = 7
    val_len = max(max(map(len, value_list)), len(value) + 2)

    hi_lo = 'Lowest' if golf_logic else 'Highest'
    d = ' | '  # delimiter

    print(f'\n--- Top 5 Laptops With The {hi_lo} {value}s ---')
    print(f'{"BRAND":^{br_len}}{d}{"MODEL":^{mod_len}}{d}{value.upper():^{val_len}}')

    for br, mod, val in zip(brand_list, model_list, value_list):
        print(f'{br:<{br_len}}{d}{mod:<{mod_len}}{d}{val:<{val_len}}')


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

        top_5(lap, top_5_expensive, lambda x: x.raw_price)  # finding TOP 5 MOST EXPENSIVE laptops
        top_5(lap, top_5_cheapest, lambda x: x.raw_price, golf_logic=True)  # finding TOP 5 CHEAPEST laptops
        top_5(lap, top_5_heaviest, lambda x: x.raw_weight)  # finding TOP 5 HEAVIEST laptops
        top_5(lap, top_5_rams, lambda x: x.raw_ram)  # finding TOP 5 laptops with the BIGGEST RAMs

        adding_to_dict(laptop_oss, lap, lambda x: x.the_os, reformat=True)  # finding number of laptops for each OS
        adding_to_dict(laptop_rams, lap, lambda x: x.raw_ram)  # finding number of laptops for EACH RAM SIZE
        adding_to_dict(laptop_brands, lap, lambda x: x.manufacturer)  # finding number of laptops for EACH BRAND

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

    # Printing the results

    print_like_a_table(top_5_expensive, 'Price', lambda x: x.raw_price, lambda x: x.price)
    print_like_a_table(top_5_cheapest, 'Price', lambda x: x.raw_price, lambda x: x.price, golf_logic=True)

    print('\n--- Number of laptops for each Operating System ---')
    laptop_oss_keys_sorted_in_list = sorted(laptop_oss)  # to print in alphabetical order
    for oss in laptop_oss_keys_sorted_in_list:
        osf = oss.title()  # formatting the oss string
        if osf[-2:] == 'os':  # if there is 'os' at the end,
            osf = ' '.join((osf[:-2], 'OS'))  # let's make it uppercase
        print(f'{osf}: {laptop_oss[oss]}')

    print_like_a_table(top_5_heaviest, 'Weight', lambda x: x.raw_weight, lambda x: x.weight)
    print_like_a_table(top_5_rams, 'RAM', lambda x: x.raw_ram, lambda x: x.ram)

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
