def is_prime(num):
    """Checks whether the given number is a prime number
    and returns 'Yes' or 'No' accordingly:
        'Yes' - if the given number IS prime,
        'No'  - if the given number IS NOT prime"""

    if num == 2:
        return True

    if num % 2 == 0:
        return False

    for i in range(3, num//2 + 1, 2):
        if num % i == 0:
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
