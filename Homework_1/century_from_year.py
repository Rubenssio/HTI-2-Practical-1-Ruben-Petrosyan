print('\nYou are about to define "year" as a "century"!')
print('You can enter a year between 1 and 2021')
year = int(input('.\nPlease enter the year: '))

if year % 100 > 0:
    century = year // 100 + 1
else:
    century = year // 100

if 0 < year < 2022:

    if 3 < century < 21:
        suffix = 'th'
    elif century == 1 or century == 21:
        suffix = 'st'
    elif century == 2:
        suffix = 'nd'
    else:
        suffix = 'rd'

    print(f'-ANSWER-\nYear {year} is the {century}{suffix} century.\n')

else:
    print('-ANSWER-\nThe year entered is out of range (1-2021)\n')
