def draw_arrow(n):
    for i in range(1, n + 1):
        print('* ' * i)
    for i in range(1, n):
        print('* ' * (n - i))

    # for i in range(n * 2 - 1):
    #     if i < n:
    #         print('* ' * (i + 1))
    #     else:
    #         print('* ' * (n * 2 - i - 1))


num = int(input('enter a positive number: '))

draw_arrow(num)
