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
    d = ' |  '  # delimiter

    print(f'\n\n*** Top 5 Laptops With The {hi_lo} {value}s ***')
    print(f'{"BRAND":>{br_len}}{d}{"MODEL":>{mod_len}}{d}{value.upper():>{val_len}}')

    for br, mod, val in zip(brand_list, model_list, value_list):
        print(f'{br:>{br_len}}{d}{mod:>{mod_len}}{d}{val:>{val_len}}')


def print_two_cols(dict1, col1, decoder=lambda x: x):
    sorted_list = sorted(dict1)  # to print in the alphabetical order

    keys_list = []
    values_list = []

    for key in sorted_list:  # sorted_list is the sorted list of keys of dict1
        keys_list.append(decoder(key))
        values_list.append(dict1[key])

    keys_len = max(max(map(len, keys_list)), len(col1))
    val_len = max(max(map(len, str(values_list))), len('COUNT'))
    d = ' : '  # delimiter

    print(f'\n\n*** Number of Laptops For Each {col1} ***')
    print(f'{col1.upper():>{keys_len}}{d}{"COUNT":>{val_len}}')

    for key, val in zip(keys_list, values_list):
        print(f'{key:>{keys_len}}{d}{val:>{val_len}}')


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
    laptop_sizes = {' less than 10"': 0, '10" - 13"': 0, '13" - 15"': 0, '15" and bigger': 0}
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
            laptop_sizes[' less than 10"'] += 1
        elif current_screen_size < 13:
            laptop_sizes['10" - 13"'] += 1
        elif current_screen_size < 15:
            laptop_sizes['13" - 15"'] += 1
        else:
            laptop_sizes['15" and bigger'] += 1

    # Printing the results

    print_like_a_table(top_5_expensive, 'Price', lambda x: x.raw_price, lambda x: x.price)
    print_like_a_table(top_5_cheapest, 'Price', lambda x: x.raw_price, lambda x: x.price, golf_logic=True)
    print_two_cols(laptop_oss, "Operating System",
                   lambda x: ' '.join((x[:-2].title(), 'OS')) if x[-2:] == 'os' else x.title())
    print_like_a_table(top_5_heaviest, 'Weight', lambda x: x.raw_weight, lambda x: x.weight)
    print_like_a_table(top_5_rams, 'RAM', lambda x: x.raw_ram, lambda x: x.ram)
    print_two_cols(laptop_rams, "RAM size", LaptopWithSpecs.byte_to_human)
    print_two_cols(laptop_sizes, "Screen Size")
    print_two_cols(laptop_brands, "Brand")
