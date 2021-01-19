def is_prime(num):
    """Checks whether the given number is a prime number
    and returns 'Yes' or 'No' accordingly:
        'Yes' - if the given number IS prime,
        'No'  - if the given number IS NOT prime"""

    for i in range(2, num):
        if num % i == 0:
            return 'No'
    return 'Yes'


print(is_prime(int(input("Enter the number: "))))

"""
Wikipedia-ում պարզ թիվ ստուգելու Python կոդի շատ հետաքրքիր տարբերակ կա,
ու ոնց հասկանում եմ՝ շատ էֆեկտիվ աշխատող
https://en.wikipedia.org/wiki/Primality_test#Python_Code
չնայած ֆունկցիան հայտարարելուց «-> bool» գրառումը դեռ չեմ հասկանում
"""
