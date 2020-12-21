# վերնագիր
print('''
You are about to define "year" as a "century"!
You can enter a year between 1 and 2021
''')

# տարվա մուտքագրում user-ի կողմից
year = int(input('Please enter the year: '))

# ստուգում, արդյոք ներմուծված տարեթիվը բավարարում է խնդրի 1-2021 պահանջին
if 0 < year < 2022:

    # # ԳԼԽԱՎՈՐ ԿՈԴԸ՝ տարեթվից դարի ստացումը
    century = round(year / 100 + 0.49)

    # խնդիրը լուծելու այլ տարբերակ
    """
    import math
    century = math.ceil(year / 100)
    """

    # որոշում ենք թե դարի վերջում ինչ վերջավորություն ենք տպելու
    if 3 < century < 21:
        suffix = 'th'
    elif century == 1 or century == 21:
        suffix = 'st'
    elif century == 2:
        suffix = 'nd'
    else:
        suffix = 'rd'

    # արդյունքի տպում
    print(f'\n-ANSWER-\nYear {year} is the {century}{suffix} century.\n')

else:  # այն դեպքը երբ մուտքագրված թիվը 1-2021 միջակայքում չէ
    print('\n-ANSWER-\nEntered year is out of range (1-2021)\n')
