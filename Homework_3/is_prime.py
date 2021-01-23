def is_prime(num):
    """Checks whether the given number is a prime number
    and returns True or False accordingly:
        True  - if the given number IS prime,
        False - if the given number IS NOT prime"""

    if num == 2:
        return True

    if num % 2 == 0 or num == 1:
        return False

    for i in range(3, num//2 + 1, 2):
        if num % i == 0:
            print(num, 'can be divided by', i, '\b, so...')
            return False
    return True


num = int(input("Enter the number: "))

if is_prime(num):
    print('Yes')
else:
    print('No')

"""
Wikipedia-ում պարզ թիվ ստուգելու Python կոդի շատ հետաքրքիր տարբերակ կա,
ու ոնց հասկանում եմ՝ շատ էֆեկտիվ աշխատող
https://en.wikipedia.org/wiki/Primality_test#Python_Code
չնայած ֆունկցիան հայտարարելուց «-> bool» գրառումը դեռ չեմ հասկանում
"""
