def is_in(text, symbols):
    for sym in text:
        if sym in symbols:
            return True
    return False


def is_password_safe(password):
    up, up1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 0
    low, low1 = 'abcdefghijklmnopqrstuvwxyz', 0
    num, num1 = '0123456789', 0
    sym, sym1 = '$#@', 0
    ln1 = False

    if not is_in(password, up):
        return False
    if not is_in(password, up):
        return False
    if not is_in(password, num):
        return False
    if not is_in(password, sym):
        return False

    if 6 <= len(password) <= 16:
        return True

    return False


if is_password_safe(input('Enter your password: ')):
    print('Yes')
else:
    print('No')
