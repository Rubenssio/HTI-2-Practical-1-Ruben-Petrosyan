def roman_to_integer(roman):
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    integer = 0
    i = 0
    while i < len(roman) - 1:
        if values[roman[i]] >= values[roman[i + 1]]:
            integer += values[roman[i]]
            i += 1
        else:
            integer += values[roman[i + 1]] - values[roman[i]]
            i += 2
    if values[roman[-1]] <= values[roman[-2]]:
        integer += values[roman[-1]]

    return integer


rom = input('Enter the roman number: ')

print("Thant's equal to", roman_to_integer(rom))
