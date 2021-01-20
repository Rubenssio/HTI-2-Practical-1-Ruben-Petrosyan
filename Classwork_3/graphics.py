def draw_arrow(n, *, symbol='*', direction='right'):

    if direction == 'right':
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

    if direction == 'left':

        increment = 1
        i = 1
        while i != 0:
            print('  ' * (n - i) + f' {symbol}' * i)

            if i == n:
                increment = -1

            i += increment

    if direction == 'up':
        print('\nThe "up" direction is not supported yet')

    if direction == 'down':
        print(('\nThe "down" direction is not supported yet'))


num = int(input('enter a positive number: '))
symb = input('enter the symbol or press "Enter" to use the default: ')
dir = input('enter "right", "left", "up" or "down" for the direction: ')

if symb == '':
    draw_arrow(num, direction=dir)
else:
    draw_arrow(num, symbol=symb, direction=dir)
