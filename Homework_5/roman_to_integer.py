def roman_to_integer(roman):
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    integer = 0
    i = len(roman) - 1
    while i > 0:
        if values[roman[i-1]] >= values[roman[i]]:
            integer += values[roman[i]]
            i -= 1
        else:
            integer += values[roman[i]] - values[roman[i - 1]]
            i -= 2
    if values[roman[0]] >= values[roman[1]]:
        integer += values[roman[0]]

    return integer


rom = input('Enter the roman number: ')

print("Thant's equal to", roman_to_integer(rom))
