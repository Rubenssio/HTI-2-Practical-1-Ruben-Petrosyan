def is_in(value, symbols):
    return value in symbols


def is_password_safe(password):
    up, up1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 0
    low, low1 = 'abcdefghijklmnopqrstuvwxyz', 0
    num, num1 = '0123456789', 0
    sym, sym1 = '$#@', 0
    ln1 = False

    for i in password:

        if not up1:
            up1 = is_in(i, up)
        if not low1:
            low1 = is_in(i, up)
        if not num1:
            num1 = is_in(i, num)
        if not sym1:
            sym1 = is_in(i, sym)

    if 6 <= len(password) <= 16:
        ln1 = True

    return up1 and low1 and num1 and sym1 and ln1


if is_password_safe(input('Enter your password: ')):
    print('Yes')
else:
    print('No')
