def draw_arrow(n, symbol='*'):
    for i in range(1, n + 1):
        print(f'{symbol} ' * i)
    for i in range(1, n):
        print(f'{symbol} ' * (n - i))

    # another solution
    # for i in range(n * 2 - 1):
    #     if i < n:
    #         print(f'{symbol} ' * (i + 1))
    #     else:
    #         print(f'{symbol} ' * (n * 2 - i - 1))


num = int(input('enter a positive number: '))
symbol = input('enter the symbol or press enter to use the default: ')

if symbol == '':
    draw_arrow(num)
else:
    draw_arrow(num, symbol)
