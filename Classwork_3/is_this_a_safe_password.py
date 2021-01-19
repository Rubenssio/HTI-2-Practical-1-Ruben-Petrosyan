def is_in(text, symbols):
    for sym in text:
        if sym in symbols:
            return True
    return False


def is_password_safe(password):
    symbols_list = [
        'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
        'abcdefghijklmnopqrstuvwxyz',
        '0123456789', '$#@']

    for symbols in symbols_list:
        if not is_in(password, symbols):
            return False

    if 6 <= len(password) <= 16:
        return True

    return False


if is_password_safe(input('Enter your password: ')):
    print('Yes')
else:
    print('No')
