def is_in(text, symbols):
    for sym in text:
        if sym in symbols:
            return True
    return False


def is_password_safe(password):
    up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    low = 'abcdefghijklmnopqrstuvwxyz'
    num = '0123456789'
    sym = '$#@'

    if not is_in(password, up):
        return False
    if not is_in(password, low):
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
