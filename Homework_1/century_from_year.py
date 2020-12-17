print('\nYou are about to define a year as a century!')
print('You can enter a year between 1 and 2021')
year = int(input('.\nPlease enter the year: '))

if year % 100 > 0:
    century = year // 100 + 1
else:
    century = year // 100

if century == 1 or century == 21:
    suffix = 'st'
elif century == 2:
    suffix = 'nd'
elif century == 3:
    suffix = 'rd'
else:
    suffix = 'th'

print(f'Year {year} is the {century}{suffix} century.\n')
