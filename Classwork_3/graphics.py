def draw_arrow(n, *, symbol='*', direction='right'):

    if direction == 'right' or 'left':
        increment = 1
        i = 1
        while i != 0:
            if direction == 'right':
                print(f'{symbol} ' * i)
            if direction == 'left':
                print('  ' * (n - i) + f' {symbol}' * i)

            if i == n:
                increment = -1

            i += increment

    if direction == 'up' or 'down':
        for i in range(n):
            if direction == 'up':
                print((n - i - 1) * '  ' + (2 * i + 1) * f' {symbol}')
            if direction == 'down':
                print(i * '  ' + (2 * (n - i) - 1) * f' {symbol}')


num = int(input('enter the lenght of the arrow: '))
symb = input('enter the symbol or press "Enter" to use the default: ')
dir = input('enter "right", "left", "up" or "down" for the direction: ')

if symb == '':
    draw_arrow(num, direction=dir)
else:
    draw_arrow(num, symbol=symb, direction=dir)
