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

    # the end of 'for lap in laptops()'

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
