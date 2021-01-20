def largest_number(number):
    num = number % 10
    number //= 10
    while number != 0:
        if num > number % 10:
            return True
        num = number % 10
        number //= 10

    return False

number = int(input('Enter number: '))

if largest_number(number):
    print('Yes')
else:
    print('No')
