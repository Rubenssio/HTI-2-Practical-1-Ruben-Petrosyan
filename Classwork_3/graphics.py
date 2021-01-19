def draw_arrow(n, symbol='*'):

    # solution N3
    increment = 1
    i = 1
    while i != 0:
        print(f'{symbol} ' * i)

        if i == n:
            increment = -1

        i += increment

    # solution N1
    # for i in range(1, n + 1):
    #     print(f'{symbol} ' * i)
    # for i in range(1, n):
    #     print(f'{symbol} ' * (n - i))

    # solution N2
    # for i in range(n * 2 - 1):
    #     if i < n:
    #         print(f'{symbol} ' * (i + 1))
    #     else:
    #         print(f'{symbol} ' * (n * 2 - i - 1))


num = int(input('enter a positive number: '))
sign = input('enter the symbol or press enter to use the default: ')

if sign == '':
    draw_arrow(num)
else:
    draw_arrow(num, sign)